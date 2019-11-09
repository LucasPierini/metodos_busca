from busca_ordenada import *
from busca_largura import *
from busca_backtracking import *
from maps import MAPA_BUSCAS_NAO_ORDENADAS, MAPA_BUSCA_ORDENADA_1, MAPA_BUSCA_ORDENADA_2

while True:

    print('\n\n\n\n ~~~~~~~~~~ Ações ~~~~~~~~~~ \n')

    print('Feito por Lucas M. Pierini :) \n')

    print('1. Realizar Busca em Largura')
    print('2. Realizar Busca em Profundidade')
    print('3. Realizar Backtracking')
    print('4. Realizar Busca Ordenada')
    print('5. Realizar Busca ???')
    print('6. Realizar Busca A Estrela')

    print('\n0. Sair \n')

    user_input = input('Selecione: ')
    print('\n')

    if user_input == 1 or user_input == '1':
        busca_em_largura()

    elif user_input == 3 or user_input == '3':
        busca_backtracking()

    elif user_input == 4 or user_input == '4':
        busca_ordenada()


    elif user_input == 2 or user_input == '2':
        print('\n- Realizando Busca em Profundidade...')

        return_dict = busca_em_profundidade(initial_node, final_node)

        if return_dict['success']:
            print('    - O nó', final_node.name, 'foi encontrado!')
            print('    - Caminho percorrido:', return_dict['visiting_node_path'])
            print('    - Caminho até o nó:', return_dict['final_node_path'])

        else:
            print('    - O nó não pôde ser encontrado! :(')




    # ------------------ #
    # ----- Saindo ----- #
    # ------------------ #
    elif user_input == 0 or user_input == '0' or user_input == 'exit':
        print('\n- Okay! Tchaaaau')
        break