def run():
    # square= [ 
    #     i**2 for i in range(1,101) if i % 3 != 0
    
    # ]

    # print(square)
    
    square2= [
        i for i in range(1,1000) if i % 4 == 0 and i % 6 ==0 and i % 9==0
    ]
    print(square2)
    # squares= []
    # for i in range(1,101):
    #     if i % 3!= 0:
            
    #         squares.append(i**2)
    # print(squares)

if __name__== "__main__":
    run() 