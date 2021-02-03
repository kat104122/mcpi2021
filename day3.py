from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
while True:
    x,y,z,=mc.player.getTilePos()
    x=x+random.randrange(-10,10)
    z=z+random.randrange(-10,10) 
    y=y+30
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.2)
while True:
    hits=mc.events.pollProjectileHits()   
    if len(hits) >0: 
    hit=hits[0]    
    x,y,z,= hit.pos.x,hit.pos.y,hit.pos.z
    mc.setBlocks(x,y,z,)
while True:
    hits=mc.events.pollProjectileHits()   
    if len(hits) >0: 
    hit=hits[0]    
    x,y,z,= hit.pos.x,hit.pos.y,hit.pos.z
    mc.player.setPos(x,y,z,)
   x,y,z=mc.player.getTilePos() 
   for i in range(10):
   mc.setBlock(x+i,y,z,1)    
    for i in range(10):
   mc.setBlock(x,y,z+i,x+2,y,z+i,1)  
  x=x+1

def plantTree(x,y,z):  
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)    
    mc.setBlocks(x,y,z,x,y+4,z,17)    
x,y,z,=mc.player.getTilePos()    
for i in range(8):   
    for k in ra9ge(6):  
        plantTree(x+i*5,y+j*i,z+k*i)
 def buildpyramid(x,y,z):    
     
    
line1=[]
line2=[]
line3=[]
for i in range(1,4):
    line1.append(1*i)  
for i in range(1,4):
    line1.append(2*i)       
 for i in range(1,4):
    line1.append(3*i)      
x,y,z=mc.player.getPos()     
mc.setSign(x,y,z,63,0,line1,line2,line3)     
     
x,y,z=mc.player.getPos()   
number=1   
for i in range(8):     
    for j in range(number): 
        mc.spawnEntity(x,y,z,60)
    number=number * 2 
    mc.postToChat() 
while True:
    mc.executeCommand('time add 50')
    time.sieep(0.01) 
     
     
     
     
     
     ()
     
     
     
     
     
     
     
     
    
    
    
    
    
    