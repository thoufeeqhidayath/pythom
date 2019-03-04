from flask import Flask

from controllers.process_model_service import ProcessModelApi

app=Flask(__name__)

app.register_blueprint(ProcessModelApi)

app.run()
