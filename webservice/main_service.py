from flask import Flask

from webservice.atom_service import atom_api
from webservice.process_model_service import processmodel_api
from webservice.process_run_service import ProcessRunService, processrun_api
from webservice.users_service import users_api

api=Flask(__name__)
api.register_blueprint(atom_api)
api.register_blueprint(users_api)
api.register_blueprint(processrun_api)
api.register_blueprint(processmodel_api)

@api.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    api.run()