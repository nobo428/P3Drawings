w, h = 1000, 1000

cellCount = 200

cellSizex = w/cellCount
cellSizey = h/cellCount

noiseScalex = .02
noiseScaley = .02
seed = 200

numlines = 200

cells = [[0 for x in range(cellCount)] for y in range(cellCount)]
lines = [[0 for x in range(2)] for y in range(numlines)]
lines2 = [[0 for x in range(2)] for y in range(numlines)]
lines3 = [[0 for x in range(2)] for y in range(numlines)]
lines4 = [[0 for x in range(2)] for y in range(numlines)]

linespace = h/numlines

def resetField():
    global seed
    noiseSeed(seed)
    seed += 1
    
    stroke(255)
                
    for a in range(numlines):
        lines[a][0] = w/2
        lines[a][1] = (a * linespace)+random(0,linespace/2)
        
        lines2[a][0] = w/2
        lines2[a][1] = lines[a][1]
        
        lines3[a][0] = 1
        lines3[a][1] = (a * linespace)+random(0,linespace/2)
        
        lines4[a][0] = w-1
        lines4[a][1] = (a * linespace)+random(0,linespace/2)
    
    for x in range(cellCount):
        for y in range(cellCount):
            n = noise(x * noiseScalex, y * noiseScaley)
            
            rot = n * (2 * PI)
            
            #pushMatrix()
            #translate(x*cellSize, y*cellSize)
            #rotate(rot)
            cells[x][y] = rot
            #line(0, 0, cellSize, 0)
            #popMatrix()
daw = 1
def setup():
    size(w,h)
    pixelDensity(2)
    smooth()
    background(0)
    strokeWeight(daw)
    resetField()      
def draw():
    global daw, running2
    running = 0
    for b in range(numlines):
        lx = lines2[b][0]
        ly = lines2[b][1]
    
        if lx < w and lx >= 0 and ly < h and ly >= 0:
            #point(dx, dy)
            lines2[b][0] = lx - cos(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            lines2[b][1] = ly - sin(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            #stroke(255-lx/w*255)
            stroke(255)
            line(lx, ly, lines2[b][0], lines2[b][1])
            #if daw > 0.02:
                #daw -= .002
                #strokeWeight(daw)
            running = 1
            
    #if running2 == 0:
        #daw = 100
        #strokeWeight(daw)
    for a in range(numlines):
        dx = lines[a][0]
        dy = lines[a][1]
        
        if dx < w and dx >= 0 and dy < h and dy >= 0:
            #point(dx, dy)
            lines[a][0] = dx + cos(cells[int(dx/cellSizex)][int(dy/cellSizey)])
            lines[a][1] = dy + sin(cells[int(dx/cellSizex)][int(dy/cellSizey)])
            #stroke(dy/w*255, dx/w*255, 255-dx/w*255)
            stroke(255)
            line(dx, dy, lines[a][0], lines[a][1])
            #if daw > 0.02:
                #daw -= .002
                #strokeWeight(daw)
    
    for c in range(numlines):
        lx = lines3[c][0]
        ly = lines3[c][1]
    
        if lx < w and lx >= 0 and ly < h and ly >= 0:
            #point(dx, dy)
            lines3[c][0] = lx - cos(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            lines3[c][1] = ly - sin(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            #stroke(ly/w*255, lx/w*255, 255-lx/w*255)
            stroke(255)
            line(lx, ly, lines3[c][0], lines3[c][1])
            
    for d in range(numlines):
        lx = lines4[d][0]
        ly = lines4[d][1]
    
        if lx < w and lx >= 0 and ly < h and ly >= 0:
            #point(dx, dy)
            lines4[d][0] = lx + cos(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            lines4[d][1] = ly + sin(cells[int(lx/cellSizex)][int(ly/cellSizey)])
            #stroke(ly/w*255, lx/w*255, 255-lx/w*255)
            stroke(255)
            line(lx, ly, lines4[d][0], lines4[d][1])

def mousePressed():
    if mouseButton == LEFT:
        noLoop()
        setup()
        #resetField()
        loop()
    elif mouseButton == RIGHT:
        save("lines.png")
    
