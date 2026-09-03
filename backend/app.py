from flask import Flask
from routes.query import query_router
from routes.feedback import feedback_router
from utils.database import db
from utils.config import DATABASE_URL


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(feedback_router)
app.register_blueprint(query_router)


@app.route("/")
def home():
    return "MAINT AI Backend Running"


if __name__ == "__main__":
    app.run(debug=True)