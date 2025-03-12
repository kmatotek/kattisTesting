class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_bst(elements):
    """Builds a Binary Search Tree from a list of elements."""
    if not elements:
        return None

    root_node = TreeNode(elements[0])
    for element in elements[1:]:
        insert_node(root_node, element)
    return root_node

def insert_node(root, element):
    """Inserts a new node into the BST."""
    if element < root.data:
        if root.left is None:
            root.left = TreeNode(element)
        else:
            insert_node(root.left, element)
    else:
        if root.right is None:
            root.right = TreeNode(element)
        else:
            insert_node(root.right, element)

def count_permutations(root):
    """Counts the number of permutations that result in the same BST."""
    if root is None:
        return 1

    left_count = count_permutations(root.left)
    right_count = count_permutations(root.right)

    # Calculate binomial coefficient (n choose k)
    n = left_count + right_count
    k = left_count
    binomial_coeff = 1
    for i in range(1, k + 1):
        binomial_coeff = binomial_coeff * (n - k + i) // i

    return binomial_coeff * left_count * right_count

if __name__ == "__main__":
    while True:
        num_elements = int(input())
        if num_elements == 0:
            break

        elements = list(map(int, input().split()))
        tree_root = build_bst(elements)
        permutations = count_permutations(tree_root)
        print(permutations)