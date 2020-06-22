#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random

import matplotlib.pyplot as plt
import networkx as nx


def generateLinks(nodes, links, alpha):
    network = []  # Empty array to hold network topography
    for i in range(len(alpha) - 1):  # Create at least one connection between nodes going down the line
        network.append([alpha[i], alpha[i + 1], random.randint(1, 9)])
    while len(network) < links:
        present = True  # Var to check if link already exists
        while present:
            node1 = alpha[random.randint(0, nodes - 1)]  # Random node in network
            node2 = alpha[random.randint(0, nodes - 1)]  # Random node in network #2
            while node1 == node2:  # Make the nodes different
                node2 = alpha[random.randint(0, nodes - 1)]
            for k in range(10):  # Test every possible combination to see if it exists already
                test = [node1, node2, k]
                test2 = [node2, node1, k]
                if test in network or test2 in network:
                    present = True
                    break  # End the for loop if it exists
                present = False  # If the connection does not exist, end the while loop and add it to network
        network.append([node1, node2, random.randint(1, 9)])
    return network


def solve(G, base):
    print(nx.single_source_dijkstra_path(G, base))  # Find least cost and display node path
    print(nx.single_source_dijkstra_path_length(G, base))  # Find least cost and display path cost


def gui(network, nodes):
    G = nx.Graph()  # Create networkx variable
    G.add_nodes_from(nodes)  # Add all the nodes to networkx
    for n in network:  # Add links (edge connections) between nodes to networkx
        G.add_edge(n[0], n[1], weight=(n[2]))
    pos = nx.spring_layout(G)  # Specify random layout for use in labeling edge connections
    nx.draw(G, pos, with_labels=True, font_size=20)  # Create the nodes and links
    for n in network:  # Add numerical cost as a label on each path
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(n[0], n[1]): '^'+str(n[2])+'^'}, font_size=20)
    plt.savefig("path.png")  # Save file as a png to display in webpage
    solve(G, nodes[0])
    plt.show()  # Show the file


def main():
    parser = argparse.ArgumentParser(description='Network Topology Generator')  # Argument code taken from UDPClient
    parser.add_argument("--node", "-n", type=int, help='Number of nodes in the network.')
    parser.add_argument("--link", "-l", type=int, help='Number of links in the network.')
    args = parser.parse_args()
    nodes = args.node
    links = args.link
    # nodes = int(input("Enter number of nodes: "))
    # links = int(input("Enter number of links: "))

    linkMax = int(nodes * (nodes - 1) / 2)  # n(n-1)/2
    if nodes > 26:  # Max of 26 connections
        nodes = 26
    elif nodes < 2:  # Has to be at least 2 nodes in a  network
        nodes = 2
    if links < nodes:  # Each node must have at least one link
        links = nodes
    elif links > linkMax:  # Will cause infinite loop in duplicate checking for loop
        links = linkMax
    selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']  # Possible labels for nodes
    alpha = selection[-nodes:]  # Start at the end, select from there
    network = generateLinks(nodes, links, alpha)
    gui(network, alpha)


if __name__ == "__main__":
    main()
