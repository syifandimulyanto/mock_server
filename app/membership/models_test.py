from app.membership.models import Member

def test_answer():
    '''
    Testing for successful create new member model
    '''
    
    register = {}
    register['project'] = 'piggybank'
    register['password'] = 'coba'

    new_member = Member(**register)