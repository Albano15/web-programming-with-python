from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página principal (index)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para calcular o tipo de triângulo
@app.route('/calc-triangulo', methods=['GET', 'POST'])
def calc_triangulo():
    result_triangulo = None
    imagem_triangulo = None

    if request.method == 'POST':
        lado1 = float(request.form['lado1'])
        lado2 = float(request.form['lado2'])
        lado3 = float(request.form['lado3'])

        # Determina o tipo de triângulo
        if lado1 == lado2 == lado3:
            result_triangulo = 'Triângulo Equilátero'
            imagem_triangulo = 'triangulo-equilatero.png'  # Nome da imagem para triângulo equilátero
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            result_triangulo = 'Triângulo Isósceles'
            imagem_triangulo = 'triangulo-isosceles.png'  # Nome da imagem para triângulo isósceles
        else:
            result_triangulo = 'Triângulo Escaleno'
            imagem_triangulo = 'triangulo-escaleno.png'  # Nome da imagem para triângulo escaleno

    return render_template('calc-triangulo.html', result_triangulo=result_triangulo, imagem_triangulo=imagem_triangulo)

# Rota para calcular a média das notas
@app.route('/media-notas', methods=['GET', 'POST'])
def media_notas():
    result_media = None
    mensagem_media = None
    imagem_media = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        nota4 = float(request.form['nota4'])
        
        result_media = (nota1 + nota2 + nota3 + nota4) / 4

        # Definir mensagens para a média
        if result_media >= 7:
            mensagem_media = "Aprovado"
            imagem_media = '../static/aprovado.jpg'
        else:
            mensagem_media = "Reprovado"
            imagem_media = '../static/reprovado.jpg'


    return render_template('media-notas.html', result_media=result_media, mensagem_media=mensagem_media, imagem_midia=imagem_media)

if __name__ == '__main__':
    app.run(debug=True)
