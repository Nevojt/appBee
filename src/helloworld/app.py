import toga
from toga import Button, Box
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class MyApp(toga.App):

    def startup(self):

        self.name_input = toga.TextInput(style=Pack(flex=1))
        self.password_input = toga.PasswordInput(style=Pack(flex=1))
        
        button = Button("butt", on_press=self.say_hello)
        button_2 = Button("butt2")
        top =       Box(style=Pack(direction=COLUMN, flex=1, background_color='blue'), children=[self.name_input, self.password_input])
        bottom =    Box(style=Pack(direction=ROW, flex=0), children=[button, button_2])
        
        main_box =  Box(style=Pack(direction=COLUMN, padding=9),  
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

























































# """
# My first application
# """

# # import httpx
# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, ROW


# def greeting(name):
#     if name:
#         return f"Hello, {name}"
#     else:
#         return "Hello, stranger"

# class HelloWorld(toga.App):
#     def startup(self):
#         """Construct and show the Toga application.

#         Usually, you would add your application to a main content box.
#         We then create a main window (with a name matching the app), and
#         show the main window.
#         """
#         # main_box = toga.Box(style=Pack(direction=COLUMN, padding=5, background_color="#3F00FF"))
        
        
#         # label_box = toga.Box(style=Pack(direction=ROW, padding=5, background_color="#ADD8E6"))
        
#         # name_label = toga.Label(
#         #     text="Get started!",
#         #     style=Pack(padding_right=5, flex=1, text_align="center")
#         # )
#         # label_box.add(name_label)
        
        
        
        
#         # self.name_input = toga.TextInput(style=Pack(flex=1))
#         # self.password_input = toga.PasswordInput(style=Pack(flex=1))
        
#         # input_box_name = toga.Box(style=Pack(direction=COLUMN, padding=(25, 5, 5)))
#         # input_box_name.add(self.name_input)
        
#         # input_box_password = toga.Box(style=Pack(direction=COLUMN, padding=(5, 5)))
#         # input_box_password.add(self.password_input)
        
#         # spicer = toga.
        
#         # button_box = toga.Box(style=Pack(direction=ROW, padding=(650, 5, 5)))
#         # button = toga.Button(
#         #     text="Say hello!",
#         #     on_press=self.say_hello,
#         #     style=Pack(padding=5)
#         # )
#         # button2 = toga.Button(
#         #     text="Say hello!",
#         #     on_press=self.say_hello,
#         #     style=Pack(padding=5)
#         # )
#         # button_box.add(button)
#         # button_box.add(button2)
        
#         # main_box.add(label_box)
#         # main_box.add(input_box_name)
#         # main_box.add(input_box_password)
#         # main_box.add(button_box)
        
        
        
#         self.main_window = toga.MainWindow(title=self.formal_name)
#         # self.main_window.content = main_box
#         self.main_window.show()

#     # def say_hello(self, widget):
#     #     with httpx.Client() as client:
#     #         response = client.get("https://jsonplaceholder.typicode.com/posts/42")

#     #     payload = response.json()

#     #     self.main_window.info_dialog(
#     #     greeting(self.name_input.value),
#     #     payload["body"],
#     # )
    
#     # async def say_hello(self, widget):
#     #     ask_a_question = toga.QuestionDialog("Sing Up?", "Дані вірно вказані?")
#     #     say = toga.InfoDialog(title="Your credentials",
#     #                              message=f"Name: {self.name_input.value}\nPassword: {self.password_input.value}"
#     #     )
#     #     if await self.main_window.dialog(ask_a_question):
            
#     #         await self.main_window.dialog(say)

# def main():
#     return HelloWorld()