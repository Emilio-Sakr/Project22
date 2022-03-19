from tkinter import filedialog
import os
from PIL import Image

class Dir():
    def __init__(self, name) -> None:
        self.name = name
        self.index = 0
        pass

    def getPath(self):
        path = filedialog.askdirectory(initialdir='C:\\', mustexist=True) 
        if path:
            self.path=path+'/'

    def getItems(self):
        f_list=[]
        for f in os.listdir(self.path):
            if f.endswith(('.jpg','.jpeg','.png')):
                f_list.append(f)
        self.dir_list = f_list
        self.items = len(self.dir_list)
        self.index = 0

    def getImage(self):
        image = Image.open(str(self.path)+str(self.dir_list[self.index]))
        resized_image= image.resize((900,600), Image.ANTIALIAS)
        return resized_image

    def getPindex(self):
        self.index+=1
        if self.index>self.items-1:
            self.index=0

    def getMindex(self):
        self.index-=1
        if self.index<(-self.items):
            self.index=0

    def destroy(self):
        del self

    
    
    