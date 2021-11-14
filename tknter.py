from tkinter import scrolledtext  
from tkinter import *  
from tkinter import Menu  
from tkinter import filedialog
import fileinput
import pyperclip
from tkinter.messagebox import * 
from tkinter.filedialog import * 

def undo(*argv):
    txt.edit_undo()

def open_file():
    temp = askopenfilename()
    txt.delete('1.0', END)
    for i in fileinput.input(temp):
        txt.insert(END, i)
def save_file():
    temp = asksaveasfilename()
    letter = txt.get(1.0,END)
    f = open(temp,"w")
    f.write(letter)
    f.close() 
def paste_file():
    x, y = 0, 0
    p = window.Tk()
    x, y = p.winfo_pointerxy()
    txt.insert(x, y, pyperclip.paste())
def copy_file():
    txt.clipboard_clear()
    txt.clipboard_append(txt.get(1.0, END))


def open_new_window(): 
    new_window = Tk()
    new_window.title("Найти") 
    new_window.geometry("450x200") 

    label1 = Label(new_window, text ="Что: ")
    label1.place(x = 10, y = 16)

    tex = Text(new_window, width=25, height=1)
    tex.place(x = 55, y = 16)
    
    def find_nxt():
        txt1 = txt.get('1.0', 'end-1c')
        txt2 = tex.get('1.0', 'end-1c')
        index = txt1.find(txt2)
        txt.mark_set("insert", "1.0+%d chars" % index)
        new_window.destroy()

    btn = Button(new_window, text="Найти далее", command=find_nxt)
    btn.place(x = 280, y = 15)

def task():
    new_window = Tk()
    new_window.title("Задания 2, 4, 6:") 
    new_window.geometry("450x250") 
    label1 = Label(new_window, text ="")
    label1.place(x = 200, y = 58)
    label2 = Message( new_window, width = 9*9)
    label2.place(x = 100, y = 20)
    label3 = Message( new_window, width = 9*9)
    label3.place(x = 200, y = 20)
    label4 = Message( new_window, width = 10*9)
    label4.place(x = 300, y = 20)
    def task_2():
        label1.configure(text = str(chr(65)+chr(71)+chr(69)))
        label2.configure(text = "")
        label3.configure(text = "")
        label4.configure(text = "")
    btn1 = Button(new_window, text="Задание 2",  command=task_2)
    btn1.place(x = 10, y = 20) 

    def task_4():
        txt1 = txt.get('1.0', 'end-1c')
        index = txt1.find('a')
        index1 =txt1.find('z') 
        b = True
        while index1>=index:
            if ord(txt1[index]) < 96 or ord(txt1[index]) >123:
                b = False
                break
            index+=1
        if b == True:
            label1.configure(text = "True")
        else:
            label1.configure(text = "False")

        label2.configure(text = "")
        label3.configure(text = "")
        label4.configure(text = "")
    btn2 = Button(new_window, text="Задание 4",  command=task_4)
    btn2.place(x = 10, y = 60)  

    def task_6():
        label1.configure(text = "")

        label3.configure(text = "999999999 088888888 007777777 000666666 000055555 000004444 000000333 000000022 000000001")
        label4.configure(text = "0123456789 1234567890 2345678901 3456789012 4567890123 5678901234 6789012345 7890123456 8901234567 9012345678")
        label2.configure(text = "100000000 020000000 003000000 000400000 000050000 000006000 000000700 000000080 000000009")
    btn3 = Button(new_window, text="Задание 6",  command=task_6)
    btn3.place(x = 10, y = 100) 
    

def open_new_window1(): 
    new_window = Tk()
    new_window.title("Заменить") 
    new_window.geometry("450x200") 

    label1 = Label(new_window, text ="Что: ")
    label1.place(x = 10, y = 16)
    tex1 = Text(new_window, width=25, height=1)
    tex1.place(x = 55, y = 16)
    label2 = Label(new_window, text ="Чем: ")
    label2.place(x = 10, y = 50)
    tex2 = Text(new_window, width=25, height=1)
    tex2.place(x = 55, y = 50)

    def replace():
        txt1 = txt.get('1.0', 'end-1c')
        txt2 = tex1.get('1.0', 'end-1c')
        tex = tex2.get('1.0', 'end-1c')

        txt1 = txt1.replace(txt2, tex)
        txt.delete('1.0', END)
        for i in txt1:
            txt.insert(END, i)
        new_window.destroy()

    btn1 = Button(new_window, text="Заменить",  command=replace)
    btn1.place(x = 280, y = 15)

window = Tk()  
window.title("Блокнот.py")  
window.geometry()  

txt = scrolledtext.ScrolledText(window, undo = True)  
txt.grid(column=0, row=0) 

menu = Menu(window)  
item_file = Menu(menu, tearoff=0)  
item_edit = Menu(menu, tearoff=0)  
item_format = Menu(menu, tearoff=0)  
item_view = Menu(menu, tearoff=0)  
item_reference = Menu(menu, tearoff=0)  

item_file.add_command(label='Создать', state = DISABLED)  
item_file.add_command(label='Новое окно', state = DISABLED)  
item_file.add_command(label='Открыть...', accelerator = 'CTRL + O', command = open_file)  
item_file.add_command(label='Сохранить', accelerator = 'CTRL + S', command = save_file)  
item_file.add_command(label='Сохранить как...', accelerator = 'CTRL + S', command = save_file)  
item_file.add_separator()  
item_file.add_command(label='Параметры страницы...', state = DISABLED)  
item_file.add_command(label='Печать', state = DISABLED)  
item_file.add_separator()  
item_file.add_command(label='Выход', command = window.quit)  

item_edit.add_command(label='Отменить', accelerator = 'CTRL + Z', command = undo)  
item_edit.add_separator()  
item_edit.add_command(label='Вырезать', state = DISABLED)  
item_edit.add_command(label='Копировать', accelerator = 'CTRL + C', command = copy_file)  
item_edit.add_command(label='Вставить', accelerator = 'CTRL + V', command = paste_file)  
item_edit.add_command(label='Удалить', state = DISABLED)  
item_edit.add_separator()  
item_edit.add_command(label='Найти с помощью Bing...', state = DISABLED)  
item_edit.add_command(label='Найти...', accelerator = 'CTRL + F', command = open_new_window)  
item_edit.add_command(label='Найти далее', state = DISABLED)  
item_edit.add_command(label='Найти ранее', state = DISABLED)  
item_edit.add_command(label='Заменить...', accelerator = 'CTRL + H', command = open_new_window1)  
item_edit.add_separator()  
item_edit.add_command(label='Выделить все', state = DISABLED)  
item_edit.add_command(label='Время и дата', state = DISABLED)  


item_format.add_command(label='Перенос по словам', state = DISABLED)  
item_format.add_command(label='Шрифт...', state = DISABLED) 

item_view.add_command(label='Масштаб', state = DISABLED)  
item_view.add_command(label='Строка состояния', state = DISABLED) 

item_reference.add_command(label='Посмотреть справку', state = DISABLED) 
item_reference.add_command(label='Отправить отзыв', state = DISABLED) 
item_reference.add_separator()  
item_reference.add_command(label='О программе', command = task) 

window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-f>", open_new_window)
window.bind("<Control-h>", open_new_window1)
window.bind("<Control-c>", copy_file)
window.bind("<Control-v>", paste_file)
window.bind("<Control-z>", undo)

menu.add_cascade(label='Файл', menu=item_file)  
menu.add_cascade(label='Правка', menu=item_edit)  
menu.add_cascade(label='Формат', menu=item_format) 
menu.add_cascade(label='Вид', menu=item_view)  
menu.add_cascade(label='Справка', menu=item_reference)  

window.config(menu=menu)  
window.mainloop()