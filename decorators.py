

def some_func():
    print('hey you guys')

def my_decorator(func):
    def inner():
        print('before func')
        func()
        print('after func')

    return inner

print('some func()')

some_func()

print('')

some_func_decorated = my_decorator(some_func)

print('some_func with decorator')

some_func_decorated()