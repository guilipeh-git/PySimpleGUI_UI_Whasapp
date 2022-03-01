#https://www.youtube.com/watch?v=zGHgiIiFiMo&list=PLwsAoT89dh3qJ8JcprQ8AuHY8AGasvx4G&index=8

from PyQt5 import uic,QtWidgets
import campo_msg as msg_arqv
class TelaUIWhatsapp:
    def __init__(self):

        self.app=QtWidgets.QApplication([])
        self.form = uic.loadUi("src/tela.ui")
        
        self.main() #corpo 
        
        self.criar_janela()# fim 
        
    def criar_janela(self):
        self.form.show()
        self.app.exec()

    def start(self):
        texto = self.form.textEdit.toPlainText() # pega valor do textEdit
        print(texto)
    
    def message1(self):
        self.form.textEdit.setText(msg_arqv.message_1)
    
    def message2(self):
        self.form.textEdit.setText(msg_arqv.message_2)
    
    def message3(self):
        self.form.textEdit.setText(msg_arqv.message_3)
    
    
    def main(self):
        self.form.pushButton_1.clicked.connect(self.message1)
        self.form.pushButton_2.clicked.connect(self.message2)
        self.form.pushButton_3.clicked.connect(self.message3)
        self.form.Enviar.clicked.connect(self.start)
        
        
        
        
        
        
        
window = TelaUIWhatsapp()
