from datetime import datetime
from pydantic import BaseModel

class Member(BaseModel):
    '''
    Property of Member
    '''
    id: int = None
    project: str
    password: str
    signup_ts = datetime.utcnow()