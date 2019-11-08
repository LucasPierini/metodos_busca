from classes import *


def find_smaller_path(path_list):
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


def create_path_string(path):
    ''' Cria uma string do percurso realizado até o nó '''

    node_name = base_path_string(path.node)
    return node_name[::-1]





def reset(node_list, relation_list):
    for x in node_list:
        x.parent = None

    for x in relation_list:
        x.status = RelationStatus.NOVA
