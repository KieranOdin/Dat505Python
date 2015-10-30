from graphics import *
import random, time

colour = ["red", "orange", "yellow", "green", "blue", "violet"]
line = []

def readfile():
    f = open('data.txt')
    for x in range(0,31):
        line.append(f.readline())
        print line[x] 
    return line 


def main():
    win = GraphWin('Face', 400, 400) # give title and dimensions
    for i in range(0,31):
        
        print(' ')
        randomMark = random.choice(line)
        print('The random mark is  ' + randomMark)
        eyediv = (float(randomMark) * 0.25)
        
        head = Circle(Point(200,200), float(randomMark)) # set center and radius
    	head.setFill(random.choice(colour))
    	head.draw(win)
        eye1 = Circle(Point(180, 185), eyediv)
        eye1.setFill(random.choice(colour))
        eye1.draw(win)
        eye2 = Circle(Point(220, 185), eyediv)
        eye2.setFill(random.choice(colour))
        eye2.draw(win)
        mouth = Oval(Point(180, 210), Point(220, 220)) # set corners of bounding box
        mouth.setFill(random.choice(colour))
        mouth.draw(win)
        
        label = Text(Point(100, 120), 'Your Mark is: ' + randomMark)
        label.draw(win)
        
        message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(win)
        
        time.sleep(2)
        i = i + 1
        
        head.undraw()
        eye1.undraw()
        eye2.undraw()
        mouth.undraw()
        label.undraw()
        message.undraw()
        
        win.update()

        
    win.getMouse()
    win.close()


	
readfile()



	
main()