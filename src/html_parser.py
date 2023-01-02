from typing import List

from html.parser import HTMLParser

from const import NON_PROCESSING_TAGS, INNER_TAGS, OUTER_TAGS, LINE_BREAK_SYMBOLS


class CustomHTMLParser(HTMLParser):
    """
        Custom HTMLParser class based on standart python HTMLParser
        
        This class contains rewrated methods of standart HTMLParser class.
        This class parses html and creates a list of entities (tags, scripts, data) for further use by child classes.
    """
    def __init__(self):
        super().__init__()
        self.all_html_entities = []
        self.last_tag_in_non_processing = False
        
    def __validate_incomming_data(self, data):
        """
            @param data : str
                html data as a string
                
            Func for check incomming data type is str or not. Parser will works only with string
        """
        if not isinstance(data, str):
            raise Exception('Make sure you are trying to parse string')
        
    def handle_starttag(self, tag, attrs):
        if tag in NON_PROCESSING_TAGS:
            self.last_tag_in_non_processing = True
        else:
            self.last_tag_in_non_processing = False
        tag_attrs = []
        for attr in attrs:
            tag_attrs.append(f'{attr[0]}="{attr[1]}"')
        tag_str = f'<{tag} {" ".join(tag_attrs)}>' if len(tag_attrs) != 0 else f'<{tag}>'
        if tag in INNER_TAGS:
            data_to_append = ('tag', tag_str, 'inner')
        elif tag in OUTER_TAGS:
            data_to_append = ('tag', tag_str, 'outer')
        else:
            data_to_append = ('tag', tag_str, 'other')
        self.all_html_entities.append(data_to_append)
        
    def handle_endtag(self, tag):
        if tag in INNER_TAGS:
            data_to_append = ('tag', f'</{tag}>', 'inner')
        elif tag in OUTER_TAGS:
            data_to_append = ('tag', f'</{tag}>', 'outer')
        else:
            data_to_append = ('tag', f'</{tag}>', 'other')
        self.all_html_entities.append(data_to_append)
        
    def handle_data(self, data):
        if not self.last_tag_in_non_processing:
            self.all_html_entities.append(('data', data))
        else:
            self.all_html_entities.append(('tag', data, 'other'))
            
    def get_entities(self, data: str) -> List[tuple]:
        self.__validate_incomming_data(data=data)
        self.feed(data=data)
        
        return self.all_html_entities