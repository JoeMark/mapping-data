# A Decorator Function
def function_decorator(func):
    def wrapper():
        print('=' * 20)
        func()
        print('=' * 20)
    return wrapper

@function_decorator
def test():
    print('Joe-Mark Lippert')

test()

