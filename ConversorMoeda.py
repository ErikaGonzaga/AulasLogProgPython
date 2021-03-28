x = False

while(x != True):
    print("Digite para qual tipo de moeda deseja converter")
    print("Digite 1 para Dólar")
    print("Digite 2 para Euro")
    tipo_de_moeda = int(input())
    if tipo_de_moeda == 1:
        print("O tipo de moeda escolhido foi Dólar")
        x = True
    elif tipo_de_moeda == 2:
        print("O tipo de moeda escolhido foi Euro")
        x = True

cotacao_euro = 6.81
cotacao_dolar = 5.76

print("Digite o valor em Real que deseja converter")

valor_para_converter = float(input())
print("O valor solicitado para a conversão é", valor_para_converter)

valor_convertido = 0.0

if tipo_de_moeda == 1:
    valor_convertido = valor_para_converter/cotacao_dolar
elif tipo_de_moeda == 2:
    valor_convertido = valor_para_converter/cotacao_euro
else:
    print("Não foi possível fazer a conversão")

print("O resultado da conversão é %.2f" % valor_convertido)