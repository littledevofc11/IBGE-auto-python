import webbrowser
from time import sleep


estados = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to']

def vizualizar_pais():
    url_acesso = 'ibge.gov.br/cidades-e-estados/'
    webbrowser.open(url_acesso)

def procurar_estado():
    estado_procurado = input("Qual estado está sendo procurado? ")
    estado = estado_procurado.lower()
    if estado in estados:
        url_acesso = 'ibge.gov.br/cidades-e-estados/'+estado
        webbrowser.open(url_acesso)
    else:
        raise ValueError("Estado indisponivel")

def procurar_cidade():
    cidade_procurada = input("Qual cidade está sendo procurada? ")
    cidade = cidade_procurada.strip()
    cidade = cidade.lower()
    for estado in estados:
        url_acesso = 'https://ibge.gov.br/cidades-e-estados/'+estado+'/'+cidade+'.html'
        webbrowser.open(url_acesso)

procurar_cidade()
#vizualizar_pais()
#procurar_estado()
