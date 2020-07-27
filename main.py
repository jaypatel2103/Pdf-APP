from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager

# from android.permissions import request_permissions, Permission
# from android.storage import primary_external_storage_path

# request_permissions(
#     [Permission.WRITE_EXTERNAL_STORAGE,
#     Permission.READ_EXTERNAL_STORAGE]
# )

# SD_CARD = primary_external_storage_path()

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

    selected_imgs_path_list = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        self.theme_cls.primary_palette = "Green"
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )

    def build(self):

        return

    def open_filemanager(self):
        self.file_manager.show("/")
        self.manager_open = True

    def select_path(self, path):
        if path not in self.selected_imgs_path_list:
            self.selected_imgs_path_list.append(path)
        else:
            self.selected_imgs_path_list.remove(path)
        # self.exit_manager()
        print(self.selected_imgs_path_list)

    def exit_manager(self, *args):
        if "selection_done" in args:
            print("jay")
        else:
            self.manager_open = False
            self.file_manager.close()

    def change_screen(self, name, *args):
        if "is_drawer_call" in args:
            self.root.ids.manager.transition.direction = "right"
            self.root.ids.manager.current = name
            # self.root.ids.nav_drawer.set_state('close')
        else:
            self.root.ids.manager.transition.direction = "right"
            self.root.ids.manager.current = name


PdfApp().run()
