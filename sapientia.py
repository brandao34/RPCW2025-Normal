import json
from pprint import pprint

import shutil
        
novo_ficheiro = "sapientia_ind.ttl"

shutil.copy2("sapientia_base.ttl", novo_ficheiro)

#JSON com os aprendizes
with open("pg57874.json", encoding="utf-8") as f:
    aprendizes = json.load(f)

ttl = ""

for aprendiz in aprendizes:
    nome = aprendiz["nome"].replace('"', '\\"')
    idade = aprendiz.get("idade", "Desconhecida")
    disciplinas = aprendiz.get("disciplinas", [])

    ttl += f':{nome.replace(" ", "_")} rdf:type :Aprendiz ;\n'
    ttl += f'    :nome "{nome}" ;\n'
    ttl += f'    :idade {idade} .\n\n'

    for disciplina in disciplinas:
        ttl += f':{nome.replace(" ", "_")} :aprende :{disciplina.replace(" ", "_")} .\n'

#JSON com os mestres
with open("mestres.json", encoding="utf-8") as f:
    mestres = json.load(f)["mestres"]

for mestre in mestres:
    nome = mestre["nome"].replace('"', '\\"')
    periodo = mestre["períodoHistórico"].replace('"', '\\"')
    disciplinas = mestre.get("disciplinas", [])

    ttl += f':{nome.replace(" ", "_")} rdf:type :Mestre ;\n'
    ttl += f'    :nome "{nome}" ;\n'
    ttl += f'    :periodoHistorico "{periodo}" .\n\n'

    for disciplina in disciplinas:
        ttl += f':{nome.replace(" ", "_")} :ensina :{disciplina.replace(" ", "_")} .\n'

#JSON com as disciplinas
with open("disciplinas.json", encoding="utf-8") as f:
    disciplinas = json.load(f)["disciplinas"]

for disciplina in disciplinas:
    nome = disciplina["nome"].replace('"', '\\"')
    tipos = disciplina.get("tiposDeConhecimento", [])
    conceitos = disciplina.get("conceitos", [])

    ttl += f':{nome.replace(" ", "_")} rdf:type :Disciplina ;\n'
    ttl += f'    :nome "{nome}"'
    if tipos:
        ttl += " ;\n"
        ttl += "    " + " ;\n    ".join([f':pertenceA :{t.replace(" ", "_")}' for t in tipos])
    ttl += " .\n\n"

    for conceito in conceitos:
        ttl += f':{nome.replace(" ", "_")} :eEstudadoEm :{conceito.replace(" ", "_")} .\n'

# o JSON com as obras
with open("obras.json", encoding="utf-8") as f:
    obras = json.load(f)["obras"]

for obra in obras:
    titulo = obra["titulo"].replace('"', '\\"')
    autor = obra["autor"].replace('"', '\\"')
    conceitos = obra.get("conceitos", [])

    ttl += f':{titulo.replace(" ", "_")} rdf:type :Obra ;\n'
    ttl += f'    :titulo "{titulo}" ;\n'
    ttl += f'    :autor "{autor}" .\n\n'

    for conceito in conceitos:
        ttl += f':{titulo.replace(" ", "_")} :explica :{conceito.replace(" ", "_")} .\n'

# JSON com os conceitos
with open("conceitos.json", encoding="utf-8") as f:
    conceitos = json.load(f)["conceitos"]

for conceito in conceitos:
    nome = conceito["nome"].replace('"', '\\"')
    aplicacoes = conceito.get("aplicações", [])
    periodo = conceito.get("períodoHistórico", "")
    relacionados = conceito.get("conceitosRelacionados", [])

    ttl += f':{nome.replace(" ", "_")} rdf:type :Conceito ;\n'
    ttl += f'    :nome "{nome}"'
    if periodo:
        ttl += f' ;\n    :periodoHistorico "{periodo}"'
    if aplicacoes:
        ttl += " ;\n"
        ttl += "    " + " ;\n    ".join([f':temAplicacaoEm :{a.replace(" ", "_")}' for a in aplicacoes])
    ttl += " .\n\n"

    for rel in relacionados:
        ttl += f':{nome.replace(" ", "_")} :estaRelacionadoCom :{rel.replace(" ", "_")} .\n'

# Gerar Ontologia 
with open(novo_ficheiro, "a", encoding="utf-8") as f:
    f.write(ttl)

print(f"Ficheiro TTL gerado: {novo_ficheiro}")