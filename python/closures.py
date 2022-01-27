def outer_fun(msg):
    message = msg

    def inner_fun(name):
        print(f'{message} {name}')

    return inner_fun


closure_fun = outer_fun('Hi')
closure_fun('Nitesh')
