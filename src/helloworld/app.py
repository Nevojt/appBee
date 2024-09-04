"""
My first application
"""
import httpx
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


def greeting(name):
    if name:
        return f"Hello, {name}"
    else:
        return "Hello, stranger"

class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            text="Your name:",
            style=Pack(padding=5, flex=1)
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)
        
        button = toga.Button(
            text="Say hello!",
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        main_box.add(name_box)
        main_box.add(button)
        
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        with httpx.Client() as client:
            response = client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        self.main_window.info_dialog(
        greeting(self.name_input.value),
        payload["body"],
    )

def main():
    return HelloWorld()
