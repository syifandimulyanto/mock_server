from app.membership.models import Member

def test_create_new_member():
    '''
    Testing for successful create new member model
    '''
    
    register = {}
    register['project'] = 'piggybank'
    register['password'] = 'coba123'

    new_member = Member(**register)