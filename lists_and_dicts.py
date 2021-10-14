def run():
    my_list= [1, 'Hello', True, 4.5]
    my_dict= {'firstname':'Facundo', 'lastname': 'Garcia'}
    
    super_list= [
        {'firstname':'Facundo', 'lastname': 'Garcia'},
        {'firstname':'Miguel', 'lastname': 'Torres'},
        {'firstname':'Luis', 'lastname': 'Gutierres'},
        {'firstname':'Javier', 'lastname': 'Orrego'}
    ]

    super_dict={
        'natural_nums': [1,2,3,4,5],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums': [1.2,4.5,3.56]
    }
    
    
    # for value in super_list:
    #     for key, value in value.items():
    #         print(key, '=', value)
    for item in super_list:
        print('Nombre Completo: ', item['firstname'] , '' , item['lastname'])
    # for i in super_list:
    #     print(i.items())
        
    for key,value in super_dict.items():
        print(key, '=', value)

if __name__== "__main__":
    run() 