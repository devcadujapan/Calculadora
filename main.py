from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
import math
import re 

# Define tamanho fixo da janela
Window.size = (400, 600)


class Calculadora(GridLayout):
    texto_entrada = StringProperty("")

    def clicar(self, valor):
        self.texto_entrada += str(valor)

    def limpar(self):
        self.texto_entrada = ""

    def voltar(self):
        self.texto_entrada = self.texto_entrada[:-1]

    def calcular(self):
        try:
            expr = self.texto_entrada.strip()

            if expr.startswith("√"):
                resultado = math.sqrt(float(expr[1:]))

            elif expr.endswith("^2") and "^2" in expr:
                base = expr[:-2]
                base_conv = re.sub(r'(\d+(\.\d+)?)\s*%', r'(\1/100)', base)
                resultado = eval(f"({base_conv})**2")

            else:
                expr_conv = re.sub(r'(\d+(\.\d+)?)\s*%', r'(\1/100)', expr)
                resultado = eval(expr_conv)

            self.texto_entrada = str(resultado)
        except Exception:
            self.texto_entrada = "Erro"

class CalculadoraApp(App):
    def build(self):
        return Calculadora()

if __name__ == "__main__":
    CalculadoraApp().run()
