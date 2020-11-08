# GUITranslator.PY
from tkinter import *
#จากไลบรารีชื่อ tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk # ttk is theme of tk
###-------Goole Translate-------
from googletrans import Translator
translator = Translator() #สร้างฟังชั่นแปลภาษา

    
    

GUI = Tk() #ส้รางหน้าต่างหลัก
GUI.geometry('500x300') #กว้าง X สูง
GUI.title('โปรแกรมแปลภาษา By Weerawat')
#-----Config-----
FONT = ('Angsana New',12)

#-----Label-----
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()

# ----Enrty (ช่องกรอกข้อความ)------
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)

# ----Button (ปุ่มแปล)------
def Translate():
    vocab = v_vocab.get() #.get คือการให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print( vocab + ' : ' + meaning.text)
    print ( meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text) #สั่งโชว์มน GUI
   

B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10) # show ปุ่มขึ้นมาวางจากบนลงล่าง
#-----Label-----
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()
#-----Result-------  
v_result = StringVar()# กล่องเเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label (GUI,textvariable=v_result, font=FONT2, foreground='green')
R1.pack()



GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดจนกว่าจะปิด (บรรทัดสุดท้าย)
