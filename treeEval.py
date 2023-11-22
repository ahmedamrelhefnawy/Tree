from parseTree import buildParseTree
from Tree import binaryTree
import operator

def evaluate(parseTree):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
    leftC  = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:
        fn = operators[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    
if __name__ == "__main__":
    mytree = buildParseTree("( 6 + ( 5 * 2 ) )")
    print(evaluate(mytree))