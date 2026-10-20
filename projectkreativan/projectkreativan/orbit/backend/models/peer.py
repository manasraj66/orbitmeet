from dataclasses import dataclass
@dataclass
class Peer:
    id: str
    name: str
    state: str = 'connected'
