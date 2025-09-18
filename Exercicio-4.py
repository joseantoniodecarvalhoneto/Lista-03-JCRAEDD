'''4. Defina uma função makeTwoWay que espera uma estrutura unicamente ligada como o
argumento. A função cria e retorna uma estrutura duplamente ligada que contém os
itens na estrutura unicamente ligada. (Nota: A função não deve alterar a estrutura do
argumento). '''

class Node(object):
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next

class Two_node(Node):
        def __init__(self,data,previous = None,next = None):
            self.data = data
            self.next = next
            self.previous = previous

head = None
tamanho_lista = 1
for count in range(1,tamanho_lista+1):
    head = Node(count,head)
   
def makeTwoWay(head):
    
    if head is None:
        return None
    else:

        new_head = Two_node(head.data)
        tail = new_head
        old_point = head.next

        while old_point is  not None:
             
            new_node = Two_node(old_point.data)

            tail.next = new_node
            new_node.previous = tail

            tail = new_node
            old_point = old_point.next
               
    
    
    return new_head