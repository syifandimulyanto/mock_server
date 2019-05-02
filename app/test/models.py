from datetime import datetime
from typing import Optional, Union, Dict
from pydantic import BaseModel

class DataFromUser(BaseModel):
    '''
    The data from
    '''
    project_name: str
    version: str
    path: str
    method: str
    body: Optional[Union[dict, list]]
    query_string: Optional[dict]
    