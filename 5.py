import random 

num1= random.randint(1,60)

sorteio=[0,0,0,0,0,0]

aposta=[0,0,0,0,0,0]

igual=0 

for i in range(len(sorteio)):
    sorteio[i]= random.randint(1,20)
    print(sorteio)
   
    
    aposta[i]= int(input("Digite um número entre 1 e 20:"))
    
    if aposta[i] > 20 or aposta[i] < 0:
        print("Invalido. Digite um numero entre 1 e 20")
    
    elif aposta[i]== sorteio[0]:
        print("você acertou na 1 posiçao")
        igual+=1
    
    elif aposta[i]== sorteio[1]:
        print("você acertou na 2 posiçao")
        igual+=1
    
    elif aposta[i]== sorteio[2]:
        print("você acertou na 3 posiçao")
        igual+=1
    
    elif aposta[i]== sorteio[3]:
        print("você acertou na 4 posiçao")
        igual+=1
    
    elif aposta[i]== sorteio[4]:
        print("você acertou na 5 posiçao")
        igual+=1
    
    elif aposta[i]== sorteio[5]:
        print("você acertou na 6 posiçao")
        igual+=1

print(f'Você acertou {igual} de 6')
    
    
    
    