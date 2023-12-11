import tkinter as tk
from tkinter import filedialog
from transcribe import transcribe, transcribe_audio
import threading
import mimetypes


def transcribe_file(file_path):
    file_type = mimetypes.guess_type(file_path)[0]
    status_label.config(text='Processing...')
    if 'video' in file_type:
        result = transcribe(file_path, 'base')
    elif 'audio' in file_type:
        result = transcribe_audio(file_path, 'base')
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, result)
    status_label.config(text='Done')

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4'), ('Audio Files', '*.mp3 *.wav')])
    if file_path:
        threading.Thread(target=transcribe_file, args=(file_path,)).start()

root = tk.Tk()
root.title('Transcription')
root.geometry('500x300')

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

frame.grid_columnconfigure(0, weight=1)  # Add this line

open_button = tk.Button(frame, text='Open File', command=open_file)
open_button.grid(row=0, column=0, sticky='w')

status_label = tk.Label(frame, text='')
status_label.grid(row=1, column=0, sticky='w')

result_label = tk.Label(frame, text='Transcription Result:')
result_label.grid(row=2, column=0, sticky='w')

result_text = tk.Text(frame, height=10)
result_text.grid(row=3, column=0, sticky='we')

root.mainloop()