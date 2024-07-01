#Importa funções random para o computador conseguir realizar as jogadas
import random 
#classe do tabuleiro para criar e manipular as regraas do jogo
class tabuleiro(): 
    def __init__(self):
        #tamanho default do tabuleiro
        self.__tamanho = 19 
        self.__tabuleiro = []
        #peças do jogo
        self.__peça1 = "X" 
        self.__peça2 = "O"
      #cria o tabuleiro com o tamanho default e com pontos para melhor visualização do jogo   
    def criar_tabuleiro(self):
        for i in range(self.__tamanho):
            adicionar = []
            for x in range(self.__tamanho):
                adicionar.append('.')
            self.__tabuleiro.append(adicionar)
    
      #cria o tabuleiro com o tamanho default e com pontos para melhor visualização do jogo         
    def mostrar_tabuleiro(self):
        for x in range(self.__tamanho):
            print(f'{x}\t', end=' ')
            for y in range(self.__tamanho):
                print(self.__tabuleiro[x][y], end=' ')
            print()
        print('         0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18')
        print()
        #não consegui encaixar as coordenadas das colunas corretamente, pois quando criava um espaçamento ("  .") entre os "." na hora de criar o tabuleiro , a função
        #de vitoria analisava os espaços entre as peças e a contagem voltava do 0 toda hora, já que os identificadores do tabuleiro são os "." e não os espaços em branco que tinha colocado anteriormente
        #então decidi retirar os espaços para ver se o erro parava, e funcionou. Até pensei em retirar essas coordenadas do jogo ou pesquisar na internet como resolver, mas achei interessante como
        
        #se certifica que as jogadas dos jogadores estão dentro dos parametros do tabuleiro    
    def posicao_correta(self, linha, coluna):
        if linha < 0 or coluna < 0 or linha >= self.__tamanho or coluna >= self.__tamanho:
            print('faça uma jogada com as coordenadas entre 0 e 18!')
            return False
        elif self.__tabuleiro[linha][coluna] != '.':
            print('essa posição já está ocupada!')
            return False
        else:
            return True
    #jogada do primeiro jogador com a peça X 
    def jogada1(self, linha, coluna):
        if self.posicao_correta(linha, coluna):
            self.__tabuleiro[linha][coluna] = self.__peça1
            self.mostrar_tabuleiro()
            return True
        else:
            return False
    #jogada do segundo jogador com a peça O  
    def jogada2(self, linha, coluna):
        if self.posicao_correta(linha, coluna):
            self.__tabuleiro[linha][coluna] = self.__peça2
            self.mostrar_tabuleiro()
            return True
        else:
            return False
        
     #instancia de vitoria    
    def vitoria(self, sequencia, peça):
        con = 0
        for peca in sequencia:
            #verifica se há peças em sequencia e realiza a contagem até o limite 5
            if peca == peça:
                con += 1
                if con == 5:
                    return True
            else:
                con = 0
        return False
      #a função verificava os dois objetos ao mesmo tempo, corrigido.
    
        #verifica as posições necessarias pra vitoria dentro da matriz que é o tabuleiro (linhas, diagonais, colunas etc) 

    def verificar_pos_vitoria(self):
        
        #linha
        for i in range(self.__tamanho):
            linha = self.__tabuleiro[i]
            if self.vitoria(linha, self.__peça1) or self.vitoria(linha, self.__peça2):
                return True
        # coluna
        for col in range(self.__tamanho):
            coluna = [self.__tabuleiro[lin][col] for lin in range(self.__tamanho)]
            if self.vitoria(coluna, self.__peça1) or self.vitoria(coluna, self.__peça2):
                return True
        #diagonais
        for i in range(self.__tamanho):
            diagonal_1 = [self.__tabuleiro[i + j][j] for j in range(self.__tamanho - i)]
            if self.vitoria(diagonal1, self.__peça1) or self.vitoria(diagonal1, self.__peça2):
                return True
            diagonal_2 = [self.__tabuleiro[j][i + j] for j in range(self.__tamanho - i)]
            if self.vitoria(diagonal2, self.__peça1) or self.vitoria(diagonal2, self.__peça2):
                return True
            diagonal3 = [self.__tabuleiro[i - j][j] for j in range(i + 1)]
            if self.vitoria(diagonal3, self.__peça1) or self.vitoria(diagonal3, self.__peça2):
                return True
            diagonal4 = [self.__tabuleiro[self.__tamanho - 1 - j][i + j] for j in range(self.__tamanho - i)]
            if self.vitoria(diagonal4, self.__peça1) or self.vitoria(diagonal4, self.__peça2):
                return True
            
        return False

     #retorna true sempre que a condicional de 5 peças encontrada em diversos angulos for verdadeira, e apenas retorna falso se nenhum dos parametros foi encontrado
    #verifica se o jogo deu empate

    def empate(self):
        for linha in self.__tabuleiro:
             #se caso ainda tenha lugares vazios no tabuleiro, retorna falso, se não, retorna true
            if '.' in linha:
                return False
        return True
# classe para as jogadas dos jogadores e a interface do console para as jogadas   
class jogar():
    def __init__(self, nome, peca, humano=True):
        self.__nome = nome
        self.__peca = peca
        #verifica se é humano com base nos booleanos True ou False
        self.__humano = humano
    
     #função para realizar a jogada com o parametro tab para instanciar a classe tabuleiro
    def fazer_jogada(self, tab):
        if self.__humano:
              #caso seja humano a jogada sera feita e escolhida pelo console
            while True:
                linha = int(input("Escolha a linha para posicionar a peça: "))
                coluna = int(input("Escolha a coluna para posicionar a peça: "))
                #checa se as oposiçoes escolidas pelo usuario estao corretas com base na funçao da primeira classe 
                if tab.posicao_correta(linha, coluna):
                    if self.__peca == "X":
                        tab.jogada1(linha, coluna)
                    else:
                        tab.jogada2(linha, coluna)
                    break
                
          #caso não seja humano, a jogada sera aleatoria pelo computador        
        else:
            while True:
                linha = random.randint(0, 18)
                coluna = random.randint(0, 18)
                if tab.posicao_correta(linha, coluna):
                    if self.__peca == "X":
                        tab.jogada1(linha, coluna)
                    else:
                        tab.jogada2(linha, coluna)
                    break
#função que começa o jogo com base em todas as classes feitas anteriormente               
def jogar_gomoku():
    jogo = tabuleiro()
    jogo.criar_tabuleiro()
    jogo.mostrar_tabuleiro()
    #escolhe com quem quer jogar
    print("Você quer jogar com: ")
    print("1 - Humano Vs. Humano")
    print("2 - Computador Vs. Humano")
    escolher_jogador = int(input("Escolha: "))
    
    if escolher_jogador == 2:
        jogador1 = jogar("Jogador 1", "X", humano=True)
        jogador2 = jogar("Computador", "O", humano=False)
    else:
        jogador1 = jogar("Jogador 1", "X", humano=True)
        jogador2 = jogar("Jogador 2", "O", humano=True)
    #jogo
    while True:
        jogador1.fazer_jogada(jogo)
        if jogo.verificar_pos_vitoria():
            print("Jogador 1 venceu!")
            break
        if jogo.empate():
            print("Empate!")
            break
            
        jogador2.fazer_jogada(jogo)
        if jogo.verificar_pos_vitoria():
            if escolher_jogador == 2:
                print("Computador venceu!")
            else:
                print("Jogador 2 venceu!")
            break
        if jogo.empate():
            print("Empate!")
            break

jogar_gomoku()
