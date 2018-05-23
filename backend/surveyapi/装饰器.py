from functools import wraps


def login_required(f):
    # @wraps(f)
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


print(create_task.__doc__)  # 输出`这个是被修饰的函数`
print(create_task.__name__)  # 输出`create_task`
create_task()
