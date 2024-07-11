def my_super_decorator(func):
    def wrapper():
        print('начинаем по декорированию')
        print('пока всё идет хорошо')
        func()
        print('заканчиваем декорирование')
        print('всем спасибо')

    return wrapper()


@my_super_decorator
def hello_world():
    print("hello world")


@my_super_decorator
def privet_mir():
    print("privet_mir")

if __name__ == '__main__':
    privet_mir()
    hello_world()
