#important #[sg.Listbox(values=["teste","teste1","teste2"],size=(100,20),select_mode="single",key="-ListaBox-")],
#important #https://build-system.fman.io/ link do pytq5

import PySimpleGUI as sg
from random import randint

class Tela_whatsapp:
    def __init__(self):
        self.tela_inicial()


    def tela_inicial(self):
        lista_temas = ["DarkGreen4","DarkTeal9","DarkBlue14","BlueMono","BrownBlue","TealMono","DarkGrey14",'DarkBlue3']
        self.tema = lista_temas[randint(0,len(lista_temas)-1)]
        sg.theme(self.tema)
        #print(self.tema)
        frame_msg = [[sg.Multiline(size=(1980,5),enter_submits=True,key="-MSG-")]]
        self.menu = [["     file     ",["Arquivo Excel","Inserir Numero Manual"]],["Opções",["Exit"]],["Help",["Excel"]]]
        
        frame_nums = [
            [sg.Radio("Todos os Contatos","nums")],
            [sg.Radio("teste","nums")],
        ]
        self.layout = [
            [sg.Frame("Mensagem Bot",frame_msg)],
            [sg.T("Arquivo: ",size=(6,1)),sg.T("",key="-ARQV-")],
            [sg.T("")],
            [sg.B("Envia Mensagem")]

        ]
        
        
    def janela(self):
        return sg.Window("Whatsapp Bot",[[sg.Menu(self.menu),self.layout]],resizable=False,size=(600,400),finalize=True);   
    
    
    def mostra_tela(self):
        self.window = self.janela()
        while True:
            window,event,value = sg.read_all_windows()
            print(value["-MSG-"])
            if(event in [sg.WIN_CLOSED,"Exit"]):
                break
            if(event == "Arquivo Excel"):
                import pathlib
                import pandas as pd
                filename = sg.popup_get_file("Open",no_window=True)
                file = pathlib.Path(filename)
                try:
                    x = pd.read_excel(file)
                    x.to_excel("teste.xlsx",index=False)
                    
                    if self.tema in ["BlueMono","TealMono"]:
                        cor = "black"
                    else:cor = "light green"
                    
                    self.window["-ARQV-"].update(value=filename,text_color=cor)
                except:
                    self.window["-ARQV-"].update(value="[Erro] importe um arquivo Excel",text_color="#FF7700")
                    
                #self.window["-MSG-"].update(value=file.read_text())
            
        
w = Tela_whatsapp()
w.mostra_tela()