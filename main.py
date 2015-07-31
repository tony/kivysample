from kivy.app import App
from kivy.uix.button import Button

__version__ = "0.1"


class TutorialApp(App):
    def build(self):
        return Button(
            text="hey mom! want taco bell?",
            background_color=(0, 0, 1, 1),
            font_size=12
        )

if __name__ == "__main__":
    TutorialApp().run()
