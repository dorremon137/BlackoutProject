"""
141 Tree Lab - Derp the Interpreter

These are the definitions of the node classes that
are used by the interpreter. It is meant to be imported by the main program
and the derp_tree file.

Author: Sean Strout (sps@cs.rit.edu)\
Author: Scott C Johnson (scj@cs.rit.edu)

Phuvit Kittisapkajon
"""

from rit_lib import *

##############################################################################
# structure definitions for parse tree
##############################################################################

class MultiplyNode(struct):
    """Represents a multiply operator, *"""
    
    _slots = ((object, 'left'), (object, 'right'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        :return:
        """
        left = self.left.getInfixString()
        right = self.right.getInfixString()

        return "(" + left + '*' + right + ")"

    def addLeftSide(self, side):
        """
        sets the left side of the operand
        """
        self.left = side

    def addRightSide(self, side):
        """
        Sets the right side of the operand
        """
        self.right = side

    def calculateValue(self, symbolTable):
        """
        Calculates the value of this node using the
        left and right hand sides.
        :return:
        """
        left = self.left.calculateValue(symbolTable)
        right = self.right.calculateValue(symbolTable)
        return left * right

    
class DivideNode(struct):
    """Represents an integer divide operator, //"""

    _slots = ((object, 'left'), (object, 'right'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        :return:
        """
        left = self.left.getInfixString()
        right = self.right.getInfixString()

        return "(" + left + '//' + right + ")"

    def addLeftSide(self, side):
        """
        sets the left side of the operand
        """
        self.left = side

    def addRightSide(self, side):
        """
        Sets the right side of the operand
        """
        self.right = side

    def calculateValue(self, symbolTable):
        """
        Calculates the value of this node using the
        left and right hand sides.
        :return:
        """
        left = self.left.calculateValue(symbolTable)
        right = self.right.calculateValue(symbolTable)
        return left // right
    
class AddNode(struct):
    """Represents an addition operator, +"""

    _slots = ((object, 'left'), (object, 'right'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        :return:
        """
        left = self.left.getInfixString()
        right = self.right.getInfixString()

        return "(" + left + '+' + right + ")"

    def addLeftSide(self, side):
        """
        sets the left side of the operand
        """
        self.left = side

    def addRightSide(self, side):
        """
        Sets the right side of the operand
        """
        self.right = side

    def calculateValue(self, symbolTable):
        """
        Calculates the value of this node using the
        left and right hand sides.
        :return:
        """
        left = self.left.calculateValue(symbolTable)
        right = self.right.calculateValue(symbolTable)
        return left + right
    
class SubtractNode(struct):
    """Represents a subtraction operator, -"""

    _slots = ((object, 'left'), (object, 'right'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        :return:
        """
        left = self.left.getInfixString()
        right = self.right.getInfixString()

        return "(" + left + '-' + right + ")"
    def addLeftSide(self, side):
        """
        sets the left side of the operand
        """
        self.left = side

    def addRightSide(self, side):
        """
        Sets the right side of the operand
        """
        self.right = side

    def calculateValue(self, symbolTable):
        """
        Calculates the value of this node using the
        left and right hand sides.
        :return:
        """
        left = self.left.calculateValue(symbolTable)
        right = self.right.calculateValue(symbolTable)
        return left - right
    
class LiteralNode(struct):
    """Represents an operand node"""
    
    _slots = ((int, 'val'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        """
        return str(self.val)

    def calculateValue(self, symbolTable):
        """
        Returns the value of this node using the
        left and right hand sides.
        :return:
        """
        return int(self.val)
    
class VariableNode(struct):
    """Represents a variable node"""
    
    _slots = ((str, 'name'))

    def getInfixString(self):
        """
        Return a string representing this node in an infix notation.
        """
        return str(self.name)

    def calculateValue(self, symbolTable):
        """
        Calculates the value of this node using the
        left and right hand sides.
        :return:
        """
        number = symbolTable [self.name]
        return int(number)

if __name__ == '__main__':
    tree=MultiplyNode(LiteralNode(3),SubtractNode(LiteralNode(2),LiteralNode(1)))
    print(tree.getInfixString())
