from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout)

from PyQt5.QtCore import pyqtSlot
 
import sys
 
class Dialog(QDialog):
 
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.button = QPushButton('Enter', self)
        self.button.clicked.connect(self.on_click)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.button)
        self.setLayout(mainLayout)
 
        self.setWindowTitle("Python Project")
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Enter The Fields Below")
        self.layout = QFormLayout()
        self.csvbox = QLineEdit()
        self.namebox = QLineEdit()
        self.emailbox = QLineEdit()
        self.subjectbox = QLineEdit()
        self.messagebox = QLineEdit()

        self.layout.addRow(QLabel("CSV File:"),self.csvbox)
        self.layout.addRow(QLabel("Name:"),self.namebox)
        self.layout.addRow(QLabel("Email:"), self.emailbox)
        self.layout.addRow(QLabel("Subject:"), self.subjectbox)
        self.layout.addRow(QLabel("Message:"), self.messagebox)
        self.formGroupBox.setLayout(self.layout)
 

    @pyqtSlot()
    def on_click(self):
        csv = self.csvbox.text
        csv = str(csv)

        if "<built-" in csv:
            name = self.namebox.text
            email = self.emailbox.text
        else:
            print(" ")
            #call csv parser
            
        
        subject = self.subjectbox.text
        message = self.messagebox.text

        self.namebox.clear()
        self.emailbox.clear()
        self.csvbox.clear()
        
        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
