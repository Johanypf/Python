import numbers
def suma_args(*args):
    rest = 0
    for number in args:
        if isinstance(number,numbers.Number):
            rest += number
    
    return (f"{rest:,}")

print(f"Sin Argumentos : {suma_args()}")
print(f"Con un Argumento : {suma_args(3)}")
print(f"Con Argumentos : {suma_args(4,34,12)}")
print(f"Con Argumentos : {suma_args(4,34000,12343)}")


