#!/usr/bin/env python

from manimlib.imports import *
from Auxiliary import *
import numpy as np
import scipy as sp

NP=NumberPlane()
NL=NumberLine()
NPac=NumberPlane().add_coordinates()
NLan=NumberLine().add_numbers()

cPrototype = {"stroke_width":2,"stroke_color":BLACK,"fill_opacity":1,"color": PURPLE}
cArc = {"stroke_width":0,"stroke_color":"#00ff00","fill_opacity":0,"color": PURPLE}
cArc2 = {"stroke_width":3,"stroke_color":YELLOW,"fill_opacity":0,"color": PURPLE}
cArc3 = {"stroke_width":5,"stroke_color":"#ff0000","fill_opacity":0,"color": PURPLE}
cExclusion = {"stroke_width":2,"stroke_color":WHITE,"fill_opacity":0.5,"color": RED}
#There's some issue in the pentagons that makes the black show barely beneath with white borders
#That's why there's a second exclusion config with a slightly broader border
cExclusion2 = {"stroke_width":2.6,"stroke_color":WHITE,"fill_opacity":0.5,"color": RED}
texconf = {"background_stroke_color":WHITE,"stroke_color":BLUE}

#These triangles have a miniscule angle to them to force the creation of additional points
#That ensures a much smoother transformation to Reuleaux triangles
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=0.0001,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=0.0001,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=0.0001,**cArc)
pTriangle=ArcPolygon(arc0.copy(),arc1.copy(),arc2.copy(),**cPrototype).shift([-0.5,-r3/6,0])

arc0h=ArcBetweenPoints(np.array([1,0,0]),np.array([1,0,0]),angle=0.0001,**cArc)
arc1h=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0.5,r3/2,0]),angle=0.0001,**cArc)
arc2h=ArcBetweenPoints(np.array([0,0,0]),np.array([0,0,0]),angle=0.0001,**cArc)
pTTriangle=ArcPolygon(arc0,arc1,arc1h,arc2,**cPrototype).shift([-0.5,-r3/6,0])

#These triangles have completely straight lines, needed for the trapezoid transformation
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=0,**cArc)
arc1h=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0.5,r3/2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=0,**cArc)
pFTTriangle=ArcPolygon(arc0,arc1,arc1h,arc2,**cPrototype).shift([-0.5,-r3/6,0])

arc0h=ArcBetweenPoints(np.array([0.5,0,0]),np.array([0.5,0,0]),angle=0,**cArc)
arc0=ArcBetweenPoints(np.array([0.5,0,0]),np.array([1,r3/2,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1,r3/2,0]),np.array([0,r3/2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0,r3/2,0]),np.array([0.5,0,0]),angle=0,**cArc)
pFTTriangle2=ArcPolygon(arc0h,arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])

#These are the Realeux triangles
ang=computeABPAngle(np.array([0,0,0]),np.array([1,0,0]))*2
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=ang,**cArc)
pRTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Reuleaux Triangle
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=-ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=-ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=-ang,**cArc)
pRMTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Thinned triangle

#These are the trapezoids for the transformation in between triangles and squares
h=363122996/455427957
a=0.5+1/(2*r2)
b=1/(2*r2)
bOff=(a-b)/2
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([a,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([a,0,0]),np.array([bOff+b,h,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([bOff+b,h,0]),np.array([bOff,h,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([bOff,h,0]),np.array([0,0,0]),angle=0,**cArc)
pTrapezoid=ArcPolygon(arc0,arc1,arc2,arc3,**cPrototype).move_to([0,0,0])

arc0=ArcBetweenPoints(np.array([bOff,0,0]),np.array([bOff+b,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([bOff+b,0,0]),np.array([a,h,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([a,h,0]),np.array([0,h,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0,h,0]),np.array([bOff,0,0]),angle=0,**cArc)
pTrapezoid2=ArcPolygon(arc0,arc1,arc2,arc3,**cPrototype).move_to([0,0,0])

#This square has two 0-length arcs inserted for transforming into an hexagon with intact exclusion zone
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1/(2*r2),0,0]),angle=0,**cArc)
arc0f=ArcBetweenPoints(np.array([0,0,0]),np.array([1/r2,0,0]),angle=0,**cArc)
arc0h=ArcBetweenPoints(np.array([1/(2*r2),0,0]),np.array([1/r2,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1/r2,0,0]),np.array([1/r2,1/r2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([1/r2,1/r2,0]),np.array([1/(2*r2),1/r2,0]),angle=0,**cArc)
arc2f=ArcBetweenPoints(np.array([1/r2,1/r2,0]),np.array([0,1/r2,0]),angle=0,**cArc)
arc2h=ArcBetweenPoints(np.array([1/(2*r2),1/r2,0]),np.array([0,1/r2,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0,1/r2,0]),np.array([0,0,0]),angle=0,**cArc)
pSquare=ArcPolygon(arc0f,arc1.copy(),arc2f,arc3.copy(),**cPrototype).move_to([0,0,0])
pTSquare=ArcPolygon(arc0,arc0h,arc1,arc2,arc2h,arc3,**cPrototype).move_to([0,0,0])

#The hexagon, nothing special here
arc0=ArcBetweenPoints(np.array([-0.5,0,0]),np.array([-0.25,-r3/4,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([-0.25,-r3/4,0]),np.array([0.25,-r3/4,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0.25,-r3/4,0]),np.array([0.5,0,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0.5,0,0]),np.array([0.25,r3/4,0]),angle=0,**cArc)
arc4=ArcBetweenPoints(np.array([0.25,r3/4,0]),np.array([-0.25,r3/4,0]),angle=0,**cArc)
arc5=ArcBetweenPoints(np.array([-0.25,r3/4,0]),np.array([-0.5,0,0]),angle=0,**cArc)
pHexagon=ArcPolygon(arc0,arc1,arc2,arc3,arc4,arc5,**cPrototype).rotate(math.pi/6)

#This is the De Grey pentagon
p1=np.array([0.5-(r3/2),0,0])
p2=np.array([-0.5+(r3/2),0,0])
p3=np.array([0.5,0.5,0])
p4=np.array([0,1.5-(r3/2),0])
p5=np.array([-0.5,0.5,0])
ang=computeABPAngle(p2,p3)*2
arc0=ArcBetweenPoints(p1,p2,angle=0,**cArc)
arc1=ArcBetweenPoints(p2,p3,angle=ang,**cArc)
arc2=ArcBetweenPoints(p3,p4,angle=-ang,**cArc)
arc3=ArcBetweenPoints(p4,p5,angle=-ang,**cArc)
arc4=ArcBetweenPoints(p5,p1,angle=ang,**cArc)
pGreyPent=ArcPolygon(arc0,arc1,arc2,arc3,arc4,**cPrototype)
pGreyUnit=VGroup(pGreyPent,pGreyPent.deepcopy().rotate(math.pi).shift([0,-1.5+(r3/2),0]),
                 pGreyPent.deepcopy().rotate(-math.pi/2).shift([-0.685,(-1.5+(r3/2))/2,0]),
                 pGreyPent.deepcopy().rotate(math.pi/2).shift([0.685,(-1.5+(r3/2))/2,0])).move_to([0,0,0])

titleRect=Rectangle(height=1,width=8,color=BLACK,fill_opacity=1,stroke_color=WHITE)
CC8=ColorCircle(["#aaaaaa","#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.15,0,0])
CC7=ColorCircle(["#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.15,0,0])
eight=TexMobject("8",**texconf).shift([1.15,0,0])
seven=TexMobject("7",**texconf).shift([1.15,0.04,0])
yGRect=Rectangle(height=1.2,width=3.5,color=BLACK,fill_opacity=1,stroke_color=WHITE)
yGt=TexMobject("\gamma(G_{T})=",**texconf).shift([-0.55,0,0])
yGr=TexMobject("\gamma(G_{R})=",**texconf).shift([-0.55,0,0])
yGs=TexMobject("\gamma(G_{S})=",**texconf).shift([-0.55,0,0])
yGhs=TexMobject("\gamma(G_{HS})=",**texconf).shift([-0.55,0,0])
yGh=TexMobject("\gamma(G_{H})=",**texconf).shift([-0.55,0,0])
yGdp=TexMobject("\gamma(G_{DP})=",**texconf).shift([-0.5,0,0])

general_zoom=0.59

def update_EX(mob,alpha,tile):
    new_mob=ExclusionZone(tile,**mob.__dict__)
    mob.become(new_mob)
def update_EX_multi(mobs,alpha,tiles):
    i=0
    for mob in mobs:
        new_mob=ExclusionZone(tiles[i],**mob.__dict__)
        mob.become(new_mob)
        i+=1

def partialColor(t,arr):
    for x,y in arr:
        t.tileDict[x][y].set_fill("#0000ff")
        t.tileDict[0][0].set_fill("#0000ff")

def standardColor(t):
    for x in t.xRange:
        for y in t.yRange:
            if ((x+y)%4==0) and (y%2==0):   t.tileDict[x][y].set_fill("#0000ff")
            if ((x+y)%4==1) and (y%2==0):   t.tileDict[x][y].set_fill("#ff0000")
            if ((x+y)%4==2) and (y%2==0):   t.tileDict[x][y].set_fill("#ffff00")
            if ((x+y)%4==3) and (y%2==0):   t.tileDict[x][y].set_fill("#aaaaaa")
            if ((x+y)%4==0) and (y%2==1):   t.tileDict[x][y].set_fill("#dd00ff")
            if ((x+y)%4==1) and (y%2==1):   t.tileDict[x][y].set_fill("#ff7b00")
            if ((x+y)%4==2) and (y%2==1):   t.tileDict[x][y].set_fill("#00ff00")
            if ((x+y)%4==3) and (y%2==1):   t.tileDict[x][y].set_fill("#00ffff")
            
def sevenColor(t):
    for x in t.xRange:
        for y in t.yRange:
            if ((x+3*y)%6==0):              t.tileDict[x][y].set_fill("#0000ff")
            if ((x+3*y)%6==2):              t.tileDict[x][y].set_fill("#00ff00")
            if ((x+3*y)%6==4):              t.tileDict[x][y].set_fill("#ffff00")
            if ((x+y)%4==1) and (y%2==0):   t.tileDict[x][y].set_fill("#dd00ff")
            if ((x+y)%4==3) and (y%2==0):   t.tileDict[x][y].set_fill("#ff7b00")
            if ((x+y)%4==1) and (y%2==1):   t.tileDict[x][y].set_fill("#00ffff")
            if ((x+y)%4==3) and (y%2==1):   t.tileDict[x][y].set_fill("#ff0000")
        
def hexColor(t):
    for x in t.xRange:
        for y in t.yRange:
            if ((x+y*2.5-6.5*(y%2))%7==0):  t.tileDict[x][y].set_fill("#0000ff")
            if ((x+y*2.5-6.5*(y%2))%7==1):  t.tileDict[x][y].set_fill("#00ffff")
            if ((x+y*2.5-6.5*(y%2))%7==2):  t.tileDict[x][y].set_fill("#00ff00")
            if ((x+y*2.5-6.5*(y%2))%7==3):  t.tileDict[x][y].set_fill("#ffff00")
            if ((x+y*2.5-6.5*(y%2))%7==4):  t.tileDict[x][y].set_fill("#ff7b00")
            if ((x+y*2.5-6.5*(y%2))%7==5):  t.tileDict[x][y].set_fill("#ff0000")
            if ((x+y*2.5-6.5*(y%2))%7==6):  t.tileDict[x][y].set_fill("#dd00ff")


#[x][y][0] - Top Tile
#[x][y][1] - Bottom Tile
#[x][y][2] - Left Tile (tip points into the block, towards the right)
#[x][y][3] - Right Tile
#y%2==0 - Middle, bottom and top row
#y%2==1 - The other rows in between
def greyColor1(t):
    for x in t.xRange:
        for y in t.yRange:
            if (y%2==0):  t.tileDict[x][y][3].set_fill("#0000ff")
def greyColor2(t):
    for x in t.xRange:
        for y in t.yRange:
            if (y%5==0):  t.tileDict[x][y][1].set_fill("#0000ff")
            if (y%5==1):  t.tileDict[x][y][0].set_fill("#0000ff")
            if (y%5==3):  t.tileDict[x][y][2].set_fill("#0000ff")

def greyColorFull(t):
    for x in t.xRange:
        for y in t.yRange:
            if (y%5==0):  t.tileDict[x][y][1].set_fill("#0000ff")
            if (y%5==1):  t.tileDict[x][y][0].set_fill("#0000ff")
            if (y%5==3):  t.tileDict[x][y][2].set_fill("#0000ff")
            
            if (y%5==1):  t.tileDict[x][y][1].set_fill("#00ffff")
            if (y%5==2):  t.tileDict[x][y][0].set_fill("#00ffff")
            if (y%5==4):  t.tileDict[x][y][2].set_fill("#00ffff")
            
            if (y%5==2):  t.tileDict[x][y][1].set_fill("#00ff00")
            if (y%5==3):  t.tileDict[x][y][0].set_fill("#00ff00")
            if (y%5==0):  t.tileDict[x][y][2].set_fill("#00ff00")
            
            if (y%5==3):  t.tileDict[x][y][1].set_fill("#ffff00")
            if (y%5==4):  t.tileDict[x][y][0].set_fill("#ffff00")
            if (y%5==1):  t.tileDict[x][y][2].set_fill("#ffff00")
            
            if (y%5==4):  t.tileDict[x][y][1].set_fill("#ff7b00")
            if (y%5==0):  t.tileDict[x][y][0].set_fill("#ff7b00")
            if (y%5==2):  t.tileDict[x][y][2].set_fill("#ff7b00")

            if (y%2==0):  t.tileDict[x][y][3].set_fill("#ff0000")

            if (y%2==1):  t.tileDict[x][y][3].set_fill("#dd00ff")

            
tracer=VGroup(Annulus(fill_opacity=1,color=BLUE,inner_radius=0.99,
                          outer_radius=1.010),Circle(color=BLUE,
                          fill_opacity=1).scale(0.0075))

def hexChromaTransformTiles(t):
    c0=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
    c1=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)
    c2=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)
    c3=t.tileDict[-1][0].copy().set_stroke(opacity=0).scale(0.85)
    c4=t.tileDict[-2][0].copy().set_stroke(opacity=0).scale(0.85)
    c5=t.tileDict[-3][0].copy().set_stroke(opacity=0).scale(0.85)
    c6=t.tileDict[-4][0].copy().set_stroke(opacity=0).scale(0.85)
    return [c0,c1,c2,c3,c4,c5,c6]
    
class Thumbnail(ZoomedScene):
    def construct(self):
        xRange=range(-1,1)
        yRange=range(-1,1)

        #Hexagons
        tH=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 range(-1,2),yRange)
        vH=tH.get_VGroup().shift([2.5,2.2,0])
        hexColor(tH)
        #Reuleaux Triangles
        def pRT(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pRTriangle
            else:
                return pRMTriangle
        tR=Tiling(pRT,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],
                 range(-2,2),range(-1,1))
        vR=tR.get_VGroup().shift([-3,2.2,0])
        standardColor(tR)
        #Squares
        tS=Tiling(pSquare,
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([0,1/r2,0])]],
                 range(-2,2),yRange)
        vS=tS.get_VGroup().shift([-3,-2.2,0])
        standardColor(tS)
        #Pentagons
        tP=Tiling(pGreyUnit,
                 [[Mobject.shift,np.array([2,0,0])]],
                 [[Mobject.shift,np.array([1,1,0])],[Mobject.shift,np.array([-1,1,0])]],
                 range(0,1),range(0,1))        
        vP=tP.get_VGroup().shift([2,-2.6,0])
        greyColorFull(tP)

        #Title
        T=Text(r"Hadwiger-Nelson Tilings",**texconf).scale(2)
        self.add(vH,vR,vS,vP,T)
        self.wait()
        #Save via -s
        
class TestZone(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.3,
    }
    def construct(self):
        ###
        self.wait(1)

class S01_Intro(ZoomedScene): # Intro scene to explain how the subsequent scenes work
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        logoX=NewSVGMO({"file_name_prefix":"Ex","fill_opacity":1,"color":WHITE,
                        "stroke_opacity":0},"X").scale(1.5)
        
        xRange=range(-2,2)
        yRange=range(-2,2)
        
        t=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 xRange,yRange)
        v=t.get_VGroup()
        hexColor(t)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        line=Line([0,0,0],[0,1,0],color="#dddddd")
        lbrace = Brace(line,[0.1,0,0],color="#dddddd").shift([-0.18,0,0])
        one=TexMobject("1",background_stroke_color="#dddddd",stroke_color=BLUE).shift([0.5,0.5,0])
        distBrace=VGroup(line,lbrace,one)#.shift([0,-0.25,0])
        excludedTiles=VGroup(t.tileDict[-2][0],t.tileDict[-1][0],t.tileDict[1][0],t.tileDict[2][0],
                             t.tileDict[-2][1],t.tileDict[-1][1],t.tileDict[0][1],t.tileDict[1][1],
                             t.tileDict[-2][-1],t.tileDict[-1][-1],t.tileDict[0][-1],t.tileDict[1][-1],
                             t.tileDict[-1][2],t.tileDict[0][2],t.tileDict[1][2],
                             t.tileDict[-1][-2],t.tileDict[0][-2],t.tileDict[1][-2])
        
        self.play(FadeIn(logoX),run_time=3)
        self.wait(1)
        self.play(FadeOut(logoX),run_time=1)
        self.wait(1)

        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        self.play(FadeIn(NP),ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(7)
        self.play(Write(v),run_time=10)
        self.wait(34)
        self.play(ApplyMethod(v.scale,0.93))
        self.play(ApplyMethod(v.scale,1/0.93))
        self.wait(20)
                  
        self.play(Write(EX),run_time=3)
        self.play(FadeIn(distBrace))
        self.wait(3)
        self.play(ApplyMethod(distBrace.shift,[0,0.5,0]))
        self.wait(1)
        self.play(ApplyMethod(distBrace.shift,[0,-1,0]))
        self.wait(2)
        self.play(FadeOut(distBrace))
        self.wait(9)
        self.bring_to_back(NP,excludedTiles)
        self.play(ApplyMethod(excludedTiles[0].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[1].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[2].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[3].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[4].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[5].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[6].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[7].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[8].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[9].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[10].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[11].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[12].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[13].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[14].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[15].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[16].rotate,math.pi/3),
                  ApplyMethod(excludedTiles[17].rotate,math.pi/3),run_time=5)
        
        self.wait(3)
        self.remove(excludedTiles)
        self.play(FadeOut(EX),FadeOut(v))
        self.play(FadeOut(NP))
        self.wait(3)

class S02_TriangleGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        #Define tilings
        def pRT(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pRTriangle
            else:
                return pRMTriangle
        pRTriangleShifted=pRTriangle.copy().shift([0,0.134,0])
        def pRTinv(x,y):#pRT and pRTinv are functions to put different tilings into the tiling depending on position
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pRMTriangle
            else:
                return pRTriangleShifted
        
        xRange=range(-9,9)
        yRange=range(-3,3)#9,4

        t=Tiling(pTriangle,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],
                 xRange,yRange)
        t.tileDict[0][0].set_fill("#0000ff")
        v=t.get_VGroup()

        
        #These are six tiles and their exclusion zone around the center tile
        #These are used to signify a single color for normal or fat triangles
        HexTiles=[[4,0],[2,-2],[-2,-2],[-4,0],[-2,2],[2,2]]
        ExHexRef=[]
        for x,y in HexTiles:
            ExHexRef.append(t.tileDict[x][y])
        #These are used for the slim triangles
        HexTilesImproved=[[3,1],[3,-1],[0,-2],[-3,-1],[-3,1],[0,2]]
        ExHexImprovedRef=[]
        for x,y in HexTilesImproved:
            ExHexImprovedRef.append(t.tileDict[x][y])

        tSPC=t.deepcopy()#This will be the standard with only one group colored
        vSPC=tSPC.get_VGroup()
        partialColor(tSPC,HexTiles)
        tFC=t.deepcopy()#This will be the fully colored
        vFC=tFC.get_VGroup()
        standardColor(tFC)

        #The original colored version to switch back
        tO=t.deepcopy()
        vO=tO.get_VGroup()
        
        #Reuleaux alternative
        tR=Tiling(pRT,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],
                 xRange,yRange)
        partialColor(tR,HexTiles)
        vR=tR.get_VGroup()
        standardColor(tR)

        #Reuleaux inverse
        tRinv=Tiling(pRTinv,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],
                 xRange,yRange)
        vRinv=tRinv.get_VGroup()
        tRinvC=tRinv.deepcopy()
        vRinvC=tRinvC.get_VGroup()
        tRinvO=tRinv.deepcopy()
        vRinvO=tRinvO.get_VGroup()
        tRinvImproved=tRinv.deepcopy()
        vRinvImproved=tRinvImproved.get_VGroup()
        tRinvImprovedC=tRinv.deepcopy()
        vRinvImprovedC=tRinvImprovedC.get_VGroup()
        partialColor(tRinv,HexTiles)
        partialColor(tRinvImproved,HexTilesImproved)
        sevenColor(tRinvImprovedC)

        T=TexMobject(r"Triangular\enspace Grid",**texconf).scale(1.2)
        R=TexMobject(r"Reuleaux\enspace Grid",**texconf).scale(1.2)
        tTitle=VGroup(titleRect.copy(),T).shift([0,1.5,0])
        rTitle=VGroup(titleRect,R).shift([0,1.5,0])
        yG1=VGroup(yGRect.copy(),yGt,eight).shift([-2,-1.5,0])
        yG2=VGroup(yGRect,yGr,seven).shift([-2,-1.5,0])
        
        #BEGIN SCENE
        self.activate_zooming(animate=False)

        self.play(Write(v),run_time=5)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        self.play(ShowCreation(EX),run_time=5)
        self.wait(4)
        self.play(FadeIn(tracer.shift([-0.5,-r3/6,0])))
        self.wait(1)
        self.play(tracer.shift,[1,0,0],run_time=2.5)
        self.wait(0.5)
        self.play(tracer.shift,[-0.5,r3/2,0],run_time=2.5)
        self.wait(0.5)
        self.play(tracer.shift,[-0.5,-r3/2,0],run_time=2.5)
        self.wait(1)
        self.play(FadeOut(tracer))
        

        ExHex=[]
        for x,y in HexTiles:
            ExHex.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex=VGroup(*ExHex)
        
        self.play(Transform(v,vSPC),
                  FadeIn(ExHex),run_time=4,rate_func=linear)
        self.wait(2)
        self.play(Transform(v,vFC),run_time=4)

        
        self.play(FadeOut(ExHex),FadeOut(EX),run_time=1.5)
        self.wait(5)
        self.play(Write(tTitle),run_time=2)
        self.play(Write(yG1,run_time=2))
        self.wait(1)

        c0=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[3][-1].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[1][-1].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)
        c7=t.tileDict[0][-1].copy().set_stroke(opacity=0).scale(0.85)

        self.play(Transform(c0,CC8[0]))
        self.play(Transform(c1,CC8[1]))
        self.play(Transform(c2,CC8[2]))
        self.play(Transform(c3,CC8[3]))
        self.play(Transform(c4,CC8[4]))
        self.play(Transform(c5,CC8[5]))
        self.play(Transform(c6,CC8[6]))
        self.play(Transform(c7,CC8[7]))
        self.wait(3)
        self.play(FadeOut(tTitle),FadeOut(yG1),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6,c7)))
        self.wait(4)

        self.play(FadeIn(EX),FadeIn(ExHex),run_time=1.5)
        
        self.play(Transform(v,vR),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=4)
        
        self.wait(4)
        self.play(FadeOut(ExHex),run_time=1.5)
        self.wait(3)
        self.play(FadeIn(tracer))
        self.wait(1)
        self.play(Rotate(tracer,np.pi/3,about_point=[0,r3/2-r3/6,0]),run_time=2.5)
        self.wait(0.5)
        self.play(Rotate(tracer,np.pi/3,about_point=[-0.5,-r3/6,0]),run_time=2.5)
        self.wait(0.5)
        self.play(Rotate(tracer,np.pi/3,about_point=[0.5,-r3/6,0]),run_time=2.5)
        self.wait(1)
        self.play(FadeOut(tracer))
        self.wait(0.5)
        self.play(FadeOut(EX),run_time=1.5)
        self.wait(4)

        
        self.play(FadeIn(ExHex),FadeIn(EX),run_time=1.5)
        
        self.wait(2)
        self.play(Transform(v,vRinv),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=4)
        self.wait(5)
        ExHex2=[]
        for x,y in HexTilesImproved:
            ExHex2.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex2=VGroup(*ExHex2)
        self.play(FadeOut(ExHex))
        self.wait(4)
        self.play(FadeIn(tracer))
        self.wait(1.5)
        self.play(Rotate(tracer,-np.pi/3,about_point=[0,-r3/2-r3/6,0]),run_time=2.5)
        self.wait(0.5)
        self.play(Rotate(tracer,-np.pi/3,about_point=[1,r3/3,0]),run_time=2.5)
        self.wait(0.5)
        self.play(Rotate(tracer,-np.pi/3,about_point=[-1,r3/3,0]),run_time=2.5)
        self.wait(1.5)
        self.play(FadeOut(tracer))
        self.wait(3)
        
        self.play(Transform(v,vRinvImproved))
        self.wait(5.5)
        self.play(FadeIn(ExHex2))
        self.wait(5)
        self.play(Transform(v,vRinvImprovedC),run_time=4)
        self.wait(5)
        self.play(FadeOut(ExHex2),FadeOut(EX))
        self.wait(2)
        
        self.play(Write(rTitle),run_time=2)
        self.play(Write(yG2,run_time=2))
        self.wait(1)

        c0=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[4][0].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[4][-1].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[3][-2].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[3][-1].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)

        self.play(Transform(c0,CC7[0]))
        self.play(Transform(c1,CC7[1]))
        self.play(Transform(c2,CC7[2]))
        self.play(Transform(c3,CC7[3]))
        self.play(Transform(c4,CC7[4]))
        self.play(Transform(c5,CC7[5]))
        self.play(Transform(c6,CC7[6]))
        self.wait(3)
        self.play(FadeOut(rTitle),FadeOut(yG2),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6)))
        self.wait(4)
        self.play(Transform(v,vO),run_time=2)
        self.play(Transform(v,vFC),run_time=2)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        self.play(FadeIn(EX))
        self.wait(2)
        
class S03_SquareGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        NLTri1=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift([-0.5,-r3/6,0]).rotate(math.radians(60))
        NLTrapezoid1=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift(pTrapezoid.get_vertices()[0]).rotate(math.radians(52.9))
        NLSquare1=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift(pSquare.get_vertices()[0]).rotate(math.radians(45))
        
        NLTri2=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift([0.5,-r3/6,0]).rotate(math.radians(-60))
        NLTrapezoid2=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift(pTrapezoid.get_vertices()[1]).rotate(math.radians(-52.9))
        NLSquare2=NumberLine(numbers_with_elongated_ticks=[],
                    color=GRAY).shift(pSquare.get_vertices()[1]).rotate(math.radians(-45))
        def pRTFC(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pFTTriangle
            else:
                return pFTTriangle2
        def pRTrapezoid(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pTrapezoid
            else:
                return pTrapezoid2
        xRangePre=range(-9,9)
        yRangePre=range(-3,3)
        xRange=range(-6,6)
        yRange=range(-3,3)

        
        tTriFC=Tiling(pRTFC,
                 [[Mobject.shift,np.array([0.5,0,0])]],
                 [[Mobject.shift,np.array([0,r3/2,0])]],
                 xRangePre,yRangePre)
        vTriFC=tTriFC.get_VGroup()
        standardColor(tTriFC)
        
        tTrapezoidFC=Tiling(pRTrapezoid,
                 [[Mobject.shift,np.array([(a+b)/2,0,0])]],
                 [[Mobject.shift,np.array([0,h,0])]],
                 xRangePre,yRangePre)
        vTrapezoidFC=tTrapezoidFC.get_VGroup()
        standardColor(tTrapezoidFC)
        
        tPreFC=Tiling(pSquare,
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([0,1/r2,0])]],
                 xRangePre,yRangePre)
        vPreFC=tPreFC.get_VGroup()
        standardColor(tPreFC)
        
        t=Tiling(pSquare,
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([0,1/r2,0])]],
                 xRange,yRange)
        v=t.get_VGroup()
        t.tileDict[0][0].set_fill("#0000ff")
        tO=t.deepcopy()
        vO=tO.get_VGroup()
        
        tSPC=t.deepcopy()
        vSPC=tSPC.get_VGroup()
        SquareTiles=[[2,2],[2,-2],[-2,-2],[-2,2]]
        partialColor(tSPC,SquareTiles)
        ExSquareRef=[]
        for x,y in SquareTiles:
            ExSquareRef.append(tTriFC.tileDict[x][y])
        
        tFC=t.deepcopy()
        vFC=tFC.get_VGroup()
        standardColor(tFC)
        tFCO=tFC.deepcopy()
        vFCO=tFCO.get_VGroup()


        t2=Tiling(pSquare,#This is the shifted, hexagonal square tiling
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([1/(2*r2),1/r2,0])],[Mobject.shift,np.array([-1/(2*r2),1/r2,0])]],
                 xRange,yRange)
        v2=t2.get_VGroup()
        t2.tileDict[0][0].set_fill("#0000ff")
        
        tSPC2=t2.deepcopy()
        vSPC2=tSPC2.get_VGroup()
        HexTiles=[[2,-1],[0,-3],[-2,-2],[-3,1],[-1,3],[2,2]]
        partialColor(tSPC2,HexTiles)
        
        tFC2=t2.deepcopy()
        vFC2=tFC2.get_VGroup()
        hexColor(tFC2)

        S=TexMobject(r"Square\enspace Grid",**texconf).scale(1.2)
        H=TexMobject(r"Hexagonal\enspace Grid\enspace (Squares)",**texconf).scale(1)
        sTitle=VGroup(titleRect.copy(),S).shift([0,1.5,0])
        hTitle=VGroup(titleRect,H).shift([0,1.5,0])
        yG1=VGroup(yGRect.copy(),yGs,eight).shift([-2,-1.5,0])
        yG2=VGroup(yGRect,yGhs,seven).shift([-2,-1.5,0])
        
        #BEGIN SCENE
        self.activate_zooming(animate=False)
        self.add(vTriFC)#We add the previous tiling to seamlessly continue
        EX=ExclusionZone(tTriFC.tileDict[0][0],**cExclusion)
        ExSquare=[]
        for x,y in SquareTiles:
            ExSquare.append(ExclusionZone(tTriFC.tileDict[x][y],**cExclusion))
        ExSquare=VGroup(*ExSquare)
        self.add(EX)
        self.play(FadeIn(ExSquare))
        self.wait(1)
        self.play(FadeIn(NLTri1),FadeIn(NLTri2))
        self.wait(1)

        self.play(Transform(vTriFC,vTrapezoidFC),
                  UpdateFromAlphaFuncArg(EX,update_EX,tTriFC.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExSquare,update_EX_multi,ExSquareRef),
                  Transform(NLTri1,NLTrapezoid1),Transform(NLTri2,NLTrapezoid2),run_time=12)
        self.wait(1)
        
        self.play(Transform(vTriFC,vPreFC),
                  UpdateFromAlphaFuncArg(EX,update_EX,tTriFC.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExSquare,update_EX_multi,ExSquareRef),
                  Transform(NLTri1,NLSquare1),Transform(NLTri2,NLSquare2),run_time=12)
        self.wait(2)
    
        self.play(FadeOut(NLTri1),FadeOut(NLTri2))
        self.remove(vTriFC)
        self.add(v)
        self.bring_to_front(EX,ExSquare)
        
        self.play(Transform(v,vFC),run_time=0)

        
        self.play(FadeOut(ExSquare),FadeOut(EX),run_time=1.5)
        self.wait(5)
        self.play(Write(sTitle),run_time=2)
        self.play(Write(yG1,run_time=2))
        self.wait(1)

        c0=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[3][-1].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[1][-1].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)
        c7=t.tileDict[0][-1].copy().set_stroke(opacity=0).scale(0.65)

        self.play(Transform(c0,CC8[0]))
        self.play(Transform(c1,CC8[1]))
        self.play(Transform(c2,CC8[2]))
        self.play(Transform(c3,CC8[3]))
        self.play(Transform(c4,CC8[4]))
        self.play(Transform(c5,CC8[5]))
        self.play(Transform(c6,CC8[6]))
        self.play(Transform(c7,CC8[7]))
        self.wait(3)
        self.play(FadeOut(sTitle),FadeOut(yG1),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6,c7)))
        self.wait(4)
        
        self.play(Transform(v,v2))
        self.wait(1)
        self.play(FadeIn(EX),run_time=1.5)
        self.wait(4)
        
        ExHex=[]
        for x,y in HexTiles:
            ExHex.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex=VGroup(*ExHex)

        self.play(Transform(v,vSPC2),
                  FadeIn(ExHex),run_time=4,rate_func=linear)
        self.wait(2)
        self.play(Transform(v,vFC2),run_time=4)
        self.wait(4)
        self.play(FadeOut(ExHex),FadeOut(EX))
        self.wait(2)
        
        self.play(Write(hTitle),run_time=2)
        self.play(Write(yG2,run_time=2))
        self.wait(1)

        c=hexChromaTransformTiles(t)
        
        self.play(Transform(c[0],CC7[0]))
        self.play(Transform(c[1],CC7[6]))
        self.play(Transform(c[2],CC7[5]))
        self.play(Transform(c[3],CC7[4]))
        self.play(Transform(c[4],CC7[3]))
        self.play(Transform(c[5],CC7[2]))
        self.play(Transform(c[6],CC7[1]))
        self.wait(3)
        self.play(FadeOut(hTitle),FadeOut(yG2),FadeOut(VGroup(*c)))
        self.wait(4)
        
class S04_HexagonGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        xRange=range(-7,6)
        yRange=range(-4,4)

        t=Tiling(pTSquare,#This is the shifted tiling again
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([1/(2*r2),1/r2,0])],[Mobject.shift,np.array([-1/(2*r2),1/r2,0])]],
                 xRange,yRange)
        v=t.get_VGroup()
        hexColor(t)
        
        tFC=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 xRange,yRange)
        vFC=tFC.get_VGroup()
        hexColor(tFC)
        
        dl1=TexMobject(r"Hexagonal\enspace Grid",**texconf).shift([-1,0,0]).scale(1.2)
        dl2=TexMobject(r"\left(d=1\right)",**texconf).scale(1.2).shift([2.7,0,0])
        ds1=TexMobject(r"Hexagonal\enspace Grid",**texconf).shift([-1,0,0]).scale(1.2)
        ds2=TexMobject(r"\left(d=\frac{2}{\sqrt{7}}\right)",**texconf).scale(0.55).shift([2.7,0,0])
        dlTitle=VGroup(titleRect.copy(),dl1,dl2).shift([0,1.5,0])
        dsTitle=VGroup(titleRect,ds1,ds2).shift([0,1.5,0])
        yG1=VGroup(yGRect,yGh,seven).shift([-2,-1.5,0])

        #BEGIN SCENE
        self.add(v)
        self.activate_zooming(animate=False)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        HexTiles=[[2,-1],[0,-3],[-2,-2],[-3,1],[-1,3],[2,2]]
        ExHexRef=[]
        for x,y in HexTiles:
            ExHexRef.append(t.tileDict[x][y])
        ExHex=[]
        for x,y in HexTiles:
            ExHex.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex=VGroup(*ExHex)
        self.play(FadeIn(EX),FadeIn(ExHex),run_time=1)
        self.wait(2)

        
        self.play(Transform(v,vFC),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=7)
        
        self.play(Write(dlTitle),run_time=2)
        self.play(Write(yG1),Write(CC7),run_time=2)
        self.wait(3)
        self.play(FadeOut(dlTitle),FadeOut(yG1),FadeOut(CC7),run_time=2)
        
        self.play(ApplyMethod(v.scale,2/r7),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=13)
        self.wait()
        
        self.play(Write(dsTitle),run_time=2)
        self.play(FadeIn(yG1),FadeIn(CC7),run_time=2)
        self.wait(3)
        self.play(FadeOut(dsTitle),FadeOut(yG1),FadeOut(CC7),run_time=2)
        self.wait(4)
        self.play(FadeOut(EX),FadeOut(ExHex),run_time=2)
        self.wait(4)
        
class S05_DeGreyGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],   
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        xRange1=range(-7,6)
        yRange1=range(-4,4)
        xRange2=range(-3,2)
        yRange2=range(-2,2)

        tHFC=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 xRange1,yRange1)
        vHFC=tHFC.get_VGroup()
        hexColor(tHFC)
        vRHFC=VGroup(*reversed([*vHFC]))
        vRHFC.scale(2/r7)
        
        t=Tiling(pGreyUnit,
                 [[Mobject.shift,np.array([2,0,0])]],
                 [[Mobject.shift,np.array([1,1,0])],[Mobject.shift,np.array([-1,1,0])]],
                 xRange2,yRange2)
        t2=t.deepcopy()#First single color pattern
        t3=t.deepcopy()#Second single color pattern
        t4=t.deepcopy()#Full color pattern
        
        v=t.get_VGroup()
        v2=t2.get_VGroup()
        v3=t3.get_VGroup()
        v4=t4.get_VGroup()

        t.tileDict[0][0][0].set_fill("#0000ff")        
        greyColor1(t2)
        greyColor2(t3)
        greyColorFull(t4)

        EX=ExclusionZone(t.tileDict[0][0][0],**cExclusion2)
        EX2List=[t.tileDict[-2][2][3],t.tileDict[-1][2][3],t.tileDict[0][2][3],t.tileDict[1][2][3],
                 t.tileDict[-2][0][3],t.tileDict[-1][0][3],t.tileDict[0][0][3],t.tileDict[1][0][3],
                 t.tileDict[-2][-2][3],t.tileDict[-1][-2][3],t.tileDict[0][-2][3],t.tileDict[1][-2][3]]
        EX2=VGroup()
        for arr in EX2List:
            EX2.add(ExclusionZone(arr,**cExclusion2))

        EX3List=[t.tileDict[-2][1][0],t.tileDict[-1][1][0],t.tileDict[0][1][0],t.tileDict[1][1][0],
        t.tileDict[-2][0][1],t.tileDict[-1][0][1],t.tileDict[0][0][1],t.tileDict[1][0][1],t.tileDict[2][0][1],
                 t.tileDict[-1][-2][2],t.tileDict[0][-2][2],t.tileDict[1][-2][2],t.tileDict[2][-2][2]]
        EX3=VGroup()
        for arr in EX3List:
            EX3.add(ExclusionZone(arr,**cExclusion2))
        
        g=TexMobject(r"De\enspace Grey\enspace Pentagon\enspace Grid",**texconf).scale(1.2)
        gTitle=VGroup(titleRect,g).shift([0,1.5,0])
        yG1=VGroup(yGRect,yGh,seven).shift([-2,-1.5,0])

        #BEGIN SCENE
        self.activate_zooming(animate=False)
        writeTileList=[*v]
        writeTileList=VGroup(*writeTileList)
        self.play(Write(vRHFC,rate_func = lambda t: 1-t),run_time=3)
        self.play(Write(writeTileList),run_time=3)
        self.wait(2)
        self.play(ShowCreation(EX),run_time=5)
        self.wait(6)
        ###

        self.play(FadeIn(tracer.shift([p1])))
        self.wait(1)
        self.play(tracer.shift,[p2[0]-p1[0],0,0],run_time=3)
        self.wait(0.5)
        self.play(Rotate(tracer,np.pi/6,about_point=arc1.get_arc_center()),run_time=4)
        self.wait(0.5)
        self.play(Rotate(tracer,-np.pi/6,about_point=arc2.get_arc_center()),run_time=4)
        self.wait(0.5)
        self.play(Rotate(tracer,-np.pi/6,about_point=arc3.get_arc_center()),run_time=4)
        self.wait(0.5)
        self.play(Rotate(tracer,np.pi/6,about_point=arc4.get_arc_center()),run_time=4)
        self.wait(1)
        self.play(FadeOut(tracer))
        self.wait(3)

        ###
        self.play(FadeOut(EX))
        self.wait(2)
        self.play(Transform(v,v2))
        self.wait(2)
        self.play(FadeIn(EX2))
        self.wait(7)
        self.play(FadeOut(EX2))
        self.wait(2)
        self.play(Transform(v,v3))
        self.wait(2)
        self.play(FadeIn(EX3))
        self.wait(7)
        self.play(FadeOut(EX3))
        self.wait(2)
        self.play(Transform(v,v4),run_time=4)
        self.wait(4)
        self.play(Write(gTitle),run_time=2)
        self.play(Write(yG1,run_time=2))
        self.wait(1)

        c0=t.tileDict[1][0][2].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[0][-1][0].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[0][-1][1].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[0][0][3].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[0][-1][3].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[0][0][1].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[0][-1][2].copy().set_stroke(opacity=0).scale(0.85)

        self.play(Transform(c0,CC7[0]))
        self.play(Transform(c1,CC7[1]))
        self.play(Transform(c2,CC7[2]))
        self.play(Transform(c3,CC7[3]))
        self.play(Transform(c4,CC7[4]))
        self.play(Transform(c5,CC7[5]))
        self.play(Transform(c6,CC7[6]))
        self.wait(3)
        self.play(FadeOut(gTitle),FadeOut(yG1),FadeOut(CC7),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6)),
                  run_time=2)
        self.wait(7)
        self.play(Write(v,rate_func = lambda t: 1-t),run_time=3)
        self.wait(1)
