from fastapi import APIRouter
router = APIRouter(prefix='/api')
@router.get('/health')
def health(): return {'status': 'ok'}
@router.get('/stats')
def stats(): return {'rooms': 0}
