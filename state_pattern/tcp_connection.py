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
        self.set_state('disconnected')

    def connect(self):
        self.state.connect()
        
    

    def disconnect(self):
        self.state.disconnect()
    
    def get_current_state(self):
        return self.state.get_current_state()
    
    def write(self, word):
        self.state.write(word)
    
    def set_state(self, name):
        self.state = self.STATES[name](self)

    # END
