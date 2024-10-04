from logging import lastResort
from os import link
from tkinter import CURRENT


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
         temporaryNode = self.head
         self.head = newNode
         self.head.next = temporaryNode
         del temporaryNode

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head

            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode

    def printList(self):
        currentNode = self.head

        while True:
            if currentNode is None:
                break

            print(currentNode.data)
            currentNode = currentNode.next

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("invalid position")
            return

        if position is 0:
            self.insertHead(newNode)
            return

        currentNode = self.head
        currentPosition = 0

        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def listLength(self):
        currentNode = self.head
        length = 0

        while currentNode is not None:
            length += 1
            currentNode = currentNode.next

        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        return False

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print("Invalid Position")
            return

        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return

            currentNode = self.head
            currentPosition = 0

            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break

                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List is empty. Delete failed")

    def deleteEnd(self):
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return

            lastNode = self.head

            while lastNode.next is not None:
                previousNode = lastNode
                lastnode = lastNode.next

            previousNode .next = None
        else:
            print("Linked list is empty. Delete failed")



firstNode = Node("Ford")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Toyota")
linkedList.insertEnd(secondNode)
thirdNode = Node("Nissan")
linkedList.insertEnd(thirdNode)
fourthNode = Node("BMW")
linkedList.insertEnd(fourthNode)

linkedList.printList()

linkedList.deleteHead()
linkedList.printList()