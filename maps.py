from classes import *

def create_map_by_dict(_dict) -> Map:

    if 'type' in _dict:

        # Teste de Criação de Mapa para buscas não-ordenadas
        if _dict['type'] == SearchTypes.NAO_ORDENADA:

            # Valida se os campos do dicionário existem.
            if 'nodes' in _dict and 'adjacent' in _dict and 'first' in _dict and 'last' in _dict:
                return create_map_type_0(_dict)

            else:
                print('Não foi possível criar o mapa pois falta algum campo.')

        elif _dict['type'] == SearchTypes.ORDENADA:

            # Valida se os campos do dicionário existem.
            if 'nodes' in _dict and 'relations' in _dict and 'first' in _dict and 'last' in _dict:
                return create_map_type_1(_dict)

            else:
                print('Não foi possível criar o mapa pois falta algum campo.')

    return None


def create_map_type_0(_dict) -> Map:
    """
    Cria um mapa para buscas não ordenadas (Largura, Profundidade e Backtracking)

    :param _dict: Dicionário contendo as informações sobre o mapa
    :return: Map
    """
    new_map = Map()
    new_map.name = _dict['map_name']
    new_map.type = _dict['type']

    try:
        # Cria os nós
        for node in _dict['nodes']:
            new_map.nodes[ node['name'] ] = Node( node['name'] )

        # Cria as Adjacencias
        for adj in _dict['adjacent']:
            for key, value in adj.items():
                if key in new_map.nodes:
                    for n in value:
                        if n in new_map.nodes:
                            new_map.nodes[key].adjacent_node.append(new_map.nodes[n])
                else:
                    # print("ERRO")
                    raise Exception("Erro no dicionário do mapa. Esse nó da relação não existe no mapa!")

        new_map.start_node = new_map.nodes[_dict['first']]
        new_map.end_node = new_map.nodes[_dict['last']]

    except Exception as exc:
        return None

    return new_map


def create_map_type_1(_dict) -> Map:
    """
    Cria um mapa para buscas ordenadas ou informadas (Ordenada, Gulosa e A*)

    :param _dict: Dicionário contendo as informações sobre o mapa
    :return: Map
    """
    new_map = Map()
    new_map.name = _dict['map_name']
    new_map.type = _dict['type']

    try:
        # Cria os nós
        for node in _dict['nodes']:
            new_map.nodes[ node['name'] ] = Node( node['name'], node['cost'] )

        # Cria as relações
        for rel in _dict['relations']:
            if rel['node1'] in new_map.nodes and rel['node2'] in new_map.nodes:
                new_map.relations.append(
                    NodeRelation( new_map.nodes[ rel['node1'] ], new_map.nodes[ rel['node2'] ], rel['distance'] )
                )

        new_map.start_node = new_map.nodes[_dict['first']]
        new_map.end_node = new_map.nodes[_dict['last']]

    except Exception as exc:
        print("Ocorreu algum erro na criação do Mapa :(")
        return None

    return new_map


map_dicts = [
    {
        "map_name": "Mapa para buscas não ordenadas",
        "type": SearchTypes.NAO_ORDENADA,
        "nodes": [
            { "name": "A" },
            { "name": "B" },
            { "name": "C" },
            { "name": "D" },
            { "name": "E" },
            { "name": "F" },
            { "name": "G" },
            { "name": "H" },
            { "name": "I" },
            { "name": "J" },
            { "name": "L" },
            { "name": "M" },
            { "name": "N" },
            { "name": "O" },
            { "name": "P" },
            { "name": "Q" },
            { "name": "R" },
            { "name": "S" },
        ],
        "adjacent": [
            # Tem que seguir a ordem Baixo, Esquerda, Direita, Cima.
            # Colocar aspas vazias caso não possua relação de adjacencia (apenas por uma questão de organização)
            { "A" : [ "B", "", "", "E" ] },
            { "B" : [ "C", "", "A", "F" ] },
            { "C" : [ "", "", "B", "" ] },
            { "D" : [ "", "", "", "H" ] },
            { "E" : [ "", "A", "", "I" ] },
            { "F" : [ "G", "B", "", "" ] },
            { "G" : [ "H", "", "F", "L" ] },
            { "H" : [ "", "D", "G", "" ] },
            { "I" : [ "J", "E", "", "N" ] },
            { "J" : [ "", "", "I", "O" ] },
            { "L" : [ "M", "G", "", "" ] },
            { "M" : [ "", "", "L", "Q" ] },
            { "N" : [ "", "I", "", "" ] },
            { "O" : [ "P", "J", "", "R" ] },
            { "P" : [ "Q", "", "O", "S" ] },
            { "Q" : [ "", "M", "P", "" ] },
            { "R" : [ "", "O", "", "" ] },
            { "S" : [ "", "P", "", "" ] },
        ],
        "first": "A",
        "last": "S",
    },

    {
        "map_name": "Mapa para buscas ordenadas 1",
        "type": SearchTypes.ORDENADA,
        "nodes": [
            { "name": "A", "cost": 24 },
            { "name": "B", "cost": 15 },
            { "name": "C", "cost": 22 },
            { "name": "D", "cost": 12 },
            { "name": "E", "cost": 7 },
            { "name": "F", "cost": 7 },
            { "name": "G", "cost": 0 },
        ],
        "relations": [
            { "node1": "A", "node2": "B", "distance": 9 },
            { "node1": "A", "node2": "C", "distance": 5 },
            { "node1": "A", "node2": "D", "distance": 13 },
            { "node1": "B", "node2": "D", "distance": 3 },
            { "node1": "B", "node2": "E", "distance": 10 },
            { "node1": "C", "node2": "F", "distance": 12 },
            { "node1": "D", "node2": "E", "distance": 6 },
            { "node1": "D", "node2": "G", "distance": 14 },
            { "node1": "E", "node2": "G", "distance": 7 },
            { "node1": "F", "node2": "G", "distance": 10 },
        ],
        "first": "A",
        "last": "G",
    },

    {
        "map_name": "Mapa para buscas ordenadas 2",
        "type": SearchTypes.ORDENADA,
        "nodes": [
            { "name": "A", "cost": 16 },
            { "name": "B", "cost": 13 },
            { "name": "C", "cost": 15 },
            { "name": "D", "cost": 7 },
            { "name": "E", "cost": 10 },
            { "name": "F", "cost": 10 },
            { "name": "G", "cost": 0 },
        ],
        "relations": [
            { "node1": "A", "node2": "B", "distance": 8 },
            { "node1": "A", "node2": "C", "distance": 3 },
            { "node1": "A", "node2": "D", "distance": 16 },
            { "node1": "B", "node2": "D", "distance": 8 },
            { "node1": "B", "node2": "E", "distance": 7 },
            { "node1": "C", "node2": "D", "distance": 16 },
            { "node1": "C", "node2": "F", "distance": 6 },
            { "node1": "D", "node2": "E", "distance": 5 },
            { "node1": "D", "node2": "F", "distance": 6 },
            { "node1": "D", "node2": "G", "distance": 10 },
            { "node1": "E", "node2": "G", "distance": 15 },
            { "node1": "F", "node2": "G", "distance": 17 },
        ],
        "first": "A",
        "last": "G",
    }
]

