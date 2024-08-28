from itertools import product

from flask import Flask, render_template

app = Flask(__name__)

class Products:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

product1 = Products('dipirona', 100)
product2 = Products('chinelo', 20)
product3 = Products('jorge', 50)
product4 = Products('torta', 3)
product5 = Products('bola de futebol', 1000)
product6 = Products('bacana', 36)

lista = [product1, product2, product3, product4, product5, product6]


@app.route('/')
def index():
    return render_template('main.html', products = lista)

app.run(debug=True)