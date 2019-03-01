from flask import Blueprint, request

from repository import atom_repolib

atom_api = Blueprint("atom_api", __name__)
AtomRepo = atom_repolib.AtomRepo()


class AtomService:
    def __init__(self):
        pass


@atom_api.route("atom/create", methods=['POST'])
def create():
    atom = request.args.get("atom")
    AtomRepo.create(atom)


@atom_api.route("atom/delete", methods=['DELETE'])
def delete():
    delete_id = request.args.get("delete_id")
    AtomRepo.delete(delete_id)


@atom_api.route("atom/delete", methods=['PUT'])
def update():
    update_id = request.args.get("id")
    update_atom = request.args.get("atom")
    AtomRepo.update(update_id, update_atom)


@atom_api.route("atom/retrieve_by_id", methods=['GET'])
def retrieve_by_id():
    retrieve_id = request.args.get("id")
    AtomRepo.retrieve_by_id(retrieve_id)


@atom_api.route("atom/retrieve_all", methods=['GET'])
def retrieve_all():
    AtomRepo.retrieve_all()










