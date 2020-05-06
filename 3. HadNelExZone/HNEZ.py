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

arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=0,**cArc)
pTriangle=ArcPolygon(arc0.copy(),arc1.copy(),arc2.copy(),**cPrototype).shift([-0.5,-r3/6,0])

arc0h=ArcBetweenPoints(np.array([1,0,0]),np.array([1,0,0]),angle=0,**cArc)
arc1h=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0.5,r3/2,0]),angle=0,**cArc)
arc2h=ArcBetweenPoints(np.array([0,0,0]),np.array([0,0,0]),angle=0,**cArc)
pTTriangle=ArcPolygon(arc0,arc1,arc1h,arc2,**cPrototype).shift([-0.5,-r3/6,0])

arc0h=ArcBetweenPoints(np.array([0.5,0,0]),np.array([0.5,0,0]),angle=0,**cArc)
arc0=ArcBetweenPoints(np.array([0.5,0,0]),np.array([1,r3/2,0]),angle=0,**cArc)
arc1h=ArcBetweenPoints(np.array([1,r3/2,0]),np.array([1,r3/2,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1,r3/2,0]),np.array([0,r3/2,0]),angle=0,**cArc)
arc2h=ArcBetweenPoints(np.array([0,r3/2,0]),np.array([0,r3/2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0,r3/2,0]),np.array([0.5,0,0]),angle=0,**cArc)
pTT2riangle=ArcPolygon(arc0h,arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])

ang=computeABPAngle(np.array([0,0,0]),np.array([1,0,0]))*2
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=ang,**cArc)
pRTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Reuleaux Triangle
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=-ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=-ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=-ang,**cArc)
pRMTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Thin triangle

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

arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1/r2,0,0]),angle=0,**cArc)
arc0h=ArcBetweenPoints(np.array([1/r2,0,0]),np.array([1/r2,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1/r2,0,0]),np.array([1/r2,1/r2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([1/r2,1/r2,0]),np.array([0,1/r2,0]),angle=0,**cArc)
arc2h=ArcBetweenPoints(np.array([0,1/r2,0]),np.array([0,1/r2,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0,1/r2,0]),np.array([0,0,0]),angle=0,**cArc)
pSquare=ArcPolygon(arc0.copy(),arc1.copy(),arc2.copy(),arc3.copy(),**cPrototype).move_to([0,0,0])
pTSquare=ArcPolygon(arc0,arc0h,arc1,arc2,arc2h,arc3,**cPrototype).move_to([0,0,0])
#This square has two 0-length arcs inserted for transforming into an hexagon with intact exclusion zone

arc0=ArcBetweenPoints(np.array([-0.5,0,0]),np.array([-0.25,-r3/4,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([-0.25,-r3/4,0]),np.array([0.25,-r3/4,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0.25,-r3/4,0]),np.array([0.5,0,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0.5,0,0]),np.array([0.25,r3/4,0]),angle=0,**cArc)
arc4=ArcBetweenPoints(np.array([0.25,r3/4,0]),np.array([-0.25,r3/4,0]),angle=0,**cArc)
arc5=ArcBetweenPoints(np.array([-0.25,r3/4,0]),np.array([-0.5,0,0]),angle=0,**cArc)
pHexagon=ArcPolygon(arc0,arc1,arc2,arc3,arc4,arc5,**cPrototype).rotate(math.pi/6)

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
#titleFont="Lucida Console"
CC8=ColorCircle(["#aaaaaa","#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.15,0,0])
CC7=ColorCircle(["#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.15,0,0])
eight=TexMobject("8",background_stroke_color=WHITE,stroke_color=BLUE).shift([1.15,0,0])
seven=TexMobject("7",background_stroke_color=WHITE,stroke_color=BLUE).shift([1.15,0.04,0])
yGRect=Rectangle(height=1.2,width=3.5,color=BLACK,fill_opacity=1,stroke_color=WHITE)
yGt=TexMobject("\gamma(G_{T})=",background_stroke_color=WHITE).shift([-0.55,0,0])
yGr=TexMobject("\gamma(G_{R})=",background_stroke_color=WHITE).shift([-0.55,0,0])
yGs=TexMobject("\gamma(G_{S})=",background_stroke_color=WHITE).shift([-0.55,0,0])
yGhs=TexMobject("\gamma(G_{HS})=",background_stroke_color=WHITE).shift([-0.55,0,0])
yGh=TexMobject("\gamma(G_{H})=",background_stroke_color=WHITE).shift([-0.55,0,0])
yGdp=TexMobject("\gamma(G_{DP})=",background_stroke_color=WHITE,stroke_color=BLUE).shift([-0.5,0,0])

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
def greyColor(t):
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
            #if ((x+y*2.5-6.5*(y%2))%7==1):  t.tileDict[x][y].set_fill("#00ffff")
            #if ((x+y*2.5-6.5*(y%2))%7==2):  t.tileDict[x][y].set_fill("#00ff00")
            #if ((x+y*2.5-6.5*(y%2))%7==3):  t.tileDict[x][y].set_fill("#ffff00")
            #if ((x+y*2.5-6.5*(y%2))%7==4):  t.tileDict[x][y].set_fill("#ff7b00")
            #if ((x+y*2.5-6.5*(y%2))%7==5):  t.tileDict[x][y].set_fill("#ff0000")
            #if ((x+y*2.5-6.5*(y%2))%7==6):  t.tileDict[x][y].set_fill("#dd00ff")


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
        self.wait()
        #Save via -s
        
class TestZone(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        n0 = [0, 0, 0]  # BottomLeft
        n1 = [1, 0, 0]  # BottomRight
        n2 = [0.5, r3 / 2, 0]  # Top
        g = {0: [n0, [[1,1.5], 2], cGreenSt], 1: [n1, [0, 2], cRedSt], 2: [n2, [0, 1], cBlueSt]}
        K3 = Graph(g, lineConfig).returnVGroup()
        self.add(K3)
        self.wait(1)
        self.remove(K3)
        
        g = {0: [n0, [2], cGreenSt], 1: [n1, [2], cRedSt], 2: [n2, [0, 1], cBlueSt]}
        K3E = Graph(g, lineConfig).returnEdges()
        K3V = Graph(g, lineConfig).returnVertices()
        path = VMobject()
        path.set_points_smoothly([n0,[0.3,-0.5,0],n1])
        K3E.add(path)
        self.add(K3E,K3V)
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
        line=Line([0,0,0],[-1,0,0])
        lbrace = Brace(line,[0,0.1,0]).shift([0,-0.18,0])
        one=TexMobject("1",background_stroke_color=WHITE,stroke_color=BLUE).shift([-0.5,0.5,0])
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
        self.play(Write(v))
        self.wait(3)
        self.play(ApplyMethod(v.scale,0.9))
        self.play(ApplyMethod(v.scale,1/0.9))
        self.wait(3)
                  
        self.play(Write(EX),run_time=3)
        self.play(FadeIn(line),FadeIn(lbrace),FadeIn(one))
        self.wait(3)
        self.play(FadeOut(line),FadeOut(lbrace),FadeOut(one))
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

class S0_TriangleGrid(ZoomedScene):
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

        T=TexMobject(r"Triangular\enspace Grid").scale(1.2)
        R=TexMobject(r"Reuleaux\enspace Grid").scale(1.2)
        tTitle=VGroup(titleRect.copy(),T).shift([0,1.5,0])
        rTitle=VGroup(titleRect,R).shift([0,1.5,0])
        yG1=VGroup(yGRect.copy(),yGt,eight).shift([-2,-1.5,0])
        yG2=VGroup(yGRect,yGr,seven).shift([-2,-1.5,0])
        
        #BEGIN SCENE
        self.add(NP)
        self.activate_zooming(animate=False)

        self.play(Write(v),run_time=5)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        self.play(ShowCreation(EX),run_time=5)
        self.wait(2)

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
        self.wait(4)
        self.play(FadeOut(tTitle),FadeOut(yG1),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6,c7)))
        self.wait(4)
        
        self.play(FadeIn(ExHex),FadeIn(EX),run_time=1.5)
        
        self.play(Transform(v,vR),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=4)
        
        self.wait(5)
        self.play(FadeOut(ExHex),FadeOut(EX),run_time=1.5)
        self.wait(5)

        
        self.play(FadeIn(ExHex),FadeIn(EX),run_time=1.5)
        
        self.wait(2)
        self.play(Transform(v,vRinv),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=4)
        self.wait(2)
        ExHex2=[]
        for x,y in HexTilesImproved:
            ExHex2.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex2=VGroup(*ExHex2)
        self.play(FadeOut(ExHex))
        self.wait(4)
        self.play(Transform(v,vRinvImproved))
        self.wait(6)
        self.play(FadeIn(ExHex2))
        self.wait(5)
        self.play(Transform(v,vRinvImprovedC))
        self.wait(5)
        self.play(FadeOut(ExHex2),FadeOut(EX))
        self.wait(2)
        
        self.play(Write(rTitle),run_time=2)
        self.play(Write(yG2,run_time=2))
        self.wait(1)

        c0=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[1][-1].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[0][-1].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)

        self.play(Transform(c0,CC7[0]))
        self.play(Transform(c1,CC7[1]))
        self.play(Transform(c2,CC7[2]))
        self.play(Transform(c3,CC7[3]))
        self.play(Transform(c4,CC7[4]))
        self.play(Transform(c5,CC7[5]))
        self.play(Transform(c6,CC7[6]))
        self.wait(4)
        self.play(FadeOut(rTitle),FadeOut(yG2),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6)))
        self.wait(4)
        self.play(Transform(v,vO),run_time=2)
        self.play(Transform(v,vFC),run_time=2)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        self.play(FadeIn(EX))
        self.wait(2)
        
class S0_SquareGrid(ZoomedScene):
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
                return pTTriangle
            else:
                return pTT2riangle    
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

        S=TexMobject(r"Square\enspace Grid").scale(1.2)
        H=TexMobject(r"Hexagonal\enspace Grid\enspace (Squares)").scale(1)
        sTitle=VGroup(titleRect.copy(),S).shift([0,1.5,0])
        hTitle=VGroup(titleRect,H).shift([0,1.5,0])
        yG1=VGroup(yGRect.copy(),yGs,eight).shift([-2,-1.5,0])
        yG2=VGroup(yGRect,yGhs,seven).shift([-2,-1.5,0])
        
        #BEGIN SCENE
        self.add(NP)
        self.activate_zooming(animate=False)
        self.add(vTriFC)#We add the previous tiling to seamlessly continue
        EX=ExclusionZone(tTriFC.tileDict[0][0],**cExclusion)
        ExSquare=[]
        for x,y in SquareTiles:
            ExSquare.append(ExclusionZone(tTriFC.tileDict[x][y],**cExclusion))
        ExSquare=VGroup(*ExSquare)
        self.add(EX)
        self.play(FadeIn(ExSquare))
        self.wait(2)
        self.play(FadeIn(NLTri1),FadeIn(NLTri2))
        self.wait(2)

        self.play(Transform(vTriFC,vTrapezoidFC),
                  UpdateFromAlphaFuncArg(EX,update_EX,tTriFC.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExSquare,update_EX_multi,ExSquareRef),
                  Transform(NLTri1,NLTrapezoid1),Transform(NLTri2,NLTrapezoid2),run_time=12)
        self.wait(2)
        
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
        self.wait(4)
        self.play(FadeOut(sTitle),FadeOut(yG1),FadeOut(VGroup(c0,c1,c2,c3,c4,c5,c6,c7)))
        self.wait(4)
        
        self.play(Transform(v,v2))
        self.wait(1)
        self.play(FadeIn(EX),run_time=1.5)
        self.wait(2)
        
        ExHex=[]
        for x,y in HexTiles:
            ExHex.append(ExclusionZone(t.tileDict[x][y],**cExclusion))
        ExHex=VGroup(*ExHex)

        self.play(Transform(v,vSPC2),
                  FadeIn(ExHex),run_time=4,rate_func=linear)
        self.wait(2)
        self.play(Transform(v,vFC2),run_time=4)
        self.wait(5)
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
        self.wait(4)
        self.play(FadeOut(hTitle),FadeOut(yG2),FadeOut(VGroup(*c)))
        self.wait(4)
        
class S0_HexagonGrid(ZoomedScene):
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
        
        dl1=TexMobject(r"Hexagonal\enspace Grid",background_stroke_color=WHITE).shift([-1,0,0]).scale(1.2)
        dl2=TexMobject(r"\left(d=1\right)",background_stroke_color=WHITE).scale(1.2).shift([2.7,0,0])
        ds1=TexMobject(r"Hexagonal\enspace Grid",background_stroke_color=WHITE).shift([-1,0,0]).scale(1.2)
        ds2=TexMobject(r"\left(d=\frac{2}{\sqrt{7}}\right)",background_stroke_color=WHITE).scale(0.55).shift([2.7,0,0])
        dlTitle=VGroup(titleRect.copy(),dl1,dl2).shift([0,1.5,0])
        dsTitle=VGroup(titleRect,ds1,ds2).shift([0,1.5,0])
        yG1=VGroup(yGRect,yGh,seven).shift([-2,-1.5,0])

        #BEGIN SCENE
        self.add(NP,v)
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
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=8)
        
        self.play(Write(dlTitle),run_time=2)
        self.play(Write(yG1,run_time=2))
        self.play(FadeOut(dlTitle),run_time=1)
        self.play(FadeOut(yG1,run_time=1))
        
        self.play(ApplyMethod(v.scale,2/r7),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.tileDict[0][0]),
                  UpdateFromAlphaFuncArg(ExHex,update_EX_multi,ExHexRef),run_time=16)
        self.wait()
        
        self.play(Write(dsTitle),run_time=2)
        self.play(FadeIn(yG1,run_time=2))
        self.wait(2)
        
class S0_DeGreyGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],   
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": general_zoom,
    }
    def construct(self):
        xRange=range(-3,2)
        yRange=range(-2,2)
        self.add(NP)
        self.activate_zooming(animate=False)
        H=Text("De Grey Pentagon Grid",font=titleFont).scale(0.55)
        t=Tiling(pGreyUnit,
                 [[Mobject.shift,np.array([2,0,0])]],
                 [[Mobject.shift,np.array([1,1,0])],[Mobject.shift,np.array([-1,1,0])]],
                 xRange,yRange)
        v=t.get_VGroup()
        greyColor(t)
        #print(t.get_tileDict()[0][0][0])
        #print(t.tileDict[0][0][0])
        writeTileList=[*v]
        writeTileList=VGroup(*writeTileList)
        self.play(Write(writeTileList),run_time=30)#5
        self.wait()
        
class DecimalNumberMK2(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            SingleStringTexMobject(char, **kwargs)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(SingleStringTexMobject("\\dots"))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = SingleStringTexMobject(self.unit, color=self.color)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        """
        Configuration is based first off instance attributes,
        but overwritten by any kew word argument.  Relevant
        key words:
        - include_sign
        - group_with_commas
        - num_decimal_places
        - field_name (e.g. 0 or 0.real)
        """
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumber(number, **full_config)

        
        # Make sure last digit has constant height
        #new_decimal.scale(
        #    self[-1].get_height() / new_decimal[-1].get_height()
        #)
        height=new_decimal.get_height()
        yPos=new_decimal.get_center()[1]
        
        for nr in new_decimal:
            if nr.get_tex_string() != ".":
                nr.scale(height/nr.get_height())
                nr.shift([0,(yPos-nr.get_center()[1]),0])

        #This rest should work but doesn't.
        #It seems the horizontal twitching comes from a place after this
        #        if t==0:
        #            t=1
        #            xPos=0#nr.get_center()[0]
        #            xPos2=nr.get_center()[0]
        #            print("initial pos")
        #            print(xPos)
        #        else:
        #            xPos+=digit_width*1.4
        #            print(nr.get_center())
        #            nr.move_to([xPos,nr.get_center()[1],0])
        #            print(nr.get_center())
        #            
        #    else:
        #        xPos+=digit_width*1.4
        #        nr.move_to([xPos,nr.get_center()[1],0])
        #    print(xPos)
        #print(xPos2+xPos)
        
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)
