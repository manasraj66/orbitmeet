from fastapi import APIRouter
router = APIRouter(prefix='/api')
@router.get('/scheduled')
def scheduled(): return {'meetings': []}
