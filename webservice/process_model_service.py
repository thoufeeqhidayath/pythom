from flask import request, jsonify, Blueprint

from repository import process_model_repolib


processmodel_api=Blueprint("processModel","__name__")
process_model_service=process_model_repolib.ProcessModelRepo()

class ProcessModelService:
    def __init__(self):
        pass

@processmodel_api.route("/process_model/create",methods=['POST'])
def create():
 process_model=request.get_args.get("process_model")
 process_model_service.create(process_model)
 return jsonify({"status":"created"}),200

@processmodel_api.route("/process_model/delete",methods=['DELETE'])
def delete():
    process_id=int(request.args.get("id"))
    process_model_service.delete(process_id)
    return jsonify({"status":"deleted"}),200

@processmodel_api.route("/process_model/update",methods=['PUT'])
def update():
    process_id=int(request.args.get("id"))
    process_model=request.args.get("process_model")
    process_model_service.update(process_id,process_model)
    return jsonify({"status": "updated"}), 200


@processmodel_api.route("/process_model/retrieve_by_id",methods=['GET'])
def retrieve_by_id(self):
    user_id=int(request.args.get("process_id"))
    return jsonify(process_model_service.retrieve_by_id(user_id))

@processmodel_api.route("/proess_model/retrieve-all",methods=['GET'])
def retrieve_all(self):
     return jsonify(process_model_service.retrieve_all())
