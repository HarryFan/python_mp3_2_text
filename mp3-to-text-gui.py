import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import speech_recognition as sr

def browse_directory():
    folder_selected = filedialog.askdirectory()
    save_path.set(folder_selected)

def browse_file():
    file_selected = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    file_path.set(file_selected)

def transcribe_audio():
    file_path_str = file_path.get()
    output_directory = save_path.get()

    # 讀取 mp3 音檔
    transcript_label.config(text="正在轉換中...")
    app.update()
    audio_file = AudioSegment.from_file(file_path_str)

    # 切割音檔成多個小檔案
    chunk_size = 30 * 1000  # 30 秒
    chunks = [audio_file[i:i+chunk_size] for i in range(0, len(audio_file), chunk_size)]

    # 使用 SpeechRecognition 將每個小檔案轉成文字，然後合併在一起
    recognizer = sr.Recognizer()
    transcript = ""
       
    for chunk in chunks:
        chunk.export("temp.wav", format="wav")
        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="zh-TW")
                transcript += text
            except sr.UnknownValueError:
                transcript += "[無法識別的片段]"
            except sr.RequestError as e:
                transcript_label.config(text="語音識別請求失敗: {}".format(e))
                return        

    # 儲存轉換後的逐字稿
    with open(f"{output_directory}/逐字稿.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    transcript_label.config(text="轉換完成！")

app = tk.Tk()
app.title("MP3 轉逐字稿")

file_path_label = tk.Label(text="MP3 檔案路徑:")
file_path_label.grid(row=0, column=0, sticky="e")
file_path = tk.StringVar()
file_path_entry = tk.Entry(textvariable=file_path)
file_path_entry.grid(row=0, column=1)
browse_file_button = tk.Button(text="瀏覽", command=browse_file)
browse_file_button.grid(row=0, column=2)

save_path_label = tk.Label(text="逐字稿儲存路徑：")
save_path_label.grid(row=1, column=0, sticky="e")
save_path = tk.StringVar()
save_path_entry = tk.Entry(textvariable=save_path)
save_path_entry.grid(row=1, column=1)
browse_button = tk.Button(text="瀏覽", command=browse_directory)
browse_button.grid(row=1, column=2)

start_button = tk.Button(text="開始轉換", command=transcribe_audio)
start_button.grid(row=2, column=1, pady=10)

transcript_label = tk.Label(text="")
transcript_label.grid(row=3, column=1)

app.mainloop()
