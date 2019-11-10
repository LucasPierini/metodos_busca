Python 3.7.3

## maps.py
A lista map_dicts guarda os dicionários que são utilizados na criação de mapas.
É possível criar novos ou editar os pré-existentes. 

Cada dict de criação de mapa contém as seguintes chaves:

  - 'map_name': Contém o nome do mapa, usado apenas nos métodos de print das buscas.
  - 'type': Define se o mapa é apto para realizar buscas ordenadas ou não-ordenadas.
  - 'nodes': Guarda uma lista de dicionários utilizados na criação de cada nó do mapa. Cada dicionário da lista deverá conter a chave 'name' e, caso o 'type' seja busca ordenada, deverá conter a chave 'cost'.
  - 'adjacent': Utilizada apenas (e obrigatoriamente) quando o 'type' for não-ordenada. Guarda uma lista de dicionários que contém como chave o nome dos nós e como valor uma lista de 4 campos que guarda o nome dos nós fazem conexão com o nó-chave. Lembrando que a ordem em que as chaves aparecem devem seguir a seguinte regra: 
    - Primeira deverá ser o nó adjacente abaixo
    - Segunda deverá ser o nó adjacente à esquerda
    - Terceira deverá ser o nó adjacente acima
    - Última deverá ser o nó adjacente à direita
    - Caso não possua nenhum nó adjacente em determinada posição, apenas adicione uma string vazia (igual ao que já vem por padrão.
  - 'relations': Utilizada apenas (e obrigatoriamente) quando o 'type' for ordenada. Guarda uma lista de dicionários que contém um par de nomes de nós e a respectiva distância entre eles. Diferente de 'adjacent', deverá existir apenas UMA relação para cada par de nós.
  - 'first': Guarda o nome do nó inicial
  - 'last': Guarda o nome do nó final, do que espera ser encontrado
  
