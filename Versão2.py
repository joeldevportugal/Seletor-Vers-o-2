# importar as Bibliotecas a Utilizar ----------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pyperclip
# --------------------------------------------------------------------------------------------

# Implementar O backend ----------------------------------------------------------------------- 

# função Actualizar cor que Liga com os Sacales 
def atualiza_cor(event=None):
    # Obtém os valores dos sliders
    r = SVermelho.get()
    g = SVerde.get()
    b = SAzul.get()
    # Formata como uma string hexadecimal
    hex_color = f'#{r:02x}{g:02x}{b:02x}'
    # Atualiza o background do Label e o conteúdo da Entry
    Lcor.config(bg=hex_color)
    Ehexa.delete(0, 'end')
    Ehexa.insert(0, hex_color)

# função Copiar para Ligar com o BtnCopiar
def copiar_hex():
    hex_color = Ehexa.get()
    pyperclip.copy(hex_color)
    messagebox.showinfo('Copiar', 'Codigo Copiado com Sucesso para a Aréa de Traferençia!')

# função Limpar Para Ligar ao btn Limpar
def Limpar():
     # Define a cor preta diretamente
    SVermelho.set(0)
    SVerde.set(0)
    SAzul.set(0)
    atualiza_cor()
    # Limpa o conteúdo da entrada Ehexa
    Ehexa.delete(0, 'end')
    Ehexa.insert(0, 'hex_color')
    Lcor.config(bg='black')
    messagebox.showinfo('LIMPAR','Seus dados Foram Limpos Com Sucesso')

# Função Sair para Ligar Ao btnSair
def Sair ():
    resposta=messagebox.askyesno('SAIR', 'Deseja Sair do Programa ?')
    if resposta: 
        Janela.quit()

#----------------------------------------------------------------------------------------------
#defenir as cores a Usar-----------------------------------------------------------------------
co0 = "#000000" # cor preta
co1 = "#ffffff" # cor Branca
co2 = "#fbcdb5"# cor Laranja
co3 = "#fcfcf2" # amarelo Claro
#----------------------------------------------------------------------------------------------
Janela = Tk()
Janela.geometry('800x300+100+100')
Janela.title('Selector V2 Dev Joel Portugal ')
Janela.resizable(False, False)
Janela.config(bg=co1)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Python tkinter\\Selector versões\\Versão 2\\icon\\icon.ico')
# implementar O fronte end ---------------------------------------------------------------------

#criar O Label  Lcor 
Lcor = Label(Janela, bg=co0, width=30, height=15)
Lcor.place(x=10, y=10)

# criar Label controle e Secales
Lvermelho = Label(Janela, text='Vermelho', font=('arial 12'), bg=co1)
Lvermelho.place(x=230, y=10)
SVermelho = Scale(Janela, orient='horizontal', bg=co1, length=545, from_=0, to=255, command=atualiza_cor)
SVermelho.place(x=230, y=35)
Lverde = Label(Janela, text='Verde', font=('arial 12'), bg=co1)
Lverde.place(x=230, y=95)
SVerde = Scale(Janela, orient='horizontal', bg=co1, length=545, from_=0, to=255, command=atualiza_cor)
SVerde.place(x=230, y=120)
LAzul = Label(Janela, text='Azul', font=('arial 12'), bg=co1)
LAzul.place(x=230, y=175)
SAzul = Scale(Janela, orient='horizontal', bg=co1, length=545, from_=0, to=255, command=atualiza_cor)
SAzul.place(x=230, y=200)

# criar a Entry para Exbir a cor em Exadecimal
Ehexa = Entry(Janela, font=('arial 14'), bg=co3, width=10)
Ehexa.place(x=10, y=255)

# criar Os botões Copiar , Limpar e Sair
BtnCopiar = Button(Janela, text='Copiar', font=('arial 12'), relief=RAISED, overrelief=RIDGE, bg=co2, command=copiar_hex)
BtnCopiar.place(x=130, y=250)
BtnLimpar = Button(Janela, text='Limpar', font=('arial 12'), relief=RAISED, overrelief=RIDGE, bg=co2, command=Limpar)
BtnLimpar.place(x=195, y=250)
BtnFechar = Button(Janela, text='Fechar Aplicação', font=('arial 12'), relief=RAISED, overrelief=RIDGE, bg=co2, command=Sair)
BtnFechar.place(x=260, y=250)

#--------------------------------------------------------------------------------------------------
Janela.mainloop()