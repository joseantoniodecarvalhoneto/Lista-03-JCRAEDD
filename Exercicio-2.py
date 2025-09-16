'''Defina uma função chamada insert que insere um item em uma estrutura unicamente
ligada em determinada posição. A função espera três argumentos: o item, a posição e
a estrutura ligada. (A última pode estar vazia.) A função retorna a estrutura ligada
modificada. Se a posição é maior ou igual ao comprimento da estrutura, a função insere
o item no final. Um exemplo de chamada da função, onde head é uma variável que é
uma ligação vazia ou se refere ao primeiro nó de uma estrutura, é head = insert(1, data,
head). '''

class node(object):
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next


head = None
tamanho_lista = 1
for count in range(1,tamanho_lista+1):
    head = node(count,head)
   

def insert(item,index,head):
    if head is None or index <= 0:
        head_new = node(item,head)
        return head_new
    else:
        probe = head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        probe.next = node(item,probe.next) 
    return head

