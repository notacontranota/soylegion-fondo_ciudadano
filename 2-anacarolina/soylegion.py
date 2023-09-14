#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from soyventana import *
from soyabout import *
import soypartitura, soycompases
#import zamba
from random import randint
import os, platform
import subprocess
import pygame
import partitura, recursos

class SoyAbout(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.about = Ui_About()
        self.about.setupUi(self)

class SoyVentana(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionAcerca_de.triggered.connect(self.acercade)
        self.action_Ver_reglas_del_juego.triggered.connect(self.verReglas)
        self.actionVer_Plantilla.triggered.connect(self.verPlantilla)
        
        self.botonDados.clicked.connect(self.lanzadados)
        self.botonPlay.clicked.connect(self.tocar)
        self.botonStop.clicked.connect(self.stop)
        self.botonPDF.clicked.connect(self.ver)
        self.botonComponer.clicked.connect(self.compone)

        self.compas_01.valueChanged.connect(self.compas_01_changed)
        self.compas_02.valueChanged.connect(self.compas_02_changed)
        self.compas_03.valueChanged.connect(self.compas_03_changed)
        self.compas_04.valueChanged.connect(self.compas_04_changed)
        self.compas_05.valueChanged.connect(self.compas_05_changed)
        self.compas_06.valueChanged.connect(self.compas_06_changed)
        self.compas_07.valueChanged.connect(self.compas_07_changed)
        self.compas_08.valueChanged.connect(self.compas_08_changed)
        self.compas_09.valueChanged.connect(self.compas_09_changed)
        self.compas_10.valueChanged.connect(self.compas_10_changed)
        self.compas_11.valueChanged.connect(self.compas_11_changed)
        self.compas_12.valueChanged.connect(self.compas_12_changed)
        self.compas_13.valueChanged.connect(self.compas_13_changed)
        self.compas_14.valueChanged.connect(self.compas_14_changed)
        self.compas_15.valueChanged.connect(self.compas_15_changed)
        self.compas_16.valueChanged.connect(self.compas_16_changed)
        

        self.dados = []
        self.audio = pygame.mixer
        self.audio.init(48000, -16, 2, 1024)

        self.runLilypond = QtCore.QProcess(self)
        self.runLilypond.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.runLilypond.readyRead.connect(self.escribeSalidaLily)
        self.runLilypond.finished.connect(self.muestraPNG)

        self.botonComponer.setEnabled(True)
        
        #lanza dados y compone al iniciar el programa
        self.lanzadados()
        self.compone()

    def lanzadados(self):
        self.dados = []
        self.salidaTexto.setPlainText("lanzamos dados...")
        for c in range(len(soycompases.compases)):
            self.dados.append(randint(1,6))
        #print (self.dados)
        self.compas_01.setProperty("value", self.dados[0])
        self.compas_02.setProperty("value", self.dados[1])
        self.compas_03.setProperty("value", self.dados[2])
        self.compas_04.setProperty("value", self.dados[3])
        self.compas_05.setProperty("value", self.dados[4])
        self.compas_06.setProperty("value", self.dados[5])
        self.compas_07.setProperty("value", self.dados[6])
        self.compas_08.setProperty("value", self.dados[7])
        self.compas_09.setProperty("value", self.dados[8])
        self.compas_10.setProperty("value", self.dados[9])
        self.compas_11.setProperty("value", self.dados[10])
        self.compas_12.setProperty("value", self.dados[11])
        self.compas_13.setProperty("value", self.dados[12])
        self.compas_14.setProperty("value", self.dados[13])
        self.compas_15.setProperty("value", self.dados[14])
        self.compas_16.setProperty("value", self.dados[15])

    def compas_01_changed(self):
        self.dados[0] = self.compas_01.value()

    def compas_02_changed(self):
        self.dados[1] = self.compas_02.value()

    def compas_03_changed(self):
        self.dados[2] = self.compas_03.value()

    def compas_04_changed(self):
        self.dados[3] = self.compas_04.value()

    def compas_05_changed(self):
        self.dados[4] = self.compas_05.value()

    def compas_06_changed(self):
        self.dados[5] = self.compas_06.value()

    def compas_07_changed(self):
        self.dados[6] = self.compas_07.value()

    def compas_08_changed(self):
        self.dados[7] = self.compas_08.value()

    def compas_09_changed(self):
        self.dados[8] = self.compas_09.value()

    def compas_10_changed(self):
        self.dados[9] = self.compas_10.value()

    def compas_11_changed(self):
        self.dados[10] = self.compas_11.value()

    def compas_12_changed(self):
        self.dados[11] = self.compas_12.value()

    def compas_13_changed(self):
        self.dados[12] = self.compas_13.value()

    def compas_14_changed(self):
        self.dados[13] = self.compas_14.value()

    def compas_15_changed(self):
        self.dados[14] = self.compas_15.value()

    def compas_16_changed(self):
        self.dados[15] = self.compas_16.value()

    def escribeSalidaLily(self):
        try:
            self.textosalida = str(self.runLilypond.readAll(),"utf-8")
            self.escribeSalidas(self.textosalida)
        except UnicodeDecodeError:
            pass
        
    def escribeSalidas(self,texto):
        cursor = self.salidaTexto.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(texto)
        self.salidaTexto.ensureCursorVisible()


    def compone(self):
        #desactiva botones y saca PNG
        self.salidaTexto.clear()
        self.label.setPixmap(QtGui.QPixmap(None))
        self.label_2.setPixmap(QtGui.QPixmap(None))
        self.label_3.setPixmap(QtGui.QPixmap(None))
        self.label_4.setPixmap(QtGui.QPixmap(None))
        self.botonPlay.setEnabled(False)
        self.botonPDF.setEnabled(False)
        self.botonComponer.setEnabled(False)
        partitura = soypartitura.partitura(self.dados)
        #Escribiendo archivo .ly
        lilypond = open("soylegion.ly",'w')
        for a in range(len(partitura)):
        	lilypond.write (partitura[a])
        lilypond.close()
        #Genera MIDI, PNG y PDF a través de lilypond
        self.runLilypond.start("lilypond",['-dno-point-and-click', '--format=png', '--format=pdf', 'soylegion.ly'])

    def muestraPNG(self):    
        self.label.setPixmap(QtGui.QPixmap(os.getcwd() + '/soylegion-page1.png'))
        self.label_2.setPixmap(QtGui.QPixmap(os.getcwd() + '/soylegion-page2.png'))
        self.label_3.setPixmap(QtGui.QPixmap(os.getcwd() + '/soylegion-page3.png'))
        self.label_4.setPixmap(QtGui.QPixmap(os.getcwd() + '/soylegion-page4.png'))
        #Activa botones
        self.botonPlay.setEnabled(True)
        self.botonPDF.setEnabled(True)
        self.botonComponer.setEnabled(True)
        #Inicializa PyGame y carga el archivo de audio
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            self.audio.music.load("soylegion.midi")
        elif platform.system() == 'Windows':
            self.audio.music.load("soylegion.mid")
        self.stop()
        
    def tocar(self):
        self.botonStop.setEnabled(True)
        self.botonPlay.setEnabled(False)
        self.audio.music.play()



    def stop(self):
        self.botonStop.setEnabled(False)
        self.botonPlay.setEnabled(True)
        self.audio.music.stop()

    def ver(self):
        self.abrirArchivo('soylegion.pdf')

    def verPlantilla(self):
        self.abrirArchivo('partitura/SoyLegion-plantilla.pdf')

    def verReglas(self):
        self.abrirArchivo('partitura/SoyLegion-reglas.pdf')
    
    def abrirArchivo(self,archivo):
        self.abreArchivo = QtCore.QProcess(self)
        if platform.system() == 'Linux':
            self.abreArchivo.start("xdg-open", [archivo])
        elif platform.system() == 'Darwin':
            self.abreArchivo.start("open", [archivo])
        elif platform.system() == 'Windows':
            # self.abreArchivo.startDetached("cmd.exe /k " + archivo)
            subprocess.call(["start", archivo], shell=True)
    
    def acercade(self):
        SoyAbout().exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    SoyLegion = SoyVentana()
    SoyLegion.show()
    app.exec_()
