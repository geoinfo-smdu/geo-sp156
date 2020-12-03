import pandas as pd
import glob
import os 
from datetime import datetime
import geopandas as gpd
from slugify import slugify

path = os.getcwd()
# Define Limite mínimo para se tornar uma camada de serviço
limite = 200

# Carregando Setores 
zipfile = "zip:///home/fernando/dev/geo-sp156/arquivos/SIRGAS_SHP_setorfiscal.zip!SIRGAS_SHP_setorfiscal/SIRGAS_SHP_setorfiscal.shp"
df_setores = gpd.read_file(zipfile)

# Carregando Quadras
zipfile = "zip:///home/fernando/dev/geo-sp156/arquivos/SIRGAS_SHP_quadraMDSF.zip!SIRGAS_SHP_quadraMDSF/SIRGAS_SHP_quadraMDSF.shp"
df_quadras = gpd.read_file(zipfile)
df_quadras = df_quadras[df_quadras.qd_tipo == 'F'] # Somente Quadras Fiscais

# Carregando o limite do município de São Paulo
msp = gpd.read_file('arquivos/SP.shp')


## Itera sobre cada ano de atendimento
for y in range(2015, 2021):

    # Separa os arquivos do ano determinado
    # É necessário atentar para não sobrepor dados do mesmo ano
    all_files = glob.glob(path + f"/download/*{y}.csv")
    print(all_files)

    li = []

    # Carrega dados de cada um dos arquivos do ano y
    print(f"Carregando os arquivos de {y} - {datetime.now()}")
    for filename in all_files:
        print(f" .... {filename}")
        df = pd.read_csv(filename, index_col=None, header=0, encoding="UTF-8", delimiter=',', parse_dates=['Data de abertura', 'Data do parecer'])
        li.append(df)

    # junta todos os anos em um único DataFrame
    df = pd.concat(li, axis=0, ignore_index=True)
    print(f"{len(df)} atendimentos carregados para {y}")

    # Ajustando Lat e Long
    print('Ajustando Lat e Long')
    # df['Latitude'] = pd.to_numeric(df['Latitude'].str.replace(',', '.'), errors='coerce')
    # df['Longitude'] = pd.to_numeric(df['Longitude'].str.replace(',', '.'), errors='coerce')

    # Gerando base geográfica com Lat/Long
    print('Gerando base geográfica com Lat/Long')
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

    # Definindo e convertendo SRC
    print('Definindo e convertendo SRC')
    gdf.crs = 'epsg:4989'
    gdf = gdf.to_crs('epsg:31983')

    # Separando em dataframes para tratar
    print('Separando em dataframes para tratar')
    df_setor = gdf[gdf.Latitude.isna() & ~gdf.Setor.isna() & gdf.Quadra.isna()]
    df_quadra = gdf[gdf.Latitude.isna() & ~gdf.Setor.isna() & ~gdf.Quadra.isna()]

    # Convertendo setor e quadra em 3 digitos
    print('Convertendo setor e quadra em 3 digitos')
    df_setor['st_codigo'] = df_setor.Setor.astype(int).apply(lambda x: '{:03d}'.format(x))
    df_quadra['qd_setor'] = df_quadra.Setor.astype(int).apply(lambda x: '{:03d}'.format(x))
    df_quadra['qd_fiscal'] = df_quadra.Quadra.astype(int).apply(lambda x: '{:03d}'.format(x))

    df_setor.st_codigo = df_setor.st_codigo.astype('str')
    df_quadra.qd_setor = df_quadra.qd_setor.astype('str')
    df_quadra.qd_fiscal = df_quadra.qd_fiscal.astype('str')

    # REmovendo setores duplicados
    df_setores = df_setores.drop(df_setores[df_setores.duplicated(['st_codigo'], keep=False)].index)

    df_setores.geometry = df_setores.geometry.centroid
    df_setor['id'] = df_setor.index
    setor = df_setor.merge(df_setores[['geometry', 'st_codigo']], on=['st_codigo'], suffixes=('', '_y'), how='left')
    setor = setor.set_index('id')

    # Atualizando os centroide no DataFrame
    gdf.loc[(gdf.Latitude.isna() & ~gdf.Setor.isna() & gdf.Quadra.isna()), 'geometry'] = setor.geometry_y

    # REmovendo as quadras duplicadas
    quadras = df_quadras.drop(df_quadras[df_quadras.duplicated(['qd_setor', 'qd_fiscal', 'qd_subqua'], keep=False)].index)
    quadras = quadras.drop(quadras[quadras.qd_subqua != '001'].index)
    quadras.geometry = quadras.geometry.centroid
    df_quadra['id'] = df_quadra.index
    quadra = df_quadra.merge(quadras[['geometry', 'qd_setor', 'qd_fiscal']], on=['qd_setor', 'qd_fiscal'], suffixes=('', '_y'), how='left')
    quadra = quadra.set_index('id')

    # Atualizando os centroind da quadra no DataFrame
    gdf.loc[gdf.Latitude.isna() & ~gdf.Setor.isna() & ~gdf.Quadra.isna(), 'geometry'] = quadra.geometry_y

    # Totalizando serviços por Distrito
    df_distritos = gpd.read_file('arquivos/SIRGAS_SHP_distrito_polygon.shp')
    df_distritos.crs = 'epsg:31983'
    df_distrito = df[~df.Distrito.isna()]

    # Centroide do Distrito para casos em que alguns registros não são localizados
    gdf_servicos_pontos = gdf[gdf.is_valid].groupby(by=['Serviço']).agg({'geometry':'count'}).rename(columns={'geometry':'total_atendimentos_pontos'})
    diferenca_total_distritos = pd.concat([gdf[gdf.Serviço.isin(gdf_servicos_pontos.index)].groupby(by=['Serviço']).agg({
    'geometry':'count'}).rename(columns={'geometry':'total_atendimentos'}),gdf_servicos_pontos], axis=1)
    gdf_servicos_pontos = diferenca_total_distritos[(diferenca_total_distritos.total_atendimentos_pontos/diferenca_total_distritos.total_atendimentos)>0.8]

    servicos_sem_ponto_com_distrito = gdf[gdf.Serviço.isin(gdf_servicos_pontos.index) & ~gdf.is_valid & ~gdf.Subprefeitura.isna()]['Distrito']

    servicos_sem_ponto_com_distrito = pd.DataFrame(servicos_sem_ponto_com_distrito)
    servicos_sem_ponto_com_distrito['index'] = servicos_sem_ponto_com_distrito.index

    df_distritos['centroide'] = df_distritos.geometry.centroid

    centroide_distritos = servicos_sem_ponto_com_distrito.merge(df_distritos, left_on='Distrito', right_on='ds_nome').set_index('index').centroide

    centroide_distritos.index.name = ''

    gdf.iloc[gdf.index.isin(centroide_distritos.index), gdf.columns.get_loc('geometry')] = centroide_distritos

    # Modificando Temas em numeral para 'Outros'
    gdf.loc[df.Tema.str.len() < 5, 'Tema'] = 'Outros'

    # Gerando o arquivo das camadas
    poligonos = gdf[~gdf.Serviço.isin(gdf_servicos_pontos.index)]
    poligonos[['AGUARDANDO ATENDIMENTO','CANCELADA','FINALIZADA','INDEFERIDO']] = pd.get_dummies(poligonos['Status da solicitação'])

    df_distritos = df_distritos.drop('centroide', axis=1)

    if not os.path.exists(f'resultados/{y}'):
        os.makedirs(f'resultados/{y}')

    for t in poligonos.Tema.unique():
        if not os.path.exists(f'resultados/{y}/{slugify(t)}/poligonos'):
            os.makedirs(f'resultados/{y}/{slugify(t)}/poligonos')
        print(f"{slugify(t)}: ({len(poligonos[(poligonos.Tema == t)])})\n")
        for s in poligonos[(poligonos.Tema == t)].Serviço.unique():
            print(f"  {s}: ({len(poligonos[(poligonos.Serviço == s)])})\n")
            c = (poligonos[poligonos.Serviço == s][['Distrito', 'AGUARDANDO ATENDIMENTO', 'CANCELADA', 'FINALIZADA', 'INDEFERIDO', 'Data de abertura']]
                .groupby(['Distrito'])
                .agg({
                    'AGUARDANDO ATENDIMENTO':'sum',
                    'CANCELADA':'sum',
                    'FINALIZADA':'sum',
                    'INDEFERIDO':'sum',
                    'Data de abertura':'count'
                })
                .rename(columns={'Data de abertura':'total_atendimentos'}))
            r = df_distritos.merge(c, left_on='ds_nome', right_on='Distrito')
            if len(r) > 1:
                # r.to_file(f'resultados/Visualizador-156-2020.gpkg', layer=f'{slugify(t)} - Polígono - {s}', driver='GPKG')
                r.to_file(f'resultados/{y}/{slugify(t)}/poligonos/{slugify(s)}.gpkg', driver='GPKG')

    # Verificando atendimentos fora dos limites do município
    print('Verificando atendimentos fora dos limites do município')
    gdf_sp = gpd.sjoin(gdf, gpd.GeoDataFrame([{'municipio':'São Paulo'}], geometry=msp.geometry.buffer(1000)), how='left', op='within')
    pontos = gdf[gdf.Serviço.isin(gdf_servicos_pontos.index) & ~gdf_sp.municipio.isna()]

    # Gravando camadas de pontos
    print('Gravando camadas de pontos')
    for t in pontos.Tema.unique():
        if not os.path.exists(f'resultados/{y}/{slugify(t)}/pontos'):
            os.makedirs(f'resultados/{y}/{slugify(t)}/pontos')
        print(f"{slugify(t)}: ({len(pontos[(pontos.Tema == t)])})\n")
        for s in pontos[(pontos.Tema == t)].Serviço.unique():
            print(f"  {slugify(s)}: ({len(pontos[(pontos.Serviço == s) & (pontos.Tema == t)])})\n")
            r = pontos[(pontos.Serviço == s) & (pontos.Tema == t)]
            if len(r) > 1:
                r.to_file(f'resultados/{y}/{slugify(t)}/pontos/{slugify(s)}.gpkg', driver='GPKG')


    
