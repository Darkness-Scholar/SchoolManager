class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #> self.head:Node <#
        self.tail = None #> self.head:Node <#

    def Print(self):
        index = 0
        current = self.head
        result = 'Linked List:['
        while current != None:
            index += 1
            if index == 1:
                result += ' ' + str(current.value)
            else:
                result += ' -> ' + str(current.value) # gia tri
            current = current.next
        result += ' ]'
        print(result)

    def Push(self, value):
        node = Node(value)
        if self.head == None:
            # ADD A NODE IF THIS NODE IS EMPTY
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
             
    def Insert(self, index, value):
        node = Node(value)
        temp = None
        current = self.head
        init = 0
        while init < index and current != None:
            init += 1
            temp = current # before node
            current = current.next
        
        if temp == None:
            node.next = self.head
            self.head = node
            if self.tail == None:
                self.tail = node
        else:
            if current == None:
                # Add to end of list
                self.tail.next = node
                self.tail = node
            else:
                # Add to after of index
                temp.next = node
                node.next = current
        
        return "Thêm {} vào vị trí {}".format(value, index)

    def FindUser(self, username, password):
        current = self.head
        index = 0

        while current != None and current.value['name'] != username:
            current = current.next
            print("NEXT >>>")
            index += 1
        if current == None:
            return None
        else:
            if current.value['password'] == password:
                return index, current.value
            else: return None, { }

    def FindByUserName(self, username):
        current = self.head
        index = 0

        while current != None and current.value['name'] != username:
            current = current.next
            index += 1
        if current == None:
            return None, {}
        else:
            return index, current.value

    def Find(self, value):
        current = self.head
        index = 0
        while current != None and current.value != value:
            current = current.next
            index += 1
        if current == None:
            return None
        else:
            return index

    def Remove(self, value):
        current = self.head
        temp = None # before
        while current != None and current.value != value:
            temp = current
            current =  current.next
        if current != None:
            # find out:
            if current == self.head and current == self.tail:
                # xoa phan tu duy nhat
                self.head = self.tail = None
            elif current == self.head:
                # Delete first element
                self.head = self.head.next
            elif current == self.head:
                # Delete last element
                temp.next = None
                self.tail = temp
            else:
                # Delete any element 
                temp.next = current.next
            del current

    def Update(self, index, value):
        current = self.head
        i = 0
        while i < index and current != None:
            i += 1
            current = current.next
        if current != None:
            current.value = value
    
    def SetPassword(self, index, newpassword):
        current = self.head
        i = 0
        while i < index and current != None:
            i += 1
            current = current.next
        if current != None:
            current.value['password'] = newpassword

    def Clear(self):
        current = self.head
        self.head = self.tail = None
        while current != None:
            temp = current
            current = current.next
            del temp