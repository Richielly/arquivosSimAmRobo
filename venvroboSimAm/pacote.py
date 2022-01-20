# -*- coding:utf-8 -*-
from zipfile import ZipFile
from pyunpack import Archive
import os
import sys
import time

        #Extrair todos os arquivos mas sem as devidas pastas arquivo final txt
            #os.system('7z e 00.zip -oC:\\caminho de destino')
        #Extrair todos os arquivos conforme sua estrutura de pastas
            #os.system('7z x '+str(nome[competencia])+'.zip -oC:\\caminho de destino)

diretorio = "C:\\Users\\richielly.carvalho\Downloads\SimAm\\"

class Pacote:

    def descompactar_2():
        #import zipfile

        from zipfile import ZipFile

        with ZipFile(str(diretorio) + "\\2013\\00.zip") as zf:
            zf.extractall()

        #zip = zipfile.ZipFile(str(diretorio) + "\\2013\\00.zip")
        #zip.extractall(diretorio)

        fantasy_zip.close()

    def descompactar(self, exercicio, competencia):

        if os.path.exists("C:\\Users\\richielly.carvalho\\Downloads\\SimAm\\"+str(exercicio)+'\\'+str(competencia)):
            Archive(diretorio + str(exercicio) + '\\' + str(competencia + '.zip')).extractall(diretorio + str(exercicio) + '\\' + str(competencia)+'\\')
        else:
            caminho = os.makedirs("C:\\Users\\richielly.carvalho\\Downloads\\SimAm\\"+str(exercicio)+'\\'+str(competencia))
            Archive(diretorio + str(exercicio) + '\\' + str(competencia + '.zip')).extractall(diretorio + str(exercicio) + '\\' + str(competencia)+'\\')

    def decompactarCmd():
        #Listando exercicios baixados
        exercicios = os.listdir(diretorio)
        for exercicio in exercicios:
            #Verificando competencias baixadas para descompactação
            competencias = os.listdir(diretorio + '\\' + exercicio)
            for competencia in competencias:
                #Acessando a pasta onde esta o arquivo para descompactar
                os.chdir(diretorio + '\\' + str(exercicio))
                #Acessando pasta de instalação do 7-Zip
                os.chdir('C:\Program Files\\7-Zip')
                #Criando a pasta para descompactar os arquivos fazendo um Split do nome de arquivo encontrado e sem a extensão.
                #os.system("7z x " + str(competencia) +' -o'+ diretorio+str(exercicio)+'\\'+str(competencia.split('.')[0]+ '.zip'))

                os.system("7z x " + str(diretorio + str(exercicio)) + ' -o' + diretorio + str(exercicio) + '\\' + str(competencia.split('.')[0]))

    def lerArquivosCompactados():

        os.chdir('C:\\Users\\richielly.carvalho\\Downloads\\SimAm')

        # specifying the zip file name
        file_name = "Layout_20072723.zip"

        # abrindo o arquivo zip no modo litura
        with ZipFile(file_name, 'r') as zip:
            # imprimir todo o conteúdo do arquivo zip
            zip.printdir()

            data = zip.read('Tabelas_Cadastrais/LeiAto.txt')
            print(str(data).split('\\r\\n'))
            # extraindo todos os arquivos
            print('Extracting all the files now...')
