import os
import tkinter as tk
from tkinter import Menu,Menubutton
from tkinter import filedialog
from tkinter import *
import cv2
from PIL import Image,ImageTk
import image
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib


#from mainfunc import main
top = tk.Tk()
#top = tk.Toplevel()
top.title("Image processing")
top.geometry("1024x700")
#imgicon = ImageTk.PhotoImage(file=os.path.join(r'D:\study materials\IV-I\MAJOR\codings\partOCR\imgs','nepread.ico'))
#top.tk.call('wm', 'iconphoto', top._w, imgicon)
top.resizable(0,0)
h=300
w=400
#***********************************************************
class variables:
    fileName=""
    heighty=int
    widthx=int
    ch=int
    img=image
    size_of=[]
    
        
    frame1 = tk.Frame(top,highlightbackground="black",
                      highlightcolor="black", highlightthickness=1,bg="white",
                      width="405", height="305", colormap="new",bd="0")
    frame1.place(x=605,y=21)
    frame1.pack_propagate(0)
    
    frame3 = tk.Frame(top,highlightbackground="black",
                      highlightcolor="black", highlightthickness=1,bg="white",
                      width="405", height="305", colormap="new",bd="0")
    frame3.place(x=10,y=21)
    frame3.pack_propagate(0)
    
    frame2 = tk.Frame(top,highlightbackground="black",
                      highlightcolor="black", highlightthickness=1,bg="white",
                      width="405", height="305", colormap="new",bd="0")
    frame2.place(x=275,y=330)
    frame2.pack_propagate(0)

    
    
    L1=tk.Label(frame1,bg="white",fg="blue",text="Processed image:")
    L1.pack()

    L3=tk.Label(frame3,bg="white",fg="blue",text="Original image:")
    L3.pack()
    
    L2=tk.Label(frame2,bg="white",fg="blue",text="Histogram:")
    L2.pack()
    
    L11=tk.Label(top,fg="black",text="Original Image:")
    L11.place(x=50,y=5)
    L11.pack_propagate(0)

    L13=tk.Label(top,fg="black",text="Processed Image:")
    L13.place(x=700,y=5)
    L13.pack_propagate(0)
    
    L12=tk.Label(top,fg="black",text="Histogram:")
    L12.place(x=330,y=325)
    L12.pack_propagate(0)
    
    #L=tk.Label(frame2,bg="white",fg="green",text="(Your image appears here)")
    #L.pack()
      
#***********************************************************
def design_fun():
    
    choose_but = tk.Button(top,text ="Choose image",font='Ariel 9',compound="right",command=choose)
    
    choose_but.place(x=460,y=100)
    #mb = tk.Button(top,text ="Choose image",font='Ariel 9',compound="right")
    mb=  Menubutton ( top, text="Operations",font='Ariel 9',compound="right", relief=RAISED )
    mb.place(x=460,y=150)
    mb.menu =  Menu ( mb, tearoff = 0 )
    
    mb["menu"] =  mb.menu
    
    
    mb.menu.add_checkbutton ( label="Min Filter",command=min_filter)#,command=choose)#,variable=mayoVar )
    mb.menu.add_checkbutton ( label="Max Filter",command=max_filter)#,variable=ketchVar )
    mb.menu.add_checkbutton ( label="Mean Filter",command=mean_filter)
    mb.menu.add_checkbutton ( label="Median Filter",command=median_filter)
    mb.menu.add_checkbutton ( label="Weighted Filter",command=weighted_filter)
    mb.menu.add_checkbutton ( label="Contrast Stretching")
    mb.menu.add_checkbutton ( label="Sharpening")
    mb.menu.add_checkbutton ( label="Global Binarization",command=global_binarization)
    mb.menu.add_checkbutton ( label="Local Binarization")
    mb.menu.add_checkbutton ( label="Edge Detection")
    mb.menu.add_checkbutton ( label="High Pass Filter")
    mb.menu.add_checkbutton ( label="Low Pass Filter")
    mb.menu.add_checkbutton ( label="clear",command=clear)
    
    
    mb.pack()
    
    
    
def clear():
    variables.L3.pack_forget()
    variables.L1.pack_forget()
    
#***********************************************************
def call_exit():
    exit(0)
#***********************************************************
def choose():
    import gray
    import image as img1
    variables.fileName=""
    variables.fileName=filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),
                                                             ("PNG","*.png"),("All Files","*.*")))  

    if (variables.fileName!=""):
        img = Image.open(variables.fileName)
        print(img.size)
        #img2=np.zeros((w,h,1),np.uint8)        
        ph1=resize_img(img)
        print(ph1.size)      
        
         
        
    
        ph1 = ph1.load()
        img1=gray.grayscale(ph1,400,300)
        '''for i in range(0,400):
            for j in range(0,300):
                img2[j,i]=ph1[i,j]'''
        variables.img = img1 
        pi = Image.frombytes("L", (w,h), img1.tobytes())
        ph=ImageTk.PhotoImage(pi)
        
        
        
        variables.L3.pack_forget()
        variables.frame3.update()

        variables.L3=tk.Label(variables.frame3,image=ph)
        variables.L3.image=ph
        variables.L3.pack()

#***********************************************************    
def call_main():
    if (variables.fileName!=""):
        a = main(variables.img)
        variables.output_txt.insert(tk.END, a)
#*********************************************************** 
def resize_img(img):
    
    img = img.resize((400,300),Image.ANTIALIAS) #(a high-quality downsampling filter)       
    return img
#***********************************************************

#************************************************************************
def min_filter():
    import minfilter
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=minfilter.minfilter(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after min filteration of the picture')
    plt.show()
    

def max_filter():
    import maxfilter
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=maxfilter.maxfilter(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after max filteration of the picture')
    plt.show()

def mean_filter():
    import meanfilter
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=meanfilter.meanfilter(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after mean filteration of the picture')
    plt.show()

def median_filter():
    import medianfilter
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=medianfilter.medianfilter(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after median filteration of the picture')
    plt.show()

def weighted_filter():
    import weightedfilter
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=weightedfilter.weightedfilter(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after weighted filteration of the picture')
    plt.show()

'''def contrast_stretching():
    import gray
    import image as img1
    h,w=variables.img.size
    
    img1 = variables.img
    
    img1 = img1.load()
    
    
    img1=gray.grayscale(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (h,w), img1.tobytes())
    ph=ImageTk.PhotoImage(pi)
    variables.img=ph
    
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()'''

def global_binarization():
    import binarize
    import image as img1
    
    
    img1 = variables.img
    
    #img1 = img1.load()
    
    
    img1=binarize.binarize(img1,h,w)
    
    variables.img=None
    variables.img=img1
    
    
    
    pi = Image.frombytes("L", (w,h), img1.tobytes())
    
    ph=ImageTk.PhotoImage(pi)
    
    variables.L1.pack_forget()
    variables.frame1.update()
    variables.L1=tk.Label(variables.frame1,image=ph)
    variables.L1.image=ph
    variables.L1.pack()
    
    hist = cv2.calcHist([img1],[0],None,[256],[0,256])
    plt.hist(img1.ravel(),256,[0,256])
    plt.title('Histogram after global binarization of the picture')
    plt.show()

    
design_fun()


top.mainloop()

