from typing import List
from common import *

def busca_ordenada(map):
    print('- Realizando Busca Ordenada:')

    success = False
    path_distance = 0
    path_string = ''
    path_list = [NodePath(map.start_node, None, None, [], map.relations)]

    while len(path_list) and not success:
        path = find_lower_path(path_list, 'ordenada')

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

                    new_path = NodePath(node, parent, path, path_list, map.relations)
                    path_list.append(new_path)
                    print(' ** Encontrado caminho de', parent, 'até', node, '( Dist.:', new_path.distance,')')

                    path_list[-1].adjust_best_path(path_list)

            path_list.remove(path)
    reset(map)

    return {
        'success': success,
        'distance': path_distance,
        'path_string': path_string
    }



def printa_busca_ordenada(map_list):
    for map in map_list:
        if map.type == SearchTypes.ORDENADA:

            print('- Realizando Busca Ordenada em:', map.name, '\n')
            return_dict = busca_ordenada(map)

            if return_dict['success']:
                print('\n- O nó', map.end_node, 'foi encontrado!\n'
                      '- Menor Percurso até o nó:', return_dict['path_string'], '\n'
                      '- Distância total até o nó:', return_dict['distance']
                     )

            else:
                print('- O nó não pôde ser encontrado! :(')
