import json


class FileKV():
    def __init__(self, filepath):
        self.filepath = filepath

    def set_(self, key, value):
        data = json.loads(open(self.filepath).read())
        data.update({key: value})
        with open(self.filepath, 'w') as f:
            f.write(json.dumps(data))

    def unset_(self, key):
        data = json.loads(open(self.filepath).read())
        data.pop(key)
        with open(self.filepath, 'w') as f:
            f.write(json.dumps(data))

    def get_(self, key, default=None):
        data = json.loads(open(self.filepath).read())
        return data.get(key, default)

    def to_dict(self):
        data = json.loads(open(self.filepath).read())
        return data
