from errors import TcpConnectionError


class ConnectedState:
    # BEGIN (write your solution here)
    def __init__(self, connection):
        self.connection = connection
    
    def connect(self):
        raise TcpConnectionError
    
    def disconnect(self):
        self.connection.set_state('disconnected')
    
    def get_current_state(self):
        return 'connected'
    
    def write(self, word):
        pass
    # END
