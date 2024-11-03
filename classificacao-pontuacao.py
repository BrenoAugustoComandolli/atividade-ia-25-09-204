def eh_insuficiente(pontuacao):
    return pontuacao >= 0 and pontuacao <= 4 

def eh_regular(pontuacao):
    return pontuacao >= 5 and pontuacao <= 6

def eh_bom(pontuacao):
    return pontuacao >= 7 and pontuacao <= 8

def eh_excelente(pontuacao):
    return pontuacao >= 9 and pontuacao <= 10

def classificar_pontuacao(pontuacao):
    if eh_insuficiente(pontuacao):
        return "Insuficiente"
    if(eh_regular(pontuacao)):
        return "Regular"
    if(eh_bom(pontuacao)):
        return "Bom"
    if(eh_excelente(pontuacao)):
        return "Excelente"
    else:
        return "Pontuação inválida"
    
def inserir_valor():
    while True:
        try:
            pontuacao = float(input("Digite uma pontuação entre 0 e 10: "))
            if 0 <= pontuacao <= 10:
                break
            else:
                print("Pontuação inválida! A pontuação deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
    
    return pontuacao 

pontuacao = inserir_valor()
print(classificar_pontuacao(pontuacao))