"""
Phuvit Kittisapkajon
   Derp Tree class. Used to construct a Derp Tree from a prefix
   string, convert it to a infix string, and solve for the value.
"""
from rit_lib import *
from derp_node import *

############################################################
# Class definiton
############################################################

class DerpTree( struct ):
    """ A non-empty BinaryTree has a root BSTNode.
        A empty BinaryTree has a root of None
    """
    _slots = ((NoneType, MultiplyNode,
               AddNode, SubtractNode,
               DivideNode, LiteralNode,
               VariableNode), 'root')

    def getInfixString(self):
        """
        Prints the tree in a infix form
        :return:
        """
        return self.root.getInfixString()


    def createTreeFromPrefix(self, prefix):
        """
        Make the tree from the postfix list entered.
        """
        if prefix is []:
            pass
        else:
            x = prefix.pop(0)
            if x == "*":
                return MultiplyNode(self.createTreeFromPrefix(prefix),self.createTreeFromPrefix(prefix))
            elif x == "//":
                return DivideNode(self.createTreeFromPrefix(prefix), self.createTreeFromPrefix(prefix))
            elif x == "+":
                return AddNode(self.createTreeFromPrefix(prefix), self.createTreeFromPrefix(prefix))
            elif x == "-":
                return SubtractNode(self.createTreeFromPrefix(prefix), self.createTreeFromPrefix(prefix))
            elif x.isdigit():
                return LiteralNode(int(x))
            elif x.isidentifier():
                return VariableNode(x)

    def evaluateTree(self, symTable):
        """
        Take in a symbol table and evaluate the tree
        """
        return self.root.calculateValue(symTable)


def createDerpTree( ):
    return DerpTree( None )

if __name__ == '__main__':
    symTable = {}
    symTable['x'] = 10
    symTable['y'] = 20
    symTable['z'] = 30
    print(symTable)
    prefix = ['*','8','+','x','y']
    tree = createDerpTree()
    tree.root = tree.createTreeFromPrefix(prefix)
    print(tree.getInfixString())
    print(tree.evaluateTree(symTable))
    print(isinstance(tree.root,MultiplyNode))