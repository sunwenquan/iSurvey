from functools import wraps

from flask import jsonify,current_app
from flask import request
import jwt
# 对token进行解码可以使用pyJWT
# pyjwt : python 实现的  JSON Web Token： 
def token_required(f):
    '''
    验证前端发来的token信息是否合法，如果不合法，返回错误信息，不支持被装饰的函数f
    如果合法，执行被装饰的函数f
    '''
    @wraps(f)
    def __verfy(*args,**kwargs):
        # 要求前端发来的请求头中包含合法的认证
        # {'Authorization':'asdasdfaf asdfasfafadf asdfa'
        auth_headers = request.headers.get('Authorization','').split()
        error = {
                'message':'非法的token',
                'authenticated':False
        }
        print("如果验证失败，则return相应的信息")
        try:
            token = auth_headers[1]
            # 使用SECRET_KEY 解码
            data =jwt.decode(token,current_app.config['SECRET_KEY'])
            # 从解码获得的数据中获得sub键对应的邮箱
            email = data.get('sub')
            user = User.query.filter_by(email=email).first()
            # 如果认证不通过，抛出错误
            if not user:
                raise RuntimeError("用户不存在")
            # 否则，执行被装饰的函数,并把user作为第一个参数传给被装饰的函数
            return f(user,*args, **kwargs)
        except (jwt.InvalidTokenError,Exception) as e:
            print(e)
            return jsonify(error),401
    return __verfy


# 下面是装饰器写法的演示
def login_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        """这个是修饰函数"""

        print("如果验证失败，则return相应的信息，下面的f函数不再执行。")
        print("如果验证通过，则return f")
        return f("aaa", *args, **kwargs)
    return _verify


@login_required
def create_task(a):
    """这个是被修饰的函数"""
    print(a)
    print('create_task')

if __name__ == "__main__":
    print(create_task.__doc__)  # 输出`这个是被修饰的函数`
    print(create_task.__name__)  # 输出`create_task`
    create_task()
