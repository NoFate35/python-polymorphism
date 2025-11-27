from states.connected import ConnectedState
from states.disconnected import DisconnectedState


class TcpConnection:
    # BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.STATES = {
            'connected': ConnectedState,
            'disconnected': DisconnectedState
        }
        self.ip = ip
        self.port = port
        self.state = self.STATES['disconnected']

    def connect(self):
        print('tcp connect', self.state)
        self.state = self.STATES['connected'](self)
        
    

    def disconnect(self):
        self.state = self.STATES['disconnected'](self)
    
    def get_current_state(self):
        return self.state.get_current_state()
    
    def write(self, word):
        self.state.write(word)

    # END
