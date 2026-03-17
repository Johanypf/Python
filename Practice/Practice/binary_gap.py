
import time
inicio = time.time()
# --- Tu código aquí ---


number = 32


binario = format(number,'b')
print(binario)
print(binario[1:])

max_gap = 0
count_0 = 0
current_0 = 0
for i in binario[1:]:
    if i == '0':
          count_0 += 1 
    else:
          current_0 = count_0  
          count_0 = 0
          max_gap = max(max_gap,current_0)

        
print(max_gap)

fin = time.time()
print(f"Tiempo: {fin - inicio} segundos")
