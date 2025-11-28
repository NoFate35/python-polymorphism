import json


# BEGIN (write your solution here)
class EqualityMixin:
    def __eq__(self, value):
        return value.__dict__ == self.__dict__ and type(self) == type(value)
    
class SerializeMixin:
    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, data):
        args = json.loads(data)
        return cls(args['items'])
        
# END
