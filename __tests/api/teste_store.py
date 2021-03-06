# ToDo: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import json
import os.path

import requests

urlbase = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}


def teste_vender():
    # 1 -   Configura
    # 1.1 - dados de Entrada -> vem do arquivo add_order1.json
    # 1.2 - Resultado Esperado
    status_code_esperado = 200
    id_pedido_esperado = 5228888
    id_pet_esperado = 7730507
    status_pedido_esperado = 'placed'


    # Executa
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep

    print(f'caminho1 = {caminho}')
    resultado_obtido = requests.post(
        url=urlbase + 'store/order',
        headers=headers,
        data=open('F:\\projetoPython\\134inicial-a\\vendors\\json\\add_order1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == id_pet_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # extrassao Extrair
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # Realizar a 2 parte Transacao

    # Configura
    # dados de entrada = estraido da 1 transaçao acima

    # Resultado esperado  vamos pegar o nome do animal
    pet_name_esperado = 'doggie'
    status_code_esperado = 200

    # executa
    resultado_obtido = requests.get(
        url= urlbase + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()

    assert corpo_do_resultado_obtido['name'] == pet_name_esperado
    print(json.dumps(corpo_do_resultado_obtido, indent=4))