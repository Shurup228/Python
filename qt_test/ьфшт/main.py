import pdb
from PyQt5.QtGui import QWindow, QSurfaceFormat, QOpenGLContext, QOpenGLWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor
import sys


class MyWindow(QOpenGLWindow):
    color = QColor().fromRgb(50, 70, 90)
    a = (color.redF(), color.greenF(), color.blueF(), color.alphaF())

    def __init__(self):
        super().__init__()
        self.o_format = QSurfaceFormat()
        self.o_format.setVersion(2, 1)
        self.o_format.setProfile(QSurfaceFormat.CoreProfile)
        self.setFormat(self.o_format)
        self.context = QOpenGLContext()
        self.context.setFormat(self.o_format)
        self.context.makeCurrent(self)
        self.context.create()

        self.createUI()

    def createUI(self):

        self.show()

    def initializeGL(self):
        self.gl = self.context.versionFunctions()
        self.gl.initializeOpenGLFunctions()
        pdb.set_trace()
        self.gl.glClearColor(*self.a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MyWindow()
    sys.exit(app.exec_())
