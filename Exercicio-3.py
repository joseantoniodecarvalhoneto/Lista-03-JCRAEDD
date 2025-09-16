'''3. Defina uma função chamada pop que remove o item em determinada posição de uma
estrutura unicamente ligada. Essa função espera uma posição como primeiro
argumento, com a precondição 0 <= posição < comprimento da estrutura. Seu segundo
argumento é a estrutura ligada, que, é claro, não pode estar vazia. A função retorna uma tupla contendo a estrutura ligada modificada e o item que foi removido. Um
exemplo de chamada é (head, item) = pop(1, head). '''

class Node(object):
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next


head = None
tamanho_lista = 1
for count in range(1,tamanho_lista+1):
    head = Node(count,head)
   
def pop(index,head):
    if index <= 0 or head.next is None:
        removedItem = head.data
        head = head.next
        return (removedItem,head)
    else:
        probe = head 
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
        removedItem = probe.next.data
        probe.next = probe.next.next 
        return (removedItem,head)