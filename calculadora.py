def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def multi (a,b):
    return a*b
def div (a,b): 
    return a/b

print("__Bem vindo a calculadora em python__")   
print("Escolha sua operação: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha=int(input("Digite o número da operação desejada: "))

if escolha <= 0 or escolha > 4:
    print("\nOpção inválida!\n")
    exit(0)

n1=int(input("Digite o seu 1° número: "))
n2=int(input("Digite o seu 2° número: "))

if escolha == 1:
    print(f"A soma de {n1} + {n2} = foi de {add(n1,n2)}")
elif escolha ==2 :
    print(f"A subtração de {n1}-{n2}= foi de {sub(n1,n2)}")
elif escolha == 3:
    print(F"A multiplicação de {n1} x {n2}= foi de {multi(n1,n2)}")
elif escolha == 4:
    print(F"A dvisão de {n1}:{n2}= foi de {div(n1,n2)}")

    