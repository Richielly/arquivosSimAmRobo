import os
import shutil
import streamlit as st
from arquivo import Arquivo
# from pacote import Pacote
import configparser

# if not os.path.exists(os.getcwd() + '/RepositorioArquivosSimAm'):
#     os.mkdir('RepositorioArquivosSimAm')
# 
# # os.chdir(os.getcwd() + '/RepositorioArquivosSimAm')
# st.info(os.getcwd())
# arquivosZip = st.file_uploader('Escolha o arquivo', type="zip")
# st.info(os.getcwd())
# shutil.move(arquivosZip, os.getcwd() + '/RepositorioArquivosSimAm')
# shutil.move(arquivosZip, os.getcwd() + '/RepositorioArquivosSimAm','2014TerraRica.zip')
ler = Arquivo()
competencias = Arquivo()

if st.sidebar.checkbox("Arquivos SimAm Detalhe"):
    st.table(ler.varrerDiretorios())

    if not os.path.exists(os.getcwd() + '/RepositorioArquivosSimAm'):
        os.mkdir('RepositorioArquivosSimAm')

if st.sidebar.checkbox("Arquivos Por Módulo"):
    exercicio = st.selectbox('Exercício', [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
    competencia = st.selectbox('Competência', competencias.contar_competencias(exercicio))

    pasta = ler.varrerDiretorios()

    filtro = ler.varrerDiretoriosFiltro(exercicio, competencia, "Contabil")
    st.markdown(str(filtro).replace(',', '\n'))


if st.sidebar.checkbox("Arquivos Por Exerício/Competência"):
    exercicio = st.selectbox('Exercício',[2013,2014,2015,2016,2017,2018,2019,2020,2021])
    competencia = st.selectbox('Competência', competencias.contar_competencias(exercicio))
    with st.expander('Exercício: '+ str(exercicio)):
        st.header('Exercício: '+ str(exercicio))
        linhas = len(ler.varrerDiretorios())
        dado = ler.varrerDiretorios()
        for linha in range(linhas):
            if (dado[linha][0] == str(exercicio)):
                st.subheader('Competência: ' + dado[linha][1] + ' Pasta: ' + dado[linha][3])
                valEx, valCom = Arquivo.validarArquivoTexto(dado[linha][0], dado[linha][1])
                if(dado[linha][3] == 'Contabil'):
                    if(valEx != dado[linha][0] or valCom != dado[linha][1] ):
                        if(dado[linha][1] != '00' and dado[linha][1] != '13'):
                            st.error('Arquivo em diretório errado,' + " com exercício: " + valEx + " e competência: " + valCom)
                            st.sidebar.error('Erro no exercício: ' + dado[linha][0] + ' competênca: ' + dado[linha][1])
                if (dado[linha][0] == str(exercicio)):
                    st.text(str(dado[linha][2]).replace(',','\n'))
                    st.success(str(len(dado[linha][2])) + ' arquivo(s). ')


if st.sidebar.checkbox("Analise Geral"):
    exercicios = [2013,2014,2015,2016,2017,2018,2019,2020,2021]
    for exercicio in exercicios:
        competencia = competencias.contar_competencias(exercicio)
        
        with st.expander('Exercício: '+ str(exercicio)):
            st.header('Exercício: '+ str(exercicio))
            linhas = len(ler.varrerDiretorios())
            dado = ler.varrerDiretorios()
            for linha in range(linhas):
                if (dado[linha][0] == str(exercicio)):
                    st.subheader('Competência: ' + dado[linha][1] + ' Pasta: ' + dado[linha][3])
                    valEx, valCom = Arquivo.validarArquivoTexto(dado[linha][0], dado[linha][1])
                    if(dado[linha][3] == 'Contabil'):
                        if(valEx != dado[linha][0] or valCom != dado[linha][1] ):
                            if(dado[linha][1] != '00' and dado[linha][1] != '13'):
                                st.error('Arquivo em diretório errado,' + " com exercício: " + valEx + " e competência: " + valCom)
                                st.sidebar.error('Erro no exercício: ' + dado[linha][0] + ' competênca: ' + dado[linha][1])
                    if (dado[linha][0] == str(exercicio)):
                        st.text(str(dado[linha][2]).replace(',','\n'))
                        st.success(str(len(dado[linha][2])) + ' arquivo(s). ')

if st.sidebar.checkbox('Config'):

    secoes = []
    parser = configparser.ConfigParser()
    parser.read('cfg.ini')
    for sect in parser.sections():
        secoes.append(sect)
    if secoes != None:
        secao = st.selectbox('Seções: ', secoes)

        for k, v in parser.items(secao):
            st.text_input(k,'{}'.format(v))

    if st.checkbox('Novo'):
        secao = st.text_input('Seção')
        usuario = st.text_input('Chave')
        senha = st.text_input('Valor')
        if st.button('Gravar'):
            parser = configparser.ConfigParser()
            parser.read('cfg.ini')

            parser[secao] = {
                'usuario' : usuario,
                'senha': senha
            }

            with open('cfg.ini', 'w') as configfile:
                parser.write(configfile)

if st.sidebar.checkbox('Acesso Tce'):
    
    import configparser
    secoes = []
    parser = configparser.ConfigParser()
    parser.read('cfg.ini')
    for sect in parser.sections():
        if ((sect != 'Drive') and (sect != 'Urls') and (sect != 'Competencias')and (sect != 'Exercicios')):
            secoes.append(sect)

    dados = st.radio('Acesso Tce:',secoes)

    for k, v in parser.items(dados):
        st.text_input(k,'{}'.format(v))


    st.text(parser.items(dados)[0][1])
    st.text(parser.items(dados)[1][1])

