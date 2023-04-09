from random import randrange

jogadas = ["Pedra", "Papel", "Tesoura"]
sequencia = 0

def iniciaJogo(sequencia):
    escolhaJogador = jogadas[int(input("\nEscolha sua jogada: \n\n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n\nDigite o número de sua escolha: \n"))-1]
    escolhaCPU = jogadas[(randrange(1, 3)-1)]
    print(f"Você jogou {escolhaJogador}\n")
    print(f"O CPU jogou {escolhaCPU}\n")
    if escolhaJogador == "Pedra" and escolhaCPU == "Pedra":
        print("Empate")
        sequencia = sequencia
        continuaJogo(sequencia)
    elif escolhaJogador == "Pedra" and escolhaCPU == "Papel":
        print("CPU Ganhou!")
        sequencia = 0
        continuaJogo(sequencia)
    elif escolhaJogador == "Pedra" and escolhaCPU == "Tesoura":
        print("Você Ganhou!")
        sequencia = sequencia + 1
        continuaJogo(sequencia)
    elif escolhaJogador == "Papel" and escolhaCPU == "Papel":
        print("Empate")
        sequencia = sequencia
        continuaJogo(sequencia)
    elif escolhaJogador == "Papel" and escolhaCPU == "Pedra":
        print("Você Ganhou!")
        sequencia = sequencia + 1
        continuaJogo(sequencia)
    elif escolhaJogador == "Papel" and escolhaCPU == "Tesoura":
        print("CPU Ganhou!")
        sequencia = 0
        continuaJogo(sequencia)
    elif escolhaJogador == "Tesoura" and escolhaCPU == "Tesoura":
        print("Empate")
        sequencia = sequencia
        continuaJogo(sequencia)
    elif escolhaJogador == "Tesoura" and escolhaCPU == "Pedra":
        print("CPU Ganhou!")
        sequencia = 0
        continuaJogo(sequencia)
    elif escolhaJogador == "Tesoura" and escolhaCPU == "Papel":
        print("Você Ganhou!")
        sequencia = sequencia + 1
        continuaJogo(sequencia)
def continuaJogo(sequencia):
    print(f"\n\nVocê tem {sequencia} vitórias em sequência!\n")
    continuar = input("Deseja continuar jogando? (S/N) ")
    if continuar.upper() == "S":
        print(sequencia)
        iniciaJogo(sequencia)
    else:
        pass

iniciaJogo(sequencia)