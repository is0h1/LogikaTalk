import threading
from socket import *
from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.label = "LogikaTalk"

        self.frame = CTkFrame(self, width=200, height=700)
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.if_show_menu = False
        self.speed_animated_menu = -5
        self.frame_width = 0

        self.label = CTkLabel(self.frame, text="Ваш нікнейм")
        self.label.pack(pady=30)

        self.entry = CTkEntry(self.frame)
        self.entry.pack()

        self.label_theme = CTkOptionMenu(self,frame, values=['Темна','Світла'], command=self,change_theme)
        self.label_theme.place(x=50, y=400)
        self.theme = None
        self.btn = CTkButton(self, text= '▶️', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)
        self.menu_show_speed = 20

        self.chat_text = CTkTextbox(self, state='disable')
        self.chat_text.place(x=0, y=30)

        self.message_input = CTkEntry(self, placeholder_text='Введіть повідомлення:')
        self.message_input.place(x=0, y=30)

        self.send_button = CTkButton(self, text= '▶️', width=30, height=30)
        self.send_button.place(x=0, y=0)

        self.username = 'User'
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('localhost', 8080))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
            self.sock.send(hello.encode('utf-8'))
            threading.Thread(target=self.recv_message, daemon=True).start()
        except Exception as e:
            self.add_message(f"Не вдалося підключитися до сервера: {e}")
        self.adaptive_ui()

    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu = -1
            self.btn.configure(text="◀")
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text="▶")
            self.show_menu()

            self.label = CTkLabel(self.frame, text='Ім\'я')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.frame)
            self.entry.pack()

    def show_menu(self):
        3

    usages
    self.frame.configure(width=self.frame.winfo_width() + self.speed_animate_menu)
    if not self.frame.winfo_width() >= 208 and self.is_show_menu:
        self.after(10, self.show_ana)
    elif self.frame.winfo_width() >= 48 and not self.is_show_menu:
        if self.label and self.entry:
            self.label.destroy()
            self.entry.destroy()


def change_theme(self, value): 1


usage
if value == 'Темна':
    set_appearance_mode('dark')
else:
    set_appearance_mode('light')

