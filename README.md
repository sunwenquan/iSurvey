# iSurvey

一个问卷调查项目

## models设计

### User  用户表  __tablename__ = users
    '''
    #某个用户所有的调查表
    #建立一个１对ｎ的关系
    #使用surveys代表当前用户填写的所有问卷调查
    id
    name
    email
    password
    surveys = db.relationship('Survey',backref='creator')
    user.surveys可以获得当前用户所有的问卷调查
    '''
### Survey 调查表  __tablename__ = surveys
    '''
    id
    name # 问卷调查名
    created_at  # 问卷调查创建时间
    questions = db.relationship('Question',backref='survey')
    # survey.questions 可以获得某个调查表中的所有question
    creator_id = ... ForeignKey('users.id')
    # survey.creator可以获得当前问卷调查对应的user.
    '''

### Question 问题表 __tablename__ = questions
    '''
    id
    content # 内容
    created_at # 创建时间
    survey_id  = .... ForeignKey('surveys.id')  # 标识该问题所属的调查表
    # 问题选项 例如：A  B  C  D
    choises = db.relationship('Choise',backref='question')
    # 根据问题找该问题对应的所有的选项
    # question.choises即可
    '''

### Choise  选项表  __tablename__ = choises
    '''
    id
    content # 内容
    is_selected  # 是否选中
    created_at  # 创建时间
    # 标识该选项所属的问题
    question_id = db.Colunm(db.Integer, db.ForeignKey('questions.id'))    
    '''











