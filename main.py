from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from filemanager import MDFileManager

Window.size = (360, 600)


class Display_main(Screen):
    pass


class Mainscreen(Screen):
    pass


class Img2pdfscreen(Screen):
    pass


class File_manager(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Mainscreen(name="mainscr"))
sm.add_widget(Img2pdfscreen(name="img2pdfscr"))
sm.add_widget(File_manager(name="filemanagerscr"))


class PdfApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        self.theme_cls.primary_palette = "Green"
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, 
            ext=[".pdf"],
            select_path=self.select_path, previous=True,
        )

    def build(self):

        return

    def open_filemanager(self):
        self.file_manager.show("/")
        self.manager_open = True

    def select_path(self, path):
        # self.exit_manager()
        print(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def change_screen(self, name):
        self.root.ids.manager.transition.direction = "right"
        self.root.ids.manager.current = name


PdfApp().run()