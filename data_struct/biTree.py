# coding:utf-8


class BiNode:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        return self.element

    def dict_form(self):
        dict_set = {
            "element": self.element,
            "left": self.left,
            "right": self.right
        }
        return dict_set

    def str(self):
        return str(self.element)

    def __str__(self):
        return str(self.element)


class BiTree:
    def __init__(self, tree_node=None):
        self.root = tree_node

    def add_node_in_order(self, element):
        node = BiNode(element)
        if self.root is None:
            self.root = node
        else:
            node_queue = list()
            node_queue.append(self.root)
            while len(node_queue):
                q_node = node_queue.pop(0)
                if q_node.left is None:
                    q_node.left = node
                    print("q_node --> ", q_node, "  q_node.left --> ", q_node.left)
                    break
                elif q_node.right is None:
                    q_node.right = node
                    print("q_node --> ", q_node, "  q_node.right --> ", q_node.right)
                    break
                else:
                    node_queue.append(q_node.left)
                    node_queue.append(q_node.right)

                # 两者等价
                # if q_node.left is None:
                #     q_node.left = node
                #     print("q_node --> ", q_node, "  q_node.left --> ", q_node.left)
                #     break
                # else:
                #     node_queue.append(q_node.left)
                # if q_node.right is None:
                #     q_node.right = node
                #     print("q_node --> ", q_node, "  q_node.right --> ", q_node.right)
                #     break
                # else:
                #     node_queue.append(q_node.right)

    def set_up_in_order(self, element_list):
        for element in element_list:
            self.add_node_in_order(element)

    # 层次遍历(广度遍历)
    def display_the_tree_span(self):
        n_list = list()
        n_list.append(self.root)
        print(self.root)
        while len(n_list):
            n_node = n_list.pop(0)
            if n_node.left:
                print(n_node.left)
                n_list.append(n_node.left)
            if n_node.right:
                print(n_node.right)
                n_list.append(n_node.right)

    # 左序遍历(深度)
    def display_the_tree_depth_left(self, node):
        if node is None:
            return
        self.display_the_tree_depth_left(node.left)
        print(node)
        self.display_the_tree_depth_left(node.right)

    # 中序遍历(深度)
    def display_the_tree_depth_middle(self, node):
        if node is None:
            return
        print(node)
        self.display_the_tree_depth_middle(node.left)
        self.display_the_tree_depth_middle(node.right)

    # 右序遍历(深度)
    def display_the_tree_depth_right(self, node):
        if node is None:
            return
        self.display_the_tree_depth_middle(node.left)
        self.display_the_tree_depth_middle(node.right)
        print(node)


if __name__ == '__main__':
    A = BiNode("A")
    B = BiNode("B")
    C = BiNode("C")
    D = BiNode("D")
    E = BiNode("E")
    F = BiNode("F")
    G = BiNode("G")
    H = BiNode("H")
    R = BiTree(A)
    R.add_node_in_order(B)
    R.add_node_in_order(C)
    R.add_node_in_order(D)
    R.add_node_in_order(E)
    R.add_node_in_order(F)
    R.add_node_in_order(G)
    R.add_node_in_order(H)
    # A.display_the_tree_span()
    R.display_the_tree_depth_left(A)














