from common import *
from maps import MAPA_BUSCAS_NAO_ORDENADAS

def busca_backtracking():

    def realiza_busca(actual_node, final_node, success=False, vis_np=False, fin_np=False):
        ''' Realiza uma Busca Backtracking, retornando se encontrou o nó, qual o caminho realizado e qual o caminho encontrado até o nó '''

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
                        aux = realiza_busca(adjacent, final_node, success, vis_np, fin_np) # Chamada recursiva

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

    print('\n- Realizando Backtracking...')

    return_dict = realiza_busca(MAPA_BUSCAS_NAO_ORDENADAS.start_node, MAPA_BUSCAS_NAO_ORDENADAS.end_node)

    if return_dict['success']:
        print('\t- O nó', MAPA_BUSCAS_NAO_ORDENADAS.end_node.name, 'foi encontrado!')
        print('    - Caminho percorrido:', return_dict['visiting_node_path'])
        print('    - Caminho até o nó:', return_dict['final_node_path'])

    else:
        print('    - O nó não pôde ser encontrado! :(')