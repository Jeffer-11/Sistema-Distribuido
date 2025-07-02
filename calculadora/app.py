from flask import Flask, render_template, request, jsonify
import math
import sympy as sp

app = Flask(__name__)

# Función para evaluar expresiones matemáticas avanzadas

def safe_eval(expr):
    # Reemplazos para funciones y constantes
    expr = expr.replace('π', 'math.pi')
    expr = expr.replace('e', 'math.e')
    expr = expr.replace('sin', 'math.sin')
    expr = expr.replace('cos', 'math.cos')
    expr = expr.replace('tan', 'math.tan')
    expr = expr.replace('log', 'math.log10')
    expr = expr.replace('ln', 'math.log')
    expr = expr.replace('√', 'math.sqrt')
    expr = expr.replace('^', '**')
    expr = expr.replace('×', '*')
    expr = expr.replace('÷', '/')
    expr = expr.replace('!', 'math.factorial')
    # Factorial especial: e! -> math.factorial(math.e) no tiene sentido, así que usamos sympy para gamma
    if 'math.factorial(math.e)' in expr:
        expr = expr.replace('math.factorial(math.e)', 'sp.gamma(math.e+1)')
    try:
        # Evalúa usando math y sympy
        result = eval(expr, {"math": math, "sp": sp, "__builtins__": {}})
        return result
    except Exception as e:
        return f"Error: {e}"

@app.route("/")
def index():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expr = data.get("expression", "")
    result = safe_eval(expr)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True) 