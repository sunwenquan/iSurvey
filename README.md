# iSurvey

一个问卷调查项目

## API概要说明

| 请求方法 | 请求URL        | 描述                | 状态码 |
| -------- | -------------- | ------------------- | ------ |
| POST     | /api/register/ | 注册                | 201    |
| POST     | /api/signin/   | 登录                | 201    |
| GET      | /api/signout/  | 退出                | 200    |
| POST     | /api/surveys/  | 添加问卷调查        | 201    |
| GET      | /api/surveys/  | 获取所有问卷调查    | 200    |
| GET      | /api/survey/2/ | 获得id为2的问卷调查 | 200    |
| PUT      | /api/survey/2/ | 修改id为2的问卷调查 | 201    |

## 接口详细说明

### 1. 登录

接口地址：http://127.0.0.1:5000/api/signin/

请求方式：POST

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型   | 说明 |
> | -------- | ------ | ---- |
> | email    | string | 邮箱 |
> | password | string | 密码 |
> |          |        |      |
> |          |        |      |
>
> 返回参数说明
>
> | 参数名称      | 类型   | 说明                                |
> | ------------- | ------ | ----------------------------------- |
> | message       | string | 提示信息                            |
> | authenticated | bool   | true代表认证成功，false代表认证失败 |
> | token         | string | 认证成功时返回此字段                |
> |               |        |                                     |

示例

> 请求示例JSON
>
> ```json
> {
>     "email":"gavinsun@qq.com",
>     "password":"123456"
> }
> ```
>
> 返回示例JSON
>
> ```json
> {
>     "message":"认证成功", 
>     "authenticated":true,
>     "token":"IASDFASAFK23429877SDAN2334!FASD"
> }
> ```
>
> ```json
> {
>     "message":"认证失败", 
>     "authenticated":false,
> }
> ```

### 2.注册

接口地址：http://127.0.0.1:5000/api/register/

请求方式：POST

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

### 3.退出

接口地址：http://127.0.0.1:5000/api/signout/

请求方式：GET

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

### 4.添加问卷调查

接口地址：http://127.0.0.1:5000/api/surveys/

请求方式：POST

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

### 5.获取所有问卷调查

接口地址：http://127.0.0.1:5000/api/surveys/

请求方式：GET

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

### 6. 获取某个问卷调查

接口地址：http://127.0.0.1:5000/api/survey/2/

请求方式：GET

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

### 7.提交问卷调查

接口地址：http://127.0.0.1:5000/api/survey/2/

请求方式：POST

接口参数：

> 请求参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |
>
> 返回参数说明
>
> | 参数名称 | 类型 | 说明 |
> | -------- | ---- | ---- |
> |          |      |      |
> |          |      |      |

示例

> 请求示例JSON
>
> ```json
> 
> ```
>
> 返回示例JSON
>
> ```json
> 
> ```

## 匿名问卷调查

只关注调查结果，问题的各个选项被勾选多少次，choices.number/choices.choiced


## 实名问卷调查
1. 关注调查结果，问题的各个选项被勾选多少次，choises.number
2. 关注每个人填写的调查表   id   users.id   choises.id  


## models初步设计

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
    selected  # 记录选项被选中的个数
    created_at  # 创建时间
    # 标识该选项所属的问题
    question_id = db.Colunm(db.Integer, db.ForeignKey('questions.id'))    
    '''











