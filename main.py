#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def generateLinks(nodes, links):
    print(nodes, links)
    network = []
    selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    alpha = selection[-nodes:]
    print(alpha)
    for i in range(len(alpha) - 1):
        network.append([alpha[i], alpha[i + 1], random.randint(1, 9)])
    links -= len(network)
    for j in range(links):
        print(j)
        present = True
        while present:
            node1 = alpha[random.randint(0, nodes - 1)]
            node2 = alpha[random.randint(0, nodes - 1)]
            while node1 == node2:
                node2 = alpha[random.randint(0, nodes - 1)]
            for k in range(10):
                test = [node1, node2, k]
                test2 = [node2, node1, k]
                if test in network or test2 in network:
                    present = True
                    break
                present = False
        network.append([node1, node2, random.randint(1, 9)])
    print(network)


def main():
    nodes = int(input("Enter number of nodes: "))
    links = int(input("Enter number of links: "))
    linkMax = int(nodes*(nodes-1)/2)
    if links < nodes:
        links = nodes
    elif links > linkMax:
        links = linkMax
    generateLinks(nodes, links)


if __name__ == "__main__":
    main()
