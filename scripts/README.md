# Fluxos de trabalho

## Fazendo o download das bases

`download-bases.sh` é responsável por fazer o download de todos os links que se encontram no `links-downaloads.txt` e grava os arquivos na pasta `/download`

## Gerando o resultado de cada ano e guardando na estrutura de pastas de resultado

A partir dos arquivos gravados na pasta `/downloads` o script `processa-resultados.py` processa os atendimentos de cada ano e grava em uma estrutura de dados na pasta `resultados`
