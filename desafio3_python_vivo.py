import re

def remove_caracteres(telefone): 
    if telefone[5] == "9":
        return re.sub(r'\D', '', (telefone))        
    else:
        return 'Número de telefone inválido.'

def format_phone_number(telefone): 

    telefone_em_numeros = remove_caracteres(telefone)
   
    if len(telefone_em_numeros) == 11:
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'

telefone = str(input())

print(format_phone_number(telefone))