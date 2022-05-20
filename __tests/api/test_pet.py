# bibliotecas
import json

import pytest
import requests

from __tests.utils.file_manager import ler_csv

# variaveis publicas
urlbase = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definições das funções (defs)


def test_incluir_pet():
    # configura - prepara
    # Dados de entrada provem do arquivo json (pet1.json)

    # resultados esperados (pertence a configura)
    status_code_esperado = 200
    pet_id_esperado = 5222429
    pet_nome_categoria_esperado = "Gato"
    pet_nome_esperado = "Jurema"
    pet_tag_esperado = "vacinado"

    # executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=open('F:\\projetoPython\\134inicial\\vendors\\json\\pet2.json')

    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado

    def test_incluir_pet2():
        # configura - prepara
        # Dados de entrada provem do arquivo json (pet1.json)

        # resultados esperados (pertence a configura)
        status_code_esperado = 200
        pet_id_esperado = 5222429
        pet_nome_categoria_esperado = "gato"
        pet_nome_esperado = "Jurema"
        pet_tag_esperado = "vacinado"
        pet_status_esperado = "pending"

        # executa
        resultado_obtido = requests.post(
            url=urlbase,
            headers=headers,
            data=open('F:\\projetoPython\\134inicial\\vendors\\json\\pet1.json')

        )

        # Valida
        print(resultado_obtido)
        corpo_do_resultado_obtido = resultado_obtido.json()
        print(json.dumps(corpo_do_resultado_obtido, indent=4))

        assert resultado_obtido.status_code == status_code_esperado
        assert corpo_do_resultado_obtido['id'] == pet_id_esperado
        assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
        assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
        assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado



def teste_consultar_pet():
    # 1 Parte é dividido em 2 partes entradas e Resultados esperados
    # configura - prepara
    # Dados de entrada provem do arquivo json (pet1.json)

    # Entradas
    pet_id = '5222428'
    # Resultados esperados
    # 2 Parte
    status_code_esperado = 200
    pet_id_esperado = 5222428
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_esperado = "Jujuba"
    pet_tag_esperado = "vacinado"

    # Executa

    resultado_obtido = requests.get(
        url=urlbase + '/' + pet_id,
        headers=headers
    )

    # 3 Parte
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado


def teste_alterar_pet():
    # 1 Parte é dividido em 2 partes entradas e Resultados esperados
    # configura - prepara
    # Dados de entrada provem do arquivo json (pet1.json)

    # Entradas
    pet_id = '5222428'
    # Resultados esperados
    # 2 Parte
    status_code_esperado = 200
    pet_id_esperado = 5222428
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_esperado = "Jujuba"
    pet_tag_esperado = "vacinado"
    pet_status_esperado = "pending"


    # Executa

    resultado_obtido = requests.put(
        url=urlbase,
        headers=headers,
        data=open('F:\\projetoPython\\134inicial\\vendors\\json\\pet3.json')
    )

    # 3 Parte
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_tag_esperado


def teste_excluir_pert():
    # 1 configura
    # dados de entrada
    pet_id = '5222429'

    # dados
    status_code_esperado = 200
    status_code_interno_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '5222429'

    # 2 Executa
    resultado_obtido = requests.delete(
        url=urlbase + '/' + pet_id,
        headers=headers,
        )

    # 3 valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == status_code_interno_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == message_esperada


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',ler_csv(
'F:\\projetoPython\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))
def teste_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    # 1 configura
    # 1.1 dados de entrada
    # os dados de entrada provem do arquivo massa_incluir_pet_csv
    # 1.2 resultado esperados - os dados de entrada tambem servirao
    # visto que o retorno é um eco
    # 1.1.1 MOntagem do Json dinâmico
    corpo_json =  '{'
    corpo_json += f' "id": {pet_id}, '
    corpo_json += ' "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": "{category_name}"'
    corpo_json += '},'
    corpo_json += f' "name": "{pet_name}",'
    corpo_json += ' "photoUrls": ['
    corpo_json += '    "string"'
    corpo_json += '],'
    corpo_json += ' "tags": ['
    corpo_json += '    {'
    corpo_json += f'        "id": {tags_id},'
    corpo_json += f'        "name": "{tags_name}"'
    corpo_json += '    }'
    corpo_json += '],'
    corpo_json += f' "status": "{status}"'
    corpo_json += '}'

    status_code_esperado = 200

    # 2. executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=corpo_json
    )

    # 3. valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name