from typing import List

from html.parser import HTMLParser

from const import NON_PROCESSING_TAGS, INNER_TAGS, OUTER_TAGS


class CustomHTMLParser(HTMLParser):
    """
        Custom HTMLParser class based on standart python HTMLParser
        
        This class contains rewrated methods of standart HTMLParser class.
        This class parses html and creates a list of entities (tags, scripts, data) for further use by child classes.
    """
    def __init__(self, inner_tags: List[str] = INNER_TAGS, outer_tags: List[str] = OUTER_TAGS, non_processing_tags: List[str] = NON_PROCESSING_TAGS):
        super().__init__()
        self.all_html_entities = []
        self.inner_tags = inner_tags
        self.outer_tags = outer_tags
        self.non_processing_tags = non_processing_tags
        self.last_tag_in_non_processing = False
        
    def handle_starttag(self, tag, attrs):
        if tag in self.non_processing_tags:
            self.last_tag_in_non_processing = True
        else:
            self.last_tag_in_non_processing = False
        tag_attrs = []
        for attr in attrs:
            tag_attrs.append(f'{attr[0]}="{attr[1]}"')
        tag_str = f'<{tag} {" ".join(tag_attrs)}>' if len(tag_attrs) != 0 else f'<{tag}>'
        if tag in self.inner_tags:
            data_to_append = ('tag', tag_str, 'inner')
        elif tag in self.outer_tags:
            data_to_append = ('tag', tag_str, 'outer')
        else:
            data_to_append = ('tag', tag_str, 'other')
        self.all_html_entities.append(data_to_append)
        
    def handle_endtag(self, tag):
        if tag in self.inner_tags:
            data_to_append = ('tag', f'</{tag}>', 'inner')
        elif tag in self.outer_tags:
            data_to_append = ('tag', f'</{tag}>', 'outer')
        else:
            data_to_append = ('tag', f'</{tag}>', 'other')
        self.all_html_entities.append(data_to_append)
        
    def handle_data(self, data):
        if not self.last_tag_in_non_processing:
            self.all_html_entities.append(('data', data, 'data'))
        else:
            self.all_html_entities.append(('tag', data, 'other'))
            
    def get_entities(self, data: str) -> List[tuple]:
        assert isinstance(data, str)
        self.feed(data=data)
        
        return self.all_html_entities