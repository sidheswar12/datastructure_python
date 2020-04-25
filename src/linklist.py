
#!/bin/python3
# Author: Sidheswar Ghosh

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val 
    
    def get_next(self):
        return self.next 

    def set_next(self, next):
        self.next = next
    

class LinkList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return int(self.count)

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count +=1
    
    def insert_end(self, data):        
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node        
        last = self.head
        while (last.next):
            last = last.next
        new_node.next = None
        last.next =  new_node        
        self.count += 1
         
    def find_element(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item.val
            else:
                item = item.get_next()
    
    def delete_nodeAt(self, idx):
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            tmpidx = 0
            while tmpidx < idx - 1:
                node = self.head.get_next()
                tmpidx +=1
            node.set_next(node.get_next().get_next())
            self.count -= 1
    
    def display_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

    def sort_list_assending(self):
        swap = 0
        if self.head != None:
            while(1):
                swap = 0
                node = self.head
                while(node.next != None):
                    if node.val > node.next.val:                        
                        swap += 1
                        p = node.val
                        node.val = node.next.val
                        node.next.val = p
                        node = node.next
                    else:
                        node = node.next

                if swap == 0:
                    break
                else:
                    continue
        

def main():    
    itemlist = LinkList()
    itemlist.insert_beg(38)
    itemlist.insert_beg(49)
    itemlist.insert_beg(13)
    itemlist.insert_beg(15)
    itemlist.insert_beg(44)
    itemlist.insert_beg(25)
    itemlist.insert_beg(98)
    itemlist.insert_beg(10)
    itemlist.insert_beg(30)
    print("Elements in List: ")
    itemlist.display_list()    

    print("Number of elements in Original List: ", itemlist.get_count())

    print("One Element deleted from Index 3 ")
    itemlist.delete_nodeAt(3)
    
    print("Find element from List: ", itemlist.find_element(49))    

    print("Elements in List after deletetion operation: ")
    itemlist.display_list()
    print("Number of elements in List after deletion: ", itemlist.get_count())    

    
    itemlist.insert_beg(20) 
    itemlist.insert_beg(95)   
    print("Elements in List after insertion at begining: ")
    itemlist.display_list()

    print("Number of elements in List after insertion at begining: ", itemlist.get_count())
    
    itemlist.insert_end(90)
    itemlist.insert_end(80)
    print("Elements in List after insertion at end: ")
    itemlist.display_list()
    print("Number of elements in List after insertion at end: ", itemlist.get_count())
    
    itemlist.sort_list_assending()
    print("Elements in List after sorting: ")
    itemlist.display_list()

if __name__ == "__main__":
    main()






