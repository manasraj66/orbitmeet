from pydantic import BaseModel
class CreateMeetingRequest(BaseModel):
    name: str = 'Host'
class JoinMeetingRequest(BaseModel):
    code: str
    name: str = 'Guest'
