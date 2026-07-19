# we will use TUPLES since they are ordered and unchangeable {can use lists too but they are changeable and we dont want a numpad will changeable keys}

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ('*',0,'#'))

for row in num_pad:
    for num in row :
        print(num , end= " ")
    print()