from random import *

class Node:
    def __init__ (self, data):
        self.data = data
        self.link = None
    
class LinkedList :
    def __init__(self):
        self.head= None
    
    def append(self, data) :
        if not self.head: #빔
            self.head = Node(data)
        else: #안빔
            node = self.head
            while node is not None :
                node = node.link
            node.link = Node(data)

class Term : 
    def __init__(self, coef, expo) :
        self.coef = coef
        self.expo = expo

class Polynomial(LinkedList):
    def read(coef, exp):
        while True :

    def display(self):
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef} x ^{term.expo}")
            node = node.link
        return " + ".join(terms)

    def add(self, P2) :
        result = Polynomial()
        nodeA = self.head
        nodeB = P2.head
