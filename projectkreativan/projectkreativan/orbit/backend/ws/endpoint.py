import json
from collections import defaultdict
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()
_rooms: dict[str, dict[str, WebSocket]] = defaultdict(dict)

@router.websocket('/ws/{room}/{peer}')
async def websocket_endpoint(websocket: WebSocket, room: str, peer: str):
    room = room.upper()
    await websocket.accept()
    clients = _rooms[room]
    existing = list(clients.keys())
    clients[peer] = websocket
    try:
        await websocket.send_text(json.dumps({"type": "peers", "peers": existing}))
        for other_id, client in list(clients.items()):
            if other_id != peer:
                try:
                    await client.send_text(json.dumps({"type": "peer-joined", "peer": peer}))
                except Exception:
                    pass
        while True:
            raw = await websocket.receive_text()
            try:
                message = json.loads(raw)
            except json.JSONDecodeError:
                continue
            target = message.pop("to", None)
            message["from"] = peer
            if target:
                client = clients.get(target)
                if client:
                    await client.send_text(json.dumps(message))
            else:
                # Broadcast non-private signaling messages to everyone else.
                for other_id, client in list(clients.items()):
                    if other_id != peer:
                        await client.send_text(json.dumps(message))
    except WebSocketDisconnect:
        pass
    finally:
        clients.pop(peer, None)
        for client in list(clients.values()):
            try:
                await client.send_text(json.dumps({"type": "peer-left", "peer": peer}))
            except Exception:
                pass
        if not clients:
            _rooms.pop(room, None)
