import json

from flask import Blueprint

from repository.process_type_repolib import ProcessTypeRepo

ProcessTypeApi=Blueprint("process_type"," ")
class processTypeService:
    def __init__(self):
        pass

@ProcessTypeApi.route("/process_type/get_all",methods=["GET"])
def retrieve_all_processtypes():
    process_type_repo=ProcessTypeRepo()
    return json.dumps(process_type_repo.retrieve_all_processtypes())

