def outer(msg):
    def inner():
        print('+'* 10)
        print(msg)
        print('+'* 10)
    return inner

f=outer('welcome')
f()
