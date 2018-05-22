# iSurvey

一个问卷调查项目

## models设计

### User  用户表  __tablename__ = users
    '''
    某个用户所有的调查表
    建立一个１对ｎ的关系
    使用surveys代表当前用户填写的所有问卷调查
    surveys = db.relationship('Survey',backref='creator')
    user.surveys可以获得当前用户所有的问卷调查
    '''
### Survey 调查表  __tablename__ = surveys
    '''
    creator_id = ... ForeignKey('users.id')
    survey.creator可以获得当前问卷调查对应的user.
    '''

### Question 问题表 __tablename__ = questions

### Choise  选项表  __tablename__ = choises


