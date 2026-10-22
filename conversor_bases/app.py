from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


#ALGORITMOS MANUAIS DE CONVERSÃO


def char_para_val(c):
    c = c.upper()
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'A' <= c <= 'F':
        return ord(c) - ord('A') + 10
    return None

def val_para_char(v):
    if 0 <= v <= 9:
        return chr(ord('0') + v)
    elif 10 <= v <= 15:
        return chr(ord('A') + v - 10)
    return ''

def para_decimal(num_str, base):
    num_str = num_str.strip().upper()
    if not num_str:
        raise ValueError("Entrada vazia.")
    
    dec = 0
    for char in num_str:
        v = char_para_val(char)
        if v is None or v >= base:
            raise ValueError(f"Caractere inválido '{char}' para a base {base}.")
        dec = dec * base + v
    return dec

def decimal_para_base(num_dec, base):
    if num_dec == 0:
        return "0"
    
    resultado = []
    temp = num_dec
    while temp > 0:
        resto = temp % base
        resultado.append(val_para_char(resto))
        temp //= base
    
    return "".join(reversed(resultado))

def converter_tudo(valor_str, base_origem):
    try:
        dec = para_decimal(valor_str, base_origem)
        return {
            "sucesso": True,
            "decimal": str(dec),
            "binario": decimal_para_base(dec, 2),
            "hexadecimal": decimal_para_base(dec, 16),
            "octal": decimal_para_base(dec, 8)
        }
    except ValueError as e:
        return {"sucesso": False, "erro": str(e)}


# ROTAS FLASK


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/conversor')
def conversor():
    return render_template('conversor.html')

@app.route('/api/converter', methods=['POST'])
def api_converter():
    dados = request.get_json()
    valor = dados.get('valor', '')
    base_origem = int(dados.get('base_origem', 10))
    
    resultado = converter_tudo(valor, base_origem)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
