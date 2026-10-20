from dataclasses import dataclass, field
from .peer import Peer

@dataclass
class Room:
    id: str
    host_token: str = ''
    created_at: str = ''
    peers: dict[str, Peer] = field(default_factory=dict)
    lobby: dict[str, dict] = field(default_factory=dict)
    settings: dict = field(default_factory=dict)
