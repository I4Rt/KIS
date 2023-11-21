from __future__ import annotations
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from source.dbModel.TaskTagLink import *
from source.config.flaskConfig import *
from typing import List

class TaskTag(db.Model, BaseData):
    name = db.Column(db.String(150), unique=True)
    
    def __init__(self, 
                 name:str):
        self.name = name
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
        
        
    def getTasksByTag(self) -> List[Task]:
        taskIds = [id[0] for id in db.session.query(TaskTagLink.taskId).filter(TaskTagLink.tagId == self.id).all()]
        tasks = db.session.query(Task).filter(Task.tagId.in_(taskIds)).all()
        return tasks
