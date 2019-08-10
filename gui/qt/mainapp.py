import sys
import os

from PyQt5.QtWidgets import (QApplication, QWidget, QAction, qApp, QMenu, QTextEdit, QGridLayout, 
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QDesktopWidget)
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import QFileInfo, Qt


root = QFileInfo(__file__).absolutePath()
PICTURES_DIR='/Users/public/Pictures' # change this to some directory

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.images = [entry.path for entry in os.scandir(PICTURES_DIR)]
        self.current_image = -1
        
        self.initUI()

    @property
    def next_image(self):
        if self.current_image == len(self.images) - 1:
            self.current_image = -1
        self.current_image += 1
        return self.images[self.current_image]

    @property
    def prev_image(self):
        if self.current_image == 0:
            self.current_image = len(self.images)
        self.current_image -= 1
        return self.images[self.current_image]

    def initUI(self):
        grid = QGridLayout()

        # Controls
        controls_box = QVBoxLayout()
        controls_box.addStretch(1)
        next_btn = QPushButton('Next', self)
        next_btn.clicked.connect(self.next_img)
        prev_btn = QPushButton('Prev', self)
        prev_btn.clicked.connect(self.prev_img)
        play_btn = QPushButton('Play', self)
        last_btn = QPushButton('Last', self)
        first_btn =QPushButton('First', self)

        controls_box.addWidget(next_btn)
        controls_box.addWidget(prev_btn)
        controls_box.addWidget(play_btn)
        controls_box.addWidget(last_btn)
        controls_box.addWidget(first_btn)

        # image
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap(self.next_image))
        # albums list
        albums = QHBoxLayout()
        albums.addStretch(1)

        for i in range(1, 5):
            albums.addWidget(QPushButton(f"Albamu {i}"))

        #packing
        grid.addWidget(self.img, 1, 0, 5, 1, alignment=Qt.AlignCenter)
        grid.addLayout(controls_box, 1, 1, 5, 1, alignment=Qt.AlignCenter)
        grid.addLayout(albums, 6, 0, 1, 1, alignment=Qt.AlignCenter)
        self.setLayout(grid)
        self.setWindowIcon(QIcon(f'{root}/imgs/logo.png'))
        self.setWindowTitle('Albamu ya Picha')
        self.center()
        self.show()

    def next_img(self):
        self.img.setPixmap(QPixmap(self.next_image))

    def prev_img(self):
        self.img.setPixmap(QPixmap(self.prev_image))

    def center(self):
        """
        Centers the widget on the screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() # get screen resolution and center point
        qr.moveCenter(cp) # 
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    album = App()
    sys.exit(app.exec_())
