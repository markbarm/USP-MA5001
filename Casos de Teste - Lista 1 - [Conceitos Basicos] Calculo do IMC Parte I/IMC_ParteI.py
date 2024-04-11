
while True:
    try:
        altura,massa=map(float,input().split(","))
        print(format(massa/altura**2,'.2f'),end=' ')
    except EOFError:
        break