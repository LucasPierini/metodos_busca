from typing import List
from common import *

def busca_gulosa(map):
    print('- Realizando Busca Gulosa:')

    success = False
    path_string = ''
    path_list = [NodePath(map.start_node, None, None, [], map.relations)]

    while len(path_list) and not success:
        path = find_costless_path(path_list)

        if path.node == map.end_node:
            success = True
            path_string = create_path_string(path)

        else:
            if not path.parent_node:
                print('* Começando pelo nó', path.node)
            else:
                print('\n* Checando próximo caminho menos custoso: de', path.parent_node, 'até', path.node)

            for rel in path.node.relations:

                # Se a relação ainda não foi verificada
                if rel.status == RelationStatus.NOVA:
                    node = get_another_node_from_relation(path.node, rel)
                    parent = path.node

                    path_list.append(NodePath(node, parent, path, path_list, map.relations))
                    print(' ** Encontrado caminho de', parent, 'até', node)

                    path_list[-1].adjust_best_path(path_list, "gulosa")

            path_list.remove(path)
    reset(map)

    return {
        'success': success,
        'path_string': path_string
    }



def printa_busca_gulosa(map_list):
    for map in map_list:
        if map.type == SearchTypes.ORDENADA:

            print('- Realizando Busca Gulosa em:', map.name, '\n')
            return_dict = busca_gulosa(map)

            if return_dict['success']:
                print('\n- O nó', map.end_node, 'foi encontrado!\n'
                      '- Percurso Menos Custoso até o nó:', return_dict['path_string'], '\n'
                     )

            else:
                print('- O nó não pôde ser encontrado! :(')