from tkinter import *
from math import *

root = Tk ()
root.title ("CALC")
root.geometry ("650x650")

frame = Frame (root )
frame.pack ( side = TOP)


def click (number):
    current = screen.get("1.0", "end-1c") 
    screen.delete ("1.0" , "end")
    screen.insert ("end" , str(current) + str(number)) 

def result ():
    """تحسب القيمة المعروضة في الشاشة الرئيسية وتعرض النتيجة في شاشة النتيجة."""
    try :
        # الحصول على التعبير الرياضي من الشاشة الرئيسية (screen - Text widget)
        expression = screen.get("1.0", "end-1c")
        # التحقق إذا كانت الشاشة فارغة لتجنب خطأ في eval()
        if not expression.strip():
            # مسح شاشة النتيجة إذا كانت الشاشة الرئيسية فارغة
            screen_result.delete(0, END) # Entry widget uses 0, END
            return # الخروج من الدالة
        # تقييم التعبير الرياضي
        the_result = eval (expression)
        # مسح شاشة النتيجة (screen_result - Entry widget)
        screen_result.delete (0 , END) # Entry widget uses 0, END
        # عرض النتيجة في شاشة النتيجة (screen_result)
        screen_result.insert (END , str(the_result)) # Entry widget uses END
        # اختياري: مسح الشاشة الرئيسية بعد عرض النتيجة
        # screen.delete("1.0", "end")
    except (SyntaxError, NameError):
        # التعامل مع أخطاء الصيغة أو الأسماء غير المعرفة
        # عرض الخطأ في شاشة النتيجة
        screen_result.delete(0, END)
        screen_result.insert(END, "Error: Invalid Input")
        # اختياري: مسح الشاشة الرئيسية
        # screen.delete("1.0", "end")
    except ZeroDivisionError:
        # التعامل مع خطأ القسمة على صفر
        # عرض الخطأ في شاشة النتيجة
        screen_result.delete(0, END)
        screen_result.insert(END, "Error: Division by Zero")
        # اختياري: مسح الشاشة الرئيسية
        # screen.delete("1.0", "end")
    except Exception as e:
        # التعامل مع أي أخطاء أخرى غير متوقعة
        # عرض الخطأ في شاشة النتيجة
        screen_result.delete(0, END)
        screen_result.insert(END, f"Error: {e}") 

# screen 
screen_result = Entry (frame , width = 1 , font = ("Arial" , 25))
screen_result.grid (row = 8 , column = 0 , columnspan = 5 , sticky = "we" )

screen = Text (frame , width = 1 , height = 2 , font = ("Arial" , 15))
screen.grid (row = 0 , column = 0 , columnspan = 3 , sticky = "we" )

# BIGINING 
bign = Label (frame , text = "BY: F&M" , fg = "RED" , font = "arial 15 bold")
bign.grid (row = 0 , column = 3 , columnspan = 2 , sticky = "we" )

bign_ = Label (frame , text = "CALCULATROR" , fg = "cyan" , font = "arial 20 bold")
bign_.grid (row = 1 , column = 0 , columnspan = 5 , sticky = "we" )

# NUMBERS BUTTONS
but_1_ = Button (frame , text = "1" , width = 5 , command = lambda : click (1) )
but_1_.grid (row = 2 , column = 0 , sticky = "we" )

but_2_ = Button (frame , text = "2" , width = 5 , command = lambda : click (2))
but_2_.grid (row = 2 , column = 1 , sticky = "we" )

but_3_ = Button (frame , text = "3" , width = 5 , command = lambda : click (3))
but_3_.grid (row = 2 , column = 2 , sticky = "we" )

but_4_ = Button (frame , text = "4" , width = 5 , command = lambda : click (4))
but_4_.grid (row = 3 , column = 0 , sticky = "we" )

but_5_ = Button (frame , text = "5" , width = 5 , command = lambda : click (5))
but_5_.grid (row = 3 , column = 1 , sticky = "we" )

but_6_ = Button (frame , text = "6" , width = 5 , command = lambda : click (6))
but_6_.grid (row = 3 , column = 2 , sticky = "we" )

but_7_ = Button (frame , text = "7" , width = 5 , command = lambda : click (7))
but_7_.grid (row = 4 , column = 0 , sticky = "we" )

but_8_ = Button (frame , text = "8" , width = 5 , command = lambda : click (8))
but_8_.grid (row = 4 , column = 1 , sticky = "we" )

but_9_ = Button (frame , text = "9" , width = 5 , command = lambda : click (9))
but_9_.grid (row = 4 , column = 2 , sticky = "we" )

but_0_ = Button (frame , text = "0" , width = 5 , command = lambda : click (0))
but_0_.grid (row = 5 , column = 0 , columnspan = 3 , sticky = "we" )

# OPERATION 
PLS = Button (frame , text = "+" , width = 10 , bg = "white" , fg = "black" , command = lambda : click ('+'))
PLS.grid (row = 2 , column = 3 , sticky = "nswe")

MINS = Button (frame , text = "-" , bg = "white" , fg = "black" , command = lambda : click ('-'))
MINS.grid (row = 3 , column = 3 , sticky = "nswe")

MULTP = Button (frame , text = "*" , bg = "white" , fg = "black" , command = lambda : click ('*'))
MULTP.grid (row = 4 , column = 3 , sticky = "nswe")

DEVD = Button (frame , text = "/" , bg = "white" , fg = "black" , command = lambda : click ('/'))
DEVD.grid (row = 5 , column = 3 , sticky = "nswe")

EQUL = Button (frame , text = "=" , bg = "white" , fg = "black" , command = result )
EQUL.grid (row = 6 , column = 0 , columnspan = 3 , rowspan = 2 , sticky = "nswe")

# CLEAR 
def clear_screens():
    """تمسح محتوى الشاشة الرئيسية وشاشة النتيجة."""
    screen.delete("1.0", "end") # مسح الشاشة الرئيسية (Text widget)
    screen_result.delete(0, END) # مسح شاشة النتيجة (Entry widget)

def delete_last_char():
    """تحذف آخر حرف من الشاشة الرئيسية."""
    # الحصول على المحتوى الحالي
    current = screen.get("1.0", "end-1c")
    # التحقق إذا كانت الشاشة ليست فارغة
    if current:
        # حذف آخر حرف
        screen.delete("1.0", "end") # مسح الكل أولاً
        screen.insert("end", current[:-1]) # إعادة إدراج الكل ما عدا الحرف الأخير

CLR = Button (frame , text = "CLR" , width = 10 , bg = "red" , fg = "white" , command = clear_screens )
CLR.grid (row = 6 , column = 3 , sticky = "nswe")

DLT = Button (frame , text = "DLT" , width = 10 , bg = "red" , fg = "white" , command = delete_last_char )
DLT.grid (row = 7 , column = 3 , sticky = "nswe")






root.mainloop ()
