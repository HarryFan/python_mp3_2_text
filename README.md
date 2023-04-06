MP3 轉逐字稿應用程式
============

這個應用程式可以將 MP3 音檔轉換成逐字稿。它使用了 `SpeechRecognition` 庫進行語音辨識並將 MP3 音檔拆分成較小的片段進行處理。用戶可以通過應用程式的圖形界面選擇音檔並指定輸出路徑。

安裝
--

### Python 庫

在開始使用應用程式之前，您需要安裝以下 Python 庫：

*   `tkinter`
    
*   `pydub`
    
*   `speech_recognition`
    

使用以下命令安裝：

```
pip install pydub SpeechRecognition
```

### 打包應用程式

要將應用程式打包為 Windows、macOS 和 Linux 可執行的應用，請參考上面的[回應](https://github.com/openai/openai-cookbook/blob/main/examples/package-python-app.md)。

使用方法
----

1.  運行應用程式
    
2.  點擊「瀏覽」按鈕，選擇要轉換的 MP3 音檔
    
3.  點擊「瀏覽」按鈕，選擇輸出逐字稿的路徑
    
4.  點擊「開始轉換」按鈕，等待轉換過程完成
    
5.  在指定的輸出路徑下，查看名為 `逐字稿.txt` 的文件
    

注意事項
----

*   轉換速度取決於音檔的長度和您的網絡連接速度
    
*   這個應用程式使用 Google Speech Recognition 服務，可能會受到 Google API 限制
    
*   目前，應用程式僅支援中文（繁體）的語音辨識
    

技術實現
----

這個應用程式使用了以下庫和技術：

*   `tkinter`：用於構建圖形用戶界面
    
*   `pydub`：用於處理音檔，將 MP3 檔案拆分成較小的片段
    
*   `speech_recognition`：用於將音檔片段轉換為文字
    

應用程式將 MP3 音檔拆分成多個 30 秒的片段，並使用 Google Speech Recognition 進行語音識別。之後，將所有片段的識別結果合併並儲存到輸出路徑。