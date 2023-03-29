import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    link = link_entry.get()
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        messagebox.showinfo('Download', 'Download concluído com sucesso!')
    except Exception as e:
        messagebox.showerror('Erro', 'Insira primeiro a URL: do video')

root = tk.Tk()
root.title('Youtube Downloader')
root.geometry('400x200')

link_label = tk.Label(root, text='Insira o link do vídeo:')
link_label.pack()

link_entry = tk.Entry(root, width=50)
link_entry.pack()

download_button = tk.Button(root, text='Download', command=download_video)
download_button.pack()

root.mainloop()
