class tela():
    def __init__(self, matriz_pixels):
        self.__tela = matriz_pixels
        
    
    def getTela(self):
        return self.__tela
    
    

class tela_mobile(tela):
    def __init__(self, matriz_pixels):
        super().__init__(matriz_pixels)
        lin = 0
        col = 0
        linhas = len(matriz_pixels)
        colunas = len(matriz_pixels[0])
        
        if linhas > 300 and colunas > 300:
            if linhas < 1024 and colunas < 1024:
                if linhas == colunas:
            
                    while lin < linhas:
                        while col < colunas:
                            if len(matriz_pixels[lin]) != colunas:
                                #matriz_pixels = [[0]*600]*800
                            col += 1
                        lin += 1
                        
        
                        
    def buscar_quadrado(self):
        matriz_pixels = super().getTela()
        lin = 0
        col = 0
        linhas = len(matriz_pixels)
        colunas = len(matriz_pixels[0])
        pixel_vazio = 0
        pixel_cheio = None
        quadrado = []
        
        while lin < linhas:
            col = 0
            while col < colunas:
                if matriz_pixels[lin][col] != pixel_vazio:
                    pixel_cheio = matriz_pixels[lin][col]
                col += 1
            lin += 1
            
        lin = 0
        
        while lin < linhas:
            if pixel_cheio in matriz_pixels[lin]:
                quadrado.append(matriz_pixels[lin])
            lin += 1
            
        
        return quadrado
                
  
    def verificar_quadrado(self):
        matriz = self.buscar_quadrado()
        lin = 0
        col = 0
        linhas = len(matriz)
        colunas = len(matriz[0])
        pixel_cheio = None
        pixel_vazio = 0
        começo_quadrado = 0
        final_quadrado = 0
        tamanho_base = 0
        
        # verifica pixel
        while lin < linhas:
            col = 0
            while col < colunas:
                if matriz[lin][col] != pixel_vazio:
                    pixel_cheio = matriz[lin][col]
                    break
                col += 1     
            lin += 1
                
  
        #verifica tamanho da base
        col = 0
        while col < colunas:
            if matriz[0][col] == pixel_cheio:
                tamanho_base += 1
            col += 1

        #verifica começo do quadrado
        col = 0
        while col < colunas:
            if matriz[0][col] == pixel_cheio:
                começo_quadrado = col
                break
            col += 1

        #verifica final do quadrado
        col = 0
        contador = 0
        
        while col < colunas:
            if matriz[0][col] == pixel_cheio:
                contador += 1
            if contador == tamanho_base:
                final_quadrado = col
                break
            col += 1
            
        #verifica as bases de cima e de baixo
        col = começo_quadrado
        base_cima = 0
        base_baixo = 0
        bases_iguais = None
        while col <= final_quadrado:
            
            if matriz[0][col] == pixel_cheio:
                base_cima += 1
            else:
                base_cima -= base_cima
                
            
            if matriz[len(matriz) - 1][col] == pixel_cheio:
                base_baixo += 1
            else:
                base_baixo -= base_baixo
            
            
            if col == final_quadrado:
                if base_cima == tamanho_base and base_baixo == tamanho_base:
                    bases_iguais = 'verdade'
                else:
                    final_matriz_pixel = 0
                    matriz_pixels = super().getTela()
                    lin = 0
                    linhas = len(matriz_pixels)
                    while lin < linhas:
                        if pixel_cheio in matriz_pixels[-lin]:
                            final_matriz_pixel = len(matriz_pixels) - lin
                            print(f'linha: {final_matriz_pixel}, coluna: {começo_quadrado}')
                            return False
                        lin += 1
            col += 1
        
        #verificar os lados do quadrado
            
        lin = 0
        contador_linhas = 0
        
        while lin < linhas:    
            if matriz[lin][começo_quadrado] == pixel_cheio and matriz[lin][final_quadrado] == pixel_cheio:
                contador_linhas += 1       
            else:
                final_matriz_pixel = 0
                matriz_pixels = super().getTela()
                lin = 0
                linhas = len(matriz_pixels)
                while lin < linhas:
                    if pixel_cheio in matriz_pixels[-lin]:
                        final_matriz_pixel = len(matriz_pixels) - lin
                        print(f'linha: {final_matriz_pixel}, coluna: {começo_quadrado}')
                        return False
                    lin += 1
        
                    
            lin += 1
            
        
        #verificar dentro do quadrado
        col = começo_quadrado + 1
        lin = 1
            
        while lin < len(matriz) - 1:
            col = começo_quadrado + 1
            while col < final_quadrado - 1 :
                    
                if matriz[lin][col] != pixel_vazio:
                    final_matriz_pixel = 0
                    matriz_pixels = super().getTela()
                    lin = 0
                    linhas = len(matriz_pixels)
                    while lin < linhas:
                        if pixel_cheio in matriz_pixels[-lin]:
                            final_matriz_pixel = len(matriz_pixels) - lin
                            print(f'linha: {final_matriz_pixel}, coluna: {começo_quadrado}')
                            return False
                        lin += 1
   
                    
                col += 1
            lin += 1
            
            
        #verifica se tem pixel diferente
        col = 0
        lin = 0
        while lin < linhas:
            col = 0
            while col < colunas:
                
                if matriz[lin][col] != pixel_vazio:
                    if matriz[lin][col] != pixel_cheio:
                        
                        final_matriz_pixel = 0
                        matriz_pixels = super().getTela()
                        lin = 0
                        linhas = len(matriz_pixels)
                        while lin < linhas:
                            if pixel_cheio in matriz_pixels[-lin]:
                                final_matriz_pixel = len(matriz_pixels) - lin
                                print(f'linha: {final_matriz_pixel}, coluna: {começo_quadrado}')
                                return False
                            lin += 1
                        
                    
                
                col += 1
            lin += 1
            
        #vitória    
        final_matriz_pixel = 0
        matriz_pixels = super().getTela()
        lin = 0
        linhas = len(matriz_pixels)
        while lin < linhas:
            if pixel_cheio in matriz_pixels[-lin]:
                final_matriz_pixel = len(matriz_pixels) - lin
                break
            lin += 1
            
        print(f'linha: {final_matriz_pixel}, coluna: {começo_quadrado}')
        return True
        
    

celular = tela_mobile([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 0, 7, 7, 0, 7, 0, 0],
    [0, 0, 7, 7, 7, 7, 0, 7, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 7, 7, 7, 7, 7, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

print(celular.verificar_quadrado())


