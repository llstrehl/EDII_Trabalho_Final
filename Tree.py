from dataclasses import dataclass
from typing import Optional, List
from operator import add, sub, mul, truediv

@dataclass
class Node:
    valor: str
    left: Optional['Node']
    right: Optional['Node']

    def is_calculado(self) -> bool:
        return self.left is None and self.right is None

@dataclass
class Tree:
    root: Node
    
    @classmethod
    def _tokenize(cls, text: str) -> List[str]:
        prev = ''
        tokenized = []
        for char in text:
            if (prev.isdigit() or prev == '.') and (char.isdigit() or char == '.'):
                tokenized.append(tokenized.pop() + char)
            else:
                tokenized.append(char)
            prev = char
        return tokenized

    def evaluate(self, node: Optional[Node] = None):
        OPS = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv
        }
        node = node or self.root
        if node.is_calculado():
            return float(node.valor)
        else:
            op = OPS[node.valor]
            return op(self.evaluate(node.left), self.evaluate(node.right))
    
    @classmethod
    def build(cls, text: str) -> 'Tree':
        operator_stack: List[str] = []
        operand_stack: List[Node] = []
        for char in cls._tokenize(text):
            if char.isdigit() or '.' in char:
                operand_stack.append(Node(valor=char, left=None, right=None))
            elif char in '+-' and len(operator_stack) > 0 and operator_stack[-1] in '*/':
                right = operand_stack.pop()
                op = operator_stack.pop()
                left = operand_stack.pop()
                operand_stack.append(Node(valor=op, left=left, right=right))
                operator_stack.append(char)
            elif char == ')':
                while len(operator_stack) > 0 and operator_stack[-1] != '(':
                    right = operand_stack.pop()
                    op = operator_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(Node(valor=op, left=left, right=right))
                operator_stack.pop()
            else:
                operator_stack.append(char)
        while len(operator_stack) > 0:
            right = operand_stack.pop()
            op = operator_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(Node(valor=op, left=left, right=right))
        return cls(root=operand_stack.pop())
    