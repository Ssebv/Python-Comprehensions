from functools import reduce

def run():
    
    my_list = [1,3,4,5,6,7,8,23,44,67,74]
    
    # odd= [ i for i in my_list if i % 2 != 0]
    
    odd = list(filter(lambda x : x%2 != 0, my_list)) # Funcion de orden superiro
    #Recive dos parametros = Funcion and interable(Cualquer elemento que logre recorrerce)
    
    print(odd)
    
    odd2 = list(map(lambda x : x**2, my_list)) # 
     
    print(odd2)
    
    all_multipied = reduce(lambda a,b: a * b, my_list)
    
    print(all_multipied)
    
    

if __name__== "__main__":
    run() 
    
    
