from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty,BooleanProperty,ObjectProperty

class WindowManager(ScreenManager):
    pass
class MenuWindow(Screen):
    pass
class  ElectronicsWindow(Screen):
        tbill = 0
        my_textl =  StringProperty("")
        my_textm =  StringProperty("")
        my_textw =  StringProperty("")
        my_textf =  StringProperty("")
        my_texta =  StringProperty("")
        my_textt =  StringProperty("")
        my_texto =  StringProperty("")
        totalbill = StringProperty("")
        lnum = 0
        mnum = 0
        wnum = 0
        fnum = 0
        anum = 0
        tnum = 0
        onum = 0
        def minusl(self,*args):
            if self.lnum > 0:
                self.lnum = self.lnum - 1
                self.my_textl = f"{self.lnum}"
        def on_lbutton_click(self,*args):
                self.lnum = self.lnum + 1
                self.my_textl = f"{self.lnum}"
        def minusm(self,*args):
            if self.mnum > 0:
                self.mnum = self.mnum - 1
                self.my_textm = f"{self.mnum}"
        def on_mbutton_click(self):
                self.mnum = self.mnum + 1
                self.my_textm = f"{self.mnum}"
        def minusw(self,*args):
            if self.wnum > 0:
                self.wnum = self.wnum - 1
        def on_wbutton_click(self):
                self.wnum = self.wnum + 1
                self.my_textw = f"{self.wnum}"
        def minusf(self,*args):
            if self.fnum > 0:
                self.fnum = self.fnum - 1
                self.my_textf = f"{self.fnum}"
        def on_fbutton_click(self):
                self.fnum = self.fnum + 1
                self.my_textf = f"{self.fnum}"
        def minusa(self,*args):
            if self.anum > 0:
                self.anum = self.anum - 1
                self.my_texta = f"{self.anum}"
        def on_abutton_click(self):
                self.anum = self.anum + 1
                self.my_texta = f"{self.anum}"
        def minust(self,*args):
            if self.tnum > 0:
                self.tnum = self.tnum - 1
                self.my_textt = f"{self.tnum}"
        def on_tbutton_click(self):
                self.tnum = self.tnum + 1
                self.my_textt = f"{self.tnum}"
        def minuso(self,*args):
            if self.onum > 0:
                self.onum = self.onum - 1
                self.my_texto = f"{self.onum}"
        def on_obutton_click(self):
                self.onum = self.onum + 1
                self.my_texto = f"{self.onum}"
        totalbill = str((lnum*50000)+(mnum*20000)+(wnum*45000)+(fnum*40000)+(anum*25000)+(tnum*50000)+(onum*25000))

class  TextileWindow(Screen):
        tbill = 0
        my_textl =  StringProperty("")
        my_textm =  StringProperty("")
        my_textw =  StringProperty("")
        my_textf =  StringProperty("")
        my_texta =  StringProperty("")
        my_textt =  StringProperty("")
        my_texto =  StringProperty("")
        totalbill = StringProperty("")
        lnum = 0
        mnum = 0
        wnum = 0
        fnum = 0
        anum = 0
        tnum = 0
        onum = 0
        def minusl(self,*args):
            if self.lnum > 0:
                self.lnum = self.lnum - 1
                self.my_textl = f"{self.lnum}"
        def on_lbutton_click(self,*args):
                self.lnum = self.lnum + 1
                self.my_textl = f"{self.lnum}"
                self.tbill = self.tbill + self.lnum*500
        def minusm(self,*args):
            if self.mnum > 0:
                self.mnum = self.mnum - 1
                self.my_textm = f"{self.mnum}"
        def on_mbutton_click(self):
                self.mnum = self.mnum + 1
                self.my_textm = f"{self.mnum}"
                self.tbill = self.tbill + self.mnum*2500
        def minusw(self,*args):
            if self.wnum > 0:
                self.wnum = self.wnum - 1
                self.my_textw = f"{self.wnum}"
        def on_wbutton_click(self):
                self.wnum = self.wnum + 1
                self.my_textw = f"{self.wnum}"
                self.tbill = self.tbill + self.wnum*500
        def minusf(self,*args):
            if self.fnum > 0:
                self.fnum = self.fnum - 1
                self.my_textf = f"{self.fnum}"
        def on_fbutton_click(self):
                self.fnum = self.fnum + 1
                self.my_textf = f"{self.fnum}"
                self.tbill = self.tbill + self.fnum*2000
        def minusa(self,*args):
            if self.anum > 0:
                self.anum = self.anum - 1
                self.my_texta = f"{self.anum}"
        def on_abutton_click(self):
                self.anum = self.anum + 1
                self.my_texta = f"{self.anum}"
                self.tbill = self.tbill + self.anum*2500
        def minust(self,*args):
            if self.tnum > 0:
                self.tnum = self.tnum - 1
                self.my_textt = f"{self.tnum}"
        def on_tbutton_click(self):
                self.tnum = self.tnum + 1
                self.my_textt = f"{self.tnum}"
                self.tbill = self.tbill + self.tnum*2000
        def minuso(self,*args):
            if self.onum > 0:
                self.onum = self.onum - 1
                self.my_texto = f"{self.onum}"
        def on_obutton_click(self):
                self.onum = self.onum + 1
                self.my_texto = f"{self.onum}"
                self.tbill = self.tbill + self.onum*500
        totalbill = str(tbill)

class  GroceriesWindow(Screen):
        tbill = 0
        my_textl =  StringProperty("")
        my_textm =  StringProperty("")
        my_textw =  StringProperty("")
        my_textf =  StringProperty("")
        my_texta =  StringProperty("")
        my_textt =  StringProperty("")
        my_texto =  StringProperty("")
        totalbill = StringProperty("")
        lnum = 0
        mnum = 0
        wnum = 0
        fnum = 0
        anum = 0
        tnum = 0
        onum = 0
        def minusl(self,*args):
            if self.lnum > 0:
                self.lnum = self.lnum - 1
                self.my_textl = f"{self.lnum}"
        def on_lbutton_click(self,*args):
                self.lnum = self.lnum + 1
                self.my_textl = f"{self.lnum}"
                self.tbill = self.tbill + self.lnum*75
        def minusm(self,*args):
            if self.mnum > 0:
                self.mnum = self.mnum - 1
                self.my_textm = f"{self.mnum}"
        def on_mbutton_click(self):
                self.mnum = self.mnum + 1
                self.my_textm = f"{self.mnum}"
                self.tbill = self.tbill + self.mnum*100
        def minusw(self,*args):
            if self.wnum > 0:
                self.wnum = self.wnum - 1
                self.my_textw = f"{self.wnum}"
        def on_wbutton_click(self):
                self.wnum = self.wnum + 1
                self.my_textw = f"{self.wnum}"
                self.tbill = self.tbill + self.wnum*250
        def minusf(self,*args):
            if self.fnum > 0:
                self.fnum = self.fnum - 1
                self.my_textf = f"{self.fnum}"
        def on_fbutton_click(self):
                self.fnum = self.fnum + 1
                self.my_textf = f"{self.fnum}"
                self.tbill = self.tbill + self.fnum*750
        def minusa(self,*args):
            if self.anum > 0:
                self.anum = self.anum - 1
                self.my_texta = f"{self.anum}"
        def on_abutton_click(self):
                self.anum = self.anum + 1
                self.my_texta = f"{self.anum}"
                self.tbill = self.tbill + self.anum*200
        def minust(self,*args):
            if self.tnum > 0:
                self.tnum = self.tnum - 1
                self.my_textt = f"{self.tnum}"
        def on_tbutton_click(self):
                self.tnum = self.tnum + 1
                self.my_textt = f"{self.tnum}"
                self.tbill = self.tbill + self.tnum*100
        def minuso(self,*args):
            if self.onum > 0:
                self.onum = self.onum - 1
                self.my_texto = f"{self.onum}"
        def on_obutton_click(self):
                self.onum = self.onum + 1
                self.my_texto = f"{self.onum}"
                self.tbill = self.tbill + self.onum*150
        totalbill = str(tbill)

class  StationaryWindow(Screen):
        tbill = 0
        my_textl =  StringProperty("")
        my_textm =  StringProperty("")
        my_textw =  StringProperty("")
        my_textf =  StringProperty("")
        my_texta =  StringProperty("")
        my_textt =  StringProperty("")
        my_texto =  StringProperty("")
        totalbill = StringProperty("")
        lnum = 0
        mnum = 0
        wnum = 0
        fnum = 0
        anum = 0
        tnum = 0
        onum = 0
        def minusl(self,*args):
            if self.lnum > 0:
                self.lnum = self.lnum - 1
                self.my_textl = f"{self.lnum}"
        def on_lbutton_click(self,*args):
                self.lnum = self.lnum + 1
                self.my_textl = f"{self.lnum}"
                self.tbill = self.tbill + self.lnum*10
        def minusm(self,*args):
            if self.mnum > 0:
                self.mnum = self.mnum - 1
                self.my_textm = f"{self.mnum}"
        def on_mbutton_click(self):
                self.mnum = self.mnum + 1
                self.my_textm = f"{self.mnum}"
                self.tbill = self.tbill + self.mnum*50
        def minusw(self,*args):
            if self.wnum > 0:
                self.wnum = self.wnum - 1
                self.my_textw = f"{self.wnum}"
        def on_wbutton_click(self):
                self.wnum = self.wnum + 1
                self.my_textw = f"{self.wnum}"
                self.tbill = self.tbill + self.wnum*150
        def minusf(self,*args):
            if self.fnum > 0:
                self.fnum = self.fnum - 1
                self.my_textf = f"{self.fnum}"
        def on_fbutton_click(self):
                self.fnum = self.fnum + 1
                self.my_textf = f"{self.fnum}"
                self.tbill = self.tbill + self.fnum*45
        def minusa(self,*args):
            if self.anum > 0:
                self.anum = self.anum - 1
                self.my_texta = f"{self.anum}"
        def on_abutton_click(self):
                self.anum = self.anum + 1
                self.my_texta = f"{self.anum}"
                self.tbill = self.tbill + self.anum*50
        def minust(self,*args):
            if self.tnum > 0:
                self.tnum = self.tnum - 1
                self.my_textt = f"{self.tnum}"
        def on_tbutton_click(self):
                self.tnum = self.tnum + 1
                self.my_textt = f"{self.tnum}"
                self.tbill = self.tbill + self.tnum*25
        def minuso(self,*args):
            if self.onum > 0:
                self.onum = self.onum - 1
                self.my_texto = f"{self.onum}"
        def on_obutton_click(self):
                self.onum = self.onum + 1
                self.my_texto = f"{self.onum}"
                self.tbill = self.tbill + self.onum*50
        totalbill = str(tbill)

#This is required to run the program
class ConfirmWindow(Screen):
        pass
class TheSupApp(App):
    pass

TheSupApp().run() 