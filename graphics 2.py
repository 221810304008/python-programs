import turtle as tt
colors = ['red','yellow','blue','violet','purple','green']
al =tt.Turtle()

for x in range(360):
    al.pencolor(colors[x%6])
    al.width(x/150+1)
    al.forward(x*5)
    al.right(90)

tt.done()
