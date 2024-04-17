angle= 0
mx = 0
my = 0
velocity = 0.01
Red = 0
Green = 0
Blue = 0
def setup():
    size(1000, 1000)
    background(255, 0, 0)
    
                
def draw():

    global angle
    global mx
    global my
    global velocity
    global Red
    global Green
    global Blue
    
    background(Red,Green,Blue)#refresh the background in each frame
    
    columns = 8 #input column number
    rows = columns#input row number

    columnwidth = width/columns #calculate the width of each column
    rowheight = height/rows #calculate the height of each row

    s = 5.0/float(columns)#apply scale
                 
    for c in range(columns):
        for r in range(rows):
            offset = columnwidth/2  #center the rotate axis
       
            drawObject(c * columnwidth + offset + (c-columns/2)*mx,#offset the movement center in x
                       r * rowheight + offset + (r-rows/2)*my,#offset the movement center in y
                       s * (1+mx/40), 
                       (r-3.5)*angle)
            
            #motion
            mx += velocity  # x movement
            if mx > 40:
                velocity = velocity * -1
            if mx < -40:
                velocity = velocity * -1
                
            my += velocity # y movement
            if my > 40:
                velocity = velocity * -1
            if my < -40:
                velocity = velocity * -1
            
            #background color change
            Red += 13*velocity 
            Green += -12*velocity
            Blue += -15*velocity
            
            angle += 0.001#angle change
            
                
def drawObject(x,y,s,R):
    
    pushMatrix()# save the current transformation state
    translate(x,y)# apply coordinate
    scale(s)# apply scale
    rotate(R)# rotation

    translate(-100,-100) 
    
# Drawingobject    
   # Left foot
    fill(228,95,138)#purple
    bezier(50, 145, -30, 200, 180, 200, 70, 120)#left foot
    
    # Body parts
    fill(252,184,195) # pink 
    ellipse(165,115,60,40)# right hand
    ellipse(100,100,140,140)# body

    # Mouth
    bezier(85, 105, 100, 120, 110, 105, 110, 105) # mouth
    bezier(40, 70, 5, 70, 5, 95, 30, 110) # left hand
     
    # Blush
    fill(246,128,155)  
    ellipse(60,95,20,10)
    ellipse(140,95,20,10)
    
    # Eyes
    fill(3,117,189)# blue
    ellipse(83,75,15,40)
    ellipse(117,75,15,40)
    fill(0) # black
    ellipse(83,66,13,25)
    ellipse(117,66,13,25)
    fill(255)# white
    ellipse(83,62,11,18)
    ellipse(117,62,11,18)
    
    # Right foot
    fill(228,95,138)
    translate(130, 160)
    rotate(radians(140))
    ellipse(-10,-5,70,50)#right foot
    
    popMatrix()# Restore the previous transformation state
    


        
    



    



    
    
    
    
