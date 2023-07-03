import threading
import time
import matplotlib.pyplot as plt

def minha_funcao(tempos):
    # Registrar o tempo de início da execução da thread
    tempo_inicio = time.time()


    valor  = 6000

    fib_1 = 1
    fib_2 = 0

    for _ in range(2, valor + 1):
        fib_n = fib_1 + fib_2
        fib_2 = fib_1
        fib_1 = fib_n


    print("O número de Fibonacci correspondente a", valor, "é", fib_n)

    # Registrar o tempo de fim da execução da thread
    tempo_fim = time.time()

    # Calcular a diferença de tempo
    tempo_total = tempo_fim - tempo_inicio

    # Adicionar o tempo total à lista compartilhada
    tempos.append(tempo_total)

# Obter a quantidade de threads a serem criadas
quantidade_threads = int(input("Digite a quantidade de threads a serem criadas: "))

# Lista para armazenar os tempos de execução (compartilhada entre as threads)
tempos = []

# Criar e iniciar as threads
threads = []
for _ in range(quantidade_threads):
    thread = threading.Thread(target=minha_funcao, args=(tempos,))
    thread.start()
    threads.append(thread)

# Aguardar pela conclusão das threads
for thread in threads:
    thread.join()

# Gerar o gráfico
plt.plot(range(1, len(tempos)+1), tempos)
plt.xlabel('Thread')
plt.ylabel('Tempo de execução')
plt.title('Tempo de execução das threads')
plt.show()
