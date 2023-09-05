class Node:
    def __init__(self,myData):
        self.data = myData
        self.left = None
        self.right = None

def insert_data(new_data ,node):
    """
    for inserting data
    :return: pass
    """
    if node is None:
        new_node :Node =Node(new_data)
        return new_node

    if new_data < node.data:
        node.left =insert_data(new_data , node.left)

    else:
        node.right =insert_data(new_data,node.right)

    return node

def show_all_data(node: Node):

    if node:
        show_all_data(node.left) # node.left.data == ?
        print("Data: ",node.data)
        show_all_data(node.right)

if __name__ == "__main__":

    input("Press 1 to insert new cus:\nPress 2 to find cus info:")
    root_node = Node(15)
    root_node =insert_data(10,root_node)
    root_node =insert_data(20,root_node)
    root_node =insert_data(5,root_node)
    root_node =insert_data(1,root_node)
    root_node =insert_data(7,root_node)
    root_node =insert_data(21,root_node)
    root_node =insert_data(30,root_node)

    show_all_data(root_node)


