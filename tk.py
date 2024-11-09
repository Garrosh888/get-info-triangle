from tkinter import*
from  main import Triangle
import creatting_triangle
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
entr1 = Entry(cnv,font=(None,10))
entr1.place(x=350,y=400)
entr2 = Entry(cnv,font=(None,10))
entr2.place(x=350,y=350)
entr3 = Entry(cnv,font=(None,10))
entr3.place(x=350,y=300)
btn_analiz = Button(cnv,text="analiz",font=(None,30),command=analiz_triangle)
btn_analiz.place(x= 350,y = 40)
triangle_perimeter =  cnv.create_text(20, 20, anchor=NW, text="triangle description", font=(None, 20))
triangle_type_side = cnv.create_text(20,80,anchor=NW,text="",font=(None,20))
triangle_type_corner = cnv.create_text(20,140,anchor=NW,text="",font=(None,20))

window.mainloop()
