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

Inicialmente vamos utilzar o Python, bilbioteca Pandas e GeoPandas para tratar, epacializar e analisar os dados obtidos, descritos no notebook: [Primeiros processamentos e análises](Primeiros Prcessamentos e Análises.ipynb) Em um segundo momento o desafio vai ser publicar esses dados que são diversos em relação ao espaçõ tanto quanto a classificação e a imensidão de temas e possibilidades.
Existe ainda um outro grande desafio que não devemos e nem podemos deixar para trás que é a cronologia das ocorrências. Elas podem estar ligadas a fenomenos sazonais da cidade, como período de chuvas e estiagem, assim como datas festivas, férias, temperatura entre outros tantos.

## Convenções 

Definimos que a pasta download vai conter os arquivos que podem ser baixados nos links abaixo, ou ainda se preferir fazer o download de maneira automática através do script `scripts/DownloadSP156.ps1`

* [Dados do SP156 - 3º TRI 2019](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/8e9bd81b-5219-471b-9539-20ab39d9329f/download/dados-do-sp156---3o-tri-2019.csv)
* [Dados do SP156 - 1º SEM 2019](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/3cd96a69-16a3-4609-8685-26d967398bc7/download/dados-do-sp156---1o-sem-2019.csv)
* [Dados do SP156 - 2º SEM 2018](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/6264fae0-d435-4bf3-9a80-d8084f9f689d/download/dados-do-sp156---2o-sem-2018.csv)
* [Dados do SP156 - 1º SEM 2018](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d26b6f21-29e2-49dc-a9a3-13941661f2ae/download/dados-do-sp156---1o-sem-2018.csv)
* [Dados do SP156 - 2° SEM 2017](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c439343b-6e2e-4cc5-84fe-aba0e54688a1/download/dados-do-sp156---2o-sem-2017.csv)
* [Dados do SP156 - 1° SEM 2017](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/542c3405-5a2d-4e76-b318-92ab4869d453/download/dados-do-sp156---1o-sem-2017.csv)
* [Dados do SP156 - 2° SEM 2016](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c3ef2030-77ec-4eed-945b-297fd52459d1/download/dados-do-sp156---2o-sem-2016.csv)
* [Dados do SP156 - 1° SEM 2016](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/3a5ff4b6-d6b3-458c-a050-04af05a171ee/download/dados-do-sp156---1o-sem-2016.csv)
* [Dados do SP156 - 2º SEM 2015](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c3394c98-d5f1-4202-85a1-af174d86a38a/download/dados-do-sp156---2o-sem-2015.csv)
* [Dados do SP156 - 1º SEM 2015](http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/de1e9b0a-e185-4e0f-9d95-d25d1bebbd36/download/dados-do-sp156---1o-sem-2015.csv)
