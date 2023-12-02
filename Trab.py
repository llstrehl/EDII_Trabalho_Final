import re
from Tree import Tree

#Ignorar erro
regex_expression = "[\/\+\-\*\(\)]|[0-9]{0,15}[.]{0,1}[0-9]{0,4}"
regex_vari = "[A-Za-z]{1,255}"
variaveis = {}

def calcular(variaveis, string):
    for vari in variaveis.keys():
        if(re.search(r'\b' + vari + r'\b', string)):
            string = re.sub(r'\b' + vari + r'\b', variaveis[vari], string)

    if(re.search(regex_vari, string)):
        variErro = re.findall(regex_vari, string)
        for vari in variErro:
            raise Exception("Erro: Variável \""+ vari +"\" não inicializada")

    for char in string:
        if not re.search(regex_expression, char):
            raise Exception("Erro: caracter \""+ char +"\" inválido")

    if(string.count("(") != string.count(")")):
        raise Exception("Erro: parênteses desbalanceados")
            
    txt_list = re.findall(regex_expression, string)
    tree = Tree.build("".join(txt_list))  
    return tree.evaluate()


while(True):
    expr = input()
    expr = expr.replace(" ", "")

    if(expr == "exit"):
        break

    if('=' in expr):
        key = expr[:expr.index('=')]
        value = expr[expr.index('=')+1:]

        try:
            variaveis[key] = str(calcular(variaveis,value))
        except ZeroDivisionError:
            print("Erro:Divisão por zero")
        except Exception as err:
            print(err)

    else:
        try:
            print(calcular(variaveis, expr))
        except ZeroDivisionError:
            print("Erro:Divisão por zero")
        except Exception as err:
            print(err)