import streamlit as st
from arquivo import Arquivo
from pacote import Pacote

ler = Arquivo()
competencias = Arquivo()
if st.sidebar.checkbox("Arquivos SimAm Detalhe"):
    st.table(ler.varrerDiretorios())

if st.sidebar.checkbox("Arquivos Por Módulo"):
    exercicio = st.selectbox('Exercício', [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
    competencia = st.selectbox('Competência', competencias.contar_competencias(exercicio))

    pasta = ler.varrerDiretorios()

    filtro = ler.varrerDiretoriosFiltro(exercicio, competencia, "Contabil")
    st.markdown(str(filtro).replace(',', '\n'))

if st.sidebar.checkbox("Arquivos Por Exerício/Competência"):
    exercicio = st.selectbox('Exercício',[2013,2014,2015,2016,2017,2018,2019,2020,2021])
    competencia = st.selectbox('Competência', competencias.contar_competencias(exercicio))
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
