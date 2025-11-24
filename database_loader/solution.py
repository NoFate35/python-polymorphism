import json

class DatabaseConfigLoader():
    def __init__(self, path):
        self.path = path
    
    def load(self, env):
        filename = self.path / f'database.{env}.json'
        config = json.loads(open(filename).read())
        if 'extend' not in config:
            return config
        ext_name = config['extend']
        ext_config = {k: v for k, v in config.items() if k != 'extend'}
        return {**self.load(ext_name), **ext_config}
        '''
        ext_file = self.path / f'database.{ext_name}.json'
        extention = json.loads(open(ext_file).read())
        if 'extend' in extention:
            extention = self.load(ext_name)
        diff = set(extention) - set(config)
        for key in diff:
            config[key] = extention[key]
        return config
        '''
    
    '''
        def load(self, env):
        filename = f'database.{env}.json'
        filepath = self.path_to_config / filename
        raw_config = json.loads(open(filepath).read())

        if 'extend' not in raw_config:
            return raw_config

        extend = raw_config['extend']
        rest = {k: v for k, v in raw_config.items() if k != 'extend'}
        return {**self.load(extend), **rest}
    '''