from utils import *

while True:
    cmd = input("Digite o nome do medicamento: ")
    match cmd:
        case 'exit':
            print('saindo')
            break

        case '':
            print('o campo está vazio!')

        case _:
            if not existMed(cmd):
                print('O medicamento não foi encontrado no banco de dados.')
            else:
                print(f'Medicamento buscado: {cmd}')
                farmacos = searchFarm(cmd)
                if len(farmacos) > 1:
                    print('Medicamentos encontrados:')
                    while True:
                        for i in range(0, len(farmacos)):
                            print(f'[{i}] - {farmacos[i]}')
                        try:
                            sel = int(input('Especifique o medicamento: '))
                            if sel < len(farmacos):
                                farmaco=farmacos[sel]
                                break
                            else:
                                print('valor inválido!')
                                print('tente novamente.\n')
                        except:
                            print('valor inválido!')
                            print('tente novamente.\n')
                    print(f'Buscando por: {farmaco}')
                else:
                    farmaco=farmacos[0]
                    print(f'Buscando por: {farmaco}')
                print('Medicamentos • Concentração • Dententor')
                for line in searchMed(farmaco):
                    print(f'{line[0]} • {line[1]} • {line[2]}')

