from datetime import datetime, timezone
from pathlib import Path
import sqlite3, uuid
from fastapi import APIRouter, HTTPException, Header
from backend.core.room_manager import create_room, get_room, all_rooms
from backend.models.schemas import CreateMeetingRequest, JoinMeetingRequest

router = APIRouter(prefix='/api')
DB = Path(__file__).resolve().parents[2] / 'meeting_history.sqlite3'

def init_db():
    with sqlite3.connect(DB) as con:
        con.execute('CREATE TABLE IF NOT EXISTS meeting_history (room_id TEXT PRIMARY KEY, created_at TEXT NOT NULL, ended_at TEXT, status TEXT NOT NULL DEFAULT \'created\')')
init_db()

@router.post('/create')
def create(req: CreateMeetingRequest):
    room = create_room()
    with sqlite3.connect(DB) as con:
        con.execute('INSERT OR REPLACE INTO meeting_history(room_id,created_at,status) VALUES(?,?,?)',(room.id,room.created_at,'created'))
    return {'room_id': room.id, 'name': req.name, 'host_token': room.host_token}

@router.post('/join')
def join(req: JoinMeetingRequest):
    room = get_room(req.code)
    if not room: raise HTTPException(404, 'Room not found. Ask the host to create a new meeting.')
    request_id = uuid.uuid4().hex
    room.lobby[request_id] = {'name': req.name or 'Guest', 'status':'pending', 'created_at':datetime.now(timezone.utc).isoformat()}
    return {'room_id': room.id, 'request_id':request_id, 'status':'pending'}

@router.get('/join-status/{room_id}/{request_id}')
def join_status(room_id: str, request_id: str):
    room=get_room(room_id)
    if not room: raise HTTPException(404,'Meeting has ended or server restarted.')
    item=room.lobby.get(request_id)
    if not item: raise HTTPException(404,'Join request not found.')
    return {'status':item['status']}

@router.get('/room/{room_id}/requests')
def join_requests(room_id: str, host_token: str = ''):
    room=get_room(room_id)
    if not room: raise HTTPException(404,'Room not found')
    if not host_token or host_token != room.host_token: raise HTTPException(403,'Only the host can view join requests.')
    return {'requests':[{'id':k,'name':v['name']} for k,v in room.lobby.items() if v['status']=='pending']}

@router.post('/room/{room_id}/requests/{request_id}/{decision}')
def decide_join(room_id: str, request_id: str, decision: str, host_token: str = Header(default='', alias='X-Host-Token')):
    room=get_room(room_id)
    if not room: raise HTTPException(404,'Room not found')
    if not host_token or host_token != room.host_token: raise HTTPException(403,'Only the host can approve requests.')
    if decision not in ('approve','deny'): raise HTTPException(400,'Decision must be approve or deny')
    item=room.lobby.get(request_id)
    if not item: raise HTTPException(404,'Join request not found')
    item['status']='approved' if decision=='approve' else 'denied'
    return {'status':item['status']}

@router.get('/history')
def history():
    with sqlite3.connect(DB) as con:
        rows=con.execute('SELECT room_id,created_at,ended_at,status FROM meeting_history ORDER BY created_at DESC LIMIT 20').fetchall()
    return {'meetings':[{'room_id':r[0],'created_at':r[1],'ended_at':r[2],'status':r[3]} for r in rows]}

@router.get('/stats')
def stats():
    with sqlite3.connect(DB) as con:
        total=con.execute('SELECT COUNT(*) FROM meeting_history').fetchone()[0]
        recent=con.execute('SELECT room_id,created_at,status FROM meeting_history ORDER BY created_at DESC LIMIT 20').fetchall()
    return {'active_rooms':len(all_rooms()),'total_meetings':total,'recent_meetings':[{'room_id':r[0],'created_at':r[1],'status':r[2]} for r in recent]}
