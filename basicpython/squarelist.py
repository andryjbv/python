def run():
    num=[]
    for n in range(0,100):
        if (n+1) % 3 == 0:
            num.append((n+1)**2)      
    print(num)
if __name__=='__main__':
    run()
