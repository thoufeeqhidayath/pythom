from flask import Blueprint, request

from repository import atom_repolib

atom_api=Blueprint("/atom_api",__name__)
AtomRepo=atom_repolib.AtomRepo()
class AtomService:
    def __init__(self):
        pass

@atom_api.route("/atom/create",methods=['POST'])
def create():
    atom=request.args.get("atom")
    AtomRepo.create(atom)
    return "created"

@atom_api.route("/atom/delete",methods=['POST'])
def delete():
   atom_id=int(request.args.get("atom_id"))
   AtomRepo.delete(atom_id)
   return "deleted"

@atom_api.route("/atom/update",methods=['PUT'])
def update():
    update_id=request.args.get("atom_id")
    update_atom=request.args.get("atom")
    AtomRepo.update(update_id,update_atom)
    return "updated"

@atom_api.route("/atom/retrieve_by_id",methods=['GET'])
def retrieve_by_id():
      retrieve_id=request.args.get("atom_id")
      return AtomRepo.retrieve_by_id(retrieve_id)

@atom_api.route("/atom/retrieve_all",methods=['GET'])
def retrieve_all():
    return AtomRepo.retrieve_all()










