import math

#Diccionary comprehension

def run():
    numeros = {i: math.sqrt(i) for i in range (1, 1001)}
    print(numeros)
    
#Lists comprehension

    squares = [i for i in range (1, 1000) if i % 4 == 0]
    print(squares)
     
   

if __name__ == "__main__":
    run()


