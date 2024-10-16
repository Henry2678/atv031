# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade(nm1):
    if nm1%2==0:
        return "e par"
    else:
        return "nao e par"
    

nm1 = int(input("digite um numero "))
par = verificar_paridade(nm1)
print(f"o numero {par} " )