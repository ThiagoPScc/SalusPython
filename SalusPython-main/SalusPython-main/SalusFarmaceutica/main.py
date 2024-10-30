from itertools import product
from pickle import GLOBAL

from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)

app.secret_key = 'kU2K6_8w3G8m-QZ0_Fl6A3PqYY0X6yN7VebWX7XtwXg='


class Products:
    def __init__(self, id, img, nome, preco):
        self.id = id
        self.img = img
        self.nome = nome
        self.preco = preco


products_promotion = [
    {'id': 1, 'name': 'Paracetamol 500mg', 'price': 5.00, 'img': 'template_product.png',
     'details': 'Analgésico e antipirético para tratamento de dor e febre.'},
    {'id': 2, 'name': 'Ibuprofeno 400mg', 'price': 7.50, 'img': 'template_product.png',
     'details': 'Anti-inflamatório não esteroidal para dor, febre e inflamação.'},
    {'id': 3, 'name': 'Amoxicilina 500mg', 'price': 12.00, 'img': 'template_product.png',
     'details': 'Antibiótico para infecções bacterianas.'},
    {'id': 13, 'name': 'Loperamida 2mg', 'price': 5.50, 'img': 'template_product.png',
     'details': 'Antidiarreico para tratamento de diarreia aguda.'},
    {'id': 14, 'name': 'Prednisona 20mg', 'price': 18.00, 'img': 'template_product.png',
     'details': 'Corticosteroide para tratamento de inflamações e doenças autoimunes.'},
    {'id': 15, 'name': 'Buscopan 10mg', 'price': 8.50, 'img': 'template_product.png',
     'details': 'Antiespasmódico para alívio de cólicas e espasmos intestinais.'}
]

products = [
    {'id': 1, 'name': 'Paracetamol 500mg', 'price': 5.00, 'img': 'template_product.png',
     'details': 'Analgésico e antipirético para tratamento de dor e febre.'},
    {'id': 2, 'name': 'Ibuprofeno 400mg', 'price': 7.50, 'img': 'template_product.png',
     'details': 'Anti-inflamatório não esteroidal para dor, febre e inflamação.'},
    {'id': 3, 'name': 'Amoxicilina 500mg', 'price': 12.00, 'img': 'template_product.png',
     'details': 'Antibiótico para infecções bacterianas.'},
    {'id': 4, 'name': 'Omeprazol 20mg', 'price': 8.00, 'img': 'template_product.png',
     'details': 'Inibidor de bomba de prótons para tratamento de úlceras e refluxo ácido.'},
    {'id': 5, 'name': 'Dipirona 1g', 'price': 6.00, 'img': 'template_product.png',
     'details': 'Analgésico e antipirético para tratamento de dor e febre.'},
    {'id': 6, 'name': 'Cloridrato de Loratadina 10mg', 'price': 10.00, 'img': 'template_product.png',
     'details': 'Antialérgico para alívio dos sintomas de rinite alérgica.'},
    {'id': 7, 'name': 'Ranitidina 150mg', 'price': 9.00, 'img': 'template_product.png',
     'details': 'Antagonista dos receptores H2 para tratamento de úlceras gástricas e refluxo ácido.'},
    {'id': 8, 'name': 'Captopril 25mg', 'price': 11.00, 'img': 'template_product.png',
     'details': 'Anti-hipertensivo para controle da pressão arterial.'},
    {'id': 9, 'name': 'Diazepam 10mg', 'price': 15.00, 'img': 'template_product.png',
     'details': 'Ansiolítico para tratamento de ansiedade e distúrbios do sono.'},
    {'id': 10, 'name': 'Metformina 500mg', 'price': 14.00, 'img': 'template_product.png',
     'details': 'Antidiabético para controle da glicemia em pacientes com diabetes tipo 2.'},
    {'id': 11, 'name': 'Sulfato de Magnésio 10g', 'price': 4.00, 'img': 'template_product.png',
     'details': 'Suplemento mineral para prevenir deficiência de magnésio.'},
    {'id': 12, 'name': 'Vitamina C 1000mg', 'price': 13.00, 'img': 'template_product.png',
     'details': 'Suplemento vitamínico para reforçar o sistema imunológico.'},
    {'id': 13, 'name': 'Loperamida 2mg', 'price': 5.50, 'img': 'template_product.png',
     'details': 'Antidiarreico para tratamento de diarreia aguda.'},
    {'id': 14, 'name': 'Prednisona 20mg', 'price': 18.00, 'img': 'template_product.png',
     'details': 'Corticosteroide para tratamento de inflamações e doenças autoimunes.'},
    {'id': 15, 'name': 'Buscopan 10mg', 'price': 8.50, 'img': 'template_product.png',
     'details': 'Antiespasmódico para alívio de cólicas e espasmos intestinais.'}

]

cart = []

frete = None
tempo = None
compra = False
total = 0


@app.route('/')
def index():
    return render_template('index.html', products=products, products_promotion=products_promotion)


@app.route('/add_to_cart/<int:product_id>/<string:tela>')
def add_to_cart(product_id, tela):
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        # Check if the product is already in the cart
        for item in cart:
            if item['product']['id'] == product_id:
                item['quantity'] += 1
                break
        else:
            # Product is not in the cart, add it
            cart.append({'product': product, 'quantity': 1})

    if (tela == 'cart'):
        return redirect(url_for('show_cart'))
    else:
        return redirect(url_for('index'))


@app.route('/remove_unity_from_cart/<int:item_id>')
def remove_unity_from_cart(item_id):
    # Find the item in the cart
    for item in cart:
        if item['product']['id'] == item_id:
            item['quantity'] -= 1
            if item['quantity'] <= 0:
                cart.remove(item)
            break
    return redirect(url_for('show_cart'))


@app.route('/remove_product_from_cart/<int:item_id>')
def remove_product_from_cart(item_id):
    # Find the item in the cart
    for item in cart:
        if item['product']['id'] == item_id:
            cart.remove(item)
    return redirect(url_for('show_cart'))


@app.route('/cart')
def show_cart():
    global total
    total = 0.0
    for item in cart:
        product_price = item['product']['price']
        total += product_price * item['quantity']

    return render_template('cart.html', cart=cart, total=total, frete=frete, tempo=tempo)


@app.route('/calcular_frete', methods=['POST'])
def calcular_frete():
    global frete
    global tempo

    import requests
    import openrouteservice
    import math
    from geopy.geocoders import Nominatim

    cep = request.form.get('cep', '')  # Exemplo de CEP

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    print(data)
    if "erro" in data:
        raise ValueError(f"CEP {cep} não encontrado.")

    geolocator = Nominatim(user_agent="test_app")
    location = geolocator.geocode(data['localidade'] + " - " + data['cep'])

    destino = (location.longitude, location.latitude)
    origem = (-46.733920, -23.527747)

    if origem and destino:
        API_KEY_ORS = '5b3ce3597851110001cf624848b39b2d9d0c44fb8d518f7da462a92e'

        # Inicializa o cliente OpenRouteService
        client = openrouteservice.Client(key=API_KEY_ORS)

        # Solicitar direções usando o profile 'driving-car'
        rota = client.directions(coordinates=[origem, destino], profile='driving-car', format='geojson')

        # Extrair distância e nome das ruas
        distancia = rota['features'][0]['properties']['segments'][0]['distance'] / 1000  # metros para km
        print(distancia)
    frete = math.floor((distancia * 1.67) / 5) * 5
    frete = f"R${frete:.2f}"
    tempo = math.floor((distancia * 1.5 + 15) / 5) * 5
    tempo = f"{tempo:.0f} minutos"

    print(frete)

    return render_template('cart.html', cart=cart, total=total, frete=frete, tempo=tempo)

@app.route('/compra', methods=['POST'])
def compra():
    global compra
    compra = True
    return render_template('cart.html', cart=cart, total=total, frete=frete, tempo=tempo, compra=compra)

if __name__ == '__main__':
    app.run(debug=True)
