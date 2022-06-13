# QGIS tips & tricks - PYTHON - SCRIPTS

Scripts feitos para rodar no terminal python do qgis  
Assista ao vídeo de como utilizar scripts python no QGIS:  
[![Assista ao vídeo dPython + Qgis = Mais tempo na Vida](https://img.youtube.com/vi/0kaYuPeM0wI/0.jpg)](https://www.youtube.com/watch?v=0kaYuPeM0wI)  


* [salva_camadas](./salva_camadas): Esse script salva todas as camadas do projeto em um arquivo kml dentro das pastas das respectivas camadas (não funciona em camadas de texto delimitado).
* [save_selected](./save_selected): Esse script seleciona dentro de cada camada do projeto feições usando uma expressão (feita na calculadora de campo) e salva a seleção em um arquivo, dentro da pasta da camada.
* [vector_layers_attribute_txt](./scripts/vector_layers_attribute_txt): Esse script exporta todos os campos e seus tipos de cada camada vetorial ou tabular para um arquivo TXT.
* [reorder_vertices](./reorder_vertices): Esse script gera uma nova camada de pontos com os vértices de um polígonos, reordenando ele a partir de um vértice escolhido.
* [generate_label](./generate_label): Esse script gera uma nova camada virtual com a nova coluna com o rótulo da feição, ordenada pela área da geometria

