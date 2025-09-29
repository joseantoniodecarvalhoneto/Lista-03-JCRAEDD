'''5. Faça um programa que cadastre n produtos. Para cada produto devem ser cadastrados
código do produto, preço e quantidade estocada. Os dados devem ser armazenados
em uma lista simplesmente encadeada e não ordenada. Posteriormente, receber do
usuário a taxa de desconto (ex.: digitar 10 para taxa de desconto de 10%). Aplicar a taxa
digitada ao preço de todos os produtos cadastrados e finalmente mostrar um relatório
com o código e o novo preço. O final desse relatório deve apresentar também a
quantidade de produtos com quantidade estocada superior a 500. '''

class produto():
    def init (self, codigo, preco, quant_estocada):  
        self.codigo = codigo
        self.preço = preco
        self.quant_estocada = quant_estocada
        self.proximo = None  #criação do ponteiro, que ainda não aponta para nada

class lista_produtos():  #criação lista encadeada
    def init (self):
        self.head = None

    def adicionar_produto(self, codigo, preco, quant_estocada): #adicionando um novo nó
        novo_no = produto(codigo, preco, quant_estocada)

        if not self.head:    #confere se a lista está vazia e aponta o head para o primeiro elemento adicionado
            self.head = novo_no
            return
        atual = self.head

        while atual.proximo:   #enquanto tiver elementos os nós estão sendo ligados
            atual= atual.proximo
        atual.proximo = novo_no 

    def gerar_desconto(self, taxa_desconto):  #função para desconto
        if not self.head: 
            print("Não há produtos cadaastrados.")
            return
        
        produtos_acima_500 = 0
        fator_desconto = 1 - (taxa_desconto / 100)

        atual = self.head  #head aponta para o nó atual
        while atual:
            novo_preco = atual.preco * fator_desconto

            print(f"{atual.codigo} / {novo_preco}")

            if atual.quant_estocada > 500:
                produtos_acima_500 += 1

            atual = atual.proximo 

        print(f"Total de produtos no estoque acima de 500: ", {produtos_acima_500})


def main():
        lista = lista_produtos()
        n = 0

        while True:
            try:
                n = int(input("Quantos produtos você deseja cadastrar? "))
                if n >= 0:
                    break
                else:
                    print("O número de produtos deve ser zero ou positivo.")
            except ValueError:
                print("Entrada inválida, digite novamente.")

        for i in range(n):
            codigo = input("Digite o código do produto: ")

            while True:
                try:
                    preco = float(input("Digite o preço do produto: "))
                    if preco >= 0:
                        break
                    else:
                        print("O preço deve ser positivo.")
                except ValueError:
                    print(" Digite um número positivo.")

                while True:
                    try:
                        quantidade = int(input("Digite a quantidade estocada: "))
                        if quantidade >= 0:
                            break
                        else:
                            print("A quantidade deve ser zero ou maior que zero.")
                    except ValueError:
                        print("Digite um número inteiro.")

                lista.adicionar_produto(codigo, preco, quantidade)
                print("Produto cadastrado!")

        taxa_desconto = 0
        if n > 0:
             while True:
                try:
                    taxa_desconto = float(input("Digite a taxa de desconto a ser aplicada: "))
                    if taxa_desconto >= 0:
                        break
                    else:
                        print("A taxa de desconto deve ser zero ou maior")
                except ValueError:
                    print("Digite um número.")
        
                lista.gerar_desconto(taxa_desconto)
        else:
            print("Nenhum produto foi cadastrado.")

main()
        
    








