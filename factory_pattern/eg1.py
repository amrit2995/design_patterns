import json
import xml.etree.ElementTree as etree
import sys
sys.path.insert(0,'/Users/amritprusty/Desktop/interview_preparation/design_patterns/factory_pattern')


class XMLDataExtractor:  
    def __init__(self, filepath):  
        self.tree =  etree.parse(filepath)  
        @property  
        def parsed_data(self):  
            return self.tree

            
class JSONDataExtractor:  
    def __init__(self, filepath):    
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)    
            @property    
            def parsed_data(self):        
                return self.data
            
            
def dataextraction_factory(filepath):    
    if filepath.endswith('json'):        
        extractor = JSONDataExtractor    
    elif filepath.endswith('xml'):        
        extractor = XMLDataExtractor    
    else:        
        raise ValueError('Cannot extract data from {}'.format(filepath))    
    return extractor(filepath)


def extract_data_from(filepath):    
    factory_obj = None    
    try:        
        factory_obj = dataextraction_factory(filepath)
        return factory_obj  
    except ValueError as e:        
        print(e)
        
def main():    
    import pdb;pdb.set_trace()
    # sqlite_factory = extract_data_from('data/person.sq3')
    data = extract_data_from('persons.xml')
    data = extract_data_from('text.json')
    print(data)
    
    
main()