from flask import Flask

from controllers.process_model_service import ProcessModelApi
from webservice.go_service import go_api
from webservice.process_type_service import ProcessTypeApi

app=Flask(__name__)

app.register_blueprint(ProcessModelApi)
app.register_blueprint(go_api)
app.register_blueprint(ProcessTypeApi)
app.run()
