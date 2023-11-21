from __future__ import annotations
from source.dbModel.BaseData import *
from source.config.flaskConfig import *
from typing import List

class Task(db.Model, BaseData):
    name = db.Column(db.Text, unique=False)
    info = db.Column(db.Text, unique=False)
    createTime = db.Column(db.DateTime(timezone=False))
    dueTo = db.Column(db.DateTime(timezone=False))
    fileSystemRoute = db.Column(db.Text, nullable=False)
    
    creatorId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    acceptorId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    groupId = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)
    
    def __init__(self, 
                 name, 
                 creator: "User" | int, 
                 acceptor: "User" | int, 
                 dueTo: datetime,
                 createTime: datetime = datetime.now(),
                 info = '',
                 group: "Group" | int | None = None):
        self.name = name
        
        if type(creator) == int:
            self.creatorId = creator
        else:
            self.creatorId = creator.id
    
        if type(acceptor) == int:
            self.acceptorId = acceptor
        else:
            self.acceptorId = acceptor.id
            
        if type(group) == int:
            self.groupId = group
        else:
            self.groupId = group.id
            
        self.createTime = createTime
        self.dueTo = dueTo
        
        self.info = info
        
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
    
    
    
    # def getAcceptor(self) -> User:
    #     return db.session.query(User).filter(User.id == self.acceptorId).first()
    
    # def getCreator(self) -> User:
    #     return db.session.query(User).filter(User.id == self.creatorId).first()
        
    # def getTags(self) -> List[TaskTag]:
    #     tagsIds = [id[0] for id in db.session.query(TaskTagLink.tagId).filter(TaskTagLink.taskId == self.id).all()]
    #     tags = db.session.query(TaskTag).filter(TaskTag.id.in_(tagsIds)).all()
    #     return tags
    
    