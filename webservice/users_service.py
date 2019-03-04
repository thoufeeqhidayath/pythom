import json

from flask import Blueprint, request, jsonify
import repository.process_run_repolib
from repository import process_run_repolib, user_repolib

users_api=Blueprint("users",__name__)
user_repo=user_repolib.UserRepo()

class UsersService:
    def __init__(self):
        pass

@users_api.route("/user/create",methods=['POST'])
def create():
    user=request.args.get("user")
    user_repo.create(user)
    return jsonify({"status":"created"}),200


@users_api.route("/user/delete",methods=['DELETE'])
def delete():
    user_id=request.args.get("user_id")
    user_repo.delete(int(user_id))
    return jsonify({"status":"deleted"}),200

@users_api.route("/user/update",methods=['PUT'])
def update():
    user_id=request.args.get("user_id")
    user=request.args.get("user")
    user_repo.update(int(user_id),user)
    return jsonify({"status": "updated"}), 200

@users_api.route("/user/retrieve_by_id",methods=['GET'])
def retrieve_by_id():
    user_id=request.args.get("user_id")
    return jsonify(json.loads(user_repo.retrieve_by_id(int(user_id)))),200

@users_api.route("/user/retrieve_all",methods=['GET'])
def retrieve_all():
     return jsonify(json.loads(user_repo.retrieve_all())),200
