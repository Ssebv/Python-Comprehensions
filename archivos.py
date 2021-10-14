

def read():
    numbers=[]
    with open('./archivos/numbers.txt','r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)
def write():
    names =['Facundo','Gregorio','Marta','Susana','Jose']
    with open('./archivos/name.txt','a', encoding='utf-8')as v2:
        for name in names:
            v2.write(name)
            v2.write('\n')
def run():
    write()

if __name__ == '__main__':
    run()