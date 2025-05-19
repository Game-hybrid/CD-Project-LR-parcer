def evaluate(node, symbols):
    if node.type == 'NUMBER':
        return float(node.value)
    elif node.type == 'IDENT':
        return symbols.get(node.value)
    elif node.type == 'ASSIGN':
        value = evaluate(node.right, symbols)
        symbols.set(node.value, value)
        return value
    elif node.type == 'PLUS':
        return evaluate(node.left, symbols) + evaluate(node.right, symbols)
    elif node.type == 'MINUS':
        return evaluate(node.left, symbols) - evaluate(node.right, symbols)
    elif node.type == 'MUL':
        return evaluate(node.left, symbols) * evaluate(node.right, symbols)
    elif node.type == 'DIV':
        return evaluate(node.left, symbols) / evaluate(node.right, symbols)
    else:
        raise Exception(f"Unknown node type: {node.type}")
