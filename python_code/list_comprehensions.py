def run():
    num=[(n+1)**2  for n in range(0,100) if (n+1) % 3 == 0]     
    print(num)
if __name__=='__main__':
    run()
