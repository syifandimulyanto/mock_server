from app.review.models import EachVersionData, MockApiData
from datetime import datetime

def test_create_data():
    '''
    Testing for successful create new member model
    '''

    jirachi = MockApiData(**{'project':'jirachi'})
        
    each_data = {
        'date': datetime.utcnow(),
        'data': {
            '/test':{
                "post": {
                }
            }
        }
    }

    data = EachVersionData(**each_data)

    jirachi.version.append(data)