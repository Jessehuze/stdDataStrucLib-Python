#!/usr/bin/env python

# Author: Jesse Hughes
# FileName: singlyLinkedList.py
# Purpose: Data Structure for a singly linked list
# Date: 5/29/2016

class Node:
    def __init__(self, d = None, next_node = None):
        self.data = d
        self.next = next_node


class SinglyLinkedList:
    def __init__(self, data = None):
        if data == None:
            self.head = None
            self.size = 0
            self.tail = None
        else:
            self.head = Node(d = data)
            self.size = 1
            self.tail = self.head

    # Function: append
    # Purpose: Creates a new node with the given data and appends it to the
    #          end of the list.
    # Input: data
    # Output: None
    def append(self, data):
        self.size += 1
        if self.head == None:  # Checking for empty list
            self.head = Node(d = data)
            self.tail = self.head
            return
        self.tail.next = Node(d = data)
        self.tail = self.tail.next

    def deleteHeadNode(self):
        if self.size == 0:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def deleteNode(self, node, prev_node = None):
        if prev_node != None:  # Given the previous node O(1)
            prev_node.next = node.next
        else:  # Not given the previous node O(n)
            if node == self.head:
                self.deleteHeadNode()
                return
            if node == self.tail:
                print("Error: Can't delete tail node w/o prior node")
                return
            runner = node
            while runner.next.next != None:
                runner.data = runner.next.data
                runner = runner.next
            runner.data = runner.next.data
            runner.next = None
            self.tail = runner
            self.size -= 1

    # Function: delData
    # Purpose: Deletes all nodes containing the specified data
    # Input: data
    # Output: number of deleted elements
    def delData(self, data):
        if self.size == 0:
            return
        numDel = 0
        while self.head.data == data: #???????????????
            self.deleteHeadNode()
            numDel += 1
        if self.head == None:
            return
        runner = self.head
        while runner.next != None:
