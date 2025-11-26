from dispatcher import defmethod


# BEGIN (write your solution here)
def init():
    print('init__square', __name__)
    defmethod(__name__, 'get_area', lambda self:  self['data']['side'] * self['data']['side'])

def make(side):
    print('makeee square', __name__)
    return {'name': __name__, 'data': {'side': side}}

def get_circle_radius(self):
    return self['data']['side']
# END