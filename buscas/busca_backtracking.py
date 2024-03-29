from common import *

def busca_backtracking(actual_node, final_node, success=False, vis_np=None, fin_np=None):
    """
    Realiza uma Busca Backtracking, retornando se encontrou o nó,
    qual o caminho realizado e qual o caminho encontrado até o nó

    :param actual_node: Recebe o nó atual da busca
    :param final_node: Recebe o último nó / nó a ser encontrado da busca
    :param success: booleano que indica se o nó foi encontrado
    :param vis_np: String do percurso total realizado pela função
    :param fin_np: String do percurso do primeiro nó até o nó encontrado (None se o nó não foi encontrado)

    :return: Dicionário contendo:
     "success": booleano para indicar se encontrou ou não o nó.
     "visiting_node_path": String do percurso total realizado pela função
     "final_node_path": String do percurso do primeiro nó até o nó encontrado
    """


    success = success if success else False     # Variável que guarda se encontrou o nó final
    vis_np = vis_np if vis_np else ''           # Variável que guarda a string do percurso total realizado
    fin_np = fin_np if fin_np else ''           # Variável que guarda a string do percurso do primeiro nó até o nó encontrado

    node = actual_node
    node.status = NodeStatus.VISITADO
    vis_np = vis_np + node.name + ' > '

    # Se for o último nó
    if node == final_node:
        success = True
        fin_np = create_path(node)
        vis_np = vis_np[:-3]

    else:
        # Se ainda não encontrou o nó
        if not success:

            # Para cada nó adjacente, faça...
            for adjacent in node.adjacent_node:

                # Verifica se o nó adjacente é o nó procurado.
                if adjacent == final_node:
                    success = True
                    fin_np = create_path_string(node, adjacent)
                    vis_np = vis_np + adjacent.name
                    break

                # Se o nó adjacente estiver livre e ainda não foi encontrado o nó final
                elif adjacent.status == NodeStatus.LIVRE and not success:

                    # Define o nó atual como raíz do nó adjacente
                    adjacent.parent = node
                    aux = busca_backtracking(adjacent, final_node, success, vis_np, fin_np) # Chamada recursiva

                    # Atualiza os Dados
                    success = aux['success']
                    vis_np = aux['visiting_node_path']
                    fin_np = aux['final_node_path']

    # Define o nó atual como fechado
    node.status = NodeStatus.FECHADO

    return {
        'success': success,
        'visiting_node_path': vis_np,
        'final_node_path': fin_np
    }



def printa_busca_backtracking(map_list):
    for map in map_list:
        if map.type == SearchTypes.NAO_ORDENADA:

            print('- Realizando Backtracking em:', map.name, '\n')
            return_dict = busca_backtracking(map.start_node, map.end_node)

            if return_dict['success']:
                print('\n\t\t- O nó', map.end_node.name, 'foi encontrado!\n'
                      '\t\t- Caminho percorrido:', return_dict['visiting_node_path'],'\n'
                      '\t\t- Caminho até o nó:', return_dict['final_node_path']
                      )

            else:
                print('\t\t- O nó não pôde ser encontrado! :(')

            reset(map)