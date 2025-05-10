from sympy import symbols, sympify, simplify, solve_univariate_inequality, expand
from sympy.parsing.sympy_parser import parse_expr
from sympy.core.relational import Relational
from sympy.abc import x
import sympy

def parse_inequality(expr_str):
    try:
        ineq = parse_expr(expr_str, transformations='all')
        if isinstance(ineq, Relational):
            return ineq
        else:
            raise ValueError("Girdi bir eşitsizlik değil.")
    except Exception as e:
        raise ValueError(f"Eşitsizlik ayrıştırılamadı: {e}")

def solve_or_simplify_inequality(expr_str):
    try:
        ineq = parse_inequality(expr_str)
        expanded_ineq = expand(ineq)
        print(f"Genişletilmiş eşitsizlik: {expanded_ineq}")

        if len(ineq.free_symbols) == 1:
            var = list(ineq.free_symbols)[0]
            sol = solve_univariate_inequality(ineq, var, relational=False)
            return f"Çözüm kümesi: {sol}"
        else:
            simplified_ineq = simplify(ineq)
            return f"Çok değişkenli ifade. Sadeleştirilmiş hali: {simplified_ineq}"
    except Exception as e:
        return f"Hata: {e}"

print("Matematiksel eşitsizlik girin (örn: x**2 - 4 < 0):")
user_input = input(">> ")
result = solve_or_simplify_inequality(user_input)
print(result)


