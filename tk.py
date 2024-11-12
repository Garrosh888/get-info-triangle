from tkinter import*
from  main import Triangle
import creatting_triangle
def validate_input(symbol):

    if len(symbol) > 3:
        return False
    if symbol == "0":
        return False
    if len(symbol) == 0:#разрешвем все удалить из елемента ентри
        clear_last_triangle()
        return True
    if symbol.isdigit():#isdigit - проверка является ли символ числом
        clear_last_triangle()
        return True
    else:
        return False


def clear_info():
    entr1.delete(0,END)
    entr2.delete(0,END)
    entr3.delete(0,END)
    clear_last_triangle()
def clear_last_triangle():
    global btn_create
    btn_create.destroy()
    btn_create = None
    cnv.itemconfigure(triangle_perimeter,text = "triangle description")
    cnv.itemconfigure(triangle_type_corner,text = "")
    cnv.itemconfigure(triangle_type_side,text= "")
    creatting_triangle.close_graphic()

def create_triangle():
    global btn_create
    creatting_triangle.draw_triangle(tk_triangle.length1,tk_triangle.length2,tk_triangle.length3)

def analiz_triangle():
    global btn_create,tk_triangle

    tk_triangle = Triangle(int(entr1.get()),int(entr2.get()),int(entr3.get()))#писать код можно только после создания
    if tk_triangle.is_triangle == False:
        message = "incorrect length of sides"
        cnv.itemconfigure(triangle_perimeter,text = message)
        cnv.itemconfigure(triangle_perimeter,fill = "red")
        return
    btn_create = Button(cnv,text="create",font=(None,20),command=create_triangle)
    btn_create.place(x= 50,y= 400 )
    perimeter= f"perimeter triangle = {tk_triangle.show_perimeter()}"
    type_side = f"side triangle = {tk_triangle.type_triangle_side()}"
    type_corner = f"corner triangle = {tk_triangle.type_triangle_corner()}"
    cnv.itemconfigure(triangle_perimeter, text ="triangle description" + f"\n{perimeter}")
    cnv.itemconfigure(triangle_type_side,text = "triangle type by side is" f"\n{type_side}")
    cnv.itemconfigure(triangle_type_corner,text = "triangle type by corner is" f"\n{type_corner}" )
window = Tk()
tk_triangle = None
btn_create = None
cnv = Canvas(window,width = 500,height=500)
cnv.pack()
validate_object = window.register(validate_input)
entr1 = Entry(cnv,font=(None,10),validate="key",validatecommand=(validate_object,"%P"))
entr1.place(x=350,y=400)
entr2 = Entry(cnv,font=(None,10),validate="key",validatecommand=(validate_object,"%P"))
entr2.place(x=350,y=350)
entr3 = Entry(cnv,font=(None,10),validate="key",validatecommand=(validate_object,"%P"))
entr3.place(x=350,y=300)
btn_analiz = Button(cnv,text="analiz",font=(None,30),command=analiz_triangle)
btn_analiz.place(x= 350,y = 40)
btn_cleaar = Button(cnv,text="clear",font=(None,30),command=clear_info)
btn_cleaar.place(x=200,y=380)
triangle_perimeter =  cnv.create_text(20, 20, anchor=NW, text="triangle description", font=(None, 20))
triangle_type_side = cnv.create_text(20,80,anchor=NW,text="",font=(None,20))
triangle_type_corner = cnv.create_text(20,140,anchor=NW,text="",font=(None,20))

window.mainloop()
