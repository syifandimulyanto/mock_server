from flask import Flask

from app.membership.web.urls import membership
from app.review.web.urls import review

app = Flask(__name__)

app.register_blueprint(membership, url_prefix='/membership')
app.register_blueprint(review, url_prefix='/review')