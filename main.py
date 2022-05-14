from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp
class HotReload(App,MDApp):
    CLASSES={'Manager':'app.main_ui'}
    KV_FILES=['app/kivy_lang.kv','app/defaults.kv']
    AUTORELOADER_PATHS=[('.',{'recursive':True})]
    def build_app(self):
        return Factory.Manager()

if __name__=='__main__':
    HotReload().run()
