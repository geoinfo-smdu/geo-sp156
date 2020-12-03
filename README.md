# Geo SP156

Repositório dedicado a análise espacial dos atendimentos realizados pela central 156 da Prefeitura do Município de São Paulo, que podem ser obtidos atravéz de download no [Portal de Dados Abertos](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/dados-do-sp156)

## Motivação

É comum a todas as cidades, mas São Paulo em específico não é hegemônica. As carências e necessidades são diversas e portanto, reconhecer essa diversidade e um ensejo para conhece-la. Para isso estamos utilizando esse repositório para estudar, analisar e tentar compreender espacialmente os atendimentos realizados pela central de atendimento 156.

## Objetivos

O objetivo princpal é desenvolver uma metodologia e documentar o conhecimento que possa colaborar com a análise espacial dos atendimentos obtidos no portal de Dados Abertos da Município de São Paulo. Para isso elencamos alguns objetivos específicos:

* Desenvolver uma metodologia para espacializar os resgistros
* Divulgar o conhecimento acumulado com as análises realizadas pelo departamento
* Publicar os dados de atendimento espacializados

## Metodologia

Inicialmente vamos utilzar o Python, bilbioteca Pandas e GeoPandas para tratar, epacializar e analisar os dados obtidos, descritos no notebook: [Primeiros processamentos e análises](https://github.com/geoinfo-smdu/geo-sp156/blob/sp156/Primeiros%20Prcessamentos%20e%20An%C3%A1lises.ipynb) Em um segundo momento o desafio vai ser publicar esses dados que são diversos em relação ao espaçõ tanto quanto a classificação e a imensidão de temas e possibilidades.
Existe ainda um outro grande desafio que não devemos e nem podemos deixar para trás que é a cronologia das ocorrências. Elas podem estar ligadas a fenomenos sazonais da cidade, como período de chuvas e estiagem, assim como datas festivas, férias, temperatura entre outros tantos.

## Resultados

Os resultados obtidos neste geoprocessamento vão ficar disponíveis na pasta `resultados` em formato GeoPackage em subpastas por Ano, Tema e eventualmente tipo de geometria gerada (Polígono ou Ponto), onde o nome do arquivo é composto pelo serviço. 

## Convenções 

Definimos que a pasta download vai conter os arquivos que podem ser baixados nos links do arquivo `scripts\links-download.txt`, ou ainda se preferir fazer o download de maneira automática pode executar o script `scripts/download-bases.sh`

