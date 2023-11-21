from source.config.flaskConfig import *
from source.config.blueprints import *
from source.controller.restControllers.fileSysMain import *
from source.controller.templatesControlers.testMain import *

from source.dbModel.LinkTables import *
from source.dbModel.User import *
from source.dbModel.Group import *
from source.dbModel.Task import *

kis.register_blueprint(fileSystemBlueprint)
kis.register_blueprint(appBlueprint)

if __name__ == '__main__':
    with kis.app_context():
        db.create_all()
        user1 = User.getByID(7)
        print(user1.login, user1.getGroups())
        
        user12:User = User.getByID(11)
        # user12.addGroup('user_groop1', users=[User.getByID(1),User.getByID(5)])
        print(user12.addMemberToGroop(user12.getGroups()[0], user1))
        
        print(user1.login, user1.getGroups())
        gr = Group.getByID(6)
        print(gr.getMembers())
        
    