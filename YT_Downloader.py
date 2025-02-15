import os
import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

def download_video():
    url = url_entry.get()
    quality = quality_var.get()
    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube valide.")
        return
    
    save_path = filedialog.askdirectory()
    if not save_path:
        return
    
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': f'bestvideo[height={quality}]+bestaudio/best'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", f"Téléchargement terminé !\nVidéo enregistrée dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Interface graphique
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x250")

tk.Label(root, text="Entrez l'URL de la vidéo YouTube:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Choisissez la qualité de la vidéo:").pack(pady=5)
quality_var = tk.StringVar(value="1080")
quality_menu = tk.OptionMenu(root, quality_var, "2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p")
quality_menu.pack()

tk.Button(root, text="Télécharger", command=download_video).pack(pady=20)

root.mainloop()
