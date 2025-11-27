from errors import TcpConnectionError


class ConnectedState:
    # BEGIN (write your solution here)
    def __init__(self, connection):
        self.connection = connection
        print('yyyyy')
    
    def connect():
        print('connnnect')
        raise TcpConnectionError()
    
    def disconnect(self):
        self.connection.state = self.STATES['disconnected'](self)
    
    def get_current_state(self):
        return 'connected'
    
    def write(self, word):
        print('word')


    # END
