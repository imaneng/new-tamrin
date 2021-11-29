import numpy as np
Matrix_size = int(input("size matris ra vared konid : "))

main_list = []
for i in  range(Matrix_size) :
    temp = Matrix_size
    L = []
    
    while Matrix_size :
        
        Matrix_size = Matrix_size-1
        no = int(input("adade satre aval ra vared konid : "))
        L.append(no)
    print("L" + str(i) , " = ", L)
    main_list.append (L)
    Matrix_size = temp
print("main_list : " , main_list)
print(main_list[2,1])

