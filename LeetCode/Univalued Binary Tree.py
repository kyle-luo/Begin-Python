# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
#
#
# Example 1:
#
# Input: [1,1,1,1,1,null,1]
# Output: true
#
# Example 2:
#
# Input: [2,2,2,5,2]
# Output: false

def isUnivalTree(root):
    for x in root:
        if x == root[0] or x == 'null':
            continue
        else:
            return False
    return True

print(isUnivalTree([1,1,1,1,1,null,1]))