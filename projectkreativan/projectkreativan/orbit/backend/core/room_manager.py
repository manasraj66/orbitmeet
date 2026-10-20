import secrets, string
from datetime import datetime, timezone
from backend.models.room import Room
_rooms: dict[str, Room] = {}

def create_room():
    code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    room = Room(id=code, host_token=secrets.token_urlsafe(24), created_at=datetime.now(timezone.utc).isoformat())
    _rooms[code] = room
    return room

def get_room(code): return _rooms.get(code.upper())
def destroy_room(code): return _rooms.pop(code.upper(), None)
def all_rooms(): return list(_rooms.values())
