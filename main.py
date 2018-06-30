# Importando a biblioteca ElementTree para manipulação do xml
import xml.etree.ElementTree as ET

tree = ET.parse('cnpq.xml')
root = tree.getroot()

atributos_root = root.attrib
primeiro_no = root[0].attrib
resumo = root[0][0]
artigo = root[1][1]
arquivo = root[1][1]
idiomas = root[1][1][0][0]

numero_identificador = "NUMERO-IDENTIFICADOR"
nome = "NOME-COMPLETO"
resumo_cv = "TEXTO-RESUMO-CV-RH"
cont = 0
cont_idioma = 0

def show_xml_content(path, string):
    valor = ''
    for key, value in path.items():
        if key == string:
            valor = value
    return valor

numero = show_xml_content(atributos_root,numero_identificador)
nome = show_xml_content(primeiro_no,nome)
resumo = show_xml_content(resumo,resumo_cv)

for arquivos in arquivo:
    cont += 1
valor_artigo = str(cont)


for artigos in artigo:
    for k, v in idiomas.items():
        if k == 'IDIOMA':
            cont_idioma += 1
valor_idioma = str(cont_idioma)

# Criação da estrutura do arquivo xml de saída
add = ET.Element('add')
doc = ET.SubElement(add,'doc')
field1 = ET.SubElement(doc, 'field')
field2 = ET.SubElement(doc, 'field')
field3 = ET.SubElement(doc, 'field')
field4 = ET.SubElement(doc, 'field')
field5 = ET.SubElement(doc, 'field')
field1.set('name','NUMERO-IDENTIFICADOR')
field2.set('name','NOME-COMPLETO')
field3.set('name','TEXTO-RESUMO-CV-RH')
field4.set('name','numero_artigos')
field5.set('name','numero_idiomas')
field1.text = numero
field2.text = nome
field3.text = resumo
field4.text = valor_artigo
field5.text = valor_idioma

#escrevendo o arquivo
dados = ET.tostring(add)
file = open("saida_test_fapesp.xml", "wb")
file.write(dados)