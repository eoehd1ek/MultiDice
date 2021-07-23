from tkinter import *
from tkinter import messagebox
from random import *
import tkinter.font		#글씨 크기 변경할 때 필요함

sum = 0

def roll():
	global sum
	sum = 0
	
	## 1번째 부분
	if (pad1.get() == 0):
		pad1_value.set(" ")
	else:
		result = randint(1, pad1.get())
		pad1_value.set(str(result))
		sum += result
		
	## 2번째 부분
	if (pad2.get() == 0):
		pad2_value.set(" ")
	else:
		result = randint(1, pad2.get())
		pad2_value.set(str(result))
		sum += result
		
	## 3번째 부분
	if (pad3.get() == 0):
		pad3_value.set(" ")
	else:
		result = randint(1, pad3.get())
		pad3_value.set(str(result))
		sum += result
		
	## 4번째 부분
	if (pad4.get() == 0):
		pad4_value.set(" ")
	else:
		result = randint(1, pad4.get())
		pad4_value.set(str(result))
		sum += result
		
	## 5번째 부분
	if (pad5.get() == 0):
		pad5_value.set(" ")
	else:
		result = randint(1, pad5.get())
		pad5_value.set(str(result))
		sum += result
		
	## 6번째 부분
	if (pad6.get() == 0):
		pad6_value.set(" ")
	else:
		result = randint(1, pad6.get())
		pad6_value.set(str(result))
		sum += result
		
	## 7번째 부분
	if (pad7.get() == 0):
		pad7_value.set(" ")
	else:
		result = randint(1, pad7.get())
		pad7_value.set(str(result))
		sum += result
		
	## 8번째 부분
	if (pad8.get() == 0):
		pad8_value.set(" ")
	else:
		result = randint(1, pad8.get())
		pad8_value.set(str(result))
		sum += result
		
	sumStringVar.set(sum)
	
	messagebox.showinfo("ROLL", "주사위를 굴렸습니다!")	

def reset():
	radio_pad1_0.select()
	radio_pad2_0.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()
	
	messagebox.showinfo("ROLL", "초기화를 수행했습니다.")	

def D1_6():
	radio_pad1_6.select()
	radio_pad2_0.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D2_6():
	radio_pad1_6.select()
	radio_pad2_6.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D1_4():
	radio_pad1_4.select()
	radio_pad2_0.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D2_4():
	radio_pad1_4.select()
	radio_pad2_4.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D1_8():
	radio_pad1_8.select()
	radio_pad2_0.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D2_8():
	radio_pad1_8.select()
	radio_pad2_8.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D1_10():
	radio_pad1_10.select()
	radio_pad2_0.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def D2_10():
	radio_pad1_10.select()
	radio_pad2_10.select()
	radio_pad3_0.select()
	radio_pad4_0.select()
	radio_pad5_0.select()
	radio_pad6_0.select()
	radio_pad7_0.select()
	radio_pad8_0.select()

def on_key_down_handler(event):
    # 키 바인드 추가 
	s = event.char
	if s == "1":
		reset()
	elif s == "2":
		D1_6()
	elif s == "3":
		D2_6()
	elif s == "4":
		D1_4()
	elif s == "5":
		D2_4()
	elif s == "6":
		D1_8()
	elif s == "7":
		D2_8()
	elif s == "8":
		D1_10()
	elif s == "9":
		D2_10()
	elif s == " ":
		roll()
	print(type(event.char))
	
if __name__ == "__main__":
	tk = Tk()
	tk.title("Dice")
	tk.geometry("850x600")
	tk.resizable(0, 0)

	## 칸 안에 들어갈 값
	Vpad1=0; Vpad2=0; Vpad3=0; Vpad4=0; Vpad5=0; Vpad6=0; Vpad7=0; Vpad8=0
	## 라디오 버튼을 사용하기 위해 만듬
	pad1 = IntVar(); pad2 = IntVar(); pad3 = IntVar(); pad4 = IntVar()
	pad5 = IntVar(); pad6 = IntVar(); pad7 = IntVar(); pad8 = IntVar()

	## key bind
	tk.bind("<Key>", on_key_down_handler)


	## 폰트 데이터 모음
	fontData_Entry = ("Verdana", 50)
	fontData_Radio = ("Verdana", 10)
	fontData_DICE = ("Verdana", 15)

	## 1번째 부분
	pad1_value = StringVar(value = Vpad1)
	pad_1_Entry = Entry(tk, width = 2, text = pad1_value, font = fontData_Entry)
	pad_1_Entry.place(x=80, y=80)
	## 텍스트 부분
	label_1_0 = Label(tk, text = "0")
	label_1_0.place (x= 55, y = 180)
	label_1_4 = Label(tk, text = "4")
	label_1_4.place (x= 85, y = 180)
	label_1_6 = Label(tk, text = "6")
	label_1_6.place (x= 115, y = 180)
	label_1_8 = Label(tk, text = "8")
	label_1_8.place (x= 145, y = 180)
	label_1_10 = Label(tk, text = "10")
	label_1_10.place (x= 170, y = 180)
	## 라디오 부분
	radio_pad1_0 = Radiobutton(tk, variable = pad1, value = 0, font = "fontData_Radio")
	radio_pad1_0.place(x=50, y=200)
	radio_pad1_4 = Radiobutton(tk, variable = pad1, value = 4, font = "fontData_Radio")
	radio_pad1_4.place(x=80, y=200)
	radio_pad1_6 = Radiobutton(tk, variable = pad1, value = 6, font = "fontData_Radio")
	radio_pad1_6.place(x=110, y=200)
	radio_pad1_8 = Radiobutton(tk, variable = pad1, value = 8, font = "fontData_Radio")
	radio_pad1_8.place(x=140, y=200)
	radio_pad1_10 = Radiobutton(tk, variable = pad1, value = 10, font = "fontData_Radio")
	radio_pad1_10.place(x=170, y=200)
	radio_pad1_0.select()

	## 2번째 부분
	pad2_value = StringVar(value = Vpad2)
	pad_2_Entry = Entry(tk, width = 2, text = pad2_value, font = fontData_Entry)
	pad_2_Entry.place(x=280, y=80)
	## 2 - 텍스트 부분
	label_2_0 = Label(tk, text = "0")
	label_2_0.place (x= 255, y = 180)
	label_2_4 = Label(tk, text = "4")
	label_2_4.place (x= 285, y = 180)
	label_2_6 = Label(tk, text = "6")
	label_2_6.place (x= 315, y = 180)
	label_2_8 = Label(tk, text = "8")
	label_2_8.place (x= 345, y = 180)
	label_2_10 = Label(tk, text = "10")
	label_2_10.place (x= 370, y = 180)
	## 2 - 라디오 부분
	radio_pad2_0 = Radiobutton(tk, variable = pad2, value = 0, font = "fontData_Radio")
	radio_pad2_0.place(x=250, y=200)
	radio_pad2_4 = Radiobutton(tk, variable = pad2, value = 4, font = "fontData_Radio")
	radio_pad2_4.place(x=280, y=200)
	radio_pad2_6 = Radiobutton(tk, variable = pad2, value = 6, font = "fontData_Radio")
	radio_pad2_6.place(x=310, y=200)
	radio_pad2_8 = Radiobutton(tk, variable = pad2, value = 8, font = "fontData_Radio")
	radio_pad2_8.place(x=340, y=200)
	radio_pad2_10 = Radiobutton(tk, variable = pad2, value = 10, font = "fontData_Radio")
	radio_pad2_10.place(x=370, y=200)
	radio_pad2_0.select()

	## 3번째 부분
	pad3_value = StringVar(value = Vpad3)
	pad_3_Entry = Entry(tk, width = 2, text = pad3_value, font = fontData_Entry)
	pad_3_Entry.place(x=480, y=80)
	## 3 - 텍스트 부분
	label_3_0 = Label(tk, text = "0")
	label_3_0.place (x= 455, y = 180)
	label_3_4 = Label(tk, text = "4")
	label_3_4.place (x= 485, y = 180)
	label_3_6 = Label(tk, text = "6")
	label_3_6.place (x= 515, y = 180)
	label_3_8 = Label(tk, text = "8")
	label_3_8.place (x= 545, y = 180)
	label_3_10 = Label(tk, text = "10")
	label_3_10.place (x= 570, y = 180)
	## 3 - 라디오 부분
	radio_pad3_0 = Radiobutton(tk, variable = pad3, value = 0, font = "fontData_Radio")
	radio_pad3_0.place(x=450, y=200)
	radio_pad3_4 = Radiobutton(tk, variable = pad3, value = 4, font = "fontData_Radio")
	radio_pad3_4.place(x=480, y=200)
	radio_pad3_6 = Radiobutton(tk, variable = pad3, value = 6, font = "fontData_Radio")
	radio_pad3_6.place(x=510, y=200)
	radio_pad3_8 = Radiobutton(tk, variable = pad3, value = 8, font = "fontData_Radio")
	radio_pad3_8.place(x=540, y=200)
	radio_pad3_10 = Radiobutton(tk, variable = pad3, value = 10, font = "fontData_Radio")
	radio_pad3_10.place(x=570, y=200)
	radio_pad3_0.select()

	## 4번째 부분
	pad4_value = StringVar(value = Vpad4)
	pad_4_Entry = Entry(tk, width = 2, text = pad4_value, font = fontData_Entry)
	pad_4_Entry.place(x=680, y=80)
	## 4 - 텍스트 부분
	label_4_0 = Label(tk, text = "0")
	label_4_0.place (x= 655, y = 180)
	label_4_4 = Label(tk, text = "4")
	label_4_4.place (x= 685, y = 180)
	label_4_6 = Label(tk, text = "6")
	label_4_6.place (x= 715, y = 180)
	label_4_8 = Label(tk, text = "8")
	label_4_8.place (x= 745, y = 180)
	label_4_10 = Label(tk, text = "10")
	label_4_10.place (x= 770, y = 180)
	## 4 - 라디오 부분
	radio_pad4_0 = Radiobutton(tk, variable = pad4, value = 0, font = "fontData_Radio")
	radio_pad4_0.place(x=650, y=200)
	radio_pad4_4 = Radiobutton(tk, variable = pad4, value = 4, font = "fontData_Radio")
	radio_pad4_4.place(x=680, y=200)
	radio_pad4_6 = Radiobutton(tk, variable = pad4, value = 6, font = "fontData_Radio")
	radio_pad4_6.place(x=710, y=200)
	radio_pad4_8 = Radiobutton(tk, variable = pad4, value = 8, font = "fontData_Radio")
	radio_pad4_8.place(x=740, y=200)
	radio_pad4_10 = Radiobutton(tk, variable = pad4, value = 10, font = "fontData_Radio")
	radio_pad4_10.place(x=770, y=200)
	radio_pad4_0.select()

	## 5번째 부분
	pad5_value = StringVar(value = Vpad5)
	pad_5_Entry = Entry(tk, width = 2, text = pad5_value, font = fontData_Entry)
	pad_5_Entry.place(x=80, y=280)
	## 5 - 텍스트 부분
	label_5_0 = Label(tk, text = "0")
	label_5_0.place (x= 55, y = 380)
	label_5_4 = Label(tk, text = "4")
	label_5_4.place (x= 85, y = 380)
	label_5_6 = Label(tk, text = "6")
	label_5_6.place (x= 115, y = 380)
	label_5_8 = Label(tk, text = "8")
	label_5_8.place (x= 145, y = 380)
	label_5_10 = Label(tk, text = "10")
	label_5_10.place (x= 170, y = 380)
	## 5 - 라디오 부분
	radio_pad5_0 = Radiobutton(tk, variable = pad5, value = 0, font = "fontData_Radio")
	radio_pad5_0.place(x=50, y=400)
	radio_pad5_4 = Radiobutton(tk, variable = pad5, value = 4, font = "fontData_Radio")
	radio_pad5_4.place(x=80, y=400)
	radio_pad5_6 = Radiobutton(tk, variable = pad5, value = 6, font = "fontData_Radio")
	radio_pad5_6.place(x=110, y=400)
	radio_pad5_8 = Radiobutton(tk, variable = pad5, value = 8, font = "fontData_Radio")
	radio_pad5_8.place(x=140, y=400)
	radio_pad5_10 = Radiobutton(tk, variable = pad5, value = 10, font = "fontData_Radio")
	radio_pad5_10.place(x=170, y=400)
	radio_pad5_0.select()

	## 6번째 부분
	pad6_value = StringVar(value = Vpad6)
	pad_6_Entry = Entry(tk, width = 2, text = pad6_value, font = fontData_Entry)
	pad_6_Entry.place(x=280, y=280)
	## 6 - 텍스트 부분
	label_6_0 = Label(tk, text = "0")
	label_6_0.place (x= 255, y = 380)
	label_6_4 = Label(tk, text = "4")
	label_6_4.place (x= 285, y = 380)
	label_6_6 = Label(tk, text = "6")
	label_6_6.place (x= 315, y = 380)
	label_6_8 = Label(tk, text = "8")
	label_6_8.place (x= 345, y = 380)
	label_6_10 = Label(tk, text = "10")
	label_6_10.place (x= 370, y = 380)
	## 6 - 라디오 부분
	radio_pad6_0 = Radiobutton(tk, variable = pad6, value = 0, font = "fontData_Radio")
	radio_pad6_0.place(x=250, y=400)
	radio_pad6_4 = Radiobutton(tk, variable = pad6, value = 4, font = "fontData_Radio")
	radio_pad6_4.place(x=280, y=400)
	radio_pad6_6 = Radiobutton(tk, variable = pad6, value = 6, font = "fontData_Radio")
	radio_pad6_6.place(x=310, y=400)
	radio_pad6_8 = Radiobutton(tk, variable = pad6, value = 8, font = "fontData_Radio")
	radio_pad6_8.place(x=340, y=400)
	radio_pad6_10 = Radiobutton(tk, variable = pad6, value = 10, font = "fontData_Radio")
	radio_pad6_10.place(x=370, y=400)
	radio_pad6_0.select()

	## 7번째 부분
	pad7_value = StringVar(value = Vpad7)
	pad_7_Entry = Entry(tk, width = 2, text = pad7_value, font = fontData_Entry)
	pad_7_Entry.place(x=480, y=280)
	## 7 - 텍스트 부분
	label_7_0 = Label(tk, text = "0")
	label_7_0.place (x= 455, y = 380)
	label_7_4 = Label(tk, text = "4")
	label_7_4.place (x= 485, y = 380)
	label_7_6 = Label(tk, text = "6")
	label_7_6.place (x= 515, y = 380)
	label_7_8 = Label(tk, text = "8")
	label_7_8.place (x= 545, y = 380)
	label_7_10 = Label(tk, text = "10")
	label_7_10.place (x= 570, y = 380)
	## 7 - 라디오 부분
	radio_pad7_0 = Radiobutton(tk, variable = pad7, value = 0, font = "fontData_Radio")
	radio_pad7_0.place(x=450, y=400)
	radio_pad7_4 = Radiobutton(tk, variable = pad7, value = 4, font = "fontData_Radio")
	radio_pad7_4.place(x=480, y=400)
	radio_pad7_6 = Radiobutton(tk, variable = pad7, value = 6, font = "fontData_Radio")
	radio_pad7_6.place(x=510, y=400)
	radio_pad7_8 = Radiobutton(tk, variable = pad7, value = 8, font = "fontData_Radio")
	radio_pad7_8.place(x=540, y=400)
	radio_pad7_10 = Radiobutton(tk, variable = pad7, value = 10, font = "fontData_Radio")
	radio_pad7_10.place(x=570, y=400)
	radio_pad7_0.select()

	## 8번째 부분
	pad8_value = StringVar(value = Vpad8)
	pad_8_Entry = Entry(tk, width = 2, text = pad8_value, font = fontData_Entry)
	pad_8_Entry.place(x=680, y=280)
	## 8 - 텍스트 부분
	label_8_0 = Label(tk, text = "0")
	label_8_0.place (x= 655, y = 380)
	label_8_4 = Label(tk, text = "4")
	label_8_4.place (x= 685, y = 380)
	label_8_6 = Label(tk, text = "6")
	label_8_6.place (x= 715, y = 380)
	label_8_8 = Label(tk, text = "8")
	label_8_8.place (x= 745, y = 380)
	label_8_10 = Label(tk, text = "10")
	label_8_10.place (x= 770, y = 380)
	## 8 - 라디오 부분
	radio_pad8_0 = Radiobutton(tk, variable = pad8, value = 0, font = "fontData_Radio")
	radio_pad8_0.place(x=650, y=400)
	radio_pad8_4 = Radiobutton(tk, variable = pad8, value = 4, font = "fontData_Radio")
	radio_pad8_4.place(x=680, y=400)
	radio_pad8_6 = Radiobutton(tk, variable = pad8, value = 6, font = "fontData_Radio")
	radio_pad8_6.place(x=710, y=400)
	radio_pad8_8 = Radiobutton(tk, variable = pad8, value = 8, font = "fontData_Radio")
	radio_pad8_8.place(x=740, y=400)
	radio_pad8_10 = Radiobutton(tk, variable = pad8, value = 10, font = "fontData_Radio")
	radio_pad8_10.place(x=770, y=400)
	radio_pad8_0.select()

	## 합계 글씨 부분 (Label)
	sum_Label = Label(tk, text = "총합 : ", font = fontData_DICE)
	sum_Label.place(x= 600, y=475)

	## 합계 엔트리 부분
	sumStringVar = StringVar(value = sum)
	sum_Entry = Entry(tk, width = 2, text = sumStringVar, font = fontData_Entry)
	sum_Entry.place(x= 680, y=450)

	## 0으로 초기화
	CustomButton1 = Button(tk, width = 7, height = 2, text = "초기화", font = fontData_Radio, command = reset)
	CustomButton1.place(x=25, y=450)
	## 여러 옵션 버튼
	CustomButton2 = Button(tk, width = 7, height = 2, text = "1D6", font = fontData_Radio, command = D1_6)
	CustomButton2.place(x=95, y=450)	## 2번
	CustomButton3 = Button(tk, width = 7, height = 2, text = "2D6", font = fontData_Radio, command = D2_6)
	CustomButton3.place(x=165, y=450)	## 3번
	CustomButton4 = Button(tk, width = 7, height = 2, text = "1D4", font = fontData_Radio, command = D1_4)
	CustomButton4.place(x=25, y=500)	## 4번
	CustomButton5 = Button(tk, width = 7, height = 2, text = "1D8", font = fontData_Radio, command = D1_8)
	CustomButton5.place(x=95, y=500)	## 5번
	CustomButton6 = Button(tk, width = 7, height = 2, text = "1D10", font = fontData_Radio, command = D1_10)
	CustomButton6.place(x=165, y=500)	## 6번
	CustomButton7 = Button(tk, width = 7, height = 2, text = "2D4", font = fontData_Radio, command = D2_4)
	CustomButton7.place(x=25, y=550)	## 7번
	CustomButton8 = Button(tk, width = 7, height = 2, text = "2D8", font = fontData_Radio, command = D2_8)
	CustomButton8.place(x=95, y=550)	## 8번
	CustomButton9 = Button(tk, width = 7, height = 2, text = "2D10", font = fontData_Radio, command = D2_10)
	CustomButton9.place(x=165, y=550)	## 9번

	## 다운로드 버튼
	downButton = Button(tk, width = 15, height = 3, text = "ROLL!", justify = "right", font = fontData_DICE, command = roll)		#클릭시 다운로드
	downButton.place(x=320, y=450)

	tk.mainloop()