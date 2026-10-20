from backend.core.room_manager import create_room, get_room, destroy_room
def test_room_lifecycle():
    room=create_room(); assert get_room(room.id) is room; assert destroy_room(room.id) is room
