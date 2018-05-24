from functools import wraps


import requests
class Api():
    host = 'http://127.0.0.1:5000'
    def url(self, rule, **options):# 接收函数和参数
        def decorator(f):  # 接收函数
            full_url = self.host + rule
            method = options.pop('method', None)
            json = options.pop('json',None)
            if method not in ['GET','POST','PUT','DELETE']:
                raise RuntimeError("请求方法必须是'GET','POST','PUT' or 'DELETE'")
            @wraps(f)
            def request(*arg,**kwargs): #接收函数的参数
                if method == 'GET':
                    r = requests.get(full_url,*arg,**kwargs)
                elif method == 'POST':
                    kwargs['json']=json
                    print(kwargs)
                    r = requests.post(full_url, *arg, **kwargs)
                    kwargs.pop('json')
                elif method == 'DELETE':
                    r = requests.delete(full_url,*arg,**kwargs)
                elif method == 'PUT':
                    r = requests.put(full_url,*arg,json=json,**kwargs)

                f(r, *arg,**kwargs)
            return request
        return decorator

api = Api()

@api.url('/api/survey/1/',method='GET')
def get(resp):
    print(resp.json())

@api.url('/api/todos/',method='POST',json={'content':"YYYYYYYYYYY"})
def add(resp):
    print(resp.json())

@api.url('/api/todos/16/',method='DELETE')
def delete(resp):
    print(resp.json())


json = {
    
        "name": "如何提高注意力",
        "questions": 
        [
            {   "id":3,
                "text": "",
                "choiced": 8,
            },
            {   "id":1,
                "text": "",
                "choiced": 1,
            },
            {   "id":2,
                "text": "",
                "choiced": 5,
            }
        ]
    
}


@api.url('/api/survey/1/',method='PUT',json=json)
def put(resp):
    print(resp.json())

# add()
# delete()
put()
get()

