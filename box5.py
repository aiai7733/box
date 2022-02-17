#coding:utf-8
import rhinoscriptsyntax as rs
import random as rnd

class Box:
    # constractor
    def __init__ (self,no,w,d,h):
        self.no = no
        self.w = w
        self.d = d
        self.h = h
        print("NO.%s" % self.no)
        print("W%s,D%s,H%s" % (self.w,self.d,self.h))

    def drawText(self):
        text = "NO.%s\n" % self.no
        text+= "W%s,D%s,H%s" % (self.w,self.d,self.h)
        point = [0,-150,0]
        height = 150
        font = "Arial"
        font_style = 0
        justification = None
        id = rs.AddText( text,
                    point,
                    height,
                    font,
                    font_style,
                    justification)
        return id

    def drawBox(self):
        pts = [
             [0,0,0],
             [self.w,0,0],
             [self.w,self.d,0],
             [0,self.d,0],
             [0,0,self.h],
             [self.w,0,self.h],
             [self.w,self.d,self.h],
             [0,self.d,self.h]
        ]
        id = rs.AddBox(pts)
        return id

##########
# make instance
boxes = []
xNum = 10
yNum = 10
for i in range(xNum*yNum):
    w = rnd.randint(300,1800)
    d = rnd.randint(300,1800)
    h = rnd.randint(300,1800)
    box = Box(i,w,d,d)
    boxes.append(box)

 #draw Text, drawBox
cnt = 0
for x in range(xNum):
    for y in range(yNum):
        id_text = boxes[cnt].drawText()
        id_box = boxes[cnt].drawBox()
        rs.MoveObject(id_text,[2100*x,2100*y,0])
        rs.MoveObject(id_box,[2100*x,2100*y,0])
        cnt+=1
    
