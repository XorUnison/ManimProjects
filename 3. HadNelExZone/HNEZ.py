#!/usr/bin/env python

from manimlib.imports import *
from Auxiliary import *
import numpy as np
import scipy as sp

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.

NP=NumberPlane()
NL=NumberLine()
NPac=NumberPlane().add_coordinates()
NLan=NumberLine().add_numbers()

cPrototype = {"stroke_width":2,"stroke_color":BLACK,"fill_opacity":1,"color": PURPLE}
cArc = {"stroke_width":0,"stroke_color":RED,"fill_opacity":0,"color": PURPLE}
cArc2 = {"stroke_width":3,"stroke_color":YELLOW,"fill_opacity":0,"color": PURPLE}
cArc3 = {"stroke_width":5,"stroke_color":"#ff0000","fill_opacity":0,"color": PURPLE}
cExclusion = {"stroke_width":2,"stroke_color":WHITE,"fill_opacity":0.5,"color": RED}

arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=0,**cArc)
pTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])

ang=computeABPAngle(np.array([0,0,0]),np.array([1,0,0]))*2
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=ang,**cArc)
pRTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Reuleaux Triangle
arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),angle=-ang,**cArc)
arc1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),angle=-ang,**cArc)
arc2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),angle=-ang,**cArc)
pRMTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])#Thin triangle

arc0=ArcBetweenPoints(np.array([0,0,0]),np.array([1/r2,0,0]),angle=0,**cArc)
arc1=ArcBetweenPoints(np.array([1/r2,0,0]),np.array([1/r2,1/r2,0]),angle=0,**cArc)
arc2=ArcBetweenPoints(np.array([1/r2,1/r2,0]),np.array([0,1/r2,0]),angle=0,**cArc)
arc3=ArcBetweenPoints(np.array([0,1/r2,0]),np.array([0,0,0]),angle=0,**cArc)
pSquare=ArcPolygon(arc0,arc1,arc2,arc3,**cPrototype).move_to([0,0,0])

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
titleFont="Lucida Console"
CC8=ColorCircle(["#aaaaaa","#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.2,0,0])
CC7=ColorCircle(["#00ff00","#ffff00","#ff7b00","#ff0000","#dd00ff","#0000ff","#00ffff"]).scale(0.35).shift([-2,-1.5,0]).shift([1.2,0,0])
eight=TexMobject("8").shift([1.2,0,0])
seven=TexMobject("7").shift([1.2,0.05,0])
yGRect=Rectangle(height=1.2,width=3.5,color=BLACK,fill_opacity=1,stroke_color=WHITE)
yGt=TexMobject("\gamma(G_{T})=").shift([-0.55,0,0])
yGr=TexMobject("\gamma(G_{R})=").shift([-0.55,0,0])
yGs=TexMobject("\gamma(G_{S})=").shift([-0.55,0,0])
yGh=TexMobject("\gamma(G_{H})=").shift([-0.55,0,0])
yGdp=TexMobject("\gamma(G_{DP})=").shift([-0.5,0,0])

def update_EX(mob,alpha,tile):
    new_mob=ExclusionZone(tile,**mob.__dict__)
    mob.become(new_mob)
def update_EX_multi(mobs,alpha,tiles):
    i=0
    for mob in mobs:
        new_mob=ExclusionZone(tiles[i],**mob.__dict__)
        mob.become(new_mob)
        i+=1
    
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
            
        self.add(NP)
        self.activate_zooming(animate=False)


        

        
        #self.add(rect)
        self.play(Write(yG),run_time=2)
        #self.play(Write(TM),run_time=2)
        #self.play(FadeOut(TM),run_time=2)
        #self.play(Transform(TM,TM2))

        self.wait(3)

class S0_TriangleGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        #Define tilings
        def pRT(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pRTriangle
            else:
                return pRMTriangle
        pRTriangleShifted=pRTriangle.copy().shift([0,0.134,0])
        def pRTinv(x,y):
            if ((x+y)%2==0 and (y%2==0)) or ((x+y)%2==0 and (y%2==1)):
                return pRMTriangle
            else:
                return pRTriangleShifted
        def standardColor(t):
            for x in t.xRange:
                for y in t.yRange:
                    if ((x+y)%4==0) and (y%2==0):   t.tileDict[x][y].set_fill("#0000ff")
                    if ((x+y)%4==1) and (y%2==0):   t.tileDict[x][y].set_fill("#dd00ff")##
                    if ((x+y)%4==2) and (y%2==0):   t.tileDict[x][y].set_fill("#00ff00")
                    if ((x+y)%4==3) and (y%2==0):   t.tileDict[x][y].set_fill("#ff7b00")##
                    if ((x+y)%4==0) and (y%2==1):   t.tileDict[x][y].set_fill("#ffff00")
                    if ((x+y)%4==1) and (y%2==1):   t.tileDict[x][y].set_fill("#00ffff")##
                    if ((x+y)%4==2) and (y%2==1):   t.tileDict[x][y].set_fill("#aaaaaa")
                    if ((x+y)%4==3) and (y%2==1):   t.tileDict[x][y].set_fill("#ff0000")##
        def sevenColor(t):
            for x in t.xRange:
                for y in t.yRange:
                    if ((x+3*y)%6==0):              t.tileDict[x][y].set_fill("#0000ff")
                    if ((x+3*y)%6==2):              t.tileDict[x][y].set_fill("#00ff00")
                    if ((x+3*y)%6==4):              t.tileDict[x][y].set_fill("#ffff00")

                    
                    if ((x+y)%4==1) and (y%2==0):   t.tileDict[x][y].set_fill("#dd00ff")##
                    if ((x+y)%4==3) and (y%2==0):   t.tileDict[x][y].set_fill("#ff7b00")##
                    if ((x+y)%4==1) and (y%2==1):   t.tileDict[x][y].set_fill("#00ffff")##
                    if ((x+y)%4==3) and (y%2==1):   t.tileDict[x][y].set_fill("#ff0000")##
        def partialColor(t,arr):
            for x,y in arr:
                t.tileDict[x][y].set_fill("#0000ff")
                t.tileDict[0][0].set_fill("#0000ff")
            
            
        xRange=range(-9,9)
        yRange=range(-4,4)#9,4

        t=Tiling(pTriangle,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],
                 xRange,yRange)
        t.tileDict[0][0].set_fill("#0000ff")
        #standardColor(t)
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

        T=Text("Triangular Tiling",font=titleFont).scale(0.7)
        R=Text("Reuleaux Tiling",font=titleFont).scale(0.7)
        tTitle=VGroup(titleRect.copy(),T).shift([0,1.5,0])
        rTitle=VGroup(titleRect,R).shift([0,1.5,0])
        yG1=VGroup(yGRect.copy(),yGt,eight).shift([-2,-1.5,0])
        yG2=VGroup(yGRect,yGr,seven).shift([-2,-1.5,0])
        
        #BEGIN SCENE
        self.add(NP)
        self.activate_zooming(animate=False)

        self.play(ShowCreation(v),run_time=2)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        self.play(ShowCreation(EX),run_time=3)
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

        c0=t.tileDict[3][-1].copy().set_stroke(opacity=0).scale(0.85)
        c1=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)
        c2=t.tileDict[1][-1].copy().set_stroke(opacity=0).scale(0.85)
        c3=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)
        c4=t.tileDict[0][-1].copy().set_stroke(opacity=0).scale(0.85)
        c5=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)
        c6=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)
        c7=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)

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

        c0=t.tileDict[2][0].copy().set_stroke(opacity=0).scale(0.85)##
        c1=t.tileDict[1][-1].copy().set_stroke(opacity=0).scale(0.85)##
        c2=t.tileDict[3][0].copy().set_stroke(opacity=0).scale(0.85)##
        c3=t.tileDict[0][-1].copy().set_stroke(opacity=0).scale(0.85)##
        c4=t.tileDict[1][0].copy().set_stroke(opacity=0).scale(0.85)##
        c5=t.tileDict[0][0].copy().set_stroke(opacity=0).scale(0.85)##
        c6=t.tileDict[2][-1].copy().set_stroke(opacity=0).scale(0.85)##

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
        
class S0_SquareGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        self.add(NP)
        self.activate_zooming(animate=False)
        t=Tiling(pSquare,
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([0,1/r2,0])]],
                 range(-6,6),range(-3,3))
        v=t.get_VGroup()
        for x in t.xRange:
            for y in t.yRange:
                if ((x+y)%4==0) and (y%2==0):   t.tileDict[x][y].set_color("#0000ff")
                if ((x+y)%4==1) and (y%2==0):   t.tileDict[x][y].set_color("#dd00ff")
                if ((x+y)%4==2) and (y%2==0):   t.tileDict[x][y].set_color("#00ff00")
                if ((x+y)%4==3) and (y%2==0):   t.tileDict[x][y].set_color("#ff0000")
                if ((x+y)%4==0) and (y%2==1):   t.tileDict[x][y].set_color("#ffff00")
                if ((x+y)%4==1) and (y%2==1):   t.tileDict[x][y].set_color("#00ffff")
                if ((x+y)%4==2) and (y%2==1):   t.tileDict[x][y].set_color("#ff7b00")
                if ((x+y)%4==3) and (y%2==1):   t.tileDict[x][y].set_color("#aaaaaa")
        #self.play(ShowCreation(v),run_time=1)
        EX=ExclusionZone(t.tileDict[0][0],**cExclusion)
        #self.play(ShowCreation(EX),run_time=5)
        #self.play(FadeOut(EX))

        
        t2=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 range(-6,6),range(-3,3))
        for x in t2.xRange:
            for y in t2.yRange:
                if ((x+y)%4==0) and (y%2==0):   t2.tileDict[x][y].set_color("#0000ff")
                if ((x+y)%4==1) and (y%2==0):   t2.tileDict[x][y].set_color("#ff8a00")
                if ((x+y)%4==2) and (y%2==0):   t2.tileDict[x][y].set_color("#ffff00")
                if ((x+y)%4==3) and (y%2==0):   t2.tileDict[x][y].set_color("#ff0000")
                if ((x+y)%4==0) and (y%2==1):   t2.tileDict[x][y].set_color("#cc00ff")
                if ((x+y)%4==1) and (y%2==1):   t2.tileDict[x][y].set_color("#00ffff")
                if ((x+y)%4==2) and (y%2==1):   t2.tileDict[x][y].set_color("#00ff00")
                if ((x+y)%4==3) and (y%2==1):   t2.tileDict[x][y].set_color("#aaaaaa")
        v2=t2.get_VGroup()
        self.play(Transform(v,v2),run_time=4)
        self.wait(2)
        
class S0_HexagonGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        self.add(NP)
        t=Tiling(pHexagon,
                 [[Mobject.shift,np.array([r3/2,0,0])]],
                 [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],
                 range(-7,7),range(-4,4))
        self.activate_zooming(animate=False)
        v=t.get_VGroup()
        self.play(ShowCreation(v),run_time=10,rate_func=linear)
        #EX=ExclusionZone(t.get_dict()[0][0],**cExclusion)
        #self.play(ShowCreation(EX),run_time=5)


        
        #self.play(ApplyMethod(v.scale,0.8),
        #          UpdateFromAlphaFuncArg(EX,update_EX,t.get_dict()[0][0]),run_time=5)

        
        #self.play(ApplyMethod(v.scale,0.8),run_time=4)
        #self.play(ShowCreation(pGreyPent),run_time=3)
        #EX=ExclusionZone(pGreyPent,**cExclusion)
        #self.play(ShowCreation(EX),run_time=4,rate_func=linear)
        #self.play(ApplyMethod(pGreyPent.scale,0.02),UpdateFromAlphaFunc(EX,update_EX),run_time=4)
        self.wait()
        
class S0_DeGreyGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],   
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        self.add(NP)
        self.activate_zooming(animate=False)
        t=Tiling(pGreyUnit,
                 [[Mobject.shift,np.array([2,0,0])]],
                 [[Mobject.shift,np.array([1,1,0])],[Mobject.shift,np.array([-1,1,0])]],
                 range(-2,2),range(-2,2))
        v=t.get_VGroup()
        print(t.get_tileDict()[0][0][0])
        print(t.tileDict[0][0][0])
        self.play(ShowCreation(v),run_time=5)
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
