import hashlib

while True:
    try:
        t = input('Digite uma string: \n')
    except KeyboardInterrupt:
        exit()
    t = hashlib.sha1(t.encode())
    print(t.hexdigest())