import webview
from tkinter import *

root = Tk()
root.geometry('1000x600')
root.title("Browser Inspector")

def google_browser():
    webview.create_window("Google.com", "https://www.google.com")
    webview.start()

def yandex_browser():
    webview.create_window("Google.com", "https://ya.ru")
    webview.start()

Label(root, text="Browser Inspector", font="Ravie").pack()
Label(root, text="Select your Browser:", font="Verdana").pack(pady=50)
Button(root, text="Google", width=20, bg="orange", command=google_browser).pack(pady=25)
Button(root, text="Yandex", bg="yellow", width=20, command=yandex_browser).pack(pady=5)



root.mainloop()
