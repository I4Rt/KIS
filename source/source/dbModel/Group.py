from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from source.dbModel.LinkTables import *
from source.config.flaskConfig import *
from typing import List


class Group(db.Model, BaseData):
    name = db.Column(db.Text, unique=False)
    info = db.Column(db.Text, unique=False)
    createTime = db.Column(db.DateTime(timezone=False))
    fileSystemRoute = db.Column(db.Text, nullable=False)
    
    tasks = db.relationship('Task', backref='tasks', lazy=True, foreign_keys='Task.groupId')
    
    users = db.relationship('User', secondary=UserGroupLink.__table__, back_populates='groups')
    
    
    def __init__(self, 
                 name:str, info:str = '', 
                 createTime = datetime.now(), 
                 fileSystemRoute:str = ""):
        self.name = name
        self.info = info
        self.createTime = createTime
        self.fileSystemRoute = fileSystemRoute
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
        
    def addMember(self, user, role = 'CONSUMER'):
        UserGroupLink(user, self, role).save()
        
    
    
    def getMembers(self):
        return self.users
    
    def getTasks(self) -> List[Task]:
        return self.tasks
        