from typing import List

from razdel import sentenize

from html_parser import CustomHTMLParser


class Extractor:
    def __init__(self,
                 html: str,
                 separator: str = '|separator|',
                 inner_tags: List[str] = None,
                 outer_tags: List[str] = None,
                 non_processing_tags: List[str] = None):
        """
            @param html : str
                html in string wich you want to parse
            @param separator : str
                Example:
                    INCOMMING HTML - '<h1>First text</h1><h2>Second text</h2>'
                    
                    WITH SEPARATOR - 'First text|separator|Second text'
                    WITHOUT SEPARATOR - 'First textSecond text'
        """
        custom_html_parser_kwargs = {}
        assert isinstance(html, str)
        if inner_tags:
            assert isinstance(inner_tags, list) or isinstance(inner_tags, tuple)
            custom_html_parser_kwargs['inner_tags'] = inner_tags
        if outer_tags:
            assert isinstance(outer_tags, list) or isinstance(outer_tags, tuple)
            custom_html_parser_kwargs['outer_tags'] = outer_tags
        if non_processing_tags:
            assert isinstance(non_processing_tags, list) or isinstance(non_processing_tags, tuple)
            custom_html_parser_kwargs['non_processing_tags'] = non_processing_tags
        self.parser = CustomHTMLParser(**custom_html_parser_kwargs)
        self.entities = self.parser.get_entities(data=html)
        self.separator = separator
        
    def __concatinate_datas(self, entities: List[tuple], separator: str) -> str:
        """
            @param entities : List[tuple]
                list of tuple of entities in html data
                
            @return extracted text from html
        """
        text = ''
        last_tag_is_outer = False
        for entitie_elem in entities:
            if entitie_elem[0] == 'data':
                if last_tag_is_outer and len(text) != 0 and separator:
                    text += separator
                text += entitie_elem[1]   
            if entitie_elem[0] == 'tag' and entitie_elem[2] == 'outer':
                last_tag_is_outer = True
            else:
                last_tag_is_outer = False 
            
        return text
    
    def __sentenize(self, text_list: List[str]) -> List[str]:
        """
            @param text_list : List[str]
                List of splited text by separator
                
            @return List[str]
                List of sentences sentenized by razdel
        """
        sentences = []
        for text_elem in text_list:
            sentences += [x.text for x in list(sentenize(text_elem))]
            
        return sentences
        
    def extract_text(self) -> str:
        """     
            @return str
                extracted text from html
        """
        
        return self.__concatinate_datas(entities=self.entities, separator=self.separator)
    
    def extract_sentences(self) -> str:
        """
            @return List[str]
                List of sentences sentenized by razdel
        """
        if self.separator:
            separator = self.separator
        else:
            separator = '|separator|'
            
        text = self.__concatinate_datas(entities=self.entities, separator=separator)
        text_list = text.split(separator)
        
        return self.__sentenize(text_list=text_list)