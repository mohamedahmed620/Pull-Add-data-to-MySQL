from flask_app import app
from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller

from flask_app.models.dojo_model import dojo_model
from flask_app.models.ninja_model import ninja_model

if __name__ == "__main__":
    app.run(debug=True, port =5001)
