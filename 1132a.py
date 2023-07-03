import threading
import time
import matplotlib.pyplot as plt

def minha_funcao(tempos):
    tempo_inicio = time.time()

    x = 100
    y = 200 


    soma = 0

    for num in range(x, y, +1):
        if num % 13 != 0:
            soma += num
    
    print(soma)

    tempo_fim = time.time()


    tempo_total = tempo_fim - tempo_inicio


    tempos.append(tempo_total)


quantidade_threads = int(input("Digite a quantidade de threads a serem criadas: "))

tempos = []


threads = []
for _ in range(quantidade_threads):
    thread = threading.Thread(target=minha_funcao, args=(tempos,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Gerar o gráfico
plt.plot(range(1, len(tempos)+1), tempos)
plt.xlabel('Thread')
plt.ylabel('Tempo de execução')
plt.title('Tempo de execução das threads')
plt.show()
