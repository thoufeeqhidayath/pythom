import json

from flask import Blueprint, request, jsonify

from webservice.users_service import user_repo

UserApi = Blueprint("User",__name__)

class UserService:
    def __init__(self):
        pass

@UserApi.route('/UserMethods', methods=['GET'])
def index():
    urls = {
        'GET:/user/': 'View all processRun.',
        'POST:/user/': 'Create new processRun. (POST via json)',
        'PUT: /user/': 'Update document of specific id.',
        'DELETE:/user/': 'Delete document of specific id.'
    }
    return jsonify(urls=urls)

@UserApi.route("/user/",methods=['POST'])
def create():
 try:
     user = request.args.get("user")
     user_repo.create(user)
     return jsonify({"status": "created"}), 200
 except:
     return jsonify({"status": "error"})


@UserApi.route("/user/",methods=['DELETE'])
def delete():
 try:
     user_id = request.args.get("user_id")
     user_repo.delete(int(user_id))
     return jsonify({"status": "deleted"}), 200
 except:
     return jsonify({"status": "error"})


@UserApi.route("/user/",methods=['PUT'])
def update():
    try:
        user_id = request.args.get("user_id")
        user = request.args.get("user")
        user_repo.update(int(user_id), user)
        return jsonify({"status": "updated"}), 200
    except:
        return jsonify({"status": "error"})



@UserApi.route("/user/retrieve_by_id",methods=['GET'])
def retrieve_by_id():
    try:
        user_id = request.args.get("user_id")
        return jsonify(json.loads(user_repo.retrieve_by_id(int(user_id)))), 200
    except:
        return jsonify({"status": "error"})



@UserApi.route("/user/retrieve_all",methods=['GET'])
def retrieve_all():
    try:
        user_data=json.loads(user_repo.retrieve_all())
        return jsonify(user_data),200
    except:
        return jsonify({"status": "error"})
