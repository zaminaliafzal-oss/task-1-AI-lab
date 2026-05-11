

import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    """
    Minimax Algorithm
    curDepth   : current depth in the game tree
    nodeIndex  : index of current node
    maxTurn    : True if maximizing player's turn, False for minimizing
    scores     : leaf node values
    targetDepth: total depth of the tree
    """
    # Base case: reached leaf node
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        # Maximizing player picks the best (highest) value
        left  = minimax(curDepth + 1, nodeIndex * 2,     False, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        return max(left, right)
    else:
        # Minimizing player picks the worst (lowest) value for opponent
        left  = minimax(curDepth + 1, nodeIndex * 2,     True, scores, targetDepth)
        right = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        return min(left, right)


scores     = [3, 5, 2, 9, 3, 5, 2, 9]
treeDepth  = int(math.log(len(scores), 2))   # depth = 3 for 8 leaf nodes

print("=" * 40)
print("       Min-Max Algorithm")
print("=" * 40)
print(f"Leaf node scores : {scores}")
print(f"Tree depth       : {treeDepth}")
print(f"The optimal value: {minimax(0, 0, True, scores, treeDepth)}")
print("=" * 40)
