from source.config.flaskConfig import *
from source.dbModel.BaseData import *


class UserGroupLink(db.Model, BaseData):
    __tablename__ = 'userGroupLink'

    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    groupId = db.Column(db.Integer, db.ForeignKey('group.id'))
    role = db.Column(db.String(50), nullable=False)

    

    def __init__(self, user, group, role):
        self.userId = user.id
        self.groupId = group.id
        self.role = role
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)
        
    
    @classmethod 
    def getByMemberIdAndGroupId(cls, userId, groupId) -> str:
        res = db.session.query(UserGroupLink.role).filter(
                    and_(
                    UserGroupLink.userId == userId,
                    UserGroupLink.groupId == groupId
                )
            ).all()
        if res:
            return [data[0] for data in res]
        return []
            
    def save(self):
        if not db.session.query(UserGroupLink.role).filter(
                    and_(
                    UserGroupLink.userId == self.userId,
                    UserGroupLink.groupId == self.groupId,
                    UserGroupLink.role == self.role
                )
            ).all():
            db.session.add(self)
            db.session.commit()
            return
        raise Exception('userGroupLink_error')