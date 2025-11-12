def log_transaction(func):
    def wrapper():
        print('1 Log de la transacción...')
        func()
        print('3 Log terminado...')
    return wrapper
        

@log_transaction
def process_payment():
    print('2 Procesando pago....')

process_payment()




#Decorador que comprueba si un empleado tiene un rol específico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #Si el rol de lempleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESO DENEGAGO. Solo {required_role} pueden realizar esta acción')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando acción para el empleado {employee['name']}')
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f'El empleado {employee['name']}, ha sido eliminado')

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(admin)
