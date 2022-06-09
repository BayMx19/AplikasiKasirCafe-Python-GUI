from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;
from PIL import ImageTk, Image 

# Membuat Frame aplikasi
root = Tk()

root.geometry("1275x720+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("Eau de Cafe") # nama aplikasi

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Eau de Cafe',font=('Castellar',39,'bold'),fg='#fde4c3',bg='#302a18', bd=27,width=29) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#1c1c1c') # warna dasar / background
# batas Frame aplikasi

# VARIABLE

# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# variabel menu makanan
e_chickenkatsu=StringVar()
e_beeftoast=StringVar()
e_nasigoreng = StringVar()
e_dimsum = StringVar()
e_ricebowl = StringVar()
e_blackbeefburger = StringVar()
e_spaghettirendang = StringVar()
e_chickensteak = StringVar()
e_tomatosoup = StringVar()

# variabel menu minuman
e_applejuice=StringVar()
e_lemontea = StringVar()
e_milktea = StringVar()
e_espresso = StringVar()
e_vanillalatte = StringVar()
e_airmineral = StringVar()
e_fruitysmoothies = StringVar()
e_chocoboba = StringVar()
e_softdrink = StringVar()

# variabel menu jajanan
e_onionring=StringVar()
e_frenchfries = StringVar()
e_tempura = StringVar()
e_lumpia = StringVar()
e_icecream = StringVar()
e_takoyaki = StringVar()
e_pancake = StringVar()
e_saladbuah = StringVar()
e_pudding = StringVar()

# variabel Harga dalam struk
hargadarimakananvar=StringVar()
hargadariminumanvar=StringVar()
hargadarijajananvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_chickenkatsu.set('0')
e_beeftoast.set('0')
e_nasigoreng.set('0')
e_dimsum.set('0')
e_ricebowl.set('0')
e_blackbeefburger.set('0')
e_spaghettirendang.set('0')
e_chickensteak.set('0')
e_tomatosoup.set('0')

e_applejuice.set('0')
e_lemontea.set('0')
e_milktea.set('0')
e_espresso.set('0')
e_vanillalatte.set('0')
e_airmineral.set('0')
e_fruitysmoothies.set('0')
e_chocoboba.set('0')
e_softdrink.set('0')

e_onionring.set('0')
e_frenchfries.set('0')
e_tempura.set('0')
e_lumpia.set('0')
e_icecream.set('0')
e_takoyaki.set('0')
e_pancake.set('0')
e_saladbuah.set('0')
e_pudding.set('0')


# FUNGSI

# Awal fungsi perhitungan harga total
tax=(11/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadarimakanan,hargadariminuman,hargadarijajanan,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_chickenkatsu.get())
        item2=int(e_beeftoast.get())
        item3=int(e_nasigoreng.get())
        item4=int(e_dimsum.get())
        item5=int(e_ricebowl.get())
        item6=int(e_blackbeefburger.get())
        item7=int(e_spaghettirendang.get())
        item8=int(e_chickensteak.get())
        item9=int(e_tomatosoup.get())

        item10=int(e_applejuice.get())
        item11=int(e_lemontea.get())
        item12=int(e_milktea.get())
        item13=int(e_espresso.get())
        item14=int(e_vanillalatte.get())
        item15=int(e_airmineral.get())
        item16=int(e_fruitysmoothies.get())
        item17=int(e_chocoboba.get())
        item18=int(e_softdrink.get())

        item19=int(e_onionring.get())
        item20=int(e_frenchfries.get())
        item21=int(e_tempura.get())
        item22=int(e_lumpia.get())
        item23=int(e_icecream.get())
        item24=int(e_takoyaki.get())
        item25=int(e_pancake.get())
        item26=int(e_saladbuah.get())
        item27=int(e_pudding.get())

        hargadarimakanan=(item1*27000) + (item2*33000) + (item3*25000) + (item4*22000) + (item5*33000) + (item6*46000) + (item7*38000) \
        + (item8*27000) + (item9*22000)
        hargadariminuman=(item10*20000) + (item11*15000) + (item12*15000) + (item13*22000) + (item14*18000) + (item15*8000) \
        + (item16*22000) + (item17*20000) + (item18*15000)
        hargadarijajanan=(item19*18000) + (item20*36000) + (item21*15000) + (item22*15000) + (item23*16000) + (item24*21000) \
        + (item25*23000) + (item26*18000) + (item27*10000)

        hargadarimakananvar.set(str(hargadarimakanan))
        hargadariminumanvar.set(str(hargadariminuman))
        hargadarijajananvar.set(str(hargadarijajanan))

        subtotalItems=hargadarimakanan+hargadariminuman+hargadarijajanan
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        
        servicetaxvar.set(totaltax)
        
        tottalcost=subtotalItems+totaltax
        totalcostvar.set(str(tottalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# awal fungsi cetak struk
def struk():
    global billnumber,date
    if hargadarimakananvar.get() != '' or hargadarijajananvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'******************\n')
        textStruk.insert(END,'Items:\t\t          Harga Total (Rp)\n')
        textStruk.insert(END,'******************\n')
        if e_chickenkatsu.get()!='0':
            textStruk.insert(END,f'chicken katsu\t\t\tRp. {int(e_chickenkatsu.get())*27000}\n\n')

        if e_beeftoast.get()!='0':
            textStruk.insert(END,f'beef toast\t\t\tRp. {int(e_beeftoast.get())*33000}\n\n')

        if e_nasigoreng.get()!='0':
            textStruk.insert(END,f'nasi goreng\t\t\tRp. {int(e_nasigoreng.get())*25000}\n\n')

        if e_dimsum.get() != '0':
            textStruk.insert(END, f'dimsum:\t\t\tRp. {int(e_dimsum.get()) * 22000}\n\n')

        if e_ricebowl.get() != '0':
            textStruk.insert(END, f'rice bowl:\t\t\tRp. {int(e_ricebowl.get()) * 33000}\n\n')

        if e_blackbeefburger.get() != '0':
            textStruk.insert(END, f'black beef burger:\t\t\tRp. {int(e_blackbeefburger.get()) * 46000}\n\n')

        if e_spaghettirendang.get() != '0':
            textStruk.insert(END, f'spaghetti rendang:\t\t\tRp. {int(e_spaghettirendang.get()) * 38000}\n\n')

        if e_chickensteak.get() != '0':
            textStruk.insert(END, f'chicken steak:\t\t\tRp. {int(e_chickensteak.get()) * 27000}\n\n')

        if e_tomatosoup.get() != '0':
            textStruk.insert(END, f'tomato soup:\t\t\tRp. {int(e_tomatosoup.get()) * 22000}\n\n')

        if e_applejuice.get() != '0':
            textStruk.insert(END, f'apple juice:\t\t\tRp. {int(e_applejuice.get()) * 20000}\n\n')

        if e_lemontea.get() != '0':
            textStruk.insert(END, f'lemon tea:\t\t\tRp. {int(e_lemontea.get()) * 15000}\n\n')

        if e_milktea.get() != '0':
            textStruk.insert(END, f'milktea:\t\t\tRp. {int(e_milktea.get()) * 15000}\n\n')

        if e_espresso.get() != '0':
            textStruk.insert(END, f'espresso:\t\t\tRp. {int(e_espresso.get()) * 22000}\n\n')

        if e_vanillalatte.get() != '0':
            textStruk.insert(END, f'vanilla latte :\t\t\tRp. {int(e_vanillalatte.get()) * 18000}\n\n')

        if e_airmineral.get() != '0':
            textStruk.insert(END, f'air mineral:\t\t\tRp. {int(e_airmineral.get()) * 8000}\n\n')

        if e_fruitysmoothies.get() != '0':
            textStruk.insert(END, f'fruity smoothies:\t\t\tRp. {int(e_fruitysmoothies.get()) * 22000}\n\n')

        if e_chocoboba.get() != '0':
            textStruk.insert(END, f'chocoboba:\t\t\tRp. {int(e_chocoboba.get()) * 20000}\n\n')

        if e_softdrink.get() != '0':
            textStruk.insert(END, f'softdrink:\t\t\tRp. {int(e_softdrink.get()) * 15000}\n\n')

        if e_onionring.get() != '0':
            textStruk.insert(END, f'onionring:\t\t\tRp. {int(e_onionring.get()) * 18000}\n\n')

        if e_frenchfries.get() != '0':
            textStruk.insert(END, f'frenchfries:\t\t\tRp. {int(e_frenchfries.get()) * 36000}\n\n')

        if e_tempura.get() != '0':
            textStruk.insert(END, f'tempura:\t\t\tRp. {int(e_tempura.get()) * 15000}\n\n')

        if e_lumpia.get() != '0':
            textStruk.insert(END, f'lumpia:\t\t\tRp. {int(e_lumpia.get()) * 1500}\n\n')

        if e_icecream.get() != '0':
            textStruk.insert(END, f'icecream:\t\t\tRp. {int(e_icecream.get()) * 16000}\n\n')

        if e_takoyaki.get() != '0':
            textStruk.insert(END, f'takoyaki:\t\t\tRp. {int(e_takoyaki.get()) * 21000}\n\n')

        if e_pancake.get() != '0':
            textStruk.insert(END, f'pancake:\t\t\tRp. {int(e_pancake.get()) * 23000}\n\n')

        if e_saladbuah.get() != '0':
            textStruk.insert(END, f'saladbuah:\t\t\tRp. {int(e_saladbuah.get()) * 18000}\n\n')

        if e_pudding.get() != '0':
            textStruk.insert(END, f'pudding:\t\t\tRp. {int(e_pudding.get()) * 10000}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadarimakananvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari makanan\t\t\tRp. {hargadarimakanan}\n\n')
        if hargadariminumanvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari minuman\t\t\tRp. {hargadariminuman}\n\n')
        if hargadarijajananvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari jajanan\t\t\tRp. {hargadarijajanan}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')
# Batas fungsi simpan dalam perangkat 

# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_chickenkatsu.set('0')
    e_beeftoast.set('0')
    e_nasigoreng.set('0')
    e_milktea.set('0')
    e_espresso.set('0')
    e_vanillalatte.set('0')
    e_airmineral.set('0')
    e_fruitysmoothies.set('0')
    e_chocoboba.set('0')
    e_softdrink.set('0')

    e_onionring.set('0')
    e_frenchfries.set('0')
    e_tempura.set('0')
    e_lumpia.set('0')
    e_icecream.set('0')
    e_takoyaki.set('0')
    e_pancake.set('0')
    e_saladbuah.set('0')
    e_pudding.set('0')
    # batas untuk variables

    textchickenkatsu.config(state=DISABLED)
    textbeeftoast.config(state=DISABLED)
    textnasigoreng.config(state=DISABLED)
    textdimsum.config(state=DISABLED)
    textricebowl.config(state=DISABLED)
    textblackbeefburger.config(state=DISABLED)
    textspaghettirendang.config(state=DISABLED)
    textchickensteak.config(state=DISABLED)
    texttomatosoup.config(state=DISABLED)

    textapplejuice.config(state=DISABLED)
    textlemontea.config(state=DISABLED)
    textmilktea.config(state=DISABLED)
    textespresso.config(state=DISABLED)
    textvanillalatte.config(state=DISABLED)
    textairmineral.config(state=DISABLED)
    textfruitysmoothies.config(state=DISABLED)
    textchocoboba.config(state=DISABLED)
    textsoftdrink.config(state=DISABLED)

    textonionring.config(state=DISABLED)
    textfrenchfries.config(state=DISABLED)
    texttempura.config(state=DISABLED)
    textlumpia.config(state=DISABLED)
    texticecream.config(state=DISABLED)
    texttakoyaki.config(state=DISABLED)
    textpancake.config(state=DISABLED)
    textsaladbuah.config(state=DISABLED)
    textpudding.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    hargadariminumanvar.set('')
    hargadarimakananvar.set('')
    hargadarijajananvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')
# batas fungsi reset

# mengaktifkan fungsi entry menu makanan
def chickenkatsu():
    if var1.get()==1:
        textchickenkatsu.config(state=NORMAL)
        textchickenkatsu.delete(0,END)
        textchickenkatsu.focus()
    else:
        textchickenkatsu.config(state=DISABLED)
        e_chickenkatsu.set('0')

def beeftoast():
    if var2.get()==1:
        textbeeftoast.config(state=NORMAL)
        textbeeftoast.delete(0,END)
        textbeeftoast.focus()
    else:
        textbeeftoast.config(state=DISABLED)
        e_beeftoast.set('0')

def nasigoreng():
    if var3.get()==1:
        textnasigoreng.config(state=NORMAL)
        textnasigoreng.delete(0,END)
        textnasigoreng.focus()
    else:
        textnasigoreng.config(state=DISABLED)
        e_nasigoreng.set('0')

def dimsum():
    if var4.get()==1:
        textdimsum.config(state=NORMAL)
        textdimsum.delete(0,END)
        textdimsum.focus()

    else:
        textdimsum.config(state=DISABLED)
        e_dimsum.set('0')

def ricebowl ():
    if var5.get()==1:
        textricebowl.config(state=NORMAL)
        textricebowl.delete(0,END)
        textricebowl.focus()
    else:
        textricebowl.config(state=DISABLED)
        e_ricebowl.set('0')

def blackbeefburger():
    if var6.get()==1:
        textblackbeefburger.config(state=NORMAL)
        textblackbeefburger.delete(0,END)
        textblackbeefburger.focus()
    else:
        textblackbeefburger.config(state=DISABLED)
        e_blackbeefburger.set('0')

def spaghettirendang():
    if var7.get()==1:
        textspaghettirendang.config(state=NORMAL)
        textspaghettirendang.delete(0,END)
        textspaghettirendang.focus()
    else:
        textspaghettirendang.config(state=DISABLED)
        e_spaghettirendang.set('0')

def chickensteak():
    if var8.get()==1:
        textchickensteak.config(state=NORMAL)
        textchickensteak.delete(0,END)
        textchickensteak.focus()
    else:
        textchickensteak.config(state=DISABLED)
        e_chickensteak.set('0')

def tomatosoup():
    if var9.get()==1:
        texttomatosoup.config(state=NORMAL)
        texttomatosoup.delete(0,END)
        texttomatosoup.focus()
    else:
        texttomatosoup.config(state=DISABLED)
        e_tomatosoup.set('0')
# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu minuman
def applejuice():
    if var10.get()==1:
        textapplejuice.config(state=NORMAL)
        textapplejuice.delete(0,END)
        textapplejuice.focus()
    else:
        textapplejuice.config(state=DISABLED)
        e_applejuice.set('0')

def lemontea():
    if var11.get()==1:
        textlemontea.config(state=NORMAL)
        textlemontea.focus()
        textlemontea.delete(0, END)
    else:
        textlemontea.config(state=DISABLED)
        e_lemontea.set('0')

def milktea():
    if var12.get()==1:
        textmilktea.config(state=NORMAL)
        textmilktea.delete(0,END)
        textmilktea.focus()
    else:
        textmilktea.config(state=DISABLED)
        e_milktea.set('0')

def espresso():
    if var13.get()==1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0,END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_espresso.set('0')

def vanillalatte():
    if var14.get()==1:
        textvanillalatte.config(state=NORMAL)
        textvanillalatte.delete(0,END)
        textvanillalatte.focus()
    else:
        textvanillalatte.config(state=DISABLED)
        e_vanillalatte.set('0')

def airmineral():
    if var15.get()==1:
        textairmineral.config(state=NORMAL)
        textairmineral.delete(0,END)
        textairmineral.focus()
    else:
        textairmineral.config(state=DISABLED)
        e_airmineral.set('0')

def fruitysmoothies():
    if var16.get()==1:
        textfruitysmoothies.config(state=NORMAL)
        textfruitysmoothies.delete(0,END)
        textfruitysmoothies.focus()
    else:
        textfruitysmoothies.config(state=DISABLED)
        e_fruitysmoothies.set('0')

def chocoboba():
    if var17.get()==1:
        textchocoboba.config(state=NORMAL)
        textchocoboba.delete(0,END)
        textchocoboba.focus()
    else:
        textchocoboba.config(state=DISABLED)
        e_chocoboba.set('0')

def softdrink(): 
    if var18.get()==1:
        textsoftdrink.config(state=NORMAL)
        textsoftdrink.delete(0,END)
        textsoftdrink.focus()
    else:
        textsoftdrink.config(state=DISABLED)
        e_softdrink.set('0')
# batas mengaktifkan entry minuman

# mengaktifkan entry menu jajanan
def onionring():
    if var19.get()==1:
        textonionring.config(state=NORMAL)
        textonionring.focus()
        textonionring.delete(0,END)
    else:
        textonionring.config(state=DISABLED)
        e_onionring.set('0')

def frenchfries():
    if var20.get()==1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.delete(0,END)
        textfrenchfries.focus()
    else:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0')

def tempura():
    if var21.get()==1:
        texttempura.config(state=NORMAL)
        texttempura.delete(0,END)
        texttempura.focus()
    else:
        texttempura.config(state=DISABLED)
        e_tempura.set('0')

def lumpia():
    if var22.get()==1:
        textlumpia.config(state=NORMAL)
        textlumpia.delete(0,END)
        textlumpia.focus()
    else:
        textlumpia.config(state=DISABLED)
        e_lumpia.set('0')

def icecream():
    if var23.get()==1:
        texticecream.config(state=NORMAL)
        texticecream.delete(0,END)
        texticecream.focus()
    else:
        texticecream.config(state=DISABLED)
        e_icecream.set('0')

def takoyaki():
    if var24.get()==1:
        texttakoyaki.config(state=NORMAL)
        texttakoyaki.delete(0,END)
        texttakoyaki.focus()
    else:
        texttakoyaki.config(state=DISABLED)
        e_takoyaki.set('0')

def pancake():
    if var25.get()==1:
        textpancake.config(state=NORMAL)
        textpancake.delete(0,END)
        textpancake.focus()
    else:
        textpancake.config(state=DISABLED)
        e_pancake.set('0')

def saladbuah():
    if var26.get()==1:
        textsaladbuah.config(state=NORMAL)
        textsaladbuah.delete(0,END)
        textsaladbuah.focus()
    else:
        textsaladbuah.config(state=DISABLED)
        e_saladbuah.set('0')

def pudding():
    if var27.get()==1:
        textpudding.config(state=NORMAL)
        textpudding.delete(0,END)
        textpudding.focus()
    else:
        textpudding.config(state=DISABLED)
        e_pudding.set('0')


# FRAME KIRI

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=12)
hargaFrame.pack(side=BOTTOM)

makananFrame=LabelFrame(menuFrame,text=' Makanan ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
makananFrame.pack(side=LEFT)

minumanFrame=LabelFrame(menuFrame,text=' Minuman ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=LEFT)

jajananFrame=LabelFrame(menuFrame,text=' Jajanan ',font=('Castellar',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
jajananFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu makanan
chickenkatsu=Checkbutton(makananFrame,text=' Chicken Katsu ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=chickenkatsu, bg='#f6f6f6')
chickenkatsu.grid(row=0,column=0,sticky=W)

beeftoast=Checkbutton(makananFrame,text=' Beef Toast ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=beeftoast, bg='#f6f6f6')
beeftoast.grid(row=1,column=0,sticky=W)

nasigoreng=Checkbutton(makananFrame,text=' Nasi Goreng ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=nasigoreng, bg='#f6f6f6')
nasigoreng.grid(row=2,column=0,sticky=W)

dimsum=Checkbutton(makananFrame,text=' Dimsum ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=dimsum, bg='#f6f6f6')
dimsum.grid(row=3,column=0,sticky=W)

ricebowl=Checkbutton(makananFrame,text=' Rice Bowl ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=ricebowl, bg='#f6f6f6')
ricebowl.grid(row=4,column=0,sticky=W)

blackbeefburger=Checkbutton(makananFrame,text= ' Black Beef Burger ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=blackbeefburger, bg='#f6f6f6')
blackbeefburger.grid(row=5,column=0,sticky=W)

spaghettirendang=Checkbutton(makananFrame,text=' Spaghetti Rendang ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=spaghettirendang, bg='#f6f6f6')
spaghettirendang.grid(row=6,column=0,sticky=W)

chickensteak=Checkbutton(makananFrame,text=' Chicken Steak ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=chickensteak, bg='#f6f6f6')
chickensteak.grid(row=7,column=0,sticky=W)

tomatosoup=Checkbutton(makananFrame,text=' Tomato Soup ',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=tomatosoup, bg='#f6f6f6')
tomatosoup.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item makanan
textchickenkatsu=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_chickenkatsu)
textchickenkatsu.grid(row=0,column=1)

textbeeftoast=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_beeftoast)
textbeeftoast.grid(row=1,column=1)

textnasigoreng=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_nasigoreng)
textnasigoreng.grid(row=2,column=1)

textdimsum=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_dimsum)
textdimsum.grid(row=3,column=1)

textricebowl=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_ricebowl)
textricebowl.grid(row=4,column=1)

textblackbeefburger=Entry(makananFrame,font=('Calibri','16','bold'),bd=7, width=8,state=DISABLED,textvar=e_blackbeefburger)
textblackbeefburger.grid(row=5,column=1)

textspaghettirendang=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_spaghettirendang)
textspaghettirendang.grid(row=6,column=1)

textchickensteak=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_chickensteak)
textchickensteak.grid(row=7,column=1)

texttomatosoup=Entry(makananFrame,font=('Calibri','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_tomatosoup)
texttomatosoup.grid(row=8,column=1)


# membuat tampilan daftar menu minuman
applejuice=Checkbutton(minumanFrame,text='Apple Juice',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=applejuice, bg='#f6f6f6')
applejuice.grid(row=0,column=0,sticky=W)

lemontea=Checkbutton(minumanFrame,text='Lemon Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=lemontea, bg='#f6f6f6')
lemontea.grid(row=1,column=0,sticky=W)

milktea=Checkbutton(minumanFrame,text='Milk Tea',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=milktea, bg='#f6f6f6')
milktea.grid(row=2,column=0,sticky=W)

espresso=Checkbutton(minumanFrame,text='Espresso',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=espresso, bg='#f6f6f6')
espresso.grid(row=3,column=0,sticky=W)

vanillalatte=Checkbutton(minumanFrame,text='Vanilla Latte',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var14,
                        command=vanillalatte, bg='#f6f6f6')
vanillalatte.grid(row=4,column=0,sticky=W)

airmineral=Checkbutton(minumanFrame,text='Air Mineral',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var15,
                        command=airmineral, bg='#f6f6f6')
airmineral.grid(row=5,column=0,sticky=W)

fruitysmoothies=Checkbutton(minumanFrame,text='Fruity Smoothies',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var16,
                        command=fruitysmoothies, bg='#f6f6f6')
fruitysmoothies.grid(row=6,column=0,sticky=W)

chocoboba=Checkbutton(minumanFrame,text='Choco Boba',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var17,
                        command=chocoboba, bg='#f6f6f6')
chocoboba.grid(row=7,column=0,sticky=W)

softdrink=Checkbutton(minumanFrame,text='Soft Drink',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var18,
                        command=softdrink, bg='#f6f6f6')
softdrink.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item minuman
textapplejuice=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_applejuice)
textapplejuice.grid(row=0,column=1)

textlemontea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_lemontea)
textlemontea.grid(row=1,column=1)

textmilktea=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_milktea)
textmilktea.grid(row=2,column=1)

textespresso=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_espresso)
textespresso.grid(row=3,column=1)

textvanillalatte=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_vanillalatte)
textvanillalatte.grid(row=4,column=1)

textairmineral=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_airmineral)
textairmineral.grid(row=5,column=1)

textfruitysmoothies=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_fruitysmoothies)
textfruitysmoothies.grid(row=6,column=1)

textchocoboba=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_chocoboba)
textchocoboba.grid(row=7,column=1)

textsoftdrink=Entry(minumanFrame,font=('Calibri','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_softdrink)
textsoftdrink.grid(row=8,column=1)


# membuat tampilan daftar menu jajanan
onionring=Checkbutton(jajananFrame,text='Onion Ring',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var19,
            command=onionring, bg='#f6f6f6')
onionring.grid(row=0,column=0,sticky=W)

frenchfries=Checkbutton(jajananFrame,text='French Fries',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var20,
            command=frenchfries, bg='#f6f6f6')  
frenchfries.grid(row=1,column=0,sticky=W)

tempura=Checkbutton(jajananFrame,text='Tempura',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var21,
            command=tempura, bg='#f6f6f6')
tempura.grid(row=2,column=0,sticky=W)

lumpia=Checkbutton(jajananFrame,text='Lumpia',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var22,
            command=lumpia, bg='#f6f6f6')
lumpia.grid(row=3,column=0,sticky=W)

icecream=Checkbutton(jajananFrame,text='Ice Cream',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var23,
            command=icecream, bg='#f6f6f6')
icecream.grid(row=4,column=0,sticky=W)

takoyaki=Checkbutton(jajananFrame,text='Takoyaki',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var24,
            command=takoyaki, bg='#f6f6f6')
takoyaki.grid(row=5,column=0,sticky=W)

pancake=Checkbutton(jajananFrame,text='Pancake',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var25,
            command=pancake, bg='#f6f6f6')
pancake.grid(row=6,column=0,sticky=W)

saladbuah=Checkbutton(jajananFrame,text='Salad Buah',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var26,
            command=saladbuah, bg='#f6f6f6')
saladbuah.grid(row=7,column=0,sticky=W)

pudding=Checkbutton(jajananFrame,text='Pudding',font=('Calibri',16,'bold'),onvalue=1,offvalue=0,variable=var27,
            command=pudding, bg='#f6f6f6')
pudding.grid(row=8,column=0,sticky=W)


# menambahkan fields entri untuk item jajanan
textonionring = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_onionring)
textonionring.grid(row=0, column=1)

textfrenchfries = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_frenchfries)
textfrenchfries.grid(row=1, column=1)

texttempura = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_tempura)
texttempura.grid(row=2, column=1)

textlumpia = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_lumpia)
textlumpia.grid(row=3, column=1)

texticecream = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_icecream)
texticecream.grid(row=4, column=1)

texttakoyaki = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_takoyaki)
texttakoyaki.grid(row=5, column=1)

textpancake = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_pancake)
textpancake.grid(row=6, column=1)

textsaladbuah = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED, textvariable=e_saladbuah)
textsaladbuah.grid(row=7, column=1)

textpudding = Entry(jajananFrame, font=('Calibri','16','bold'),bd=7,width=7, state=DISABLED,textvariable=e_pudding)
textpudding.grid(row=8, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=4,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariMakanan=Label(hargaFrame,text='    HARGA DARI MAKANAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMakanan.grid(row=0,column=0)

textHargadariMakanan=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadarimakananvar)
textHargadariMakanan.grid(row=0,column=1,padx=41)

LabelHargadariMinuman=Label(hargaFrame,text='    HARGA DARI MINUMAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

LabelHargadariJajanan=Label(hargaFrame,text='  HARGA DARI JAJANAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariJajanan.grid(row=2,column=0)

textHargadariJajanan=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadarijajananvar)
textHargadariJajanan.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()
