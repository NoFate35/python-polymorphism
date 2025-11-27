from states.connected import ConnectedState
from states.disconnected import DisconnectedState


class TcpConnection:
    # BEGIN (write your solution here)
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.state = DisconnectedState

    def connect(self):
        self.state = ConnectedState(self)
    
    # END
