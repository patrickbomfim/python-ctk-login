import customtkinter as ctk

# Configuração de aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")  # Opcional

#criaçao das funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get() 
    import customtkinter as ctk

# Configuração de aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

# Criação da janela principal
janela = ctk.CTk()
janela.title('Sistema de Login Python')
janela.geometry('300x300')

# Função de validação de login
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == "patrick" and senha == "123456":
        resultado_login.configure(text="Login feito com sucesso", text_color="green")
    else:
        resultado_login.configure(text="Login incorreto", text_color="red")

# Campos de entrada
label_usuario = ctk.CTkLabel(janela, text="Usuário")
label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(janela, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(janela, text="Senha")
label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(janela, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# Botão de login
botao_login = ctk.CTkButton(janela, text="Login", command=validar_login)
botao_login.pack(pady=10)

# Campo de feedback
resultado_login = ctk.CTkLabel(janela, text="")
resultado_login.pack(pady=10)

# Loop da interface
janela.mainloop()
