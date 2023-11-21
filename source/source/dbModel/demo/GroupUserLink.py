from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from source.dbModel.TaskTag import *
from source.config.flaskConfig import *
from typing import List

class GroupUserLink(db.Model, BaseData):
    groupId = db.Column(db.Integer, unique=False)
    userId = db.Column(db.Integer, unique=False)
    
    __table_args__ = (
        db.UniqueConstraint('groupId', 'userId', name='_group_user_unique'),
    )
    
    def __init__(self, 
                 groupId:int, userId:int):
        self.groupId = groupId
        self.userId = userId
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)