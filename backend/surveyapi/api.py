"""
RESTful  API
处理前端发来的请求
返回JSON格式的响应数据
"""

from flask import Blueprint,jsonify,request
from flask import current_app
from .models import Survey,Question,Choice,User,db
from .decorator import  token_required
from datetime import datetime, timedelta

api = Blueprint('api',__name__)

@api.route('/login/',methods=['POST'])
def login():
    # 获得登录信息，前端发来的是json格式的登录信息
    data = request.get_json()
    user = User.authenticate(**data) 
    if not user:
        return jsonify({'message':'用户名或密码错误','authenticated':False}),401
    
    # 验证通过，生成一个token给客户端
    import jwt
    token = jwt.encode({
            'sub':user.email,
            'iat':datetime.utcnow(),
            'exp':datetime.utcnow + timedelta(30)
            },
            current_app.config['SECRET_KEY']
            )
    return jsonify({'token':token})
    
    return "ok"

@api.route('/signin/',methods=['POST'])
def signin():
    '''
    url: /signin/
    method:POST
    json data : { "email":"gavinsun@qq.com",
        "password":"888888"
    }
    '''
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()),201

@api.route('/signout/',methods=['POST'])
def signout():
    return "ok"
# @token_required
@api.route('/surveys/',methods=['GET','POST'])
def survey_list():
    # 如果是GET请求，返回所有surveys
    if request.method == 'GET':
        surverys = Survey.query.all()
        data = {
            "surveys":[ survery.to_dict() for survery in surverys]
        }
        print(data)
        return jsonify(data)
    # 如果是POST请求，添加一个survey到 surveys中
    elif request.method =='POST':
        '''
        url:  /api/surveys/
        method: POST
        json data: 
        {
            "survey":{
                "name":"如何提高注意力",
                "questions":[
                    { 
                        "text":"",
                        "choies":[]
                     },
                    {  
                        "text":"",
                        "choies":[]
                    },
                ]
            }

        }

        '''
        data = request.get_json()
        survey = Survey(name=data['name'])
        questions = []
        for question in data['questions']:
            # q代表着一个实例，一条questions表中的记录
            q = Question(text=question['text'])
            q.choices = [Choice(text=choice['text']) for choice in question['choices']]
            questions.append(q)
        survey.questions = questions
        survey.creator = User.query.get(1)
        db.session.add(survey)
        db.session.commit()
        return jsonify(survey.to_dict()),201

# @token_required
@api.route('/survey_admin/<int:id>/',methods=['GET','PUT','DELETE'])
def survey_admin(id):
    survey = Survey.query.get(id)
    # 如果是GET 请求，根据id返回指定的survey
    if  request.method == 'GET':
        return jsonify(survey.to_dict())
    # 如果是PUT请求，根据id修改指定的survey
    elif request.method == 'PUT':
        data = request.get_json()
        questions = []
        for question in data['questions']:
            # q代表着一个实例，一条questions表中的记录
            q = Question(text=question['text'])
            q.choices = [Choice(text=choice['text']) for choice in question['choices']]
            questions.append(q)
        survey.questions = questions
        # survey.creator = User.query.get(1)
        db.session.add(survey)
        db.session.commit()
        return jsonify(survey.to_dict()),201
    # 如果是DELETE请求，根据id删除指定的survey
    elif request.method == 'DELETE':
        for question in survey.questions:
            for choice in question.choices:
                db.session.delete(choice)
            db.session.delete(question)
        db.session.delete(survey)
        db.session.commit()
        return "删除成功"

# 普通用户
@api.route('/survey/<int:id>/',methods=['GET','PUT'])
def survery(id):
    survey = Survey.query.get(id)
    # 如果是GET 请求，根据id返回指定的survey
    if  request.method == 'GET':
        return jsonify(survey.to_dict())
    # 如果是PUT请求，根据id修改指定的survey
    elif request.method == 'PUT':
        data = request.get_json()
        for item in data['questions']:
            #  获得用户所选择的选项的id
            choice_id = item['choiced']
            # 获得id为choice_id的选项
            choice = Choice.query.get(choice_id) 
            # 把用户所选择的选项+1
            choice.selected = choice.selected + 1
        # 更改到数据库
        db.session.commit()
        return jsonify(survey.to_dict()),201


