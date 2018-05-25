

## 直接用命令行运行

首先，需要写一个wsgi.py，在wsgi.py中实例化app

然后，进入wsgi.py所在的目录，执行如下命令即可：

uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

## 使用配置文件运行

创建如下一个配置文件,假设配置文件的名字是survey.ini

```
[uwsgi]
module = wsgi:app

master = true  
processes = 4

socket = myproject.sock  
chmod-socket = 660  
vacuum = true

die-on-term = true
```

使用uwsgi  survey.ini启动app

注意：这里使用的soket