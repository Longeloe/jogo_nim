def jogo_nim():
    print('Bem vindo ao Jogo NIM!')
    modo_jogo = int(input(("Digite '1' para jogar uma partida simples ou digite '2' para jogar o modo campeonato: ")))
    global vitórias_computador
    vitórias_computador = 0
    global vitórias_jogador
    vitórias_jogador = 0
    if modo_jogo == 1:
        partida()
    elif modo_jogo == 2:
        campeonato()

def partida():
    n = int(input('Insira o número de peças: '))
    m = int(input('Insira o número máximo de peças a serem retiradas por vez: '))
    if not n > m:
        print('m deve ser menor que n')
        partida()
    global peças_restantes
    peças_restantes = n
    if n % (m+1) == 0:
        print('Você começa!')
        usuario_escolhe_jogada(n, m)
    else:
        print('Eu começo!')
        computador_escolhe_jogada(n, m)

def computador_escolhe_jogada(n, m):
    global peças_restantes
    jogada_computador = 1
    peças_restantes_teste = peças_restantes - jogada_computador
    while peças_restantes_teste % (m+1) != 0:
        jogada_computador += 1
        peças_restantes_teste -= 1
        if jogada_computador == m:
            break
    print('Vou retirar', jogada_computador, 'peças.')
    peças_restantes -= jogada_computador
    if peças_restantes > 0:
        print('Eu removi', jogada_computador, 'peças. Restam', peças_restantes, 'peças.')
        print('Sua vez!')
        usuario_escolhe_jogada(n, m)
    else:
        print('Eu ganhei!')
        global vitórias_computador
        vitórias_computador += 1

def usuario_escolhe_jogada(n, m):
    global peças_restantes
    jogada_usuario = int(input('Quantas peças quer retirar? '))
    if jogada_usuario > m or jogada_usuario < 1 or jogada_usuario > n:
        if n >= m:
            print('Escolha um número entre 1 e', m)
            usuario_escolhe_jogada(n, m)
        else:
            print('Escolha um número entre 1 e', n)
            usuario_escolhe_jogada(n, m)
    else:
        peças_restantes -= jogada_usuario
    if peças_restantes > 0:
        print('Você removeu', jogada_usuario, 'peças. Restam', peças_restantes, 'peças.')        
        print('Minha vez!')
        computador_escolhe_jogada(n, m)
    else:
        print('Você ganhou!')
        global vitórias_jogador
        vitórias_jogador += 1
        
def campeonato():
    total_partidas = 3
    partida_atual = 0
    global vitórias_computador
    vitórias_computador = 0
    global vitórias_jogador
    vitórias_jogador = 0
    while partida_atual < total_partidas:
        partida()
        partida_atual += 1
    else:
        print('Placar: Você', vitórias_jogador, 'X', vitórias_computador, 'Computador')
