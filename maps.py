from classes import *

# ------------------------------------------ #
# ----- Definição dos nós do Labirinto ----- #
# ------------------------------------------ #
MAPA_BUSCAS_NAO_ORDENADAS = Map()

node_a = Node('A');
node_b = Node('B');
node_c = Node('C');
node_d = Node('D');
node_e = Node('E');
node_f = Node('F');
node_g = Node('G');
node_h = Node('H');
node_i = Node('I');
node_j = Node('J');
node_l = Node('L');
node_m = Node('M');
node_n = Node('N');
node_o = Node('O');
node_p = Node('P');
node_q = Node('Q');
node_r = Node('R');
node_s = Node('S');


# ---------------------------------------- #
# ----- Definição dos Nós adjacentes ----- #
# ---------------------------------------- #

# --- Node A --- #
node_a.add_adjacent_node(node_b)
node_a.add_adjacent_node(node_e)

# --- Node B --- #
node_b.add_adjacent_node(node_c)
node_b.add_adjacent_node(node_a)
node_b.add_adjacent_node(node_f)

# --- Node C --- #
node_c.add_adjacent_node(node_b)

# --- Node D --- #
node_d.add_adjacent_node(node_h)

# --- Node E --- #
node_e.add_adjacent_node(node_a)
node_e.add_adjacent_node(node_i)

# --- Node F --- #
node_f.add_adjacent_node(node_g)
node_f.add_adjacent_node(node_b)

# --- Node G --- #
node_g.add_adjacent_node(node_h)
node_g.add_adjacent_node(node_f)
node_g.add_adjacent_node(node_l)

# --- Node H --- #
node_h.add_adjacent_node(node_d)
node_h.add_adjacent_node(node_g)

# --- Node I --- #
node_i.add_adjacent_node(node_j)
node_i.add_adjacent_node(node_e)
node_i.add_adjacent_node(node_n)

# --- Node J --- #
node_j.add_adjacent_node(node_i)
node_j.add_adjacent_node(node_o)

# --- Node K --- #
# Não tem hehe

# --- Node L --- #
node_l.add_adjacent_node(node_m)
node_l.add_adjacent_node(node_g)

# --- Node M --- #
node_m.add_adjacent_node(node_l)
node_m.add_adjacent_node(node_q)

# --- Node N --- #
node_n.add_adjacent_node(node_i)

# --- Node O --- #
node_o.add_adjacent_node(node_p)
node_o.add_adjacent_node(node_j)
node_o.add_adjacent_node(node_r)

# --- Node P --- #
node_p.add_adjacent_node(node_q)
node_p.add_adjacent_node(node_o)
node_p.add_adjacent_node(node_s)

# --- Node Q --- #
node_q.add_adjacent_node(node_m)
node_q.add_adjacent_node(node_p)

# --- Node R --- #
node_r.add_adjacent_node(node_o)

# --- Node S --- #
node_s.add_adjacent_node(node_p)

MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_a)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_b)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_c)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_d)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_e)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_f)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_g)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_h)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_i)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_j)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_l)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_m)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_n)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_o)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_p)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_q)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_r)
MAPA_BUSCAS_NAO_ORDENADAS.nodes.append(node_s)

MAPA_BUSCAS_NAO_ORDENADAS.start_node = MAPA_BUSCAS_NAO_ORDENADAS.nodes[0]
MAPA_BUSCAS_NAO_ORDENADAS.end_node = MAPA_BUSCAS_NAO_ORDENADAS.nodes[-1]


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# --------------------------- #
# ----- Criação dos Nós ----- #
# --------------------------- #
MAPA_BUSCA_ORDENADA_1 = Map()

MAPA_BUSCA_ORDENADA_1.nodes.append(Node('A', 24))   # 0
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('B', 15))   # 1
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('C', 22))   # 2
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('D', 12))   # 3
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('E', 7))    # 4
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('F', 7))    # 5
MAPA_BUSCA_ORDENADA_1.nodes.append(Node('G', 0))    # 6

# --------------------------------- #
# ----- Conexões entre os Nós ----- #
# --------------------------------- #
_relation_list = []

# ----- Nó A ----- #
relation_a_b = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[1], 9);    _relation_list.append(relation_a_b)
relation_a_c = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[2], 5);    _relation_list.append(relation_a_c)
relation_a_d = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[0], MAPA_BUSCA_ORDENADA_1.nodes[3], 13);   _relation_list.append(relation_a_d)

# ----- Nó B ----- #
relation_b_d = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[1], MAPA_BUSCA_ORDENADA_1.nodes[3], 3);    _relation_list.append(relation_b_d)
relation_b_e = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[1], MAPA_BUSCA_ORDENADA_1.nodes[4], 10);   _relation_list.append(relation_b_e)

# ----- Nó C ----- #
relation_c_f = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[2], MAPA_BUSCA_ORDENADA_1.nodes[5], 12);   _relation_list.append(relation_c_f)

# ----- Nó D ----- #
relation_d_e = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[3], MAPA_BUSCA_ORDENADA_1.nodes[4], 6);    _relation_list.append(relation_d_e)
relation_d_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[3], MAPA_BUSCA_ORDENADA_1.nodes[6], 14);   _relation_list.append(relation_d_g)

# ----- Nó E ----- #
relation_e_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[4], MAPA_BUSCA_ORDENADA_1.nodes[6], 7);   _relation_list.append(relation_e_g)

# ----- Nó F ----- #
relation_f_g = NodeRelation(MAPA_BUSCA_ORDENADA_1.nodes[5], MAPA_BUSCA_ORDENADA_1.nodes[6], 10);  _relation_list.append(relation_f_g)


MAPA_BUSCA_ORDENADA_1.relations = _relation_list
MAPA_BUSCA_ORDENADA_1.start_node = MAPA_BUSCA_ORDENADA_1.nodes[0]
MAPA_BUSCA_ORDENADA_1.end_node = MAPA_BUSCA_ORDENADA_1.nodes[-1]


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

# --------------------------- #
# ----- Criação dos Nós ----- #
# --------------------------- #
MAPA_BUSCA_ORDENADA_2 = Map()

MAPA_BUSCA_ORDENADA_2.nodes.append(Node('A', 16))   # 0
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('B', 13))   # 1
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('C', 15))   # 2
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('D', 7))    # 3
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('E', 10))   # 4
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('F', 10))   # 5
MAPA_BUSCA_ORDENADA_2.nodes.append(Node('G', 0))    # 6

# --------------------------------- #
# ----- Conexões entre os Nós ----- #
# --------------------------------- #
_relation_list = []

# ----- Nó A ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[1], 8))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[2], 3))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[0], MAPA_BUSCA_ORDENADA_2.nodes[3], 16))

# ----- Nó B ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[1], MAPA_BUSCA_ORDENADA_2.nodes[4], 8))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[1], MAPA_BUSCA_ORDENADA_2.nodes[5], 7))

# ----- Nó C ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[2], MAPA_BUSCA_ORDENADA_2.nodes[3], 16))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[2], MAPA_BUSCA_ORDENADA_2.nodes[5], 6))

# ----- Nó D ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[4], 5))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[5], 6))
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[3], MAPA_BUSCA_ORDENADA_2.nodes[6], 10))

# ----- Nó E ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[4], MAPA_BUSCA_ORDENADA_2.nodes[6], 15))

# ----- Nó F ----- #
_relation_list.append(NodeRelation(MAPA_BUSCA_ORDENADA_2.nodes[5], MAPA_BUSCA_ORDENADA_2.nodes[6], 17))


MAPA_BUSCA_ORDENADA_2.relations = _relation_list
MAPA_BUSCA_ORDENADA_2.start_node = MAPA_BUSCA_ORDENADA_2.nodes[0]
MAPA_BUSCA_ORDENADA_2.end_node = MAPA_BUSCA_ORDENADA_2.nodes[-1]




