from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel

class EachVersionData(BaseModel):
    date: datetime = datetime.utcnow()
    data: Dict[str, dict] = []

class MockApiData(BaseModel):
    '''
    Property of MockApiData
    '''
    id: int = None
    project: str
    version: List[EachVersionData] = []