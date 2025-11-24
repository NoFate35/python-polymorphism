import json

class DatabaseConfigLoader():
    def __init__(self, path):
        self.path = path
    
    def load(self, env):
        filename = self.path / f'database.{env}.json'
        with open(filename, 'r') as fd:
            config = json.load(fd)
        if 'extend' in config:
            ext_name = config.pop('extend')
            ext_file = self.path / f'database.{ext_name}.json'
            with open(ext_file, 'r') as fd:
                extention = json.load(fd)
            diff = set(extention) - set(config)
            for key in diff:
                config[key] = extention[key]
        return config