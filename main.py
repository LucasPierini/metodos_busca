from maps import MAPA_BUSCAS_NAO_ORDENADAS

from buscas.busca_largura      import printa_busca_em_largura
from buscas.busca_profundidade import printa_busca_em_profundidade
from buscas.busca_backtracking import printa_busca_backtracking
from buscas.busca_ordenada     import printa_busca_ordenada

while True:

    print('\n\n\n\n ~~~~~~~~~~ Ações ~~~~~~~~~~ \n')

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
        printa_busca_em_largura(MAPA_BUSCAS_NAO_ORDENADAS)

    elif user_input == 2 or user_input == '2':
        printa_busca_em_profundidade(MAPA_BUSCAS_NAO_ORDENADAS)

    elif user_input == 3 or user_input == '3':
        printa_busca_backtracking(MAPA_BUSCAS_NAO_ORDENADAS)

    elif user_input == 4 or user_input == '4':
        print('\n'
              '# -------------------------------------- #\n'
              '# --------------- Mapa 1 --------------- #\n'
              '# -------------------------------------- #\n'
              )
        printa_busca_ordenada(MAPA_BUSCA_ORDENADA_1)
        print('\n'
              '# -------------------------------------- #\n'
              '# --------------- Mapa 2 --------------- #\n'
              '# -------------------------------------- #\n'
              )
        printa_busca_ordenada(MAPA_BUSCA_ORDENADA_2)


    # ------------------ #
    # ----- Saindo ----- #
    # ------------------ #
    elif user_input == 0 or user_input == '0' or user_input == 'exit':
        print('\n- Okay! Tchaaaau')
        break