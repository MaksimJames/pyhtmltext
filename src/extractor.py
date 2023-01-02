from typing import List

from html_parser import CustomHTMLParser


class Extractor:
    def __init__(self, separator: str = '\n'):
        """
            @param separator : str
                Example:
                    INCOMMING HTML - '<h1>First text</h1><h2>Second text</h2>'
                    
                    WITH SEPARATOR - 'First text\nSecond text'
                    WITHOUT SEPARATOR - 'First textSecond text'
        """
        self.parser = CustomHTMLParser()
        self.separator = separator
        
    def __concatinate_datas(self, entities: List[tuple]) -> str:
        """
            @param entities : List[tuple]
                list of tuple of entities in html data
                
            @return extracted text from html
        """
        filtered_datas = list(filter(lambda x: x[0] == 'data', entities))
        if self.separator:
            return f'{self.separator}'.join([x[1] for x in filtered_datas])
        else:
            return ''.join([x[1] for x in filtered_datas])
        
    def extract_text(self, data: str) -> str:
        """
            @param data : str
                html data in string
                
            @return str
                extracted text from html
        """
        entities = self.parser.get_entities(data=data)
        return self.__concatinate_datas(entities=entities)