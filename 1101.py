import threading
import time
import matplotlib.pyplot as plt

def minha_funcao(tempos):
    # Registrar o tempo de início da execução da thread
    tempo_inicio = time.time()

    M = 100
    N = 3000016

    menor = min(M, N)
    maior = max(M, N)

    sequencia = list(range(menor, maior + 1))

    soma = sum(sequencia)
    


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
