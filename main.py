from PyQt5 import QtCore,  QtWidgets
import PyQt5
from PyQt5.QtWebEngineWidgets import QWebEnginePage

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget{\n"
" border:4px solid rgb(45, 45, 45);\n"
" border-radius:20px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
" background-color:rgb(20,20,20);\n"
" border-top-left-radius:20px;\n"
" border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
" background-color:rgba(0,0,0,0);\n"
" color:rgb(144, 144, 144);\n"
" font:bold;\n"
" font-size:15px;\n"
" font-family:entypro;\n"
"}\n"
"QPushButton:hover{\n"
" color:rgb(142, 176, 27);\n"
"}\n"
"QPushButton:pressed{\n"
" padding-top:5px;\n"
" padding-left:5px;\n"
"color:rgb(91, 88, 53);\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(15, 15))
        self.label_5.setMaximumSize(QtCore.QSize(15, 15))
        self.label_5.setStyleSheet("background-color:rgb(142,176,27);\n"
"border-radius:7px;\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(15, 15))
        self.label_3.setMaximumSize(QtCore.QSize(15, 15))
        self.label_3.setStyleSheet("background-color:rgb(45,45,45);\n"
"border-radius:7px;\n"
"\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(15, 15))
        self.label_6.setMaximumSize(QtCore.QSize(15, 15))
        self.label_6.setStyleSheet("background-color:rgb(255,0,0);\n"
"border:4px solid rgb(45,45, 45);\n"
"border-radius:7px;\n"
"\n"
"\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(182, 182, 182);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("background-color:rgb(31, 31, 31);\n"
"border-radius:5px;\n"
"color:rgb(144, 144, 144);\n"
"padding-left:5px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.WebEngineView = QWebEngineView(self.widget)
        self.WebEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
#         self.label.setStyleSheet("background-color:rgb(182, 182, 182);\n"
# "")
        # self.label.setText("")
        self.WebEngineView.setObjectName("WebEngineView")
        self.verticalLayout_2.addWidget(self.WebEngineView)
        
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("background-color:rgb(235, 129, 133);\n"
"border-bottom-left-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"color:rgb(144,144,144);\n"
"\n"
"\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "RainbowBroswer"))
        self.pushButton_3.setText(_translate("Form", "-"))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "X"))
        self.pushButton_6.setText(_translate("Form", ""))
        self.pushButton_5.setText(_translate("Form", ""))
        self.pushButton_4.setText(_translate("Form", " ⟳"))
        self.lineEdit.setText(_translate("Form", "https://github.com/AsjadOooO"))
        self.label_2.setText(_translate("Form", "Developed by Asjad"))


class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moWidget, self).__init__()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class browserApp(moWidget, Ui_Form):
      def __init__(self):
          super(browserApp, self).__init__()
          self.setupUi(self)
          self.pushButton.clicked.connect(sys.exit)#Exit
          self.pushButton_2.clicked.connect(self.winShowMaximized)#Maximized
          self.pushButton_3.clicked.connect(self.showMinimized)#Minimized
          self.lineEdit.returnPressed.connect(self.load)
          self.pushButton_4.clicked.connect(self.reload) #RELOAD
          self.pushButton_5.clicked.connect(self.forward) #FORWARD ARROW RIGHT 
          self.pushButton_6.clicked.connect(self.backward) #Backward #Arrow LEFT WORKING

      def load(self):
         url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
         if url.isValid():
             self.WebEngineView.load(url)

      def winShowMaximized(self):
          if self.pushButton_2.isChecked():
              self.showMaximized()
          else:
               self.showNormal()   
      def backward(self):
          self.WebEngineView.page().triggerAction(QWebEnginePage.Back)

      def forward(self):
          self.WebEngineView.page().triggerAction(QWebEnginePage.Forward)
      def reload(self):
          self.WebEngineView.page().triggerAction(QWebEnginePage.Reload)    
       


    #   def winShowMaximized(self):
    #     if self.pushButton_2.isChecked():
    #         self.showMaximized
    #     else:
    #         self.showNormal()


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = browserApp()
        # ui = Ui_Form()
        # ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())          




# sroot = Tk()
# sroot.overrideredirect(1)

# sroot.minsize(height=388, width=520)

# sroot.title("Splash window")

# sroot.configure()

# spath = 'test.gif'

# simg = ImageTk.PhotoImage(Image.open(spath))

# my = Label(sroot, image=simg)

# my.image = simg

# my.place(x=-2, y=-1.5)

# Frame(sroot, height=500, width=900, bg='black').place(x=520, y=500)
