from consulta import Consulta
from pendencia import Pendencia
import streamlit as st
import db
import arquivo as arc

if st.sidebar.checkbox("Gerar Banco"):
    if st.button("Gerar"):
        createDB = db.TransactionObject()
        #createDB.createDB()
        #Consulta.start()
        #Pendencia.validar_arquivos_processados()
        #Pacote.decompactarCmd()
        # Arquivo.deletarZip()
if st.sidebar.checkbox("Navegador"):
    if st.button("Parar Navegador"):
        Consulta.finalizarNavegador()
        
if st.sidebar.checkbox("Graficos"):
    diretorio = arc.Arquivo()
    grafico = diretorio.grafico()
    for dado in grafico:
        st.info(dado + str(len(dado[1])))
        label = dado[0]
        quantidade = len(dado[1])

#Consulta.start()

#if __name__ == '__main__':
 #   Main.principal()
