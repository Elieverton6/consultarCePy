import requests

zipcode = input('Digite seu CEP:') # Input pra receber o CEP

url = f'https://api.brasilaberto.com/v1/zipcode/{zipcode}' # URL da API

response = requests.get(url) # Enviando solicitação GET para a API

if response.status_code == 200:
    data = response.json() # Convertendo a resposta JSON em um dicionário Python

    result_data = data['result'] # Acessando o campo 'result' para obter os dados da cidade
    
    rua = result_data.get('street') # Extraindo o nome da rua do campo 'street' dentro de 'result'
    bairro = result_data.get('district') # Extraindo o nome do bairro do campo 'district' dentro de 'result'
    cidade = result_data.get('city') # Extraindo o nome da cidade do campo 'city' dentro de 'result'
    estado = result_data.get('state') # Extraindo o nome do estado do campo 'state' dentro de 'result'
    
    print("CEP Encontrado!")
    print(f"Confira o dados do CEP: Estado: {estado}, Cidade: {cidade}, Bairro: {bairro}, Rua: {rua}")
elif response.status_code == 404:
    print("CEP Digitado não existe!")
else:
    print("Falha ao acessar a API:", response.status_code)
