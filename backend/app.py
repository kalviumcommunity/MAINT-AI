from flask import Flask

from routes.query import query_router
from routes.feedback import feedback_router
from routes.auth import auth_router
from routes.documents import documents_router

from utils.database import db
from utils.config import DATABASE_URL

# Import all models so SQLAlchemy registers the tables
from models import (
    User,
    Equipment,
    Document,
    DocumentChunk,
    Issue,
    Query,
    Feedback
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(feedback_router)
app.register_blueprint(query_router)
app.register_blueprint(auth_router)
app.register_blueprint(documents_router)


# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "MAINT AI Backend Running"


if __name__ == "__main__":
    app.run(debug=True)