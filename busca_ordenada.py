from typing import List
from common import *


def busca_ordenada(start_node, end_node, relation_list):
    print('\n- Realizando Busca Ordenada:')

    success = False
    path_distance = 0
    path_string = ''
    path_list = [NodePath(start_node, None, None, [], relation_list)]

    while len(path_list) and not success:

        path = find_smaller_path(path_list)

        if path.node == end_node:
            success = True
            path_string = create_path_string(path)
            path_distance = path.distance

        else:

            if not path.parent_node:
                print('* Começando pelo nó', path.node)
            else:
                print('\n* Checando próximo caminho mais curto: de', path.parent_node, 'até', path.node)

            for rel in path.node.relations:

                # Se a relação ainda não foi verificada
                if rel.status == RelationStatus.NOVA:
                    node = get_another_node_from_relation(path.node, rel)
                    parent = path.node

                    path_list.append(NodePath(node, parent, path, path_list, relation_list))
                    print(' ** Encontrado caminho de', parent, 'até', node)

                    path_list[-1].adjust_best_path(path_list)

            path_list.remove(path)

    return {
        'success': success,
        'distance': path_distance,
        'path_string': path_string
    }


def create_first_map():

    # --------------------------- #
    # ----- Criação dos Nós ----- #
    # --------------------------- #
    _node_list: List[Node] = []

    node_a = Node('A');    _node_list.append(node_a)
    node_b = Node('B');    _node_list.append(node_b)
    node_c = Node('C');    _node_list.append(node_c)
    node_d = Node('D');    _node_list.append(node_d)
    node_e = Node('E');    _node_list.append(node_e)
    node_f = Node('F');    _node_list.append(node_f)
    node_g = Node('G');    _node_list.append(node_g)

    # --------------------------------- #
    # ----- Conexões entre os Nós ----- #
    # --------------------------------- #
    _relation_list = []

    # ----- Nó A ----- #
    relation_a_b = NodeRelation(node_a, node_b, 9);    _relation_list.append(relation_a_b)
    relation_a_c = NodeRelation(node_a, node_c, 5);    _relation_list.append(relation_a_c)
    relation_a_d = NodeRelation(node_a, node_d, 13);   _relation_list.append(relation_a_d)

    # ----- Nó B ----- #
    relation_b_d = NodeRelation(node_b, node_d, 3);    _relation_list.append(relation_b_d)
    relation_b_e = NodeRelation(node_b, node_e, 10);   _relation_list.append(relation_b_e)

    # ----- Nó C ----- #
    relation_c_f = NodeRelation(node_c, node_f, 12);   _relation_list.append(relation_c_f)

    # ----- Nó D ----- #
    relation_d_e = NodeRelation(node_d, node_e, 6);    _relation_list.append(relation_d_e)
    relation_d_g = NodeRelation(node_d, node_g, 14);   _relation_list.append(relation_d_g)

    # ----- Nó E ----- #
    relation_e_g = NodeRelation(node_e, node_g, 7);   _relation_list.append(relation_e_g)

    # ----- Nó F ----- #
    relation_f_g = NodeRelation(node_f, node_g, 10);  _relation_list.append(relation_f_g)

    return {
        'node_list': _node_list,
        'relation_list': _relation_list,
        'map_id': 1
    }


def create_second_map():

    # --------------------------- #
    # ----- Criação dos Nós ----- #
    # --------------------------- #
    _node_list = []

    node_a = Node('A');    _node_list.append(node_a)
    node_b = Node('B');    _node_list.append(node_b)
    node_c = Node('C');    _node_list.append(node_c)
    node_d = Node('D');    _node_list.append(node_d)
    node_e = Node('E');    _node_list.append(node_e)
    node_f = Node('F');    _node_list.append(node_f)
    node_g = Node('G');    _node_list.append(node_g)

    # --------------------------------- #
    # ----- Conexões entre os Nós ----- #
    # --------------------------------- #
    _relation_list = []

    # ----- Nó A ----- #
    _relation_list.append(NodeRelation(node_a, node_b, 8))
    _relation_list.append(NodeRelation(node_a, node_c, 3))
    _relation_list.append(NodeRelation(node_a, node_d, 16))

    # ----- Nó B ----- #
    _relation_list.append(NodeRelation(node_b, node_d, 8))
    _relation_list.append(NodeRelation(node_b, node_e, 7))

    # ----- Nó C ----- #
    _relation_list.append(NodeRelation(node_c, node_d, 16))
    _relation_list.append(NodeRelation(node_c, node_f, 6))

    # ----- Nó D ----- #
    _relation_list.append(NodeRelation(node_d, node_e, 5))
    _relation_list.append(NodeRelation(node_d, node_f, 6))
    _relation_list.append(NodeRelation(node_d, node_g, 10))

    # ----- Nó E ----- #
    _relation_list.append(NodeRelation(node_e, node_g, 15))

    # ----- Nó F ----- #
    _relation_list.append(NodeRelation(node_f, node_g, 17))

    return {
        'node_list': _node_list,
        'relation_list': _relation_list,
        'map_id': 2
    }


def create_map(_id):
    ''' Cria o mapa de nós e relações ;) -- 1 é o padrão '''

    if _id == 1 or _id == '1':
        return create_first_map()

    elif _id == 2 or _id == '2':
        return create_second_map()

    else:
        return create_first_map()


# ----------------- #
# ----- Setup ----- #
# ----------------- #

# Inicia com o primeiro mapa
setup_dict = create_map(1)
node_list = setup_dict['node_list']
relation_list = setup_dict['relation_list']
map_id = setup_dict['map_id']

# Define o Nó Inicial e o Nó Final, respectivamente.
start_node = node_list[0];
end_node = node_list[-1]

user_input = True
while user_input and user_input != '0' and user_input != 'exit':

    print('\n\n\n\n ~~~~~~~~~~ Ações ~~~~~~~~~~ \n')

    print('1. Realizar Busca Ordenada')
    print('2. Alterar Nó Inicial    ( Atual:', start_node, ' )')
    print('3. Alterar Nó Final      ( Atual:', end_node, ' )')

    print('\n9. Alterar Mapa          ( Atual:', map_id, ' )')
    print('\n0. Sair \n')

    user_input = input('Selecione: ')
    print('\n')

    # -------------------------- #
    # ----- Busca Ordenada ----- #
    # -------------------------- #
    if user_input == 1 or user_input == '1':

        _dict = busca_ordenada(start_node, end_node, relation_list)

        print('\n')

        if _dict['success']:
            print('- O nó', end_node, 'foi encontrado!')
            print('- Menor Percurso até o nó:', _dict['path_string'])
            print('- Distância total até o nó:', _dict['distance'])

        else:
            print('- O nó', end_node, 'não pôde ser encontrado! :(')


    # ------------------------------ #
    # ----- Alterar Nó Inicial ----- #
    # ------------------------------ #
    elif user_input == 2 or user_input == '2':

        new_node = input('\n- Insira o novo Nó Inicial (Apenas 1 char de A até G): ')
        changed = False

        for x in node_list:
            if x.name.lower() == new_node.lower():
                start_node = x
                changed = True

        if not changed:
            print('Desculpe, mas este nó não existe. :(')


    # ---------------------------- #
    # ----- Alterar Nó Final ----- #
    # ---------------------------- #
    elif user_input == 3 or user_input == '3':

        new_node = input('\n- Insira o novo Nó Final (Apenas 1 char de A até G): ')
        changed = False

        for x in node_list:
            if x.name.lower() == new_node.lower():
                end_node = x
                changed = True

        if not changed:
            print('Desculpe, mas este nó não existe. :(')


    # ------------------------ #
    # ----- Alterar Mapa ----- #
    # ------------------------ #
    elif user_input == 9 or user_input == '9':
        reset(node_list, relation_list)

        new_map = input('\n- Insira o novo Id do Mapa (1 ou 2): ')

        setup_dict = create_map(new_map)

        node_list = setup_dict['node_list']
        relation_list = setup_dict['relation_list']
        map_id = setup_dict['map_id']

        start_node = node_list[0];
        end_node = node_list[-1]


    # ------------------ #
    # ----- Saindo ----- #
    # ------------------ #
    elif user_input == 0 or user_input == '0' or user_input == 'exit':
        print('\n- Okay! Tchaaaau')
        print('Feito por Lucas M. Pierini :) \n')

    reset(node_list, relation_list)

