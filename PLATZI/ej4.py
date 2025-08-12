def print_triangle(size, character):
    # Tu código aquí 👈
    f=""
    for x in range(1,size+1):
        s= (size - x) * " "
        l= character *(2 * x -1)
         
        if x == size:
          f += s + l
        else:   
          f +=  s + l +"\n"
    return f
         
    

print(print_triangle(5,"x"))

    
    
