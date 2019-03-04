import json

from flask import Blueprint, request

from repository import process_model_repolib
from repository.process_type_repolib import ProcessTypeRepo

ProcessModelApi=Blueprint("ProcessModelApi",__name__)

class ProcessModelService:
    def __init__(self):
        pass


@ProcessModelApi.route("/process_model/get_gojs",methods=["GET"])
def retrieveg_gojs_process_type():
  processModel=process_model_repolib.ProcessModelRepo()
  process_type = ProcessTypeRepo()
  gojs=[]
  process_name=request.args.get("processType")
  process_id=process_type.retrieve_data(process_name)
  for  i in process_id:
      gojs.append(processModel.retrievegojs_by_processtype(i))
  return json.dumps(gojs,indent=1)





