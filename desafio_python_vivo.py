def recomendar_plano(consumo):  
    lista_planos = [{"consumo": 10, "plano": 50, "nome": "Essencial"},{"consumo": 19, "plano": 100, "nome": "Prata"},{"consumo": 21, "plano": 300, "nome": "Premium"}] 
  
    consumo_medio = verificar_entrada(consumo)

    consumo_selecionado = [plano_escolhido for plano_escolhido in lista_planos if plano_escolhido["consumo"] == consumo_medio]  

    nome_consumo_selecionado = consumo_selecionado[0].get("nome")
    plano__consumo_selecionado = consumo_selecionado[0].get("plano")
    
    return (f"Plano {nome_consumo_selecionado} Fibra - {plano__consumo_selecionado}Mbps") 

def verificar_entrada(consumo):
    if consumo <= 10:  
        return 10
    elif consumo > 10 and consumo <= 20:  
        return 19
    else:
        return 21 

consumo = float(input("Informe o consumo desejado: "))

print(recomendar_plano(consumo))