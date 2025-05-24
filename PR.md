## A Ontologia: estrutura base


1. Análise dos Jsons, Comparação dos dados do Json com as Classes sugeridas no enunciado


3. Análise da sugestão de Object properties, através de um desenho simplificado das classes e como elas se iriam relacionar


2. Análise dos Jsons para adicionar os atributos às classes como data properties (Autor, Idade, Nome, periodoHistorico,título).


4. Guardar o ttl com o nome indicado




## A Ontologia: povoamento/criação de indivíduos




Para povoar a ontologia segue a estratégia de criar uma string vazia e ir povoando o json a json


A estratégia utilizado foi:


Começar com os Aprendizes, já que estes não possuem relação com ninguém, de seguida os mestre e as disciplinas, pois ambos tem relação (Domain->Aprendiz). De seguida as obras e por fim os conceitos pois estes tinham as relações mais complexas.
Por fim, utilizei o reasoner do protegê para preencher principalmente os indivíduos que não possuíam tipo, sendo que isto provavelmente seria causado ou pela informação incompleta referida no enunciado, ou pela ordem que eu decidi adicionar os jsons à ontologia.




## Queries simples + Cálculo de distribuições + Inferência de novo conhecimento


Análise de querie a querie e confirmação de resultados



## Ficheiros


sapientia_base.tll  -> Ficheiro Criado em A Ontologia: estrutura base
sapientia_ind.tll ->  Ficheiro Criado em  A Ontologia: povoamento/criação de indivíduos
sapientia_ind_inferido.tll -> Ontología inferida no protege após o sapientia_ind estar criado
sapientia_graphdb -> Ontologia extraída do graphdb após as queries de insert



