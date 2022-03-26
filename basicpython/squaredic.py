def run():
    cuadrados={}
    for i in range(1,101):
        if i%3==0:
            cuadrados[i]=i**2
    print(cuadrados)
if __name__=='__main__':
    run()
