from flask import Flask, render_template, request
from exprlang.lexer import tokenize
from exprlang.parser import Parser
from exprlang.symbol_table import SymbolTable
from exprlang.evaluator import evaluate
from exprlang.codegen import generate_code

app = Flask(__name__)
symbols = SymbolTable()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    code_lines = []
    expr = ''
    error = ''
    if request.method == 'POST':
        expr = request.form['expr'].strip()
        if not expr:
            error = "Please enter an expression."
        else:
            try:
                tokens = tokenize(expr)
                print("TOKENS:", tokens)
                parser = Parser(tokens)
                ast = parser.parse()
                print("AST Root Type:", ast.type if ast else "None")
                result = evaluate(ast, symbols)
                _, code_lines = generate_code(ast, [])
            except Exception as e:
                error = str(e)
    return render_template('index.html', result=result, code=code_lines, expr=expr, error=error)

if __name__ == '__main__':
    app.run(debug=True)
