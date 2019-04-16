#/usr/bin/python
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QMessageBox)

from PyQt5.QtCore import pyqtSlot
 
import sys

import csv_parser as parse

import webInteractive as web
 
class Dialog(QDialog):
 
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.button = QPushButton('Enter', self)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)
        self.setLayout(mainLayout)
 
        self.setWindowTitle("Python Project")
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Enter The Fields Below")
        self.layout = QFormLayout()
        self.csvbox = QLineEdit()
        self.csvbox.clear()
        self.subjectbox = QLineEdit(self)
        self.messagebox = QLineEdit(self)

        self.layout.addRow(QLabel("CSV File:"),self.csvbox)
        self.layout.addRow(QLabel("Subject:"), self.subjectbox)
        self.layout.addRow(QLabel("Message:"), self.messagebox)
        self.formGroupBox.setLayout(self.layout)
 

    @pyqtSlot()
    def on_click(self):
        csv = self.csvbox.text()
        subject = self.subjectbox.text()
        message = self.messagebox.text()
        subject = str(subject)
        csv = str(csv)
        message = str(message)

        if ".csv" not in csv:
            QMessageBox.question(self, 'Error!', "Please Enter A Valid CSV", QMessageBox.Ok, QMessageBox.Ok)
            return 
        if subject == "":
            QMessageBox.question(self, 'Error!', "Please Enter A Subject", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        if message == "":
            QMessageBox.question(self, 'Error!', "Please Enter A Message", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        nameEmail = parse.csv_parser(csv)
        web.webInteractive(subject,message,nameEmail)
        self.csvbox.clear()
        self.subjectbox.clear()
        self.messagebox.clear()
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
