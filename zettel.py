__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2020"
__credits__ = ["Jason M. Pittman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jpittman@highpoint.edu"
__status__ = "Development"

import time
import os
import configparser
from datetime import datetime

class Zettel:

    __header = {
        'type': '', 
        'id': '',
        'title': '',
        'date': '',
        'tags': []
    }

    __body = []

    def __init__(self, config_file, type=None):
        self.types = configparser.ConfigParser()
        self.types.read(os.path.join(os.path.dirname(__file__), config_file))

        if type is not None:
            if self.__is_type_defined(type):
                #if type is defined, load that type
                self.__header['type'] = '[[' + type + ']]'
                self.__header['title'] = '' #argv[2]
                self.__header['tags'] = self.types[type]['tags']
            else:
                #else, default to a generic note
                self.__header['type'] = '[[note]]'
                self.__header['title'] = 'An auto-generated note'
                self.__header['tags'] = ['#note', '#auto']
            
            self.__header['id'] = self.__generate_id()
            self.__header['date'] = time.ctime()

            self.__body = self.types[type]['fields']
        else:
            self.__help(self.types)

    def __is_type_defined(self, type):
        
        if type in self.types:
            is_defined = True
        else:
            is_defined = False
        
        return is_defined
    
    def create(self):
        now = datetime.now()
        stamp = now.strftime("%Y%d%m%H%M")

        try:
            f = open(stamp + ".md", "w+")
            f.write('---\n')
            
            for k, v in self.__header.items():
                f.write(str(k) + ': ' + str(v) + '\n')
            
            f.write('---\n\n')

            fields = self.__body.split(',')
            for field in fields:
                f.write('## ' + field.strip(' ') + '\n\n')

            f.close()
        except Exception as e:
            print('Error writing zettel file: ' + str(e))

    def __generate_id(self):
        now = datetime.now()
        id = now.strftime("%Y%d%m%H%M")
        return id
    
    def __help(self, types):
        print("Zetteler automates the creation of zettels based on your defined types.\n")
        print("You create a new zettel by running zettler [type] [title]\n")
        print("Zettel types are defined in the types.ini file. Currently the types are:\n")
        
        for section in types.sections():
            print(section)