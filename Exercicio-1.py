'''1. Defina uma função length (não len) que espera uma estrutura unicamente ligada como
argumento. A função retorna o número de itens na estrutura. '''

class node(object):
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next


head = None
tamanho_lista = 1
for count in range(1,tamanho_lista+1):
    head = node(count,head)

def length(heard):
    cont = 0
    while heard != None:
        cont +=1
        heard = heard.next
    return cont