# Script para fazer download dos arquivos de atendimentos do SP156

$downloads = @(
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/8e9bd81b-5219-471b-9539-20ab39d9329f/download/dados-do-sp156---3o-tri-2019.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/3cd96a69-16a3-4609-8685-26d967398bc7/download/dados-do-sp156---1o-sem-2019.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/6264fae0-d435-4bf3-9a80-d8084f9f689d/download/dados-do-sp156---2o-sem-2018.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/d26b6f21-29e2-49dc-a9a3-13941661f2ae/download/dados-do-sp156---1o-sem-2018.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c439343b-6e2e-4cc5-84fe-aba0e54688a1/download/dados-do-sp156---2o-sem-2017.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/542c3405-5a2d-4e76-b318-92ab4869d453/download/dados-do-sp156---1o-sem-2017.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c3ef2030-77ec-4eed-945b-297fd52459d1/download/dados-do-sp156---2o-sem-2016.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/3a5ff4b6-d6b3-458c-a050-04af05a171ee/download/dados-do-sp156---1o-sem-2016.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/c3394c98-d5f1-4202-85a1-af174d86a38a/download/dados-do-sp156---2o-sem-2015.csv",
    "http://dados.prefeitura.sp.gov.br/pt_PT/dataset/0aecfa2b-aa3a-40d4-8183-0d4351b7fd0a/resource/de1e9b0a-e185-4e0f-9d95-d25d1bebbd36/download/dados-do-sp156---1o-sem-2015.csv"
)

$arquivos = @(  
    "../download/Dados_do_SP156_3_TRI_2019.csv",
    "../download/Dados_do_SP156_1_SEM_2019.csv",
    "../download/Dados_do_SP156_2_SEM_2018.csv",
    "../download/Dados_do_SP156_1_SEM_2018.csv",
    "../download/Dados_do_SP156_2_SEM_2017.csv",
    "../download/Dados_do_SP156_1_SEM_2017.csv",
    "../download/Dados_do_SP156_2_SEM_2016.csv",
    "../download/Dados_do_SP156_1_SEM_2016.csv",
    "../download/Dados_do_SP156_2_SEM_2015.csv",
    "../download/Dados_do_SP156_1_SEM_2015.csv"
)

# Ajustando as credenciais para o proxy autenticado
[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultNetworkCredentials

foreach ($i in 0..($downloads.Length - 1)) {
    Invoke-WebRequest -Uri $downloads[$i] -OutFile $arquivos[$i] -Verbose
}

#Start-BitsTransfer -Source $downloads -Destination $arquivos

