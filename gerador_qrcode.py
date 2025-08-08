import tkinter as tk
from tkinter import ttk, filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO

def gerar():
    global url
    url = f"https://api.qrserver.com/v1/create-qr-code/?data={entrada.get()}&size=200x200"
    img = Image.open(BytesIO(requests.get(url).content))
    img_tk = ImageTk.PhotoImage(img)
    rotulo.config(image=img_tk)
    rotulo.image = img_tk

def colar_clipboard(evento=None):
    try:
        entrada.delete(0, tk.END)  # Limpa o campo
        entrada.insert(0, janela.clipboard_get())
    except tk.TclError:
        pass  # Clipboard vazio ou inválido

def salvar_imagem():
    if not url:
        return
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG", "*.png"),
            ("JPEG", "*.jpg"),
            ("SVG", "*.svg"),
        ]
    )
    if not arquivo:
        return
    ext = arquivo.split('.')[-1].lower()
    formato = "png" if ext == "png" else "jpg" if ext == "jpg" else "svg"
    url_img = url + f"&format={formato}"
    conteudo = requests.get(url_img).content
    with open(arquivo, "wb") as f:
        f.write(conteudo)

def mostrar_menu(evento):
    menu = tk.Menu(janela, tearoff=0)
    menu.add_command(label="Salvar Imagem", command=salvar_imagem)
    menu.tk_popup(evento.x_root, evento.y_root)
    
janela = tk.Tk()
janela.title("Gerador de QR Code")

entrada = ttk.Entry(janela, width=40)
entrada.pack(padx=10, pady=10)
entrada.bind("<FocusIn>", colar_clipboard)  # Colar ao ganhar foco

ttk.Button(janela, text="Gerar QR", command=gerar).pack(pady=(0, 10))
rotulo = ttk.Label(janela)
rotulo.pack()
rotulo.bind("<Button-3>", mostrar_menu)

janela.mainloop() 
