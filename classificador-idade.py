def eh_crianca(idade):
    return idade >= 0 and idade <= 12

def eh_adolescente(idade):
    return idade >= 13 and idade <= 17

def eh_adulto(idade):
    return idade >= 18 and idade <= 64

def eh_idoso(idade):
    return idade >= 65

def classificar_idade(idade):
    if eh_crianca(idade):
        return "Criança"
    if(eh_adolescente(idade)):
        return "Adolescente"
    if(eh_adulto(idade)):
        return "Adulto"
    if(eh_idoso(idade)):
        return "Idoso"
    else:
        return "Idade inválida"
    
idade_teste = 25
resultado = classificar_idade(idade_teste)
print(f"A classificação da idade {idade_teste} é: {resultado}")