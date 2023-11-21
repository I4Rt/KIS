from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from source.dbModel.TaskTag import *
from source.config.flaskConfig import *
from typing import List

class TaskTagLink(db.Model, BaseData):
    tagId = db.Column(db.Integer, unique=False)
    taskId = db.Column(db.Integer, unique=False)
    
    __table_args__ = (
        db.UniqueConstraint('tagId', 'taskId', name='_task_tag_unique'),
    )
    
    def __init__(self, 
                 tagId:int, taskId:int):
        self.tagId = tagId
        self.taskId = taskId
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)