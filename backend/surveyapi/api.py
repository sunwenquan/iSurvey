"""
RESTful  API
处理前端发来的请求
返回JSON格式的响应数据
"""

from flask import Blueprint,jsonify,request
from .models import db,Survey,Question,Choice,User

api = Blueprint('api',__name__)

@api.route('/login/',methods=['POST'])
def login():
    return "ok"

@api.route('/signin/',methods=['POST'])
def signin():
    return "ok"

@api.route('/signout/',methods=['POST'])
def signout():
    return "ok"

@api.route('/surveys/',methods=['GET','POST'])
def survey_list():
    # 如果是GET请求，返回所有surveys
    # 如果是POST请求，添加一个survey到 surveys中
    return "ok"


@api.route('/survey/<int:id>/',methdos=['GET','PUT','DELETE'])
def survey(id):
    # 如果是GET 请求，根据id返回指定的survey
    # 如果是PUT请求，根据id修改指定的survey
    # 如果是DELETE请求，根据id删除指定的survey
    return "ok"


