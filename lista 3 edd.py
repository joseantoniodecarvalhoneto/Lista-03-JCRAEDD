'''7. Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados
nome e nota final. Os dados devem ser armazenados em uma lista duplamente
encadeada e não ordenada. Em seguida, o programa deve mostrar apenas o nome dos
alunos aprovados, ou seja, alunos com nota final de no mínimo 7. Se nenhum aluno
estiver aprovado, mostrar mensagem. '''

class no:    #criação da classe nó que armazena os dados para nome e nota e o ponteiro para o anterior e sucessor
    def __init__ (self, nome, nota):
        self.nome = nome  #self se refere ao objeto que esta sendo criado aqui
        self.nota = nota
        self.proximo = None
        self.anterior = None 

class listaEncadeada:  #função que define a cabeça (head) e a cauda (tall)
    def __init__(self):  #init é um método construtor para iniciar um atributo com valor inicial
        self.cabeça = None
        self.cauda = None

    def adicionar_aluno(self, nome, nota): #função para adicionar novos nós
        novo_no = no(nome, nota)
        if self.cabeça is None:  #confere se o nó esta vazio
            self.cabeça = novo_no
            self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no  #caso já tenha um nó adiciona o novo nó no fim com a localização da cauda
            novo_no.anterior = self.cauda
            self.cauda = novo_no  #direciona a cauda(tall) para o último nó que você adicionou - redefine o final

    def listar_aprovados(self):  #função para verificar os aprovados 
        aprovados = []  #lista para armazenar os aprovados 
        no_atual = self.cabeça
        while no_atual is not None:  #conferindo se há mais nó para verificar
            if no_atual.nota >= 7.0 :
                aprovados.append(no_atual.nome)
            no_atual = no_atual.proximo

            if len(aprovados) == 0:  #verificação se há alunos aprovados na lista
                print("Nenhum aluno foi aprovado.")
            else:
                print("Alunos aprovados: ")
                for nome_aprovados in aprovados:
                    print(nome_aprovados)

def main():  #função principal que ira coletar as entradas dos usuários
    lista_alunos = listaEncadeada() #chama a função de lista encadeada dupla

    while True :  #verificação das entradas dos usuários

        try:
            quant_aluno = int(input("Quantos alunos você deseja cadastrar: "))
            if quant_aluno <= 0:
                print("A quantidade de alunos deve ser maior que zero. ")
                return
            
            for i in range(quant_aluno):
                nome = input("Digite o nome do aluno: ")
                nota = float(input("Digite a nota do aluno: "))

        except ValueError:
            print("Você digitou uma entrada inválida!")

main()  #chamada do programa para executar






    