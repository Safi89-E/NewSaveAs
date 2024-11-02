from PyQt6.QtWidgets import (QApplication,QLabel,
                             QWidget, QPushButton,
                             QTextEdit,QVBoxLayout,QFileDialog)
from PyQt6.QtGui import QColor
import subprocess
import os
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

Save = QPushButton("Save as")
class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setNameFilters(["Mammad File (*.mmd)"])
        self.show()

    def accept(self):
        super(FileDialog, self).accept()
    
FileName = QTextEdit()
#FileName.setGeometry(50,50,300,10)
FileName.label = QLabel("File name:")
FileName.setTextColor(QColor("blue"))
FileName.setPlaceholderText("Write your file name here...")

FilePath =QTextEdit()
FilePath.label = QLabel("File path:")

FilePath.setTextColor(QColor("red"))
FilePath.setPlaceholderText("Write your file path here...")
Guide = QTextEdit()
Guide.setStyleSheet("QTextEdit { background-color: gray; color: white; }")
layout.addWidget(Save)
layout.addWidget(Guide)
layout.addWidget(FileName.label)
layout.addWidget(FileName)
layout.addWidget(FilePath.label)
layout.addWidget(FilePath)

Guide.setReadOnly(True)
window.setWindowTitle("Save as")


window.setLayout(layout)
#def read():
    #with open("empty.py", 'r') as file:  
            #content = file.read()
a=FileDialog(window)

def Save_as():
    counter = 1
    #content = read()
    File_name = FileName.toPlainText()
    File_path = FilePath.toPlainText()
    if os.path.exists(f"newfile{counter}.txt"):
            counter += 1
            with open(f"newfile{counter}.txt", "w") as f:
             f.write("Helo!!")
            
    else:
            with open(f"newfile{counter}.txt", "w") as f:
             f.write("Helo!!")
    '''if os.path.isfile(File_name):
            Guide.setText(f"There is {File_name}")
        else:
            os.path.dirname(File_path)
            with open(f"{File_name}.txt", "w") as f:
                f.write("defad")
'''

        


Save.clicked.connect(Save_as)


window.show()
app.exec()
