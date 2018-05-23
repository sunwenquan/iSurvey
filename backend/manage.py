from surveyapi import api
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from surveyapi.app import create_app
from surveyapi.models import db,Survey,Question,Choice,User
# pip install flask-script
# pip install flask-migrate

app = create_app()
# 创建migrate实例
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.shell
def shell_ctx():
    return dict(app=app,
        db=db,
        Surver=Survey,
        Question=Question,
        User=User,
        Choice=Choice
    )

if __name__ == '__main__':
    manager.run()