from anytree import Node, RenderTree

def div(x,z):
        if(z == 0):
            return{"Divisão por Zero."}
        else:
            return{x/z}

prec = {'*': 4, '/': 3, '+': 2, '-': 1, '(': 0, '=' : 8, '': 9}
    #ordem de prioridade

while(True):
    
    expr = input().split(' ')
    #separa expressão

    if(expr[0] == "exit"):
        break
    
    if(len(expr) == 1):
        print(expr[0])

    stack = []
    opstream = []
    last = ''
    #necessário para o shunting-yard




    print(expr)
    #teste
    





