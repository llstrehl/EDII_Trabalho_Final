from anytree import Node, RenderTree

def div(x,z):
        if(z == 0):
            return{"Divisão por Zero."}
        else:
            return{x/z}

while(True):
    
    expr = input().split(' ')
    #separa expressão

    if(expr[0] == "exit"):
        break
    
    print(expr)
    #teste
    





