
a = [180, -50, -25, -25]
d = ['2020-01-01', '2020-01-01', '2020-01-11', '2020-01-05']


def solution(A, D):

    balance = 0
    pagos_tarjeta = {}
    mes_no_fee = 0
    for i in range(len(A)):
        amount = A[i]
        date = D[i]
        month = date[5:7]  
        
        balance += amount
        
        if amount < 0:  
            if month not in pagos_tarjeta:
                pagos_tarjeta[month] = []
            pagos_tarjeta[month].append(amount)
    
   
    for month, payments in pagos_tarjeta.items():
        if len(payments) >= 3 and  sum(payments) <= -100:
            mes_no_fee += 1
            

    
    fee =  5 * (12 - mes_no_fee)
    balance -= fee

    
    return balance, mes_no_fee, fee,pagos_tarjeta

print(solution(a, d))



