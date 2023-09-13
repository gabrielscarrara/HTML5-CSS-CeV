import random

# Lista de times
times = ["Flamengo", "Palmeiras", "São Paulo", "Internacional", "Grêmio", "Atlético-MG", "Cruzeiro", "Corinthians", "Santos", "Fluminense"]

# Dicionário de jogadores por time (nome do jogador, posição, valor e pontuação)
jogadores_por_time = {
    "Flamengo": [("Jogador1", "Atacante", 10, 0), ("Jogador2", "Meio-campista", 8, 0)],
    "Palmeiras": [("Jogador3", "Atacante", 9, 0), ("Jogador4", "Defensor", 7, 0)],
    # Adicione outros times e jogadores aqui
}

# Função para simular um jogo e atualizar as pontuações dos jogadores
def simular_jogo(time):
    for jogador in jogadores_por_time[time]:
        pontuacao = random.randint(0, 10)  # Simula a pontuação do jogador no jogo
        jogador[3] += pontuacao  # Atualiza a pontuação do jogador

# Função para exibir as pontuações dos jogadores de um time
def exibir_pontuacoes(time):
    print(f"Pontuações dos jogadores do {time}:")
    for jogador in jogadores_por_time[time]:
        print(f"{jogador[0]} ({jogador[1]}): {jogador[3]} pontos")

# Loop principal do jogo
while True:
    print("\nTimes disponíveis:")
    for i, t in enumerate(times):
        print(f"{i + 1}. {t}")

    escolha = int(input("Escolha um time (1-10) ou 0 para sair: "))

    if escolha == 0:
        break

    if escolha < 1 or escolha > 10:
        print("Escolha inválida. Tente novamente.")
        continue

    time_escolhido = times[escolha - 1]
    simular_jogo(time_escolhido)
    exibir_pontuacoes(time_escolhido)
