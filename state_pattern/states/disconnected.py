from errors import TcpConnectionError


class DisconnectedState:
    # BEGIN (write your solution here)
    def __init__(self, connection):
        self.connection = connection

    def connect(self):
        self.connection.state = self.STATES['connected'](self)
    
    def disconnect(self):
        raise TcpConnectionError
    
    def get_current_state(self):
        return 'disconnected'
    
    def write(self, word):
        pass
    # END
