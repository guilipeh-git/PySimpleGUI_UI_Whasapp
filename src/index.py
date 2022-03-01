import PySimpleGUI as sg
from random import randint
import time

class Tela_Whatsapp:
    def __init__(self):
        #criando layout
        lista_tema = ["DarkTeal9","DarkBlue14","BlueMono","BrownBlue","TealMono","DarkGrey14",'DarkBlue3']
        
        tema = lista_tema[randint(0,len(lista_tema)-1)]
        sg.theme(tema)
        #print(tema)
        self.nome_janela1 = "Whatsapp Bot"
        self.menu = [["Menu",["Help","Contat","---","Exit"]]] 
        
        campo_msg = [
            [sg.Text(">Arquivo<",key="-aqv-")],
            [sg.Multiline("",size=(1980,10),key="-msg-")],
            [sg.T("",key="-teste-")]
            ]
        
        self.layout = [
            [sg.Frame("Mensagem Bot",campo_msg)]
            ]
    
    def criar_janela(self):
        #janela
        return sg.Window(self.nome_janela1,
                         layout=[[sg.Menu(self.menu),self.layout]],size=(800,500),finalize=True,
                         resizable=True,return_keyboard_events=True)
    
    def new_file(self):
        import pathlib
        filename = sg.popup_get_file("Open",no_window=True) # abre pasta de subir arquivo no windows
        file = pathlib.Path(filename)
        try:
            self.window["-msg-"].update(value=file.read_text())
        except:
            file =">Arquivo<"
        return file
    
    
    def start(self):
        self.window = self.criar_janela()
        self.window.maximize() 
        while True:
            event,value = self.window.read()
            
            print(event)
            if(event == "Help"):
                self.window['-teste-'].update(value="Mensagem Não pode esta vazio",text_color="red") # modifica meu texto na tela
                #window["-msg-"].update(visible=False) # deixa input invisivel
                self.window["-aqv-"].update(value=self.new_file())
            if(event == sg.WIN_CLOSED or event == "Exit"):
                break
            if(event == "Contat"):
                sg.popup("Autor: Guilherme Felipe \nContato: 62998080215",title="Contato")


a = Tela_Whatsapp()
a.start()


