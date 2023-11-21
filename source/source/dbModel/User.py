from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from source.dbModel.Group import *
from source.dbModel.LinkTables import *
from source.config.flaskConfig import *
from typing import List

class User(db.Model, BaseData):
    name = db.Column(db.String(150), unique=False)
    surname = db.Column(db.String(150), unique=False)
    login = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(300), unique=False)
    role = db.Column(db.String(120))
    acceptedTasks = db.relationship('Task', backref='acceptor', lazy=True, foreign_keys='Task.acceptorId')
    createdTasks = db.relationship('Task', backref='creator', lazy=True, foreign_keys='Task.creatorId')
    
    groups = db.relationship('Group', secondary=UserGroupLink.__table__, back_populates='users')
    
    def __init__(self, 
                 name:str, surname:str, 
                 login:str, password:str, 
                 role:str = "USER"):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.role = role
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
    
    def addTask(self, name, dueTo, info = '', acceptor = None, group: Group | None = None):
        if group:
            for user_group in self.groups:
                if user_group.group == group and user_group.role != 'EDITOR':
                    raise Exception(f'Пользователь {self.login} не может добавить в группу {group.id}_{group.name} задач: Текущаяя роль - {self.role}')
        if not acceptor:
            task = Task(name, self, self, dueTo, info = info, group=group)
        else:
            task = Task(name, self, acceptor, dueTo, info = info, group=group)
        task.save()
        
    
    def addGroup(self, name, info = '', users = []):
        gr = Group(name, info=info)
        gr.save()
        gr.addMember(self, 'EDITOR')
        for u in users:
            gr.addMember(u)
        gr.save()
        
    def getGroups(self):
        return self.groups
    
    def addMemberToGroop(self, group, member, role = 'CONSUMER'):
        if 'EDITOR' in UserGroupLink.getByMemberIdAndGroupId(self.id, group.id):
            try:
                group.addMember(member, role)
            except:
                return False
            return True
        return False
        