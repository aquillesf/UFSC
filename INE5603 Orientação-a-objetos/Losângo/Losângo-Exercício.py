def pegar_losango(m):
    losango_total = []
    
    i = 0
    j = 0
    pixel_vazio = 0
    
    while i < len(m):
        j = 0
        while j < len(m):
            if m[i][j] != pixel_vazio:
                losango_total.append(m[i])
            j += 1
        i += 1
    return losango_total
        
def vef_pixel(matriz1):
    m = pegar_losango(matriz1)
    pixel_vazio = 0
    pixel_cheio = 0
    i = 0
    j = 0
    
    while i < len(m):
        j = 0
        while j < len(m):
            if m[i][j] != pixel_vazio:
                pixel_cheio = m[i][j]
                i += len(m)
            j += 1
        i += 1
    
    i = 0
    j = 0
    
    while i < len(m):
        j = 0
        while j < len(m):
            if m[i][j] != pixel_vazio:
                if m[i][j] != pixel_cheio:
                    return False
            j += 1
            
        i += 1
    return True

def vef_tamanho(m):
    i = 0
    j = 0
    pixel_vazio = 0
    começo = 0
    final = 0
    
    if vef_pixel:
        
        while i < len(m):
            if m[0][i] != pixel_vazio:
                começo += i
                i += len(m)
            i += 1
        
        i = começo
        con_total = 0
        while i < len(m):
            if [0][i] != pixel_vazio:
                con_total +=1
            if m[0][i] == pixel_vazio:
                final = i - 1
                i += len(m)
            i += 1
            
        i = 0
        while i < len(m):
            con = 0
            j = 0
            while j < len(m):
                if m[i][j] != pixel_vazio:
                    con += 1
                j += 1
                
            i += 1
            
            if con != con_total:
                return False



def losango(m):
    matriz = losango_total(m)
    pixel_vazio = 0
    i = 0
    j = 0
    
    if vef_pixel(matriz):
        if vef_tamanho(matriz):
            
    

