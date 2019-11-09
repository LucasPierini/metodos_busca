from classes import *
from maps import *

def find_smaller_path(path_list) -> NodePath:
    ''' Retorna o NodePath de menor distância de uma lista '''
    smaller = path_list[0]
    for path in path_list:
        if path.distance < smaller.distance:
            smaller = path

    return smaller


def get_another_node_from_relation(node, relation):
    if relation.node_1 == node:
        return relation.node_2
    else:
        return relation.node_1


def base_path_string(node):
    ''' Cria uma string invertida do percurso até o nó '''
    node_name = node.name

    if node.parent:
        node_name = node_name + ' > ' + base_path_string(node.parent)

    return node_name


def create_path_string(path_or_node, next_node=False):
    ''' Cria uma string do percurso realizado até o nó. '''

    if type(path_or_node) == NodePath:
        node_name = base_path_string(path_or_node.node)
        return node_name[::-1]

    elif type(path_or_node) == Node:
        node_name = base_path_string(path_or_node)
        node_name = node_name[::-1]

        if next_node:
            node_name = node_name + ' > ' + next_node.name

        return node_name

    else:
        return None


def reset(map):
    ''' Reseta os nós para sua versão inicial '''
    for node in map.nodes:
        map.nodes[node].status = NodeStatus.LIVRE
        map.nodes[node].parent = None

    for rel in map.relations:
        rel.status = RelationStatus.NOVA
