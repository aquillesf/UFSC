class Player:
    def __init__(self, pl_id=0, cr=0):
        self.__playerID = pl_id
        self.__creditos = cr
        
    def __str__(self):
        return  print(f'player id: {self.__playerID}, créditos: {self.__creditos}', end = ' ')
    
    def getPlayerID(self):
        return self.__playerID
    

class player_cs(Player):
    def __init__(self, pl_id=0, cr=0, time_fav = "CT", arma_fav = "rifle"):
        super().__init__(pl_id, cr)
        self.__time_fav = time_fav
        self.__arma_fav = arma_fav
        
    
    def __str__(self):
        str_sp = super().__str__()
        return print(f'Jogo: CS, arma favorita: {self.__arma_fav}, time favorito: {self.__time_fav}')


class cadastro_players():
    def __init__(self):
        self.__cadastro = {}
        
    
    def adicionar_player(self, pl_id, cr, time_fav, arma_fav):
        jogador = player_cs(pl_id, cr, time_fav, arma_fav)
        
        if pl_id in self.__cadastro:
            return False
        else:
            self.__cadastro[pl_id] = cr, time_fav, arma_fav
        
        
        
jogador = Player(123, 100)
jogador = player_cs(123, 100, "T", "Pistola")
cadastrar = cadastro_players()
cadastrar.adicionar_player(123, 100, "T", "Pistola")
cadastrar.adicionar_player(123, 112, "CT", "rifle")
