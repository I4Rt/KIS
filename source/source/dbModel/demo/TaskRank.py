from __future__ import annotations
from source.dbModel.BaseData import *
from source.config.flaskConfig import *
from typing import List

class TaksRank(db.Model, BaseData):
    name = db.Column(db.String(150), unique=True)
    
    def __init__(self, 
                 name:str):
        self.name = name
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)    
