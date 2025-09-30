'''6. Faça um programa que cadastre n funcionários. Para cada funcionário devem ser
cadastrados nome e salário. Os dados devem ser armazenados em uma lista
simplesmente encadeada e ordenada, de forma decrescente, pelo salário do
funcionário. Posteriormente, o programa de mostrar:
a. O nome do funcionário que tem o maior salário (em caso de empate mostrar
todos);
b. A média salarial de todos os funcionários juntos;
c. A quantidade de funcionários com salário superior a um valor fornecido pelo
usuário. Caso nenhum funcionário satisfaça essa condição, mostrar mensagem. '''

class Funcionario():
    def __init__(self,nome,salario,next = None):
        self.nome = nome
        self.salario = salario
        self.next = next

def adiciona_funcionario(cabeca,nome,salario):

    novo_funcionario = Funcionario(nome,salario)

    if cabeca is None or novo_funcionario.salario > cabeca.salario:
        novo_funcionario.next = cabeca
        return novo_funcionario
    
    atual = cabeca
    while atual.next is not None and atual.next.salario > novo_funcionario.salario:
        atual = atual.next
    
    novo_funcionario.next = atual.next
    atual.next = novo_funcionario
    
    return cabeca


def filtro_salario(cabeca,filtro):
    probe = cabeca
    contador = 0
    while probe.salario > filtro and probe.next is not None:
        probe = probe.next
        contador += 1
    return contador

def main():

    funcionario = None
    contador = 0
    acumulador = 0
    print("Digite o nome e o salario dos funcionários, para finalizar, aperte a tecla 'ENTER' ")
    
    while True:
        nome = input("Qual o nome do funcionário? ")
        if nome == "":
            break

        salario = float(input("Qual o salário do funcionário? "))

        acumulador += salario
        contador += 1
        media = acumulador / contador

        funcionario = adiciona_funcionario(funcionario,nome,salario)
    
    print("Veja a quantidade de funcionários com salarios maiores que um valor digitado:")
    filtro = float(input("> "))
    qtd_funcionarios = filtro_salario(funcionario,filtro)

    print(f"O funcionário com o maior salário é: {funcionario.nome} \n")
    print(f'A média salarial é: {media} \n')
    print(f'A quantidade de  funcionários que ganham mais que o filtro são: {qtd_funcionarios}')
