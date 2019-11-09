from typing import List
from common import *

def busca_ordenada(map):
    print('\n- Realizando Busca Ordenada:')

    success = False
    path_distance = 0
    path_string = ''
    path_list = [NodePath(map.start_node, None, None, [], map.relations)]

    while len(path_list) and not success:
        path = find_smaller_path(path_list)

        if path.node == map.end_node:
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

                    path_list.append(NodePath(node, parent, path, path_list, map.relations))
                    print(' ** Encontrado caminho de', parent, 'até', node)

                    path_list[-1].adjust_best_path(path_list)

            path_list.remove(path)
    reset(map)

    return {
        'success': success,
        'distance': path_distance,
        'path_string': path_string
    }



def printa_busca_ordenada(map):
    _dict = busca_ordenada(map)

    print('\n')

    if _dict['success']:
        print('- O nó', map.end_node, 'foi encontrado!')
        print('- Menor Percurso até o nó:', _dict['path_string'])
        print('- Distância total até o nó:', _dict['distance'])

    else:
        print('- O nó', map.end_node, 'não pôde ser encontrado! :(')
