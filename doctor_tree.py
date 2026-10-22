class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        parent = self.find_doctor(self.root, parent_name)

        if parent is None:
            return False

        if side == "left":
            if parent.left is not None:
                return False
            parent.left = DoctorNode(doctor_name)

        elif side == "right":
            if parent.right is not None:
                return False
            parent.right = DoctorNode(doctor_name)

        else:
            return False

        return True

    def find_doctor(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        found = self.find_doctor(node.left, name)

        if found is not None:
            return found

        return self.find_doctor(node.right, name)

    def preorder(self, node):
        if node is None:
            return []

        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    def inorder(self, node):
        if node is None:
            return []

        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)

        return result

    def postorder(self, node):
        if node is None:
            return []

        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result


# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

# inserting doctors
print(tree.insert("Dr. Croft", "Dr. Goldsmith", "right"))
print(tree.insert("Dr. Croft", "Dr. Phan", "left"))
print(tree.insert("Dr. Phan", "Dr. Carson", "right"))
print(tree.insert("Dr. Phan", "Dr. Morgan", "left"))

# testing all 3 traversals
print("Preorder:", tree.preorder(tree.root))
print("Inorder:", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))

# testing edge cases
print("Missing parent:", tree.insert("Dr. Nobody", "Dr. Lee", "left"))
print("Invalid side:", tree.insert("Dr. Croft", "Dr. Lee", "middle"))
print("Occupied side:", tree.insert("Dr. Croft", "Dr. Lee", "left"))
