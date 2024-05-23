# Programa de do cinema Com idade

print('******************************************************************************************************************************************')
print('******************************************************************************************************************************************')
print('Para informar qual sua sala seu filme vai passar precisamos de alguns dados para oferecer uma boa experencia para vc!')

import os 
import time
time.sleep(2)
nome = input('informe o seu nome: \n')
idade = int(input('informe a sua idade \n'))

while True:

    print(f'Querido cliente {nome} nosso cinema possui 5 salas, qual filme o senhor comprou o ingresso:')
    print('1 - Ataque dos vermes maldidos, classificação indicativa: Livre')
    print('2 - Tomates verdes fritos, classificação indicativa: 12 anos')
    print('3 - Rollerball, classificação indicativa: 14 anos')
    print('4 - Marte ataca, classificação indicativa: 16 anos')
    print('5 - Não olhe para Cima, classificação indicativa: 18 anos')

    sala = input('Informe qual o filme o senhor selecionou 1 a 5: ')
    
    match sala:
        case '1': 
            if idade > 0:
                break
            else:
                os.system('cls')
                print('ENTRADA NÃO PERMITIDA')
                time.sleep(3)
                os.system('cls')
        case '2':
            if idade >= 12:
                break
            else:
                os.system('cls')
                print('ENTRADA NÃO PERMITIDA')
                time.sleep(10)
                os.system('cls') 
        case '3':
            if idade >= 14:
                break
            else:
                os.system('cls')
                print('ENTRADA NÃO PERMITIDA')
                time.sleep(10)
                os.system('cls')  
        case '4': 
            if idade >= 16: 
                break
            else:
                os.system('cls')
                print('ENTRADA NÃO PERMITIDA')
                time.sleep(10)
                os.system('cls')
        case '5':
            if idade >= 18:
                break
            else:
                os.system('cls')
                print('ENTRADA NÃO PERMITIDA')
                time.sleep(10)
                os.system('cls')
        case _:
            os.system('cls')
            print('opçao inválida')
            print('informe outra sala')

            
            continue
    
os.system('cls')
print (f'Senhor {nome} o seu filme será exibido na sala {sala}. ')
print ('Tenha um bom filme, aproveite compre uma pipoca.')
time.sleep(10)