import webbrowser
from time import sleep


estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

def vizualizar_pais():
    url_acesso = 'ibge.gov.br/cidades-e-estados/'
    webbrowser.open(url_acesso)

def procurar_estado():
    estado_procurado = input("Qual estado está sendo procurado? ")
    estado = estado_procurado.upper()
    if estado in estados:
        url_acesso = 'ibge.gov.br/cidades-e-estados/'+estado
        webbrowser.open(url_acesso)
    else:
        print("falha, erro de escrita")


#vizualizar_pais()
procurar_estado()
