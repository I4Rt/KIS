from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.TaskTagLink import *
from source.config.flaskConfig import *
from typing import List

class GroupUserRole(db.Model, BaseData):
    groupUserLinkId = db.Column(db.Integer, unique=False)
    groupUserRoleId = db.Column(db.Integer, unique=False)
    
    __table_args__ = (
        db.UniqueConstraint('groupUserLinkId', 'groupUserRole', name='_groupUserLinkId_groupUserRole_unique'),
    )
    
    def __init__(self, 
                 groupUserLinkId:int, groupUserRoleId:int):
        self.groupUserLinkId = groupUserLinkId
        self.groupUserRoleId = groupUserRoleId
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
        
    
