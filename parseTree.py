from stack import stack
from Tree import binaryTree


def buildParseTree(fpExp):

    fpList = fpExp.split()
    pStack = stack()
    etree = binaryTree('')
    pStack.push(etree)
    currentTree = etree

    for i in fpList:

        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in '+=*/)':  # Operand
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()

        elif i in '+=*/':  # Operator
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i in ')':
            currentTree=pStack.pop()
        else:
            print("Error: I Don't recognize" + i)

    return etree