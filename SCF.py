from tkinter import *
from functools import partial


def chamar_tela_cadastro(tela_anterior):
	tela_cadastro = Tk()
	tela_cadastro.geometry("500x300+300+200")
	tela_cadastro.title("Cadastro") 
	lb = Label (tela_cadastro, text="O que você deseja cadastrar?", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	bt_cadastrar_colaborador = Button (tela_cadastro, width=20, text="Colaborador", bg="white", command=partial(chamar_tela_cadastro_colaborador, tela_cadastro)).pack()
	bt_cadastrar_laboratorio = Button (tela_cadastro, width=20, text="Laboratório", bg="white", command=partial(chamar_tela_cadastro_laboratorio,tela_cadastro)).pack()
	bt_voltar = Button (tela_cadastro, width=10, text="Voltar", bg="white", command=partial(chamar_tela_inicial, tela_cadastro)).pack(side=BOTTOM, anchor=SW)
	tela_anterior.destroy()

#def cadastrar_colaborador(tela_anterior):
	
def chamar_tela_cadastro_colaborador(tela_anterior):
	tela_cadastro_colaborador = Tk()
	tela_cadastro_colaborador.geometry("500x600+300+100")
	tela_cadastro_colaborador.title("Cadastro") 
	lb = Label(tela_cadastro_colaborador, text="Informe os dados do colaborador", fg="orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	
	lb_nome = Label(tela_cadastro_colaborador, text="Nome:", bg="white")
	lb_nome.place(x=110, y=130)
	entrada_nome = Entry(tela_cadastro_colaborador, width=30, bg="white")
	entrada_nome.place(x=110, y=150)
	
	lb_dt_nasc = Label(tela_cadastro_colaborador, text="Data de Nascimento:", bg="white")
	lb_dt_nasc.place(x=110, y=180)
	entrada_dt_nasc = Entry(tela_cadastro_colaborador, width=30, bg="white")
	entrada_dt_nasc.place(x=110, y=200)

	lb_lab = Label(tela_cadastro_colaborador, text="Laboratorio:", bg="white")
	lb_lab.place(x=110, y=230)
	entrada_lab = Entry(tela_cadastro_colaborador, width=30, bg="white")
	entrada_lab.place(x=110, y=250)	

	
	



	bt_voltar = Button (tela_cadastro_colaborador, width=10, text="Voltar", bg="white", command=partial(chamar_tela_cadastro, tela_cadastro_colaborador)).pack(side=BOTTOM, anchor=SW)
	bt_ok = Button(tela_cadastro_colaborador, width=10, bg="white", text="Cadastrar", command=partial(cadastrar_colaborador, tela_cadastro_colaborador)).place(x=275, y=500)
	tela_anterior.destroy()

def chamar_tela_cadastro_laboratorio(tela_anterior):
	tela_cadastro_laboratorio = Tk()
	tela_cadastro_laboratorio.geometry("500x300+300+200")
	tela_cadastro_laboratorio.title("Cadastro") 
	lb = Label(tela_cadastro_laboratorio, text="Informe os dados do laboratório", fg="orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	lb_nome = Label(tela_cadastro_laboratorio, text="Nome:", bg="white").place(x=110, y=130)
	entrada_nome = Entry(tela_cadastro_laboratorio, width=30, bg="white").place(x=110, y=150)
	bt_voltar = Button (tela_cadastro_laboratorio, width=10, text="Voltar", bg="white", command=partial(chamar_tela_cadastro, tela_cadastro_laboratorio)).pack(side=BOTTOM, anchor=SW)
	tela_anterior.destroy()

def chamar_tela_consulta(tela_anterior):
	tela_consulta = Tk()
	tela_consulta.geometry("500x300+300+200")
	tela_consulta.title("Consulta") 
	lb = Label (tela_consulta, text="O que você deseja consultar?", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	bt_consultar_colaborador = Button (tela_consulta, width=20, text="Colaborador", bg="white").pack() 
	bt_consultar_laboratorio = Button (tela_consulta, width=20, text="Laboratório", bg="white").pack()
	bt_voltar = Button (tela_consulta, width=10, text="Voltar", bg="white", command=partial(chamar_tela_inicial, tela_consulta)).pack(side=BOTTOM, anchor=SW)
	tela_anterior.destroy()


def escolhe_tela(tela_anterior, login):
	if login.get() == "admin":
		chamar_tela_inicial(tela_anterior)
	

def chamar_tela_login():
	tela_login = Tk() 
	tela_login.geometry("500x300+300+200") #dimensoes da janela --> Largura x Altura + DistanciaDaMargemEsquerda + DistanciaDaMargemSuperior
	tela_login.title("HUB - Tecnologia e Inovação") #título da janela
	lb_inicial = Label (tela_login, text="Sistema de Controle de Frequência", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50) #criando rótulo
	lb_login = Label(tela_login, text="Login:", bg="white").place(x=110, y=130)
	entrada_login = Entry(tela_login, width=30, bg="white")
	entrada_login.place(x=110, y=150)
	lb_senha = Label(tela_login, text="Senha:", bg="white").place(x=110, y=180)
	entrada_senha = Entry(tela_login, width=30, bg="white")
	entrada_senha.place(x=110, y=200)
	bt_logar = Button(tela_login, width=10, bg="white", text="Login", command=partial(escolhe_tela, tela_login, entrada_login)).place(x=275, y=230)
	tela_login.mainloop()

	
def chamar_tela_inicial(tela_anterior):
	tela_inicial = Tk() #criacao de uma janela - instancia de Tk
	tela_inicial.geometry("500x300+300+200") #dimensoes da janela --> Largura x Altura + DistanciaDaMargemEsquerda + DistanciaDaMargemSuperior
	tela_inicial.title("HUB - Tecnologia e Inovação") #título da janela
	lb_inicial = Label (tela_inicial, text="Sistema de Controle de Frequência", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50) #criando rótulo
	bt_cadastrar = Button (tela_inicial, width=20, text="Cadastrar", command = partial(chamar_tela_cadastro, tela_inicial), bg="white").pack() #criando botao "cadastrar"
	bt_consultar = Button (tela_inicial, width=20, text="Consultar", command = partial(chamar_tela_consulta, tela_inicial), bg="white").pack() #criando botao "Consultar" 	
	tela_anterior.destroy()



if __name__ == "__main__":

	chamar_tela_login()


