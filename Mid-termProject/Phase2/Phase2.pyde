def setup():
    
    size(200,200)
    background(255)
    
def draw():
    
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
    
    
    
    
    
