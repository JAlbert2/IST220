#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def generateLinks(nodes):
    network = []
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for i in range(nodes):
        network.append([random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)])
    print(network)


def main():
    generateLinks(int(input("Enter number of nodes: ")))


if __name__ == "__main__":
    main()
