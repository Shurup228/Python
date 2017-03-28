import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QSurfaceFormat, QOpenGLContext, QColor, QOpenGLWindow


class Window(QOpenGLWindow):
    grey = QColor().fromRgb(211, 211, 211)
    a = (grey.redF(), grey.greenF(), grey.blueF(), grey.alphaF())

    def __init__(self):
        super().__init__()

        f = QSurfaceFormat()
        f.setVersion(2, 0)
        f.setProfile(f.CoreProfile)
        f.setSamples(4)
        self.setFormat(f)

        self.c = QOpenGLContext()
        self.c.setFormat(f)
        self.c.makeCurrent(self)

        self.initUI()

    def initializeGL(self):
        self.gl = self.c.versionFunctions()
        self.gl.initializeOpenGLFunctions()

    def paintGL(self):

        self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)
        self.gl.glClearColor(*self.a)

    def resizeGL(self, *args):
        pass

    def initUI(self):
        self.showMaximized()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())