import json

from flask import Flask, Blueprint, jsonify, request

from webservice.process_run_service import process_repo, processrun_api

ProcessRunApi = Blueprint("processRun",__name__)
class processRunRepo:
    def __init__(self):
        pass

@ProcessRunApi.route('/processrunMethods', methods=['GET'])
def index():
    urls = {
        'GET: /processrun': 'View all processRun.',
        'GET: /processrun/process_id': 'View processRun of specific id.',
        'POST: /processrun': 'Create new processRun.',
        'PUT: /processrun': 'Update document of specific id.',
        'DELETE: /processrun': 'Delete document of specific id.'
    }
    return jsonify(urls=urls)

@ProcessRunApi.route("/ProcessRun/",methods=['POST'])
def create():
 try:
    process = request.args.get("process")
    process_repo.create(process)
    return jsonify({"status": "created"}), 200
 except:
     return jsonify({"status": "Error On Insert"}), 200



@ProcessRunApi.route("/ProcessRun/",methods=['DELETE'])
def delete():
    try:
        process_id = request.args.get("process_id")
        process_repo.delete(int(process_id))
        return jsonify({"status": "deleted"}), 200
    except:
        return jsonify({"status": "Error On Delete"}), 200


@ProcessRunApi.route("/ProcessRun/",methods=['PUT'])
def update():
    process_id=request.args.get("id")
    process=request.args.get("process")
    process_repo.update(int(process_id),process)
    return jsonify({"status": "update"}), 200



@ProcessRunApi.route("/ProcessRun/<process_id>",methods=['GET'])
def retrieve_by_id(process_id):
    try:
        process_data = process_repo.retrieve_by_id(process_id)
        if process_data is not None:
            return jsonify(json.loads(process_data))
        else:
            return jsonify({"http_status": 400, "message": "errors during retrievel"})
    except:
        return jsonify({"http_status": 400, "message": "invalid parameter"})



@ProcessRunApi.route("/ProcessRun/<user_name>",methods=['GET'])
def retrieve_by_name(user_name):
    process_data = process_repo.retrieve_by_name(user_name)
    if process_data is not None:
        return jsonify(json.loads(process_data))
    else:
        return jsonify({"http_status": 400, "message": "errors during retrievel"})


@ProcessRunApi.route("/processRun/",methods=['GET'])
def retrieve_all():
    process_data = process_repo.retrieve_all()
    if process_data is not None:
        return jsonify(json.loads(process_data))
    else:
        return jsonify({"http_status": 400, "message": "errors during retrievel"})

