from flask import Blueprint, request, jsonify

from repository.go_repolib import GoRepoLib

go_api=Blueprint("go_service"," ")

class GoService:
    def __init__(self):
        pass


@go_api.route("/go/get_go",methods=["GET"])
def get_go_by_masterprocess():

    try:
        masterprocess = request.args.get("master_process")
        go_repo = GoRepoLib()
        go = go_repo.getgo_by_processrun(masterprocess)
        if go is not False:
            return go
        else:
            return jsonify("message:process not found")
    except Exception as e:
        return jsonify({"status":"error","message":"check master_process"})


