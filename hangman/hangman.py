from random import randint, random 
import os


def read():
    
    with open('./data.txt','r', encoding='utf-8') as word:
        data=[i for i in word]
        
        data=list(map(lambda l: l.rstrip('\n'), data))
            
    return(data)

    
def comparation(data,lineas):
    
    w=list(data)
    l=list(lineas)
    usuario= ''
    while w != l or usuario =='dedo':
        usuario = input('Ingrese una letra: ')
        
        assert len(usuario) == 1, 'Presionasete mas de una tecla'
        os.system('clear')
        for i in range(0,len(w)):
            if w[i] == usuario:
                l[i] = w[i]
        print(' '.join(l).upper())
        print('\n')
        
    print('Ganste!!! La palabra era' + data.upper())
    
    
def run():
    
    words= read()
    index= randint(0, len(words))
    word=words[index]
    
    lines= '_'*len(word)
    print('Adivina la palabra misteriosa')
    
    print(' '.join(lines))
    print('\n')
    comparation(word, lines)
    
   
                
                
                

if __name__== "__main__":
    run()
    