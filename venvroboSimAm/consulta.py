# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
import time
from pacote import Pacote
from arquivo import Arquivo

import configparser
cfg = configparser.ConfigParser()
cfg.read('cfg.ini')

browser = webdriver.Chrome(executable_path=r"C:\Users\richielly.carvalho\PycharmProjects\arquivosSimAmRobo\venvroboSimAm\chromedriver.exe")

class Consulta:
    def loginSimAm(usuario,senha):
        try:

            #global browser

            browser.get("https://servicos.tce.pr.gov.br/tcepr/municipal/simam/Paginas/Consulta.aspx")
            username = browser.find_element_by_id("Login")
            password = browser.find_element_by_id("Senha")
            username.send_keys(usuario)
            password.send_keys(senha)
            time.sleep(5)
            login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
            login_attempt.submit()
            Arquivo.registrar_log(" ########## Acesso realizado com sucesso em: " + datetime.now().strftime('%d/%m/%Y %H:%M' +" ##########"))
            return True
        except: Arquivo.registrar_log("Problema ao tentar fazer acesso em: " + datetime.now().strftime('%d/%m/%Y %H:%M'))
        return False
#browser.find_element_by_id('ContentPlaceHolder1_btnFechar').click()

    def rota(exercicio, competencia):

        try:
            global browser
            browser.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlTipo']/option[text()='Movimento Mês']").click()
            time.sleep(2)
            browser.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlAno']/option[text()="+str(exercicio)+"]").click()
            time.sleep(1)
            browser.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlMes']/option[text()='"+competencia+"']").click()
            time.sleep(1)

            checkboxes = browser.find_elements_by_xpath("//*[@type='checkbox']")

            for marcar in checkboxes:
                marcar.click()
                time.sleep(1)
            time.sleep(3)
            Consulta.processar(exercicio,competencia)

            return True

        except: Arquivo.registrar_log("Problema ao tentar selecionar arquivos: " + datetime.now().strftime('%d/%m/%Y %H:%M'))

    def processar(exercicio, competencia):
        try:
            global browser
            browser.find_element_by_id('ContentPlaceHolder1_btnProcessar').click()
            Arquivo.registrar_log("Processamento em andamento (" +competencia+"/"+str(exercicio)+ ")iniciado em: " + datetime.now().strftime('%d/%m/%Y %H:%M'))
            print("Processamento em andamento (" +competencia+"/"+str(exercicio)+ ")iniciado em: " + datetime.now().strftime('%d/%m/%Y %H:%M'))
            Consulta.download(exercicio, competencia)

            return True
        except: return False

    def liberarDownload(exercicio, competencia):
        global browser
        time.sleep(7)
        browser.find_element_by_id('ContentPlaceHolder1_btnAtualizarPagina').click()
        try:
            browser.find_element_by_id('ContentPlaceHolder1_btnDownload').click()
            time.sleep(3)
            Arquivo.renomear_arquivo(competencia,exercicio)
            # Pacote.decompactarCmd()
            # time.sleep(5)
            # Arquivo.deletarZip()
        except: return True
        return False

    def download(exercicio, competencia):
        while(Consulta.liberarDownload(exercicio, competencia)):
            time.sleep(6)
        Arquivo.registrar_log("Download (" +competencia+"/"+str(exercicio)+ ") iniciado em: "+datetime.now().strftime('%d/%m/%Y %H:%M'))
        print("Download (" +competencia+"/"+str(exercicio)+ ") iniciado em: "+datetime.now().strftime('%d/%m/%Y %H:%M'))

    def finalizarNavegador():
        global browser
        print("Navegador finalizado em: "+datetime.now().strftime('%d/%m/%Y %H:%M'))
        browser.close()
        Arquivo.registrar_log("Navegador finalizado em: "+datetime.now().strftime('%d/%m/%Y %H:%M'))

    def start():
        #global browser
        #usuario = "03158339986"
        #senha = "almir1"
        # usuario = "00029032962"  #Guamiranga
        # senha = "M000cont"
        #usuario = "89997425987" #Municipio Capitão Leonidas / Municipio Santa Lucia
        #senha = "461928"

        # usuario = "02929011947"  # Castelo Branco
        # senha = "cristian0556"

        #usuario = "08651173903"  # Samae Japurá
        #senha = "Feer60485"

        # usuario = "70954755987" #Terra Rica Samae
        # senha = "5x36d48y"

        exercicios = [2022]
        # exercicios = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

        competencias = ['Abertura de Exercício','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto',
                    'Setembro','Outubro','Novembro','Dezembro','Encerramento de Exercício']

        logado = Consulta.loginSimAm(cfg['Camara_Santa_Mariana']['usuario'],cfg['Camara_Santa_Mariana']['senha'])
        time.sleep(7)

        for exercicio in exercicios:
            for competencia in competencias:
                Consulta.rota(exercicio,competencia)

        Arquivo.registrar_log(" ########## Processo finalizado em: " + datetime.now().strftime('%d/%m/%Y %H:%M' + " ##########"))
        Consulta.finalizarNavegador()


Consulta.start()
