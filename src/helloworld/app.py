import toga
from toga import Button, Box
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MyApp(toga.App):

    def startup(self):

        
        
        self.label = toga.Label(text="Safe your password!", style=Pack(flex=0, text_align="center",
                                                                       padding=(0, 0, 20, 0), font_family="serif",
                                                                       font_style="italic", font_weight="bold", font_size=18))
        
        self.label_name = toga.Label(text="URL-address or email", style=Pack(font_family="serif",
                                                            font_style="italic"))
        
        self.label_password = toga.Label(text="Password", style=Pack(font_family="serif",
                                                            font_style="italic"))
        
        self.name_input = toga.TextInput(style=Pack(flex=1, padding=(0, 0, 20, 0), font_family="serif",
                                                            font_style="italic"))
        
        self.password_input = toga.PasswordInput(style=Pack(flex=1))
        
        
        
        button = Button(text="button", on_press=self.say_hello, style=Pack(flex=1))
        button_2 = Button("button2", style=Pack(flex=2))
        
        top =       Box(style=Pack(direction=COLUMN, flex=1),
                        children=[self.label, self.label_name, self.name_input, self.label_password, self.password_input])
        
        bottom =    Box(style=Pack(direction=ROW, flex=0), children=[button, button_2])
        
        main_box =  Box(style=Pack(direction=COLUMN, background_color="green"),  
                            children=[top, bottom])

        self.main_window = toga.MainWindow(title='myapp')
        self.main_window.content = main_box
        self.main_window.show()










    async def say_hello(self, widget):
        ask_a_question = toga.QuestionDialog("Sing Up?", "Дані вірно вказані?")
        say = toga.InfoDialog(title="Your credentials",
                                 message=f"Name: {self.name_input.value}\nPassword: {self.password_input.value}"
        )
        if await self.main_window.dialog(ask_a_question):
            
            await self.main_window.dialog(say)

def main():
    return MyApp()


