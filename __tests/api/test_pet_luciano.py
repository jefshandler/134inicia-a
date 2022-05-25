#comando para determinar diretorio onde inicial a referencia de caminho relativo
# bibliotecas
import json
import os
import pytest
import requests

urlbase = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

from __tests.utils.file_manager import ler_csv


#comando para determinar diretorio onde inicial a referencia de caminho relativo
os.chdir(f'F:{os.sep}projetoPython{os.sep}134inicial-a{os.sep}')
#lita utilizando o separador do sistema para caminho relativo
@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags,status',
                         ler_csv(f'vendors{os.sep}csv{os.sep}massa_incluir_pet_multitags.csv'))
def teste_incluir_pet_em_massa_com_multiplas_tags(pet_id, category_id, category_name, pet_name, tags, status):
    # 1. Configura
    # 1.1 Dados de entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pets.csv
    # 1.1.1 Montagem do JSON dinamico
    global itens_lista
    corpo_json = '{'
    corpo_json += f'"id":  "{pet_id}" ,'
    corpo_json += '"category": {'
    corpo_json += f'"id":  "{category_id}",'
    corpo_json += f'"name": "{category_name}"'
    corpo_json += ' },'
    corpo_json += f'"name":  "{pet_name}" ,'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    # 1.1.1.1 iteração das possiveis tags doo animal
    lista_tags = tags
    json_tag = '"tags": ['
    sub_lista_tags = []
    qtd_tags = lista_tags.count(';') + 1
    # quando for mais de uma tag, os valores devem ser separados no csv por ';'
    if lista_tags.count(';') > 0:
        lista_tags = lista_tags.split(';')
        qtd_el = len(lista_tags)
        print('Quantidade de elementos' + str(qtd_el))

        for i in range(0, qtd_el):
            # Create an index range for l of n items:
            sub_lista_tags.append(lista_tags[i].split(','))
        itens_lista = len(sub_lista_tags)
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for contador in range(0, itens_lista):
            if contador < itens_lista - 1:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"},'
            else:
                json_tag += '{"id":' + sub_lista_tags[contador][0] + \
                            ',"name":"' + sub_lista_tags[contador][1] + '"}'
    # 1.1.1.2 Quando há somente 1 tag, não é necessário usar o looping do FOR
    else:
        lista_tags = lista_tags.split(',')
        json_tag += '{"id":' + lista_tags[0] + ',"name":"' + lista_tags[1] + '"}'
        # print(f'\nExiste 1 tag na lista {lista_tags}')
    json_tag += '],'
    # 1.1.2 Continuando a montagem do Json, com adicao das tags
    corpo_json += json_tag
    corpo_json += f'"status":  "{status}"'
    corpo_json += '}'
    # print(corpo_json)

    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.post(
        url=urlbase,
        headers=headers,
        data=corpo_json
    )

    # Valida
    mostrar_corpo_json = json.loads(corpo_json)
    print(f'\n==== CORPO ENVIADO ====')
    print(json.dumps(mostrar_corpo_json, indent=4))
    print(f'\n==== CORPO OBTIDO ====')
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    # asserts dinamicos de acordo com as tags existeentes para um pet
    if qtd_tags > 1:
        # print(f'\nExistem  {itens_lista} tags na lista {sub_lista_tags}')
        for i in range(0, qtd_tags):
            for j in range(2):
                assert corpo_do_resultado_obtido['tags'][i]['name'] == sub_lista_tags[i][1]
    else:
        # print(f'\nExiste 1 tag na lista {lista_tags}')
        assert corpo_do_resultado_obtido['tags'][0]['name'] == lista_tags[1]
