from itertools import product

from flask import Flask, render_template

app = Flask(__name__)

class Products:
    def __init__(self,id, img, nome, preco):
        self.id = id
        self.img = img
        self.nome = nome
        self.preco = preco

produtos_promocao = [
    [1, "../static/template_product.png", "Paracetamol 500mg", 12.90],
    [2, "./static/template_product.png", "Ibuprofeno 400mg", 15.90],
    [3, "./static/template_product.png", "Dipirona 1g", 10.90]
]


produtos_farmacia = [
    [1, "../static/template_product.png", "Paracetamol 500mg", 12.90],
    [2, "./static/template_product.png", "Ibuprofeno 400mg", 15.90],
    [3, "./static/template_product.png", "Dipirona 1g", 10.90],
    [4, "./static/template_product.png", "Antigripal 10 Comprimidos", 18.90],
    [5, "./static/template_product.png", "Omeprazol 20mg", 22.90],
    [6, "./static/template_product.png", "Vitamina C 500mg", 8.90],
    [7, "./static/template_product.png", "Creme Hidratante", 25.90],
    [8, "./static/template_product.png", "Xarope para Tosse", 19.90],
    [9, "./static/template_product.png", "Band-aid (Caixa com 30)", 9.90],
    [10, "./static/template_product.png", "Termômetro Digital", 45.90]
]

lista_produtos = []

for produto in produtos_farmacia:
    produto_objeto = Products(id=produto[0], img=produto[1], nome=produto[2], preco=produto[3])
    lista_produtos.append(produto_objeto)

lista_promocao = []

for produto in produtos_promocao:
    produto_objeto = Products(id=produto[0], img=produto[1], nome=produto[2], preco=produto[3])
    lista_promocao.append(produto_objeto)

@app.route('/')
def index():
    return render_template('index.html', products = lista_produtos, products_promotion=lista_promocao)

app.run(debug=True)