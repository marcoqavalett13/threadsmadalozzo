import threading
import time
import matplotlib.pyplot as plt

def minha_funcao(tempos):
    tempo_inicio = time.time()

    M = 100
    N = 3000016

    menor = min(M, N)
    maior = max(M, N)

    sequencia = list(range(menor, maior + 1))

    soma = sum(sequencia)
    

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

plt.plot(range(1, len(tempos)+1), tempos)
plt.xlabel('Thread')
plt.ylabel('Tempo de execução')
plt.title('Tempo de execução das threads')
plt.show()
