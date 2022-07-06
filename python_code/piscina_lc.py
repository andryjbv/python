
def run():
    deportistas=[] 
    n=int(input("Cuantos deportistas hay? ")) 
    for i in range (0,n):
        puntajes=[]
        print("Deportista " + str(i+1) +"**************")
        puntajes=[int(input("Puntaje del juez " + str(j+1) + " para el deportista " + str(i+1) + ": ")) for j in range(0,10)]
        puntajes.remove(max(puntajes))
        puntajes.remove(min(puntajes))
        prom=sum(puntajes)/len(puntajes)
        deportistas.append(prom)
    print(deportistas)
    print("El máximo promedio fue " , max(deportistas) , " y el mínimo " , min(deportistas))
if __name__=='__main__':
    run()