from flask import Flask

from controllers.process_run_service import processRun

app=Flask(__name__)
app.register_blueprint(processRun)
app.run()