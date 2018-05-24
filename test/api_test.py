import requests

# 如何发送get请求
# GET http://127.0.0.1:5000/api/todos/
def test_get():
    url = "http://127.0.0.1:5000/api/todos/"
    r = requests.get(url)
    # print(resp.status_code)
    print(r.status_code,r.json())
# 如何发送post请求
# POST http://127.0.0.1:5000/api/todos/
def test_post():
    url = 'http://127.0.0.1:5000/api/todos/'
    data = {
        "content":"11点10分，准时订餐"
    }
    r = requests.post(url,json=data)
    # print(dir(r))
    print(r.status_code,r.json()['text'])

def test_delete():
    url = ' http://127.0.0.1:5000/api/todos/11/'
    r = requests.delete(url)
    print(r.json())
def test_put():
    url =  'http://127.0.0.1:5000/api/todos/12/'
    data = {
        'content':'明天放假'
    }
    r = requests.put(url,json=data)
    print(r.json())

# test_put()
# test_post()
# test_get()


