import sys

from PyQt5.QtWidgets import (QPushButton, QMainWindow, QWidget, QVBoxLayout, QFileDialog, QApplication,
                                QCheckBox)
from PyQt5.QtGui import QIcon

from lib.utils import home_directory, save, delete

class BackupApp(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        selectButton = QPushButton("Add folder to backup", self)
        selectButton.clicked.connect(self.select_directory)
        self.vbox.addWidget(selectButton)
        self.setLayout(self.vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Backup: Select Folders')    
        self.show()
    
    def select_directory(self):
        selected_dir = QFileDialog.getExistingDirectory(self, caption="Select a directory to backup", directory=home_directory)
        # add to db
        # add to layout
        chkbox = QCheckBox(selected_dir, self)
        chkbox.stateChanged.connect(self.save)
        self.vbox.addWidget(chkbox)

    def save(self, state):
        if state == 2:
            save(self.sender().text())
        elif state == 0:
            delete(self.sender().text())
        else:
            print("There' no way to handle tristates for now")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BackupApp()
    sys.exit(app.exec_())