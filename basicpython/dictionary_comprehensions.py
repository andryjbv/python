def run():
    numeros={n:n**2 for n in range(1,101) if n%3==0 }
    print(numeros)
if __name__=='__main__':
    run()