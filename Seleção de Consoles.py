import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dicionário de fabricantes e consoles com links de imagens
consoles = {
    "Atari": {
        "Atari 2600": "https://s2-techtudo.glbimg.com/EdpL-XG-YNh5jyYpY7Hsjsuu89w=/0x0:695x472/888x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2021/B/d/NCC82zQYCrd1t9DzH3Ew/2016-01-28-atari2600.jpg",
        "Atari 5200": "https://pop.proddigital.com.br/wp-content/uploads/sites/8/2023/07/atari-5200.jpg",
        "Atari 7800": "https://i.pinimg.com/736x/bb/7b/2f/bb7b2fa120f2b46a2fa5d7f0769ad52f.jpg",
        "Atari Jaguar": "https://www.homecomputermuseum.nl/wp-content/uploads/2022/12/Atari-Jaguar..jpg",
        "Atari Lynx": "https://toytales.ca/wp-content/uploads/2022/08/atari-lynx.jpg"
    },
    "Bandai": {
        "Wonderswan": "https://ae01.alicdn.com/kf/Hd3c05af796cf42afa96026bd6a3c8e34t/Ws-hightlight-tela-lcd-kits-brilho-luminoso-para-bandai-wonderswan-game-console.jpg",
        "Wonderswan Color": "https://i.ebayimg.com/thumbs/images/g/wr8AAOSwmvdmgGPq/s-l1200.jpg"
    },
    "Sony": {
        "Playstation 1": "https://i5.walmartimages.com/seo/Pre-Owned-Playstation-1-Video-Game-Console_9570c34b-ea05-4472-a93b-b75fe83129c0.a3ca8b7726cb241a59f89bc29b69adbb.jpeg",
        "Playstation 2": "https://s2-techtudo.glbimg.com/4y3nejQcBv7GeSvfrGsLIP3MIp8=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2020/q/E/zZjJhTRlqeGY8aX3sg7w/playstation-2-ps2-20-anos-fatos-curiosos-console-sony.jpg",
        "Playstation 3": "https://s2-techtudo.glbimg.com/E1ugszzmAoxVsXMwoOyT9qg-794=/0x0:695x575/984x0/smart/filters:strip_icc()/s.glbimg.com/po/tt2/f/original/2017/02/07/9252394sz2.jpg",
        "Playstation 4": "https://cdn.awsli.com.br/800x800/118/118222/produto/16619909/e975ecf5dc.jpg",
        "Playstation 5": "https://m.media-amazon.com/images/I/41UWxQoHMPL.jpg"
    },
    "Microsoft": {
        "Xbox": "https://http2.mlstatic.com/D_827727-MLB80143857277_102024-C.jpg",
        "Xbox 360": "https://cdn.techshake.com/imagens/xbox-360.jpg?class=article",
        "Xbox One": "https://cdn.awsli.com.br/300x300/138/138431/produto/8598395/b1a8857924-nyoxic.jpg",
        "Xbox Séries": "https://s2-techtudo.glbimg.com/VJOcrZovPEV0zF9KWInD-luUfFQ=/0x0:1920x1078/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2021/K/j/Wwd5EBTJmwJp6wfgJ1ag/xbox-series-s.jpg"
    },
    "Nintendo": {
        "Nintendo Entertainment System": "https://i5.walmartimages.com/seo/Restored-Nintendo-Entertainment-System-NES-1985-Console-with-Official-OEM-Controller-Refurbished_31e134fe-94c0-4ff1-a2c1-7323b90d0e0a_1.4e1c5ca2512c2f9413e90763e0d5b942.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF",
        "Super Nintendo": "https://s2-techtudo.glbimg.com/ORcX9bikylMtAIkem-2s7wu5MVc=/400x0/smart/filters:strip_icc()/s.glbimg.com/po/tt2/f/original/2015/12/02/supernintendo.jpg",
        "Nintendo 64": "https://images.tcdn.com.br/img/img_prod/1211726/nintendo_64_seminovo_1213_1_ba99f3b8f7d209c446584ea695e09d75.png",
        "Game Cube": "https://static.wikia.nocookie.net/nintendo/images/1/11/Console_Nintendo_Game_Cube.png/revision/latest/scale-to-width-down/250?cb=20170728023029&path-prefix=pt-br",
        "Wii": "https://s2-techtudo.glbimg.com/rJ6I8cObTPsFNTzkLXtLrps1hoE=/0x0:620x549/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2021/V/h/7W8859Txaqq5zHpIAjqA/2013-10-22-nintendo-wii.jpg",
        "Wii U": "https://www.nintendo.com/eu/media/images/10_share_images/systems_11/wii_u_11/H2x1_generic_WiiU.jpg",
        "Gameboy": "https://down-br.img.susercontent.com/file/d691f11b8d3449b11fcbc92eaa916485",
        "Gameboy Color": "https://m.media-amazon.com/images/I/71zK8xuifOL.jpg",
        "Gameboy Advance": "https://forbes.com.br/wp-content/uploads/2019/06/colunas_gba18anos_110619_divulgacao.jpg",
        "Nintendo DS": "https://i5.walmartimages.com/seo/Nintendo-DS-Handheld-game-console-silver_46971ef7-3fb0-49ce-971e-bf9fc6f588d8.8e0be90960f2025ce73092cd25b21ff1.jpeg",
        "Nintendo 2DS": "https://m.media-amazon.com/images/I/6111kmibxLL.jpg",
        "Nintendo 3DS": "https://m.media-amazon.com/images/I/61VY7UUzoFL.jpg",
        "Nintendo Switch": "https://www.popsci.com/wp-content/uploads/2021/07/22/Photo-Oct-20-9-06-53-AM-scaled.jpg"
    },
    "Sega": {
        "Master System": "https://d2j6dbq0eux0bg.cloudfront.net/images/17412255/3632771483.jpg",
        "Mega Drive": "https://www.copetti.org/images/consoles/megadrive/american.413c2f03af1f9a5fac22a1d336a16082f72e049691a98e4e7a5377ba406e3e83.png",
        "Game Gear": "https://http2.mlstatic.com/D_NQ_NP_733266-MLB72244113704_102023-O.webp",
        "Saturn": "https://s2-techtudo.glbimg.com/rn0brSaSMtOAYxcJo_UVOBS3rzo=/0x0:695x386/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2021/2/A/ZAWyBISMeviutwESHwnQ/2014-12-09-saturn-branco.jpg",
        "Dreamcast": "https://t2.tudocdn.net/526203?w=1920"
    },
    "Coleco": {
        "Colecovision": "https://oyster.ignimgs.com/mediawiki/apis.ign.com/history-of-video-game-consoles/6/64/Colecovision_console.jpg"
    },
    "NEC Corporation": {
        "PC Engine": "https://retrospace.nl/images/system.jpg"
    }
}

def update_consoles(event):
    selected_manufacturer = manufacturer_var.get()
    console_box['values'] = list(consoles[selected_manufacturer].keys())
    console_var.set('')

def show_console_image():
    selected_manufacturer = manufacturer_var.get()
    selected_console = console_var.get()
    image_url = consoles.get(selected_manufacturer, {}).get(selected_console)
    
    if image_url:
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = img.resize((400, 400), Image.LANCZOS)  # Usando LANCZOS no lugar de ANTIALIAS
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo
            image_label.config(text="")
        except requests.exceptions.RequestException:
            image_label.config(text="Erro ao carregar a imagem", image="")
    else:
        image_label.config(text="Imagem não disponível", image="")

# Janela principal
root = tk.Tk()
root.title("Seleção de Consoles")
root.geometry("500x400")
root.configure(bg='#5D6D7E')  # Cor de fundo azul escuro

# Título
title = tk.Label(root, text="Selecione o Console Desejado", font=("Helvetica", 16, "bold"), bg='#5D6D7E', fg="white")
title.pack(pady=10)

# Seleção do fabricante
manufacturer_label = tk.Label(root, text="Fabricante:", font=("Helvetica", 12), bg='#5D6D7E', fg="white")
manufacturer_label.pack(pady=5)

manufacturer_var = tk.StringVar()
manufacturer_box = ttk.Combobox(root, textvariable=manufacturer_var, values=list(consoles.keys()), font=("Helvetica", 10))
manufacturer_box.pack(pady=5)
manufacturer_box.bind("<<ComboboxSelected>>", update_consoles)

# Seleção do console
console_label = tk.Label(root, text="Console:", font=("Helvetica", 12), bg='#5D6D7E', fg="white")
console_label.pack(pady=5)

console_var = tk.StringVar()
console_box = ttk.Combobox(root, textvariable=console_var, font=("Helvetica", 10))
console_box.pack(pady=5)

# Botão para exibir a imagem
show_button = tk.Button(root, text="Mostrar Console", font=("Helvetica", 12), command=show_console_image, bg='#2980B9', fg="white")
show_button.pack(pady=10)

# Label para exibir a imagem do console
image_label = tk.Label(root, bg='#5D6D7E')
image_label.pack(pady=20)

root.mainloop()
