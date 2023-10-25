import matplotlib.pyplot as plt
import networkx as nx
import time

def lerCoordenadas():
    # x = list(map(float, input().split()))
    # y = list(map(float, input().split()))

    x = [0.0, 1.0, 2.0, 0.0, 1.0, 1.0, 3.0]
    y = [0.0, 2.0, 0.0, 2.0, 1.0, 3.0, 2.0]

    dicionario = {}
    for i in range(len(x)):
        dicionario[chr(i + ord('A'))] = (x[i], y[i])

    return dicionario

def distancia(x1, y1, x2, y2):
    return round(((x1 - x2)**2 + (y1 - y2)**2)**(1/2), 2)

def trasnformaEmGrafo(dicionario):
    grafo = nx.Graph()
    for i in dicionario:
        for j in dicionario:
            if i != j:
                grafo.add_edge(i, j, weight=distancia(dicionario[i][0], dicionario[i][1], dicionario[j][0], dicionario[j][1]))

    return grafo

def desenhaGrafo(grafo, dicionario, aresta=None, cor='red', salva=False, caminho=None):
    # Exibe o grafo
    nx.draw(
        grafo, # Grafo
        with_labels=True, # Mostrar os nomes dos nós
        font_weight='bold', # Negrito
        node_size=500, # Tamanho dos nós
        font_size=10, # Tamanho da fonte
        pos=dicionario, # Posição dos nós
        node_color='#2BB2E8', # Cor dos nós
        edge_color='black', # Cor das arestas
        width=1.5, # Espessura das arestas
        alpha=1.0, # Transparência
        labels={node: node for node in grafo.nodes()}
    )

    if aresta != None:
        nx.draw_networkx_edges(
            grafo, # Grafo
            pos=dicionario, # Posição dos nós
            edgelist=[aresta], # Aresta a ser alterada
            edge_color=cor, # Cor da aresta
            width=1.5, # Espessura da aresta
            alpha=1.0, # Transparência
        )

    # **Código comentado pois alguns valores das arestas ficam sobrepostos**
    # Exibe os valores das arestas
    # nx.draw_networkx_edge_labels(
    #     grafo, # Grafo
    #     pos=dicionario, # Posição dos nós
    #     edge_labels=nx.get_edge_attributes(grafo, 'weight'), # Valores das arestas
    #     label_pos=0.5, # Posição do valor
    #     font_size=8, # Tamanho da fonte
    #     font_color='black' # Cor da fonte
    # )

    # Exibe os valores das arestas
    # labels = nx.get_edge_attributes(grafo, 'weight')
    # print(labels)


    plt.show()

def main():
    cidades = lerCoordenadas()
    grafo = trasnformaEmGrafo(cidades)

    for node in grafo.nodes:
        print(node) 

    vizinho = list(grafo.neighbors('B'))
    print(vizinho)


if __name__ == '__main__':
    main()
