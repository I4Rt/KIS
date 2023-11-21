from __future__ import annotations
from source.config.flaskConfig import *
from source.dbModel.BaseData import *
from source.dbModel.Task import *
from typing import List

class TaksStatus(db.Model, BaseData):
    name = db.Column(db.String(150), unique=True)
    
    def __init__(self, 
                 name:str):
        self.name = name
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
        
    def getTasksByStatus(self) -> List[Task]:
        return db.session.query(Task).filter(Task.statusId == self.id).all()
