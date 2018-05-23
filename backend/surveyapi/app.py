from flask import Flask

def create_app(app_name = 'survey_api'):
    # 创建Flask应用的实例
    app = Flask(app_name)
    # 加载配置信息
    app.config.from_object('surveyapi.config')
    from surveyapi.api import api
    # 注册蓝图
    app.register_blueprint(api,url_prefix="/api")
    from surveyapi.models import db
    # 使用db初始化app
    db.init_app(app)
    # 返回创建的app实例
    return app