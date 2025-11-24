import copy



# BEGIN (write your solution here)
class InMemoryKV():
    def __init__(self, data):
        self.data = copy.deepcopy(data)
        #print('self.data', self.data, 'self.filepath', self.filepath)
    
    def set_(self, key, value):
        self.data.update({key: value})


    def unset_(self, key):
        self.data.pop(key)


    def get_(self, key, default=None):
        return self.data.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.data)

    
# END
