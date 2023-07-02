def print_packed(*args, **kwargs):
    for value in args:
        print(value)
    for key, value in kwargs.items():
        print(value)
            
print_packed(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)