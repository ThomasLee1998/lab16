# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.destroy(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
missile = drawpad.create_rectangle(395, 582, 405, 598, fill = "red")
player = drawpad.create_oval(390,580,410,600, fill="blue")
missile1 = False
rockets = 3
hit = False
direction = 5

class myApp(object):
    def __init__(self, parent):
        global rockets
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        
        
        self.rocketsTxt = Label(root, text=str(rockets), width=len(str(rockets)), bg='green')
        self.rocketsTxt.pack()
        
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rockets
        global missile
        global missile1
        px1, py1, px2, py2 = drawpad.coords(player)
        mx1, my1, mx2, my2 = drawpad.coords(missile)
        if missile1 == True:
            if my2 > 0:
                drawpad.move(missile, 0, -15)
                didwehit = self.collisionDetect()
            if my2 < 0:
                x = (mx1 - px1) - 5
                y = (py1 - my1) + 3
                drawpad.move(missile, x, y)
                missile1 = False
                
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        global missile1
        global rockets
        px1, py1, px2, py2 = drawpad.coords(player)
        if event.char == " ":
            if rockets > 0:
                missile1 = True
                rockets = rockets - 1
                self.rocketsTxt.configure(text = str(rockets))
        if event.char == "w":
            if py1 > 1:
                drawpad.move(player, 0, -10)
                drawpad.move(missile, 0, -10)
            else:
                return
        if event.char == "a":
            if px1 > 1:
                drawpad.move(player, -10, 0)
                drawpad.move(missile,-10, 0)
            else:
                return
        if event.char == "s":
            if py2 < 599:
                drawpad.move(player, 0, 10)
                drawpad.move(missile, 0, 10)
            else:
                return
        if event.char == "d":
            if px2 < 799:
                drawpad.move(player, 10, 0)
                drawpad.move(missile, 10, 0)
            else:
                return
            
    def collisionDetect(self):
        global missile
        global enemy
        global hit
        global drawpad
        rx1,ry1,rx2,ry2 = drawpad.coords(missile)
        x1, y1, x2, y2 = drawpad.coords(enemy)
        if (rx1 > x1 and rx2 < x2) and (ry1 > y1 and ry1 < y2):
            drawpad.delete(enemy)
            drawpad.delete(missile)
app = myApp(root)
root.mainloop()