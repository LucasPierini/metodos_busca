from maps import *

from buscas.busca_largura      import printa_busca_em_largura
from buscas.busca_profundidade import printa_busca_em_profundidade
from buscas.busca_backtracking import printa_busca_backtracking
from buscas.busca_ordenada     import printa_busca_ordenada
from buscas.busca_gulosa       import printa_busca_gulosa

# try:

map_list = []
for _dict in map_dicts:
    map_list.append( create_map_by_dict(_dict) )

while True:

    print('\n ~~~~~~~~~~ Ações ~~~~~~~~~~ \n')

    print('Feito por Lucas M. Pierini :) \n')

    print('1. Realizar Busca em Largura')
    print('2. Realizar Busca em Profundidade')
    print('3. Realizar Backtracking')
    print('4. Realizar Busca Ordenada')
    print('X. Realizar Busca Gulosa')
    print('X. Realizar Busca A*')

    print('\n0. Sair \n')

    user_input = input('Selecione: ')
    print('\n')

    if   user_input == 1 or user_input == '1':
        printa_busca_em_largura(map_list)

    elif user_input == 2 or user_input == '2':
        printa_busca_em_profundidade(map_list)

    elif user_input == 3 or user_input == '3':
        printa_busca_backtracking(map_list)

    elif user_input == 4 or user_input == '4':
        printa_busca_ordenada(map_list)

    elif user_input == 5 or user_input == '5':
        printa_busca_gulosa(map_list)


    # ------------------ #
    # ----- Saindo ----- #
    # ------------------ #
    elif user_input == 0 or user_input == '0' or user_input == 'exit':
        print('\n- Okay! Tchaaaau')
        break

#
# except:
#     print("Ocorreu algum erro durante a execução do programa :(")