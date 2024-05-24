def adicionar_item_lista(item):  
    lista.append(item)    
    if len(lista) == 3:        
        display_equipamento_list(lista)

def display_equipamento_list(lista):
    print("Lista de Equipamentos:")
    for list in lista:
        print(f"- {list}")


lista = []
item = str(input())
adicionar_item_lista(item)
item = str(input())
adicionar_item_lista(item)
item = str(input())
adicionar_item_lista(item)
