from flask import Flask

from app.membership.web.urls import membership
from app.review.web.urls import review
from app.test.web.urls import test
from app.setup.web.urls import setup

app = Flask(__name__)

@app.route('/')
def landing_page():
    return '''
<a href="membership">Login</a><br />
<a href="review/jirachi">Review</a><br />
<a href="test/jirachi/latest/test">Test</a><br />
<a href="setup/revision/jirachi/latest">Set Up</a><br />
    '''

app.register_blueprint(setup, url_prefix='/setup')
app.register_blueprint(membership, url_prefix='/membership')
app.register_blueprint(review, url_prefix='/review')
app.register_blueprint(test, url_prefix='/test')