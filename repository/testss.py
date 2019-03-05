from flask import Flask

from controllers.process_model_service import ProcessModelApi
from webservice.go_service import go_api

app=Flask(__name__)

app.register_blueprint(ProcessModelApi)
app.register_blueprint(go_api)
app.run()
