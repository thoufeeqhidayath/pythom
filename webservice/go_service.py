import json

from flask import Blueprint, request, jsonify

from repository.go_repolib import GoRepoLib
from repository.process_run_repolib import ProcessRunsRepo

go_api=Blueprint("go_service"," ")

class GoService:
    def __init__(self):
        pass


@go_api.route("/go/get_go",methods=["GET"])
def get_go_by_masterprocess():
        returnf=[]
        go_repo = GoRepoLib()
        process_repo = ProcessRunsRepo()
        masterprocess = request.args.get("master_process")
        master_process=process_repo.getid_by_master(masterprocess)
        length=len(master_process)
        for i in range(length):
            go = go_repo.getgo_by_processrun(str(master_process[i]))
            if go is not None:
             returnf.append(go)
        return json.dumps(returnf,indent=2)



