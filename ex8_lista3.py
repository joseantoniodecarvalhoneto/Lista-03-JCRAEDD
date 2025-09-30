'''8. Faça um programa que receba n números e armazene os pares em uma lista
simplesmente encadeada e não ordenada e os ímpares em uma segunda lista
simplesmente encadeada e não ordenada. Posteriormente, o programa deve montar
uma terceira lista, duplamente encadeada e ordenada de forma crescente, com os
números das duas listas anteriores. Para finalizar, o programa deve mostrar todos os
números da terceira lista das seguintes formas:
a. Crescente.
b. Decrescente. '''

class no_simples:  #criação do nó simples
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None

class no_duplo:  #criação nó duplo
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class lista_simples:   #criação da lista, apontando o head para o começo
    def __init__(self):
        self.head = None

    def adicionar(self, dado):  #adiciona o nó no começo da lista
        novo_no = no_simples(dado)
        novo_no.proximo = self.head
        self.head = novo_no

    def percorrer(self): #peercorre a lista ligada e retorna todos os dados
        dados = []
        atual = self.head
        while atual:
            dados.append(atual.dado)
            atual = atual.proximo
        return dados
    
class lista_dupla:
    def __init__(self):
        self.head = None
        self.tail = None 

    def adicionar_ordenado(self,dado):
        novo_no = no_duplo(dado)

        if not self.head: #verifica o caso da lista estar vazia
            self.head = novo_no
            self.tail = novo_no
            return 
            
        if dado < self.head.dado:  #se o dado for o menor deve adicionar no início
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no
            return
            
        atual = self.head
        while atual.proximo and atual.proximo.dado < dado:
            atual = atual.proximo

        novo_no.proximo = atual.proximo   #adicionando o nó no meio
        if atual.proximo:
            atual.proximo.anterior = novo_no

        novo_no.anterior = atual
        atual.proximo = novo_no

        if not novo_no.proximo: #para inserir no final, atualiza a cauda
            self.tail = novo_no

def main():
    lista_pares = lista_simples()
    lista_impares = lista_simples()

    print("Digite os números da sua lista, e digite FIM para parar: ")

    while True:
        entrada = input("-> " )
        if entrada.upper() == "FIM":
            break

        try:
            num = int(entrada)
        except ValueError:
            print("Digite um número ou encerre com FIM")
            continue

        if num % 2 == 0: #verifica se vai para lista dos pares ou dos impares
            lista_pares.adicionar(num)
        else:
            lista_impares.adicionar(num)

    lista_final_dupla = lista_dupla()
    todos_os_dados = lista_pares.percorrer() + lista_impares.percorrer() #colocando todos os dados em uma lista 

    for dado in todos_os_dados:
        lista_final_dupla.adicionar_ordenado(dado)

    
    print("Ordem Crescente:")
    if lista_final_dupla.head:
        atual = lista_final_dupla.head #começa no head pq é crescente
        saida = []
        while atual:
            saida.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(saida))
    else:
        print("Lista final vazia.")

    print("Ordem Decrescente:")
    if lista_final_dupla.tail:
        atual = lista_final_dupla.tail #começa no tail pq é decrescente
        saida = []
        while atual:
            saida.append(str(atual.dado))
            atual = atual.anterior 
        print(" -> ".join(saida)) 
    else:
        print("Lista final vazia.")

main()



    


        
    
