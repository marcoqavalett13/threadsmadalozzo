import threading
import time
import matplotlib.pyplot as plt

def minha_funcao(tempos):

    tempo_inicio = time.time()


    valor  = 6000

    fib_1 = 1
    fib_2 = 0

    for _ in range(2, valor + 1):
        fib_n = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib_n


    print("O número de Fibonacci correspondente a", valor, "é", fib_n)

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
