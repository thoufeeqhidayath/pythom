import json
#atomrepo
#compound_model_repol
#molecule_model_repolilb
#user_repolib
#process_run_repolib
#process_model_repolib


from repository import user_repolib, usermodel_repolib, process_run_repolib, atom_repolib, molecule_model_repolib, \
    compound_model_repolib, process_model_repolib
from repository.atom_repolib import AtomRepo
from repository.process_run_repolib import ProcessRunsRepo
from repository.sample_repo import SampleRepo

t=ProcessRunsRepo()
print t.retrieve_all()
#t.create("gh")
#t=user_repolib.UserRepo()
#t.create({"userid":"1010","gojs": [{"nodeKeyProperty": "id","nodeDataArray": [{"id": 0,"App": "-Spread Sheet:Frost Config","Frequency":"0","img":"frames/AML3/image_Spread SheetFrost Config.jpg"},{"id": 1,"App": "-Spread Sheet:Temp File","Frequency":"1","img":"frames/AML3/image_Spread SheetTemp File.jpg"},{"id": 2,"App": "-Spread Sheet:BSA Status Master Report","Frequency":"1","img":"frames/AML3/image_Spread SheetBSA Status Master Report.jpg"},{"id": 3,"App": "-Risk Screening:login","Frequency":"1","img":"frames/AML3/image_Risk Screeninglogin.jpg"},{"id": 4,"App": "-Risk Screening:Search","Frequency":"1","img":"frames/AML3/image_Risk ScreeningSearch.jpg"},{"id": 5,"App": "-Risk Screening:Summary","Frequency":"1","img":"frames/AML3/image_Risk ScreeningSummary.jpg"},{"id": 6,"App": "-Spread Sheet:BSA Status Master Report-189","Frequency":"1","img":"frames/AML3/image_Spread SheetBSA Status Master Report-189.jpg"},{"id": 7,"App": "-Credit Check:Authentication","Frequency":"2","img":"frames/AML3/image_Credit CheckAuthentication.jpg"},{"id": 8,"App": "-Credit Check:Terms and Condition","Frequency":"2","img":"frames/AML3/image_Credit CheckTerms and Condition.jpg"},{"id": 9,"App": "-Credit Check:Home","Frequency":"1","img":"frames/AML3/image_Credit CheckHome.jpg"},{"id": 10,"App": "-Credit Check:Save Report","Frequency":"2","img":"frames/AML3/image_Credit CheckSave Report.jpg"},{"id": 11,"App": "-Spread Sheet:BSA Status Master Report-327","Frequency":"2","img":"frames/AML3/image_Spread SheetBSA Status Master Report-327.jpg"},{"id": 12,"App": "-Sanctions Check:app","Frequency":"2","img":"frames/AML3/image_Sanctions Checkapp.jpg"},{"id": 13,"App": "-Spread Sheet:BSA Status Master Report-367","Frequency":"2","img":"frames/AML3/image_Spread SheetBSA Status Master Report-367.jpg"},{"id": 14,"App": "-News and Social Media:Save Page","Frequency":"6","img":"frames/AML3/image_News and Social MediaSave Page.jpg"},{"id": 15,"App": "-Spread Sheet:BSA Status Master Report-395","Frequency":"5","img":"frames/AML3/image_Spread SheetBSA Status Master Report-395.jpg"},{"id": 16,"App": "-Credit Check:Home-513","Frequency":"1","img":"frames/AML3/image_Credit CheckHome-513.jpg"},{"id": 17,"App": "-Credit Check:Export Report","Frequency":"1","img":"frames/AML3/image_Credit CheckExport Report.jpg"}],"linkDataArray":[{"from": 0,"to":1,"text":1},{"from": 1,"to":2,"text":1},{"from": 2,"to":3,"text":1},{"from": 3,"to":4,"text":1},{"from": 4,"to":5,"text":1},{"from": 5,"to":6,"text":1},{"from": 6,"to":7,"text":1},{"from": 7,"to":8,"text":2},{"from": 8,"to":9,"text":1},{"from": 8,"to":16,"text":1},{"from": 9,"to":10,"text":1},{"from": 10,"to":11,"text":2},{"from": 11,"to":12,"text":2},{"from": 12,"to":13,"text":2},{"from": 13,"to":14,"text":2},{"from": 14,"to":15,"text":5},{"from": 15,"to":14,"text":4},{"from": 15,"to":7,"text":1},{"from": 16,"to":17,"text":1},{"from": 17,"to":10,"text":1}]}]})
#t.update(1,{"userid":"10003","gojs": [{"nodeKeyProperty": "id","nodeDataArray": [{"id": 0,"App": "-Spread Sheet:Frost Config","Frequency":"0","img":"frames/AML3/image_Spread SheetFrost Config.jpg"},{"id": 1,"App": "-Spread Sheet:Temp File","Frequency":"1","img":"frames/AML3/image_Spread SheetTemp File.jpg"},{"id": 2,"App": "-Spread Sheet:BSA Status Master Report","Frequency":"1","img":"frames/AML3/image_Spread SheetBSA Status Master Report.jpg"},{"id": 3,"App": "-Risk Screening:login","Frequency":"1","img":"frames/AML3/image_Risk Screeninglogin.jpg"},{"id": 4,"App": "-Risk Screening:Search","Frequency":"1","img":"frames/AML3/image_Risk ScreeningSearch.jpg"},{"id": 5,"App": "-Risk Screening:Summary","Frequency":"1","img":"frames/AML3/image_Risk ScreeningSummary.jpg"},{"id": 6,"App": "-Spread Sheet:BSA Status Master Report-189","Frequency":"1","img":"frames/AML3/image_Spread SheetBSA Status Master Report-189.jpg"},{"id": 7,"App": "-Credit Check:Authentication","Frequency":"2","img":"frames/AML3/image_Credit CheckAuthentication.jpg"},{"id": 8,"App": "-Credit Check:Terms and Condition","Frequency":"2","img":"frames/AML3/image_Credit CheckTerms and Condition.jpg"},{"id": 9,"App": "-Credit Check:Home","Frequency":"1","img":"frames/AML3/image_Credit CheckHome.jpg"},{"id": 10,"App": "-Credit Check:Save Report","Frequency":"2","img":"frames/AML3/image_Credit CheckSave Report.jpg"},{"id": 11,"App": "-Spread Sheet:BSA Status Master Report-327","Frequency":"2","img":"frames/AML3/image_Spread SheetBSA Status Master Report-327.jpg"},{"id": 12,"App": "-Sanctions Check:app","Frequency":"2","img":"frames/AML3/image_Sanctions Checkapp.jpg"},{"id": 13,"App": "-Spread Sheet:BSA Status Master Report-367","Frequency":"2","img":"frames/AML3/image_Spread SheetBSA Status Master Report-367.jpg"},{"id": 14,"App": "-News and Social Media:Save Page","Frequency":"6","img":"frames/AML3/image_News and Social MediaSave Page.jpg"},{"id": 15,"App": "-Spread Sheet:BSA Status Master Report-395","Frequency":"5","img":"frames/AML3/image_Spread SheetBSA Status Master Report-395.jpg"},{"id": 16,"App": "-Credit Check:Home-513","Frequency":"1","img":"frames/AML3/image_Credit CheckHome-513.jpg"},{"id": 17,"App": "-Credit Check:Export Report","Frequency":"1","img":"frames/AML3/image_Credit CheckExport Report.jpg"}],"linkDataArray":[{"from": 0,"to":1,"text":1},{"from": 1,"to":2,"text":1},{"from": 2,"to":3,"text":1},{"from": 3,"to":4,"text":1},{"from": 4,"to":5,"text":1},{"from": 5,"to":6,"text":1},{"from": 6,"to":7,"text":1},{"from": 7,"to":8,"text":2},{"from": 8,"to":9,"text":1},{"from": 8,"to":16,"text":1},{"from": 9,"to":10,"text":1},{"from": 10,"to":11,"text":2},{"from": 11,"to":12,"text":2},{"from": 12,"to":13,"text":2},{"from": 13,"to":14,"text":2},{"from": 14,"to":15,"text":5},{"from": 15,"to":14,"text":4},{"from": 15,"to":7,"text":1},{"from": 16,"to":17,"text":1},{"from": 17,"to":10,"text":1}]}]})
#t.delete(1)
#print t.create()
#print t.retrieve_all()
#print t.retrieve_by_id(1)

