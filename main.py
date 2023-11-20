from utils import *
from time import sleep

while True:
    cmd = input("Digite o nome do medicamento: ")
    sleep(0.25)
    match cmd:
        case 'exit':
            print('saindo')
            break

        case '':
            print('\nO campo está vazio!')
            sleep(0.25)
            print('Tente novamente.\n')
            sleep(0.5)

        case _:
            if not existMed(cmd):
                sleep(0.5)
                print('\nO medicamento não foi encontrado no banco de dados.')
                sleep(0.25)
                print('Por favor, tente novamente.\n')
            else:
                print(f'Medicamento buscado: {cmd}\n')
                sleep(0.25)
                farmacos = searchFarm(cmd)
                if len(farmacos) > 1:
                    print('Medicamentos encontrados:')
                    while True:
                        for i in range(0, len(farmacos)):
                            print(f'[{i}] - {farmacos[i]}')
                            sleep(0.15)
                        try:
                            sel = int(input('Especifique o medicamento: '))
                            if sel < len(farmacos):
                                farmaco=farmacos[sel]
                                break
                            else:
                                print('valor inválido!')
                                sleep(0.15)
                                print('tente novamente.\n')
                        except:
                            print('valor inválido!')
                            print('tente novamente.\n')
                    print(f'\nBuscando por: {farmaco}')
                    sleep(0.25)
                else:
                    farmaco=farmacos[0]
                    print(f'Buscando por: {farmaco}')
                    sleep(0.25)

                print('Medicamentos • Concentração • Dententor')
                sleep(0.15)
                for line in searchMed(farmaco):
                    print(f'{line[0]} • {line[1]} • {line[2]}')
                    sleep(0.15)
                print('\n')

