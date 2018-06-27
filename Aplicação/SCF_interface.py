from SCF_backend import *
from functools import partial

def chamar_tela_cadastro(tela_anterior):
	tela_cadastro = Tk()
	tela_cadastro["bg"] = "white"
	tela_cadastro.geometry("500x300+300+200")
	tela_cadastro.title("Cadastro") 
	lb = Label (tela_cadastro, text="O que você deseja cadastrar?", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	bt_cadastrar_colaborador = Button (tela_cadastro, width=20, text="Colaborador", bg="white", command=partial(chamar_tela_cadastro_colaborador, tela_cadastro)).pack(pady=3)
	bt_cadastrar_laboratorio = Button (tela_cadastro, width=20, text="Laboratório", bg="white", command=partial(chamar_tela_cadastro_laboratorio,tela_cadastro)).pack(pady=3)
	bt_voltar = Button (tela_cadastro, width=10, text="Voltar", bg="white", command=partial(chamar_tela_inicial, tela_cadastro)).pack(side=BOTTOM, anchor=SW, pady=4, padx=4)
	tela_anterior.destroy()

def chamar_tela_cadastro_colaborador(tela_anterior):
	tela_anterior.destroy()
	tela_cadastro_colaborador = Tk()
	tela_cadastro_colaborador["bg"] = "white"
	tela_cadastro_colaborador.geometry("500x680+300+40")
	tela_cadastro_colaborador.title("Cadastro") 
	lb = Label(tela_cadastro_colaborador, text="Informe os dados do colaborador", fg="orange", bg="white", font=["Verdana", 16]).pack(pady=30)
	
	#Nome:
	dis_x = 110
	dis_y_inicial = 70

	lb_nome = Label(tela_cadastro_colaborador, text="Nome:", bg="white")
	lb_nome.place(x=dis_x, y=dis_y_inicial)
	entrada_nome = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_nome.place(x=dis_x, y=dis_y_inicial+20)
	#Data de Nascimento
	lb_dt_nasc = Label(tela_cadastro_colaborador, text="Data de Nascimento:", bg="white")
	lb_dt_nasc.place(x=dis_x, y=dis_y_inicial+50)
	entrada_dt_nasc = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_dt_nasc.place(x=dis_x, y=dis_y_inicial+70)
	#Laboratório
	lb_lab = Label(tela_cadastro_colaborador, text="Laboratório:", bg="white")
	lb_lab.place(x=dis_x, y=dis_y_inicial+100)
	lista_lab = retorna_lista_lab()
	entrada_lab = ttk.Combobox(tela_cadastro_colaborador, width=37)
	entrada_lab.place(x=dis_x, y=dis_y_inicial+120)	
	entrada_lab['values'] = lista_lab
	#Função
	lb_func = Label(tela_cadastro_colaborador, text="Função:", bg="white")
	lb_func.place(x=dis_x, y=dis_y_inicial+150)
	lista_func = ['Pesquisador', 'Gestor', 'Coordenador', 'ADM', 'Coordenador Geral']
	entrada_func = ttk.Combobox(tela_cadastro_colaborador, width=37, values=lista_func)
	entrada_func.place(x=dis_x, y=dis_y_inicial+170)			
	#Carga Horária
	lb_CH = Label(tela_cadastro_colaborador, text="Carga Horária semanal:", bg="white")
	lb_CH.place(x=dis_x, y=dis_y_inicial+200)
	entrada_CH = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_CH.place(x=dis_x, y=dis_y_inicial+220)	
	#Data de Ingresso
	lb_dt_ing = Label(tela_cadastro_colaborador, text="Data de Ingresso:", bg="white")
	lb_dt_ing.place(x=dis_x, y=dis_y_inicial+250)
	entrada_dt_ing = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_dt_ing.place(x=dis_x, y=dis_y_inicial+270)
	#Status
	lb_status = Label(tela_cadastro_colaborador, text="Status:", bg="white")
	lb_status.place(x=dis_x, y=dis_y_inicial+300)
	entrada_status = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_status.place(x=dis_x, y=dis_y_inicial+320)
	#CPF
	lb_cpf = Label(tela_cadastro_colaborador, text="CPF:", bg="white")
	lb_cpf.place(x=dis_x, y=dis_y_inicial+350)
	entrada_cpf = Entry(tela_cadastro_colaborador, width=40, bg="white")
	entrada_cpf.place(x=dis_x, y=dis_y_inicial+370)

	#Upload Foto
	line_path = StringVar()
	lb_foto = Label(tela_cadastro_colaborador, text="Insira a foto do colaborador", bg="white").place(x=dis_x, y=dis_y_inicial+400)
	entrada_foto = Entry(tela_cadastro_colaborador, width=40, bg="white", textvariable= line_path)
	entrada_foto.place(x=dis_x, y=dis_y_inicial+420)

	bt_browser = Button(tela_cadastro_colaborador, text="Browser", bg="white", command=partial(ImageMethods.get_path, line_path))
	bt_browser.place(x=dis_x+250, y=dis_y_inicial+420)

	#Senha
	lb_senha = Label(tela_cadastro_colaborador, text="Senha:", bg="white").place(x=dis_x, y=dis_y_inicial+450)
	entrada_senha = Entry(tela_cadastro_colaborador, width=40, bg="white", show="*")
	entrada_senha.place(x=dis_x, y=dis_y_inicial+470)
	#Confirme sua Senha
	lb_confirma_senha = Label(tela_cadastro_colaborador, text="Confirme sua Senha:", bg="white").place(x=dis_x, y=dis_y_inicial+500)
	entrada_confirma_senha = Entry(tela_cadastro_colaborador, width=40, bg="white", show="*")
	entrada_confirma_senha.place(x=dis_x, y=dis_y_inicial+520)

	bt_ok = Button(tela_cadastro_colaborador, width=10, text="Cadastrar", bg="white", command=partial(cadastrar_colaborador, tela_cadastro_colaborador, entrada_nome, entrada_dt_nasc,
																									  entrada_lab, entrada_func, entrada_CH, entrada_dt_ing, entrada_status, entrada_cpf,
																									  entrada_senha, entrada_confirma_senha, entrada_foto)).place(x=275, y=620)
	bt_voltar = Button(tela_cadastro_colaborador, width=10, text="Voltar", bg="white", command=partial(chamar_tela_cadastro, tela_cadastro_colaborador)).pack(side=BOTTOM, anchor=SW, pady=4, padx=4)
	

def chamar_tela_cadastro_laboratorio(tela_anterior):
	tela_anterior.destroy()
	tela_cadastro_laboratorio = Tk()
	tela_cadastro_laboratorio["bg"]="white"
	tela_cadastro_laboratorio.geometry("500x300+300+200")
	tela_cadastro_laboratorio.title("Cadastro") 
	lb = Label(tela_cadastro_laboratorio, text="Informe os dados do laboratório", fg="orange", bg="white", font=["Verdana", 16]).pack(pady=20)
	
	#Nome:
	lb_nome = Label(tela_cadastro_laboratorio, text="Nome:", bg="white").place(x=110, y=80)
	entrada_nome = Entry(tela_cadastro_laboratorio, width=40, bg="white")
	entrada_nome.place(x=110, y=100)
	#Sigla:
	lb_sigla = Label(tela_cadastro_laboratorio, text="Sigla:", bg="white").place(x=110, y=130)
	entrada_sigla = Entry(tela_cadastro_laboratorio, width=40, bg="white")
	entrada_sigla.place(x=110, y=150)

	#Upload logo
		#Label e entry
	lb_logo = Label(tela_cadastro_laboratorio, text='Insira o logo do laboratório', bg='white').place(x=110, y=180)
	line_path = StringVar()
	entrada_logo = Entry(tela_cadastro_laboratorio, width=40, bg='white', textvariable = line_path)
	entrada_logo.place(x=110, y=200)
		#button
	bt_browser = Button(tela_cadastro_laboratorio, text='Browser', bg='white', command = partial(ImageMethods.get_path, line_path))
	bt_browser.place(x=360, y=200)

	bt_voltar = Button (tela_cadastro_laboratorio, width=10, text="Voltar", bg="white", command=partial(chamar_tela_cadastro, tela_cadastro_laboratorio)).pack(side=BOTTOM, anchor=SW, pady=4, padx=4)
	bt_ok = Button(tela_cadastro_laboratorio, width=10, text="Cadastrar", bg="white", command=partial(cadastrar_laboratorio, tela_cadastro_laboratorio, entrada_nome, entrada_sigla, entrada_logo)).place(x=275, y=250)

def pop_up_cadastro_invalido():
	pop_up = Tk()
	pop_up["bg"]="white"
	pop_up.geometry("210x50+450+330")
	pop_up.title("ERROR") 
	lb = Label (pop_up, text="Cadastro Inválido", bg="white").pack(pady=20)
	
def pop_up_cadastro_valido():
	pop_up = Tk()
	pop_up["bg"]="white"
	pop_up.geometry("210x50+450+330")
	pop_up.title("SUCCESSFUL") 
	lb = Label (pop_up, text="Cadastro Realizado com Sucesso", bg="white").pack(pady=20)

def pop_up_confirma_senha():
	pop_up = Tk()
	pop_up["bg"]="white"
	pop_up.geometry("210x50+450+330")
	pop_up.title("ERROR") 
	lb = Label (pop_up, text="Confirme sua senha!", bg="white").pack(pady=20)

def chamar_tela_consulta(tela_anterior):
	tela_consulta = Tk()
	tela_consulta["bg"]="white"
	tela_consulta.geometry("500x300+300+200")
	tela_consulta.title("Consulta") 
	lb = Label (tela_consulta, text="O que você deseja consultar?", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50)
	bt_consultar_colaborador = Button (tela_consulta, width=20, text="Colaborador", bg="white").pack(pady=3) 
	bt_consultar_laboratorio = Button (tela_consulta, width=20, text="Laboratório", bg="white").pack(pady=3)
	bt_voltar = Button (tela_consulta, width=10, text="Voltar", bg="white", command=partial(chamar_tela_inicial, tela_consulta)).pack(side=BOTTOM, anchor=SW, pady=4, padx=4)
	tela_anterior.destroy()

def chamar_tela_login():
	tela_login = Tk() 
	tela_login["bg"]="white"
	tela_login.geometry("500x350+300+200") #dimensoes da janela --> Largura x Altura + DistanciaDaMargemEsquerda + DistanciaDaMargemSuperior
	tela_login.title("Sistema de Controle de Frequência") #título da janela

	#Logo
	imagem = PhotoImage(file="imagens/hub.png")
	lb_image = Label(tela_login, image = imagem, bg="white")
	lb_image.image = imagem
	lb_image.pack(pady=30)
	lb_login = Label(tela_login, text="Login:", bg="white").place(x=120, y=150)
	entrada_login = Entry(tela_login, width=40, bg="white")
	entrada_login.place(x=120, y=170)
	lb_senha = Label(tela_login, text="Senha:", bg="white").place(x=120, y=200)
	entrada_senha = Entry(tela_login, width=40, bg="white", show="*")
	entrada_senha.place(x=120, y=220)
	bt_logar = Button(tela_login, width=10, bg="white", text="Login", command=partial(escolhe_tela, tela_login, entrada_login)).place(x=285, y=250)
	tela_login.mainloop()

	
def chamar_tela_inicial(tela_anterior):
	tela_inicial = Tk() #criacao de uma janela - instancia de Tk
	tela_inicial.geometry("500x300+300+200") #dimensoes da janela --> Largura x Altura + DistanciaDaMargemEsquerda + DistanciaDaMargemSuperior
	tela_inicial.title("HUB - Tecnologia e Inovação") #título da janela
	tela_inicial["bg"]="white"
	lb_inicial = Label (tela_inicial, text="Sistema de Controle de Frequência", fg= "orange", bg="white", font=["Verdana", 16]).pack(pady=50) #criando rótulo
	bt_cadastrar = Button (tela_inicial, width=20, text="Cadastrar", command = partial(chamar_tela_cadastro, tela_inicial), bg="white").pack(pady=3) #criando botao "cadastrar"
	bt_consultar = Button (tela_inicial, width=20, text="Consultar", command = partial(chamar_tela_consulta, tela_inicial), bg="white").pack(pady=3) #criando botao "Consultar" 	
	tela_anterior.destroy()
