from errors import TcpConnectionError


class DisconnectedState:
    # BEGIN (write your solution here)
    def __init__(self, connection):
        self.connection = connection

    def connect(self):
        self.connection.set_state('connected')
    
    def disconnect(self):
        raise TcpConnectionError
    
    def get_current_state(self):
        return 'disconnected'
    
    def write(self, word):
        raise TcpConnectionError
    # END
