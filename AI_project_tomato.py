from tkinter import *
from PIL import ImageTk, Image
from keras.utils import load_img, img_to_array
from keras.models import load_model
import os
from tkinter import messagebox
from functools import partial
import cv2
import numpy as np
from tkinter import filedialog
from tkinter import ttk

# Thư viện


cs1 = Tk()
cs1.geometry('500x400+540+260')
cs1.title('TOMATO')
cs1.iconbitmap('C:\setupNGOC\\cachua_ico.ico')
cs1.resizable(False, False)
canvas1 = Canvas(cs1, width=500, height=400)
bg1 = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\bg2.png'))
canvas1.create_image(0, 0, anchor=NW, image=bg1)
canvas1.pack()
cs1.withdraw()

# ************************************************************************************Window2_test_leaf***********************************************************************
cs2 = Toplevel(cs1)
cs2.title('CÀ CHUA')
cs2.iconbitmap('C:\setupNGOC\\cachua_ico.ico')
cs2.geometry('1000x600+130+30')
cs2.resizable(False, False)
# window2.withdraw()
canvas_wd2 = Canvas(cs2, width=1000, height=600)
bg_wd2 = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\bg3.png'))
canvas_wd2.create_image(0, 0, anchor=NW, image=bg_wd2)
canvas_wd2.pack()
# frame window2 test leaf
frame_wd2 = Frame(cs2, width=260, height=260)
frame_wd2.place(x=810, y=155)
bg_frame_wd2 = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\upload.png'))
label_frame_wd2 = Label(frame_wd2, image=bg_frame_wd2, bd=1)
label_frame_wd2.pack()
file = 0


def open_file():
    global bg_frame_wd2, file, solution_leaf_label
    filename = filedialog.askopenfilename(initialdir='C:/setupNGOC/tomato_test', title='Select A File',
                                          filetype=(('jpeg files', '*.jpg'), ('png files', '*.png'), ('All', '*.*')))
    file = str(filename)
    image = Image.open(file)
    resized = image.resize((150, 150), Image.ANTIALIAS)
    bg_frame_wd2 = ImageTk.PhotoImage(resized)

    label_frame_wd2.configure(image=bg_frame_wd2)
    solution_leaf_label.configure(text='')
    Label_sol.place_forget()


op_img = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\open.png'))
bt_choose_wd2 = ttk.Button(cs2, command=lambda: open_file(), image=op_img)
bt_choose_wd2.place(x=788, y=325)


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model_h5 = load_model('C:\setupNGOC\\lacachua.h5')
result_check_leaf = ''
a = 'Tên bệnh'


def check_leaf():
    global file, result_check_leaf, solution_leaf_label, a

    img = load_img(file, target_size=(150, 150))
    img = img_to_array(img)
    img = img.astype('float32')
    img = img / 255
    img = np.expand_dims(img, axis=0)
    result = model_h5.predict(img)
    class_name = ['Bacterial', 'Early blight', 'Late blight', 'Leaf Mold', 'Septoria leaf spot',
                  'Spider mites Two-spotted spider mite', 'Tomato Target Spot',
                  'Tomato Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus',
                  'Healthy']
    result_check_leaf = int(np.argmax(result, axis=1))
    a = class_name[result_check_leaf]
    print("Đây là loại:", class_name[result_check_leaf])
    if class_name[result_check_leaf] == 'Healthy':
        solution_leaf_label.configure(text='Kết quả kiểm tra\nCây cà chua không có bệnh!\nChúc mừng!! ')
    else:
        solution_leaf_label.configure(
            text='Kết quả kiểm tra\nCà chua nhiễm bệnh: {}'.format(class_name[result_check_leaf]))


check_img = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\checkkq.png'))
bt_check_leaf = ttk.Button(cs2, text='Check', command=check_leaf, image=check_img)
bt_check_leaf.place(x=850, y=325)
# in ra ket qua tren window2
solution_leaf_label = Label(cs2, text=result_check_leaf,
                            justify=LEFT,
                            font=('Helvetica bold', 16))
solution_leaf_label.place(x=36, y=178)
# solution
Label_sol = LabelFrame(cs2, text='')
Label_sol.place_forget()
my_txt = Message(Label_sol, font=('Helvetica bold', 12, 'bold'),
                 justify=LEFT, text='',
                 width=600)
my_txt.pack()


def sol():
    global solution_leaf_label, my_txt, a, Label_sol
    if a == 'Bacterial':
        txt = open('C:\setupNGOC\giaiphap\\bacterial.txt', 'r', encoding='utf-8').read()
    elif a == 'Early blight':
        txt = open('C:\setupNGOC\giaiphap\\Early_blight.txt', 'r', encoding='utf-8').read()
    elif a == 'Late blight':
        txt = open('C:\setupNGOC\giaiphap\\Late_blight.txt', 'r', encoding='utf-8').read()
    elif a == 'Leaf Mold':
        txt = open('C:\setupNGOC\giaiphap\\Leaf_mood.txt', 'r', encoding='utf-8').read()
    elif a == 'Tomato mosaic virus':
        txt = open('C:\setupNGOC\giaiphap\\mosaic.txt', 'r', encoding='utf-8').read()
    elif a == 'Septoria leaf spot':
        txt = open('C:\setupNGOC\giaiphap\\Septoria.txt', 'r', encoding='utf-8').read()
    elif a == 'Spider mites Two-spotted spider mite':
        txt = open('C:\setupNGOC\giaiphap\\Spider.txt', 'r', encoding='utf-8').read()
    elif a == 'Tomato Target Spot':
        txt = open('C:\setupNGOC\giaiphap\\tatomato_target.txt', 'r', encoding='utf-8').read()
    elif a == 'Tomato Tomato Yellow Leaf Curl Virus':
        txt = open('C:\setupNGOC\giaiphap\\yellow.txt', 'r', encoding='utf-8').read()
    my_txt.configure(text=str(txt))
    Label_sol.configure(text=a)
    Label_sol.place_configure(x=36, y=300)


sol_img = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\solution.png'))
sol_button = ttk.Button(cs2, text='Giải pháp ', command=sol, image=sol_img)
sol_button.place(x=912, y=325)


# Tra cuu
def example():
    global i, h
    ex_frame.place_configure(x=350, y=200)
    ex_frame.configure(text=value_list.get(), font=('Times New Roman', 12, 'bold'))
    mtt_bt.place_configure(x=350, y=420)
    mtp_bt.place(x=450, y=420)
    i, h = 0, 3
    if value_list.get() == 'Bacterial':
        ex_bacterial(ex_mtp)
        mtt_bt.configure(command=lambda: ex_bacterial(ex_mtt))
        mtp_bt.configure(command=lambda: ex_bacterial(ex_mtp))
    elif value_list.get() == 'Early blight':
        ex_early_blight(ex_mtp)
        mtt_bt.configure(command=lambda: ex_early_blight(ex_mtt))
        mtp_bt.configure(command=lambda: ex_early_blight(ex_mtp))
    elif value_list.get() == 'Late blight':
        ex_late_blight(ex_mtp)
        mtt_bt.configure(command=lambda: ex_late_blight(ex_mtt))
        mtp_bt.configure(command=lambda: ex_late_blight(ex_mtp))
    elif value_list.get() == 'Leaf Mold':
        ex_leaf_mood(ex_mtp)
        mtt_bt.configure(command=lambda: ex_leaf_mood(ex_mtt))
        mtp_bt.configure(command=lambda: ex_leaf_mood(ex_mtp))
    elif value_list.get() == 'Septoria leaf spot':
        ex_sep(ex_mtp)
        mtt_bt.configure(command=lambda: ex_sep(ex_mtt))
        mtp_bt.configure(command=lambda: ex_sep(ex_mtp))
    elif value_list.get() == 'Spider mites Two-spotted spider mite':
        ex_spi(ex_mtp)
        mtt_bt.configure(command=lambda: ex_spi(ex_mtt))
        mtp_bt.configure(command=lambda: ex_spi(ex_mtp))
    elif value_list.get() == 'Tomato Target Spot':
        ex_spot(ex_mtp)
        mtt_bt.configure(command=lambda: ex_spot(ex_mtt))
        mtp_bt.configure(command=lambda: ex_spot(ex_mtp))
    elif value_list.get() == 'Tomato mosaic virus':
        ex_mosaic(ex_mtp)
        mtt_bt.configure(command=lambda: ex_mosaic(ex_mtt))
        mtp_bt.configure(command=lambda: ex_mosaic(ex_mtp))
    elif value_list.get() == 'Tomato Tomato Yellow Leaf Curl Virus':
        ex_yellow(ex_mtp)
        mtt_bt.configure(command=lambda: ex_yellow(ex_mtt))
        mtp_bt.configure(command=lambda: ex_yellow(ex_mtp))


list = ['Bacterial', 'Early blight', 'Late blight', 'Leaf Mold', 'Septoria leaf spot',
        'Spider mites Two-spotted spider mite', 'Tomato Target Spot',
        'Tomato Tomato Yellow Leaf Curl Virus', 'Tomato mosaic virus']
value_list = StringVar(cs2)
value_list.set('Tên Bệnh')
question_menu = OptionMenu(cs2, value_list, *list)
question_menu.config(bg='#FFF6BD', bd=0)
question_menu.config(width=25)
question_menu.place_forget()
ex_img = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\search.png'))
ex_button = ttk.Button(cs2, command=example, image=ex_img)
ex_button.place_forget()


def tra_cuu():
    value_list.set('Select an Option')
    sol_button.place_forget()
    Label_sol.place_forget()
    solution_leaf_label.place_forget()
    bt_choose_wd2.place_forget()
    bt_check_leaf.place_forget()
    frame_wd2.place_forget()
    ex_button.place_configure(x=250, y=150)

    question_menu.place_configure(x=36, y=152)


tcuu_icobt = PhotoImage(file='C:\setupNGOC\\tracuu.png')
tcuu_button = ttk.Button(cs2, image=tcuu_icobt, command=tra_cuu)
tcuu_button.place(x=100, y=35)
upload = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\upload.png'))


def check():
    frame_wd2.place_configure(x=810, y=155)
    label_frame_wd2.pack()
    label_frame_wd2.configure(image=upload)
    Label_sol.place_forget()
    bt_check_leaf.place_configure(x=850, y=325)
    bt_choose_wd2.place_configure(x=788, y=325)
    solution_leaf_label.configure(text='')
    solution_leaf_label.place_configure(x=36, y=178)
    sol_button.place_configure(x=912, y=325)
    ex_button.place_forget()
    question_menu.place_forget()
    ex_frame.place_forget()
    mtp_bt.place_forget()
    mtt_bt.place_forget()


check_icobt = PhotoImage(file='C:\setupNGOC\\check.png')
check_button = ttk.Button(cs2, image=check_icobt, command=check)
check_button.place(x=150, y=35)
# tạo frame exam
ex_frame = LabelFrame(cs2, width=600, height=220)
ex_frame.place_forget()
i = 0
h = 3
i1, i2, i3 = 1, 1, 1


def ex_yellow(mt):
    path1 = f'C:\setupNGOC\danhmuc\\yellow\\yellow ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\yellow\\yellow ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\yellow\\yellow ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_mosaic(mt):
    path1 = f'C:\setupNGOC\danhmuc\\mosaic\\mosaic ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\mosaic\\mosaic ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\mosaic\\mosaic ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_spot(mt):
    path1 = f'C:\setupNGOC\danhmuc\\spot\\spot ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\spot\\spot ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\spot\\spot ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_spi(mt):
    path1 = f'C:\setupNGOC\danhmuc\\spi\\spi ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\spi\\spi ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\spi\\spi ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_sep(mt):
    path1 = f'C:\setupNGOC\danhmuc\\sep\\sep ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\sep\\sep ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\sep\\sep ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_leaf_mood(mt):
    path1 = f'C:\setupNGOC\danhmuc\\mood\\mood ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\mood\\mood ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\mood\\mood ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_late_blight(mt):
    path1 = f'C:\setupNGOC\danhmuc\\late\\late ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\late\\late ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\late\\late ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_early_blight(mt):
    path1 = f'C:\setupNGOC\danhmuc\\early\\1 ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\early\\1 ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\early\\1 ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_bacterial(mt):
    path1 = f'C:\setupNGOC\danhmuc\\bacterial\\1 ({i1}).JPG'
    path2 = f'C:\setupNGOC\danhmuc\\bacterial\\1 ({i2 + 1}).JPG'
    path3 = f'C:\setupNGOC\danhmuc\\bacterial\\1 ({i3 + 2}).JPG'
    mt(path1, path2, path3)


def ex_mtt(path1, path2, path3):
    global ex_lb1, ex_lb2, ex_lb3, i, i1, i2, i3, h

    i3 = h - 1
    i2 = i3 - 1
    i1 = i2 - 1
    h = h - 1
    print(i1, i2, i3, h)
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    img3 = Image.open(path3)
    resize1 = img1.resize((150, 150), Image.ANTIALIAS)
    resize2 = img2.resize((150, 150), Image.ANTIALIAS)
    resize3 = img3.resize((150, 150), Image.ANTIALIAS)

    bg_img1 = ImageTk.PhotoImage(resize1)
    bg_img2 = ImageTk.PhotoImage(resize2)
    bg_img3 = ImageTk.PhotoImage(resize3)
    ex_lb1.configure(image=bg_img1)
    ex_lb1.image = bg_img1
    ex_lb2.configure(image=bg_img2)
    ex_lb2.image = bg_img2
    ex_lb3.configure(image=bg_img3)
    ex_lb3.image = bg_img3


def ex_mtp(path1, path2, path3):
    global ex_lb1, ex_lb2, ex_lb3, i, i1, i2, i3, h
    i1 = i + 1
    i2 = i1 + 1
    i3 = i2 + 1
    i = i + 1
    h = i3
    print(i1, i2, i3, i)
    img1 = Image.open(path1)
    img2 = Image.open(path2)
    img3 = Image.open(path3)
    resize1 = img1.resize((150, 150), Image.ANTIALIAS)
    resize2 = img2.resize((150, 150), Image.ANTIALIAS)
    resize3 = img3.resize((150, 150), Image.ANTIALIAS)

    bg_img1 = ImageTk.PhotoImage(resize1)
    bg_img2 = ImageTk.PhotoImage(resize2)
    bg_img3 = ImageTk.PhotoImage(resize3)
    ex_lb1.configure(image=bg_img1)
    ex_lb1.image = bg_img1
    ex_lb2.configure(image=bg_img2)
    ex_lb2.image = bg_img2
    ex_lb3.configure(image=bg_img3)
    ex_lb3.image = bg_img3


mtp = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\muitenphai.png'))
mtp_bt = ttk.Button(cs2, image=mtp)
mtp_bt.place_forget()

mtt = ImageTk.PhotoImage(Image.open('C:\setupNGOC\\muitentrai.png'))
mtt_bt = ttk.Button(cs2, image=mtt)
mtt_bt.place_forget()

ex_lb1 = Label(ex_frame, bg='pink', width=150, height=150)
ex_lb1.place(x=20, y=21)
ex_lb2 = Label(ex_frame, bg='blue', width=150, height=150)
ex_lb2.place(x=225, y=21)
ex_lb3 = Label(ex_frame, bg='green', width=150, height=150)
ex_lb3.place(x=430, y=21)

# **************************************************************************************************man hinh dang nhap***********************************************************
window4 = Toplevel(cs1)
window4.title('CÀ CHUA')
window4.iconbitmap('C:\setupNGOC\\cachua_ico.ico')
window4.geometry('1000x400+170+150')
window4.resizable(False, False)

# intro dang nhap
frame_wd4 = Frame(window4, width=1000, height=400)
frame_wd4.place(x=0, y=0)
label_frame_wd4 = Label(frame_wd4)
label_frame_wd4.pack()
try:

    cap = cv2.VideoCapture('C:\setupNGOC\\intro2.mp4')
    def video_stream():
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label_frame_wd4.imgtk = imgtk
        label_frame_wd4.configure(image=imgtk)
        label_frame_wd4.after(1, video_stream)


    video_stream()

except:
    pass


def frame_show():
    frame_login.place_configure(x=250, y=235)


frame_login = Frame(window4, bg='#fff5c6', width=150, height=155)
frame_login.place_forget()
window4.after(2000, frame_show)
txt1 = StringVar()
txt1_entry = Entry(frame_login, textvariable=txt1, bg='#fff5c6', bd=1, font=('Times New Roman', 16), width=10)
txt1_entry.place(x=10, y=4)
txt2 = StringVar()
txt2_entry = Entry(frame_login, show='*', textvariable=txt2, bg='#fff5c6', bd=1, font=('Times New Roman', 16), width=10)
txt2_entry.place(x=10, y=80)
STT_fake = 0
def log_in(ten, mk, event=None):
    if ten.get() == '' or mk.get() == '':
        messagebox.showinfo('Thông báo', 'Chưa nhập tên hoặc mật khẩu')

    elif ten.get() == 'myngoc' and mk.get() == '123456':
        window4.withdraw()
        cs1.deiconify()
        cs1.after(3000, cs1.withdraw)  # SAU 3S WINDOW 1 AN
        cs2.after(3500, cs2.deiconify)
    else:
        messagebox.showwarning('Cảnh báo', 'Sai tên hoặc mật khẩu')


value = partial(log_in, txt1,
                      txt2) 
Log_in = Button(frame_login, text='Đăng nhập', bg='#c9e265', bd=0, activebackground='#5ce1e6', command=value_nm_ps)
Log_in.place(x=10, y=118)
Log_in.bind('<Return>', value)
cs1.mainloop()
