"""
Author: Phuvit Kittisapkajon
"""
from rit_lib import*
from blackout import*
from blackout import evaluate

class BinaryTreeNode(struct):
    """ A BinaryTreeNode has a value and blackout amount.
        A left child that is a BinaryTreeNode or None
        A right child that is a BinaryTreeNode or None

    """
    _slots = (((NoneType, 'BinaryTreeNode'), 'left'),
              (object, 'value'),
              ((NoneType, 'BinaryTreeNode'), 'right'),
              (object, 'blackout'))

    def isLeaf(self):
        """
        Returns if this node is a leaf node
        :return: True if it is a leaf node, False if it is not
        """
        if not self.hasLeftChild() and not self.hasRightChild():
            return True
        else:
            return False

    def getValue(self):
        """
        Gets the value of this node
        :return: the value of this node
        """
        return self.value

    def hasLeftChild(self):
        """
        Returns if this node has a left child
        :return: True if this node has a left child, False otherwise
        """
        return self.left != None

    def hasRightChild(self):
        """
        Returns if this node has a right child
        :return: True if this node has a right child, False otherwise
        """
        return self.right != None


    def bstNodeToString(self):
        """
        :return: the string representing the BinaryTree
                 with this node as the root
        """
        return (self.left.bstNodeToString() if self.hasLeftChild() else "")  +  \
              ( str( self.getValue() ) + ' ' ) + \
               (self.right.bstNodeToString() if self.hasRightChild() else "")



class BinaryTree( struct ):
    """
    A non-empty BinaryTree has a root BSTNode.
        A empty BinaryTree has a root of None
    """
    _slots = ((NoneType, BinaryTreeNode), 'root')

    def add(self, value):
        """ bstSearch: BinarySearchTree * Number -> NoneType
            Adds the value to the tree.
        """
        if self.root == None:
            self.root = BinaryTreeNode(None, value, None)
        else: # we can only add to a leaf node, so get to a leaf
            current = self.root
            while True:
                if value < current.value and current.left == None:
                    current.left = BinaryTreeNode(None, value, None)
                    break
                elif value < current.value:
                    current = current.left
                elif value >= current.value and current.right == None:
                    current.right = BinaryTreeNode(None, value, None)
                    break
                elif value >= current.value:
                    current = current.right

    ############################################################
    # String Conversion
    ############################################################

    def bstToString( self ):
        """ bstToString: BinarySearchTree -> String
            Converts the BST into a string for viewing
        """
        if self.root == None:
            return ''
        else:
            return self.root.bstNodeToString()

    def isEmpty( bst ):
        """ bstSearch: BinarySearchTree -> Boolean
            Returns if this CST is empty
        """
        return bst.root == None

    def bstSearch( self, value ):
        """ bstSearch: BinarySearchTree * Number -> Boolean
            Returns if the value exists in the BST
         """
        if self.isEmpty():
            return False
        else:
            current = self.root
            while value != current.value:
                if value < current.value and current.left == None:
                    return False
                elif value < current.value:
                    current = current.left
                elif value >= current.value and current.right == None:
                    return False
                elif value >= current.value:
                    current = current.right
            return True

def treeHelper(equation, value, l_equation):
    """
    This function helps makeTree function by adding another parameter as a length of the string equation
    which is used to calculate the blacked out value for each BinaryTreeNode.
    blackout = length of the actual puzzle - length of the value of that specific BinaryTreeNode

    :param equation: a string representing a puzzle
    :param value: one of the all possible blacked out combination
    :param l_equation: length of the equation
    :return: BinaryTreeNode of the root of the tree
    """
    if equation is '':
        left = None
        right = None
    else:
        left = treeHelper(equation[1:], value, l_equation)
        right = treeHelper(equation[1:], value + equation[0],l_equation)

    leaf = BinaryTreeNode(left, value, right, 0)
    leaf.blackout = l_equation - len(value)
    return leaf

def makeTree(equation,value):
    """
    This function  makes binaryTreeNode from the string equation where value is one of the all possible blacked
    out combination. Function treeHelper is present in this function.

    :param equation: a string representing a puzzle
    :param value: one of the all possible blacked out combination
    :return: BinaryTreeNode of the root of the tree
    """

    return treeHelper(equation,value,len(equation))

def make_tree(s):
    """
    This function  makes the binary tree from the string s, s is a puzzle string. It use the BinaryTree and
    BinaryTree classes from the lecture.

    :param s: a string representing a puzzle
    :return: a binary tree who's leaf nodes are all of the possible blacked out combinations.
    """
    leaf = makeTree(s,'')
    return BinaryTree(leaf)

def node_finder(passin):
    """
    This function finds the node from the BinaryTree.

    :param passin: BinaryTree
    :return: node of BinaryTree
    """
    if isinstance(passin,BinaryTreeNode):
        return passin
    elif isinstance(passin,BinaryTree):
        return passin.root


def solve_tree(bt,number):
    """
    This function solves the given binary tree puzzle, bt, with the given number of blacked out squares
    , number. node_finder function is present to find all leaf nodes and evaluate function is present to
    evaluate any leaf node value that has the requested blacked out squares. It prints any solutions it finds.
    :param bt:BinaryTree
    :param number:number of blacked out
    :return prints any solutions that meet the requirement
    """
    node = node_finder(bt)
    if node != None:
        if node.blackout == number:
            if evaluate(node.value) is True:
                print(node.value)
        else:
            solve_tree(node.left,number)
            solve_tree(node.right,number)

def test_make_tree():
    print("Begin test_make_tree")
    print(make_tree("2=5") == BinaryTree(BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(BinaryTreeNode(None,'',None,3)\
    ,'',BinaryTreeNode(None,'5',None,2),3),'',BinaryTreeNode(BinaryTreeNode(None,'=',None,2),'=',BinaryTreeNode(None,\
    '=5',None,1 ),2 ),3 ),'',BinaryTreeNode(BinaryTreeNode(BinaryTreeNode( None, '2', None, 2 ), '2', BinaryTreeNode(\
    None, '25', None,1 ), 2 ), '2', BinaryTreeNode( BinaryTreeNode( None, '2=', None,  1 ),  '2=',  BinaryTreeNode( \
    None, '2=5', None,  0 ),  1 ),  2 ),  3 ) ))
    print("End test_make_tree")


def main():
    """
    This function prompts the user for the file containing the puzzles and the number of blacked out
    squares to look for. It prints the puzzles and call make_tree function to create tree. Then, use
    solve_tree function to print the valid solutions for the tree.
    """
    file = input("Enter the text file (EX. puzzles.txt):")
    number = input("The number of blacked out squares to look for:")
    for lines in open(file):
        line = lines.strip()
        print("")
        print("Given Equation:", line)
        tree = make_tree(line)
        print("Solution/s:")
        solve_tree(tree,int(number))

if __name__ == '__main__':
    main()