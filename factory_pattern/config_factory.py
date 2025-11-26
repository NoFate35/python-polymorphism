import os
import sys
print('sys.path', sys.path)
from config_klass import Config
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser

PARSERS = {
    ".yaml": YAMLParser,
    ".yml": YAMLParser,
    ".json": JSONParser,
}


# BEGIN (write your solution here)
class ConfigFactory():
    pass
# END
