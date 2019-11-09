from classes import *

# ------------------------------------------ #
# ----- Definição dos nós do Labirinto ----- #
# ------------------------------------------ #

map_dict_1 = {
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
        # Colocar aspas vazias caso não possua relação de adjacencia
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
    "relations": [],
    "first": "A",
    "last": "S",
}


map_dict_1 = {
    "type": SearchTypes.ORDENADA,
    "nodes": [
        { "name": "A" },
        { "name": "B" },
        { "name": "C" },
        { "name": "D" },
        { "name": "E" },
        { "name": "F" },
        { "name": "G" },
    ],
    "adjacent": [],
    "relations": [],
    "first": "A",
    "last": "S",
}

MAPA_BUSCAS_NAO_ORDENADAS = create_map_by_dict(map_dict_1)

# # -------------------------------------------------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------------------------------------------------- #
#
# # --------------------------- #
# # ----- Criação dos Nós ----- #
# # --------------------------- #
# MAPA_BUSCA_ORDENADA_1 = Map()
#
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('A', 24))   # 0
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('B', 15))   # 1
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('C', 22))   # 2
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('D', 12))   # 3
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('E', 7))    # 4
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('F', 7))    # 5
# MAPA_BUSCA_ORDENADA_1.nodes.append(Node('G', 0))    # 6
#
# # --------------------------------- #
# # ----- Conexões entre os Nós ----- #
# # --------------------------------- #
# _relation_list = []
#
# # ----- Nó A ----- #
# relation_a_b = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[1], 9);    _relation_list.append(relation_a_b)
# relation_a_c = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[2], 5);    _relation_list.append(relation_a_c)
# relation_a_d = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[3], 13);   _relation_list.append(relation_a_d)
#
# # ----- Nó B ----- #
# relation_b_d = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[1], MAPA_BUSCA_ORDENADA_1.nodes[3], 3);    _relation_list.append(relation_b_d)
# relation_b_e = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[1], MAPA_BUSCA_ORDENADA_1.nodes[4], 10);   _relation_list.append(relation_b_e)
#
# # ----- Nó C ----- #
# relation_c_f = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[2], MAPA_BUSCA_ORDENADA_1.nodes[5], 12);   _relation_list.append(relation_c_f)
#
# # ----- Nó D ----- #
# relation_d_e = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[3], MAPA_BUSCA_ORDENADA_1.nodes[4], 6);    _relation_list.append(relation_d_e)
# relation_d_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[3], MAPA_BUSCA_ORDENADA_1.nodes[6], 14);   _relation_list.append(relation_d_g)
#
# # ----- Nó E ----- #
# relation_e_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[4], MAPA_BUSCA_ORDENADA_1.nodes[6], 7);   _relation_list.append(relation_e_g)
#
# # ----- Nó F ----- #
# relation_f_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[5], MAPA_BUSCA_ORDENADA_1.nodes[6], 10);  _relation_list.append(relation_f_g)
#
#
# MAPA_BUSCA_ORDENADA_1.relations = _relation_list
# MAPA_BUSCA_ORDENADA_1.start_node = MAPA_BUSCA_ORDENADA_1.nodes[0]
# MAPA_BUSCA_ORDENADA_1.end_node = MAPA_BUSCA_ORDENADA_1.nodes[-1]
#
#
# # -------------------------------------------------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------------------------------------------------- #
# # -------------------------------------------------------------------------------------------------------------------- #
#
# # --------------------------- #
# # ----- Criação dos Nós ----- #
# # --------------------------- #
# MAPA_BUSCA_ORDENADA_2 = Map()
#
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('A', 16))   # 0
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('B', 13))   # 1
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('C', 15))   # 2
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('D', 7))    # 3
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('E', 10))   # 4
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('F', 10))   # 5
# MAPA_BUSCA_ORDENADA_2.nodes.append(Node('G', 0))    # 6
#
# # --------------------------------- #
# # ----- Conexões entre os Nós ----- #
# # --------------------------------- #
# _relation_list = []
#
# # ----- Nó A ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[1], 8))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[2], 3))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[3], 16))
#
# # ----- Nó B ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[1], MAPA_BUSCA_ORDENADA_2.nodes[4], 8))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[1], MAPA_BUSCA_ORDENADA_2.nodes[5], 7))
#
# # ----- Nó C ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[2], MAPA_BUSCA_ORDENADA_2.nodes[3], 16))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[2], MAPA_BUSCA_ORDENADA_2.nodes[5], 6))
#
# # ----- Nó D ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[4], 5))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[5], 6))
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[6], 10))
#
# # ----- Nó E ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[4], MAPA_BUSCA_ORDENADA_2.nodes[6], 15))
#
# # ----- Nó F ----- #
# _relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[5], MAPA_BUSCA_ORDENADA_2.nodes[6], 17))
#
#
# MAPA_BUSCA_ORDENADA_2.relations = _relation_list
# MAPA_BUSCA_ORDENADA_2.start_node = MAPA_BUSCA_ORDENADA_2.nodes[0]
# MAPA_BUSCA_ORDENADA_2.end_node = MAPA_BUSCA_ORDENADA_2.nodes[-1]
#
#
#
#
