import json

from flask import Blueprint, request, jsonify
import repository.process_run_repolib
from repository import process_run_repolib

processrun_api=Blueprint("process_run_service"," ")
process_repo=process_run_repolib.ProcessRunsRepo()

class ProcessRunService:
    def __init__(self):
        pass

@processrun_api.route("/processRun/create",methods=['POST'])
def create():
 process=request.args.get("process")
 process_repo.create(process)
 return jsonify({"status":"created"}),200


@processrun_api.route("/processRun/delete",methods=['DELETE'])
def delete():
    process_id=request.args.get("process_id")
    process_repo.delete(int(process_id))
    return jsonify({"status": "deleted"}), 200

@processrun_api.route("/processRun/update",methods=['PUT'])
def update():
    process_id=request.args.get("id")
    process=request.args.get("process")
    process_repo.update(int(process_id),process)
    return jsonify({"status": "update"}), 200


@processrun_api.route("/processRun/retrieve_by_id",methods=['GET'])
def retrieve_by_id():
    process_id=int(request.args.get("process_id"))
    return jsonify(json.loads(process_repo.retrieve_by_id(process_id)))

@processrun_api.route("/processRun/retrieve_all",methods=['GET'])
def retrieve_all():
     return jsonify(json.loads(process_repo.retrieve_all()))

@processrun_api.route("/processRun/getid_by_masterprocess",methods=['GET'])
def getid_by_masterprocess():
    master_process=request.args.get("master_process")
