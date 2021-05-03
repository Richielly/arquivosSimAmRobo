import os
from consulta import Consulta
from arquivo import Arquivo
caminho_destino = 'C:\\Users\\richielly.carvalho\\Downloads\\SimAm'
class Pendencia:

    def reprocessar_pendencia(pendencia):
        try:
            Consulta.loginSimAm('03158339986','almir1')
            Arquivo.registrar_log(" \n################### Reprocessando Pendencias ################")
            print(" \n################### Reprocessando Pendencias ################")
            Arquivo.registrar_log("Exercicio Pendente a Reprocessar: "+str(pendencia[0]))
            print("Exercicio Pendente a Reprocessar: " + str(pendencia[0]))
            Arquivo.registrar_log("Quantidade de Arquivos para Reprocessamento: "+str(len(pendencia[1])))
            print("Quantidade de Arquivos para Reprocessamento: " + str(len(pendencia[1])))

            for arquivo in pendencia[1]:
                Consulta.rota(pendencia[0],arquivo)
                Arquivo.registrar_log("Arquivo Processado: " + str(arquivo))
        except: Arquivo.registrar_log("Problema ao tentar reprocessar arquivo.")

    def listar_competencias_pendentes(exercicio):
        lista_competencias_baixadas = []
        competencias_pendentes = []
        competecias_baixadas = os.listdir(caminho_destino + '\\' + str(exercicio))

        for competencia in competecias_baixadas:
            #colocando em uma lista as competencias que conseguiram ser baixadas
            lista_competencias_baixadas.append(competencia)

        dic_competencias = {'Abertura de Exercício': '00', 'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04',
                'Maio': '05',
                'Junho': '06', 'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11',
                'Dezembro': '12', 'Encerramento de Exercício': '13'}

        print(dic_competencias.items())



        lista_padrao_competencia = ['Abertura de Exercício', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                                    'Julho',
                                    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',
                                    'Encerramento de Exercício']
        lista_reconsulta = list(set(lista_padrao_competencia) - set(lista_competencias_baixadas))

        return exercicio, lista_reconsulta


    def validar_arquivos_processados():
        exercicios = Arquivo.contar_arquivos()

        for exercicio in exercicios:
            Pendencia.reprocessar_pendencia(Pendencia.listar_competencias_pendentes(exercicio))

        return len(exercicios)
