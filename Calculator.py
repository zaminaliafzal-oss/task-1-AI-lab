class Calculator:
    def __init__(self, expr):
        self.expr = expr.replace(" ", "").replace("×", "*").replace("÷", "/")
        self.expr = self._fix_implicit_mul(self.expr)
    def _fix_implicit_mul(self, e):
        result = ""
        for i in range(len(e)):
            if i > 0 and e[i] == "(" and (e[i-1].isdigit() or e[i-1] == ")"):
                result += "*"
            result += e[i]
        return result
    def calculate(self):
        return eval(self.expr)
calc = Calculator("1+2×3(4-5÷4)-(3÷5)")
print(calc.calculate())