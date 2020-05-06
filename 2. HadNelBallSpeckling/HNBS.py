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

#sCR-sCRO is the inner radius of the boundary annulus
#The offset is used to keep the resulting ArcPolygon big enough to cover the whole left area
secCircRad=0.47
secCircRadOffset=0.0075
funcR=.930/2

#Actually start intro with zoom for K3, show K2 with a checkmark, switch to speckled K3 with ?
class S01_Intro(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [1.5,1.45,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.2,
    }
    def construct(self):
        
        logoX = NewSVGMO({"file_name_prefix":"Ex","fill_opacity":1,"color":WHITE},"X").scale(1.5)
        cm=TextMobject("\checkmark").shift([1.5,1.3,0]).scale(1.2).set_color(GREEN)
        qm=TextMobject("?").shift([1.5,1.3,0]).scale(1.2)
        xFullG = NewSVGMO({"height":0.28,**exBaseG},"AnnBoundary1F").shift([1,1,0])
        xFullR = NewSVGMO({"height":0.28,**exBaseR},"AnnBoundary1F").shift([2,1,0])
        speckles=ImageMobject("PureRGBNoiseCirc").scale(0.13).shift([1,1,0])
        speckles2=speckles.copy().shift([1,0,0])
        speckles3=speckles.copy().shift([0.5,r3/2,0])
        
        self.play(FadeIn(logoX),run_time=3)
        self.wait(1)
        self.play(FadeOut(logoX),run_time=1)
        self.wait(1)
        
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        self.play(FadeIn(NP),ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(8)
        self.bring_to_back(NP,xFullG,xFullR)
        self.play(FadeIn(K2a.shift([1,1,0])),FadeIn(xFullG),FadeIn(xFullR),FadeIn(cm))
        self.wait(1.9)
        self.bring_to_back(NP,speckles)
        self.play(FadeOut(K2a),FadeOut(xFullG),FadeOut(xFullR),FadeIn(qm),FadeIn(K3a.shift([1,1,0])),
                  FadeIn(speckles),FadeIn(speckles2),FadeIn(speckles3),FadeOut(cm))
        self.wait(4.5)
        self.play(FadeOut(qm),FadeOut(K3a),FadeOut(speckles),FadeOut(speckles2),FadeOut(speckles3),
                  FadeOut(NP),ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]))
        self.wait(2)

#After the intro discuss ball radius according to script, switch to the initial view without animation
class S02_BallRadius(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [0,0,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.32,
    }
    def construct(self): # Also consider adding an actual radius number scale
        closeToOne=0.5
        r=(1-closeToOne)/2
        closeToOne2=0.9
        r2=(1-closeToOne2)/2
        rTex=TextMobject("r").shift([-r-0.04,0.1,0]).scale(0.4).set_color(YELLOW)
        ctoTex=TextMobject("cto").shift([closeToOne/2,0.3,0]).scale(0.4).set_color("#ff0000")

        formula1=TexMobject("r=\\frac{1-cto}{2}").scale(0.3).shift([-1.5,0.8,0])
        formula2=TexMobject("1=cto+2r").scale(0.3).shift([-1.5,-0.8,0])
        formula3=TexMobject("r=").scale(0.3).shift([1.29,0.8,0])
        formula4=TexMobject("cto=").scale(0.3).shift([1.25,-0.8,0])

        crLine=Line([0,0,0],[-r,0,0],color=YELLOW)
        crLine2=Line([0,0,0],[-r2,0,0],color=YELLOW)
        rrLine=Line([closeToOne,0,0],[closeToOne+r,0,0],color=YELLOW)
        rrLine2=Line([closeToOne2,0,0],[closeToOne2+r2,0,0],color=YELLOW)
        ctoLine=Line([0,0,0],[closeToOne,0,0],color="#ff0000")
        ctoLine2=Line([0,0,0],[closeToOne2,0,0],color="#ff0000")
        
        rEquals=DecimalNumberMK2(0,num_decimal_places=4)#.next_to(formula4,RIGHT).shift([-0.2,0,0])
        ctoEquals=DecimalNumberMK2(0,num_decimal_places=4)#.next_to(formula4,RIGHT).shift([-0.2,0,0])
        
        rEquals.add_updater(lambda d: d.set_value(rrLine.get_length())) # Next to r=
        rEquals.add_updater(lambda d: d.scale(0.12/d.get_height()))
        rEquals.add_updater(lambda d: d.next_to(formula3,RIGHT).shift([-0.2,0,0]))
        ctoEquals.add_updater(lambda d: d.set_value(ctoLine.get_length())) # Next to cto=
        ctoEquals.add_updater(lambda d: d.scale(0.12/d.get_height()))
        ctoEquals.add_updater(lambda d: d.next_to(formula4,RIGHT).shift([-0.2,0,0]))
        
        c1=Circle(color=BLUE,fill_opacity=1,stroke_width=0).scale(r).shift([0,0,0])
        c2=Circle(color=GREEN,fill_opacity=1,stroke_width=0).scale(r).shift([0,1,0])
        c3=Circle(color=PURPLE,fill_opacity=1,stroke_width=0).scale(r).shift([closeToOne,0,0])
        c4=Circle(color=PURPLE,fill_opacity=1,stroke_width=0).scale(r).shift([2-closeToOne,0,0])
        ann=Annulus(color=RED,fill_opacity=0.5,stroke_width=0,inner_radius=1-r,outer_radius=1+r)
        
        c1_2=Circle(color=BLUE,fill_opacity=1,stroke_width=0).scale(r2).shift([0,0,0])
        c2_2=Circle(color=GREEN,fill_opacity=1,stroke_width=0).scale(r2).shift([0,1,0])
        c3_2=Circle(color=PURPLE,fill_opacity=1,stroke_width=0).scale(r2).shift([closeToOne2,0,0])
        c4_2=Circle(color=PURPLE,fill_opacity=1,stroke_width=0).scale(r2).shift([2-closeToOne2,0,0])
        ann2=Annulus(color=RED,fill_opacity=0.5,stroke_width=0,inner_radius=1-r2,outer_radius=1+r2)
        
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        self.play(FadeIn(NP),ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(0.5)
        self.play(FadeIn(c1),FadeIn(c2),FadeIn(c3),FadeIn(c4),FadeIn(ann))
        self.wait(10)
        self.play(FadeIn(crLine),FadeIn(rrLine),FadeIn(ctoLine),FadeIn(rTex),FadeIn(ctoTex),
                  FadeIn(formula1),FadeIn(formula2),FadeIn(formula3),FadeIn(formula4),
                  FadeIn(rEquals),FadeIn(ctoEquals))
        self.wait(2)
        self.play(Transform(ann,ann2),Transform(c1,c1_2),Transform(c2,c2_2),Transform(c3,c3_2),
                  Transform(c4,c4_2),Transform(crLine,crLine2),Transform(ctoLine,ctoLine2),
                  Transform(rrLine,rrLine2),ApplyMethod(rTex.shift,[r-r2,0,0]),
                  ApplyMethod(ctoTex.shift,[(closeToOne2-closeToOne)/2,-0.2,0]),run_time=30)
        self.wait(2)
        self.play(FadeOut(c1),FadeOut(c2),FadeOut(c3),FadeOut(c4),FadeOut(ann),FadeOut(ctoTex),
                  FadeOut(NP),ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]),
                  FadeOut(formula1),FadeOut(formula2),FadeOut(crLine),FadeOut(rrLine),FadeOut(ctoLine),
                  FadeOut(rTex),FadeOut(formula3),FadeOut(formula4),FadeOut(rEquals),FadeOut(ctoEquals))
        self.wait(1)
        
#Briefly concludes the previous scene with UD width n-balls, then goes into setting the stage for
#the speckling and it's actual exclusion dynamics
class S03_Measures(ZoomedScene):#Rename to encapsulate the current contents
    CONFIG = {
        "zoomed_camera_frame_starting_position": [2.5,2,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.35,
    }
    def construct(self):
        qm=TextMobject("?").shift([2.75,1.25,0]).scale(0.3).set_color("#FF0000")
        bqm=TextMobject("?").shift([3,2,0]).scale(1.3).set_color(WHITE)
        st=TextMobject("×").shift([3,2,0]).scale(2.85).set_color("#FF0000")
        x=TexMobject("\mathbb{X}",color="#FF0000").shift([3.25,1.25,0]).scale(0.28)
        areaBG=Circle(fill_opacity=1,color=BLACK).shift([2,2,0]).scale(0.49)
        areaBG2=areaBG.copy().shift([1,0,0])
        arGBG=Circle(fill_opacity=1/3,color="#00FF00").shift([2,2,0]).scale(0.49)
        arGBG2=arGBG.copy().shift([1,0,0])
        speckles=ImageMobject("PureRGBNoiseCirc").scale(0.495).shift([2,2,0])
        speckles2=speckles.copy().shift([1,0,0]).rotate(math.pi/2)
        K3MB2=K3MB.copy().shift([1,0,0])
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])

        self.bring_to_back(NP,K2aB)
        self.play(FadeIn(NP),FadeIn(K2aB.shift([2,2,0])),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(1)
        dbrace = Brace(K2aB,[1,0,0]).shift([-0.2,0,0])#we need to initialize these braces here
        rbrace = Brace(K2aB,[-1,0,0]).scale(0.5).shift([0.25,-0.25,0])
        mbrace = Brace(K3MB[1],[0,-1,0]).shift([0,0.20,0])
        rTex=TextMobject("r").next_to(rbrace,LEFT).shift([0.24,0,0])
        mTex=TextMobject("m").next_to(mbrace,DOWN).shift([0,0.24,0])
        oneTex=TextMobject("1").shift([4.1,2,0]).shift([-0.2,0,0])
        self.play(FadeIn(dbrace),FadeIn(oneTex))
        self.wait(1)
        self.play(FadeOut(dbrace),FadeOut(oneTex))
        self.bring_to_back(NP,speckles,speckles2,K2aB)
        self.add(K3MB[2][0],K3MB[2][2],K3MB[2][4],
                 K3MB2[2][0],K3MB2[2][2],K3MB2[2][4])
        self.bring_to_back(NP,K3MB[1],K3MB[2][0],K3MB[2][2],K3MB[2][4],K3MB[0],
                           K3MB2[1],K3MB2[2][0],K3MB2[2][2],K3MB2[2][4],K3MB2[0])
        self.play(FadeIn(K3MB[1]),FadeIn(K3MB[0]),FadeIn(K3MB2[1]),FadeIn(K3MB2[0]),
                  Transform(K3MB[2][0],K3MB[2][1]),Transform(K3MB[2][2],K3MB[2][3]),
                  Transform(K3MB[2][4],K3MB[2][5]),Transform(K3MB2[2][0],K3MB2[2][1]),
                  Transform(K3MB2[2][2],K3MB2[2][3]),Transform(K3MB2[2][4],K3MB2[2][5]),
                  FadeIn(speckles),FadeIn(speckles2),FadeIn(bqm),run_time=3)
        self.wait(15)
        self.play(FadeOut(K3MB2[2][0]),FadeOut(K3MB2[2][2]),FadeOut(K3MB2[2][4]),FadeOut(speckles2),
                  FadeIn(st),FadeOut(bqm))
        self.play(FadeOut(st))
        self.wait(17)
        self.play(FadeIn(mbrace),FadeIn(rbrace),FadeIn(rTex),FadeIn(mTex))
        self.wait(20)
        self.bring_to_back(NP,arGBG,arGBG2,speckles,K2aB,K3MB2[2][0],K3MB2[1])
        self.bring_to_front(K3MB2[2][0],K3MB2[0])
        self.play(FadeIn(K3MB2[2][0]),FadeOut(speckles),FadeOut(K3MB[2][2]),FadeOut(K3MB[2][4]),
                  FadeIn(qm),FadeIn(arGBG),FadeIn(arGBG2))
        #Switch to exclusion bar on the right here
        self.wait(7)
        self.play(FadeIn(K3CMB[3][1]),FadeIn(x))
        self.wait(12)
        self.play(FadeOut(K3CMB[3][1]),FadeOut(x),FadeOut(arGBG),FadeOut(arGBG2),FadeOut(K3MB[2][0]),
                  FadeOut(K3MB2[2][0]),FadeOut(qm),FadeOut(mbrace),FadeOut(rbrace),FadeOut(rTex),
                  FadeOut(mTex))
        self.wait(1)

#Here we'll start showing the actual dynamics of full exclusion 
class S04_ExclusionExplanation(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [2.5,2,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.35,
    }
        
    def construct(self):
        def update_arc(mob,alpha):
            dx = interpolate(0,0.5,alpha)
            tracerCenter=tracer.get_center()
            secCircleCenter=K2aB[1].get_center()
            intersections=get_intersections(tracerCenter[0],tracerCenter[1],1,
                                            secCircleCenter[0],secCircleCenter[1],secCircRad)
            if intersections==None:
                #arc=Arc(0,1,radius=1)
                #mob.become(ArcPolygon(arc,arc.flip(RIGHT),fill_opacity=0,stroke_width=0))
                mob.become(Line([0,0,0],[0,0,0]))
            else:
                guide_line00=Line(tracerCenter,intersections[1])
                guide_line01=Line(tracerCenter,intersections[0])
                arc0angle0=guide_line00.get_angle()
                arc0angle1=guide_line01.get_angle()-guide_line00.get_angle()
                guide_line10=Line(secCircleCenter,intersections[1])
                guide_line11=Line(secCircleCenter,intersections[0])
                arc1angle0=guide_line10.get_angle()
                arc1angle1=guide_line11.get_angle()-guide_line10.get_angle()
                
                guide_vec2=Line(tracerCenter,secCircleCenter).get_vector()

                arc0=Arc(arc0angle0,arc0angle1,radius=1).shift(tracerCenter).flip(guide_vec2)
                arc1=Arc(arc1angle0,arc1angle1,radius=secCircRad).shift(secCircleCenter)
            
                new_mob=ArcPolygon(arc0,arc1,fill_opacity=1,color=RED)
                mob.become(new_mob)
            
        x=TexMobject("\mathbb{X}",color="#FF0000").shift([3,1.25,0]).scale(0.28)
        GFull=Circle(fill_opacity=1,color="#00FF00").shift([2,2,0]).scale(0.49)
        RFull=Circle(fill_opacity=1,color=RED).shift([3,2,0]).scale(0.49)
        GBoundary=Annulus(fill_opacity=1,color="#00FF00",inner_radius=0.90/2,
                          outer_radius=0.95/2).shift([2,2,0])
        GLine=Line([1.51,2,0],[2.49,2,0],color="#00FF00",stroke_width=6.5)
        
        tracer=VGroup(Annulus(fill_opacity=1,color="#FF0000",inner_radius=0.985,
                          outer_radius=1.015),Circle(color="#FF0000",
                          fill_opacity=1).scale(0.0075)).shift([2.4625,2,0])

        
        self.activate_zooming(animate=False)
        self.add(NP,K2aB.shift([2,2,0]),K3CMB[1],K3CMB[0],K3MB[1],K3MB[0])
        self.bring_to_back(NP,GFull,K3CMB[1],K3CMB[2][0],K3CMB[0])
        #Animation begins here
        self.play(FadeIn(GFull),Transform(K3CMB[3][0],K3CMB[3][4]),FadeIn(x),
                  Transform(K3MB[2][0],K3MB[2][6]))
        self.wait(8)
        self.play(FadeOut(GFull),FadeIn(GBoundary),FadeOut(K3MB[2][0]))
        self.wait(4)
        self.bring_to_front(K2aB,tracer,K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][0],x)
        self.play(FadeIn(tracer))
        self.wait(4)


        arcP = Arc(0,2,fill_opacity=1,color="#FF0000").shift([3,2,0])
        self.bring_to_back(NP,arcP)

        
        
        self.bring_to_front(K2aB,tracer,K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][0],x)
        self.play(Rotate(tracer,np.pi,about_point=[2,2,0],axis=OUT),
                  UpdateFromAlphaFunc(arcP,update_arc),
                  run_time=11)
        self.wait(4)
        self.remove(arcP)
        self.add(RFull)
        self.bring_to_front(RFull,GLine,K2aB,tracer,K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][0],x)
        self.play(FadeOut(RFull),FadeOut(GBoundary),FadeIn(GLine))
        self.wait(1)
        self.play(ApplyMethod(tracer.shift,[(secCircRad-secCircRadOffset)*2,0,0]))
        self.bring_to_front(GLine,K2aB,tracer,K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][0],x)
        self.bring_to_back(NP,arcP)
        self.play(ApplyMethod(tracer.shift,[-(secCircRad-secCircRadOffset)*2,0,0]),
                  UpdateFromAlphaFunc(arcP,update_arc),
                  run_time=3)
        self.wait(1)
        self.add(RFull)
        self.remove(arcP)
        self.bring_to_back(NP,RFull)
        self.play(FadeOut(RFull),FadeOut(tracer))
        self.wait(1)

        funcAry=[]
        for radii in [0.2,0.4,0.6,0.8,1]:
            funcAry.append(FunctionGraph(lambda x:cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                                         x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))
            funcAry.append(FunctionGraph(lambda x:-cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                                         x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))
        funcVG=VGroup(*funcAry)
        for func in funcVG:
            self.bring_to_back(NP,func)
            self.play(ShowCreation(func),run_time=0.5)
        self.wait(3)
        self.bring_to_front(K2aB)
        self.play(FadeOut(funcVG))
        self.wait(1)


class S05_ExclusionThirdAndIteration(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [2.5,2,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.35,
    }
    def construct(self):
        def calcFormulas(i):
            powerFormula=TexMobject("\\bigg(\\frac{2}{3}\\bigg)^{"+str(i)+"}").shift([3.8,2,0]).scale(.2)
            fracFormula=TexMobject("\\frac{"+str(2**i)+"}{"+str(3**i)+"}").shift([4.2,2,0]).scale(0.2)
            decFormula=TexMobject(str((2/3)**i)).shift([4,1.6,0]).scale(0.2)
            return [powerFormula,fracFormula,decFormula]
        measText=TextMobject("Available Measure").shift([4,2.35,0]).scale(0.24)
        measRec=Rectangle(width=0.98,height=0.98,fill_opacity=1,color=BLACK,
                          stroke_width=4).shift([4,2,0])
        measNull=TextMobject("0").shift([4,1.95,0]).scale(0.8)
        GLine=Line([1.51,2,0],[2.49,2,0],color="#00FF00",stroke_width=6.5)
        GThird=Line([1.51,2,0],[2.49,2,0],color="#00FF00",stroke_width=6.5,stroke_opacity=1/3)
        tracer=VGroup(Annulus(fill_opacity=1,color="#FF0000",inner_radius=0.985,
                          outer_radius=1.015),Circle(color="#FF0000",
                          fill_opacity=1).scale(0.0075)).shift([3-(secCircRad-secCircRadOffset),2,0])
        tracer2=tracer.copy().set_color(GREEN)
        x=TexMobject("\mathbb{X}",color="#FF0000").shift([3,1.25,0]).scale(0.28)
        intArrow1=Arrow([2.09,2.15,0],[2.09,2,0])
        intArrow2=Arrow([1.85,1.85,0],[1.85,2,0])
        oos=Rectangle(height=2,width=3).shift([99,0,0])#OutOfSector
        arGBG=Circle(fill_opacity=1/3,color="#00FF00").shift([3,2,0]).scale(0.49)
        arGBGLeft=arGBG.copy().shift([-1,0,0])
        arGBGLeftLow=arGBGLeft.copy().set_opacity(0.05)
        
        funcAry=[]
        for radii in [1]:
            funcAry.append(FunctionGraph(lambda x:cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                        stroke_opacity=1/3,x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))
            funcAry.append(FunctionGraph(lambda x:-cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                        stroke_opacity=1/3,x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))

        funcAry2=[]
        for radii in [0.2,0.4,0.6,0.8]:#[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:#
            funcAry2.append(FunctionGraph(lambda x:cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                        stroke_opacity=1/3,x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))
            funcAry2.append(FunctionGraph(lambda x:-cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                        stroke_opacity=1/3,x_max=funcR,color="#00FF00",stroke_width=7).shift([2,2,0]))
        funcVG=VGroup(*funcAry2)

        
        self.activate_zooming(animate=False)
        #Add full exclusion bar
        self.add(NP,GLine,K2aB.shift([2,2,0]),K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][4],x)
        
        self.wait(1)
        self.play(Transform(GLine,GThird),Transform(K3CMB[3][4],K3CMB[3][1]),
                  ApplyMethod(x.shift,[0.25,0,0]))
        self.wait(1)
        self.bring_to_front(K2aB,tracer,K3CMB[1],K3CMB[0],K3MB[1],K3MB[0],K3CMB[3][4],x)
        self.play(FadeIn(tracer),run_time=0.5)
        self.wait(1)
        self.play(ApplyMethod(tracer.shift,[(secCircRad-secCircRadOffset)*2,0,0]))
        self.wait(1)
        self.play(Rotate(tracer,np.pi,about_point=[3,2,0],axis=OUT),run_time=3)
        self.wait(1)
        self.play(FadeOut(tracer))
        self.wait(6)
        self.play(FadeIn(tracer2.move_to([2,2.25,0])))
        self.wait(4)
        self.play(FadeIn(tracer.move_to([2.976,2.465,0])),FadeIn(intArrow1))
        self.wait(1)
        self.play(Rotate(tracer,-0.92,about_point=tracer2.get_center(),axis=OUT),run_time=6)
        self.play(FadeIn(intArrow2))
        #self.wait(1)
        self.wait(1)
        self.play(FadeOut(intArrow2),FadeOut(intArrow1),FadeOut(tracer),FadeOut(tracer2))
        self.wait(1)
        
        #Contains the animation for the 3rd iteration rendering the second speckling impossible
        sForms=calcFormulas(1)
        self.bring_to_back(NP,arGBG)
        self.play(Transform(K3CMB[2][0],K3CMB[2][1]),FadeIn(arGBG),FadeIn(measRec),FadeIn(measText),
                  ShowCreation(sForms[0]),ShowCreation(sForms[1]),ShowCreation(sForms[2]))
        self.wait(7)
        self.bring_to_back(NP,K3CMB[1],K3CMB[3][4],K3CMB[2][0],K3CMB[0])
        #self.play(Transform(K3CMB[3][4],K3CMB[3][1]))
        #self.wait(1)
        forms=calcFormulas(2)
        self.play(Transform(K3CMB[3][4],K3CMB[3][2]),FadeIn(funcAry[0]),
                  ApplyMethod(x.shift,[-0.06,0,0]),Transform(sForms[0],forms[0]),
                  Transform(sForms[1],forms[1]),Transform(sForms[2],forms[2]))
        self.wait(1)
        forms=calcFormulas(3)
        self.play(#This play and AnimationGroup combination is needed for simultaneous animation
            AnimationGroup(FadeIn(oos,run_time=2),FadeOutAndShift(K3CMB[2][0],[-0.3,0,0],run_time=1),
                           lag_ratio=1),
            AnimationGroup(FadeIn(oos,run_time=2),FadeOut(arGBG),lag_ratio=1),
            AnimationGroup(Transform(sForms[0],forms[0]),Transform(sForms[1],forms[1]),
                           Transform(sForms[2],forms[2]),run_time=3),
            AnimationGroup(Transform(K3CMB[3][4],K3CMB[3][3]),FadeIn(funcAry[1]),run_time=3,lag_ratio=0),
            AnimationGroup(ApplyMethod(x.shift,[-0.06,0,0]),run_time=3),
            AnimationGroup(ApplyMethod(K2aB.shift,[0,0,0]),run_time=3)#The NullShift is used for sorting
            )
        self.wait(2)

        
        
        zf=0.35
        mbH=0.15
        mbW=0.8
        sW =5
        i=3
        for func in funcVG:
            i+=1
            forms=calcFormulas(i)
            localMB=MeasureBar(0.15,0.8,5,[],
                  [{"height":mbH-(sW/(50/zf)),"width":mbW*Xthird(i)-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[mbW/2-(mbW*Xthird(i))/2,0,0]}
                   ]).assembleMeasureBar().shift([3,1.25,0])
            self.bring_to_back(NP,func)
            self.play(ShowCreation(func),Transform(K3CMB[3][4],localMB[3][0]),
                      ApplyMethod(x.shift,[-0.016,0,0]),Transform(sForms[0],forms[0]),
                      Transform(sForms[1],forms[1]),Transform(sForms[2],forms[2]),run_time=0.75)
        self.wait(3)
        self.bring_to_back(NP,arGBGLeft,K3MB[1],K3MB[2][0])
        self.play(FadeOut(GLine),FadeOut(funcAry[0]),FadeOut(funcAry[1]),FadeIn(arGBGLeft),
                  Transform(K3CMB[3][4],K3CMB[3][5]),ApplyMethod(x.move_to,[3,1.25,0]),
                  Transform(K3MB[2][0],K3MB[2][1]),FadeOut(funcVG),FadeOut(sForms[0]),
                  FadeOut(sForms[1]),FadeOut(sForms[2]),FadeIn(measNull))
        self.wait(2)
        self.play(Transform(arGBGLeft,arGBGLeftLow),Transform(K3MB[2][0],K3MB[2][7]))
        self.wait(2)
        self.play(FadeOut(arGBGLeft),FadeOut(K3MB[2][0]),FadeOut(K3CMB[3][4]),FadeOut(x),FadeOut(NP),
                  FadeOut(K2aB),FadeOut(K3CMB[1]),FadeOut(K3CMB[0]),FadeOut(K3MB[1]),FadeOut(K3MB[0]),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]),
                  FadeOut(measRec),FadeOut(measText),FadeOut(measNull))
        self.wait(2)
        

class S06_ContradictionFinish(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [4,2,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.435,
        #"zoom_factor": 0.1,
    }
    def construct(self):
        A1=Arc(0,math.pi*(2/3),radius=0.122)
        AP1=ArcPolygon(A1,ArcBetweenPoints(A1.get_points()[0],[0,0,0],angle=0),
                          ArcBetweenPoints([0,0,0],A1.get_points()[-1],angle=0),
                       fill_opacity=1,color="#FF0000",stroke_width=0).shift([1.5,1.5,0])
        A2=Arc(math.pi*(2/3),math.pi*(2/3),radius=0.122)
        AP2=ArcPolygon(A2,ArcBetweenPoints(A2.get_points()[0],[0,0,0],angle=0),
                          ArcBetweenPoints([0,0,0],A2.get_points()[-1],angle=0),
                       fill_opacity=1,color="#0000FF",stroke_width=0).shift([1.5,1.5,0])
        speckles=ImageMobject("PureRGBNoiseCirc").scale(0.495).shift([5.5,1.5,0])
        
        K3aB.shift([5.5,1.5,0])
        K3.shift([1.5,1.5,0])
        K3e.shift([1.5,1.5,0])
        K3AltColors.shift([1.5,1.5,0])
        xFullG=Circle(color=GREEN,fill_opacity=1).scale(0.49).move_to(K3aB[0].get_center())
        xFullR=Circle(color=RED,fill_opacity=1).scale(0.49).move_to(K3aB[1].get_center())
        xFullB=Circle(color=BLUE,fill_opacity=1).scale(0.49).move_to(K3aB[2].get_center())
        xFullP=Circle(color=PURPLE,fill_opacity=1).scale(0.49).move_to(K3aB[1].get_center())
        xFullC=Circle(color="#00ffff",fill_opacity=1).scale(0.49).move_to(K3aB[2].get_center())
        intArrow1=Arrow([3,2.5,0],[5,2.5,0])
        intArrow2=Arrow([5,1.5,0],[3,1.5,0])
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        self.play(ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]),
                  FadeIn(NP),FadeIn(xFullR),FadeIn(xFullG),FadeIn(xFullB),FadeIn(K3aB),
                  FadeIn(K3))
        self.play(ShowCreation(intArrow1),ShowCreation(intArrow2))
        self.wait(11)
        self.bring_to_back(NP,xFullR,xFullG,xFullB,speckles,K3aB)
        self.play(Transform(K3[4],K3e[4]),Transform(K3[5],K3e[5]),FadeOut(xFullB),FadeOut(xFullR),
                  FadeIn(speckles),ShowCreation(AP2),ShowCreation(AP1),Transform(K3[3],K3AltColors[3]),
                  run_time=5)
        self.remove(xFullG)
        self.wait(1)
        self.bring_to_back(NP,xFullP,xFullC,speckles,K3aB)
        self.play(Transform(K3[4],K3AltColors[4]),Transform(K3[5],K3AltColors[5]),
                  FadeIn(xFullP),FadeIn(xFullC),run_time=3)
        self.wait(10)
        self.play(FadeOut(K3),FadeOut(K3aB),FadeOut(xFullP),FadeOut(xFullC),FadeOut(NP),FadeOut(AP1),
                  FadeOut(AP2),FadeOut(intArrow1),FadeOut(intArrow2),FadeOut(speckles),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]),run_time=5)
        self.wait(2)



        #x=TexMobject("\mathbb{X}",color="#FF0000").shift([3,1.25,1]).scale(0.28)
        #x2=x.copy().shift([0,-0.25,0])
        #x3=TexMobject("\mathbb{X}",color="#0000FF").shift([3,0.75,-1]).scale(0.28)
        #speckles=ImageMobject("PureRGBNoiseCirc").scale(0.495).shift([2,2,0])
        #self.activate_zooming(animate=False)
        #self.add(NP,K3MB[2][0],K3MB[2][2],K3MB[2][4],K3CBMB[1],K3CBMB[0],K3CRMB[1],K3CRMB[0],
        #         K3CMB[1],K3CMB[0],K2aB.shift([2,2,0]),x,x2,x3)
        #self.bring_to_back(NP,K3CBMB[1],K3CBMB[0],K3CRMB[1],K3CRMB[0],K3CMB[1],K3CMB[0],
        #                   K3CBMB[3][0],K3CRMB[3][0],K3CMB[3][0],speckles,K2aB,
        #                   K3MB[1],K3MB[2][0],K3MB[2][2],K3MB[2][4],K3MB[0],K2aB)
        #self.bring_to_front(x,x2,x3)
        #self.play(FadeIn(x),FadeIn(x2),FadeIn(x3),FadeIn(K3MB[1]),FadeIn(K3MB[0]),
        #          Transform(K3MB[2][0],K3MB[2][1]),Transform(K3MB[2][2],K3MB[2][3]),
        #          Transform(K3MB[2][4],K3MB[2][5]),Transform(K3CBMB[3][0],K3CBMB[3][1]),
        #          Transform(K3CRMB[3][0],K3CRMB[3][1]),Transform(K3CMB[3][0],K3CMB[3][4]),
        #          FadeIn(speckles),run_time=1)
        #self.wait(2)
        
        
class Thumbnail(ZoomedScene):
    def construct(self):
        funcAry=[]
        for radii in [0.2,0.4,0.6,0.8,1]:
            funcAry.append(FunctionGraph(lambda x:cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                                         x_max=funcR,color="#00FF00",stroke_width=4).shift([3,2,0]))
            funcAry.append(FunctionGraph(lambda x:-cmath.sqrt(funcR**2-x**2)*radii,x_min=-funcR,
                                         x_max=funcR,color="#00FF00",stroke_width=4).shift([3,2,0]))
        funcVG=VGroup(*funcAry).scale(1.003)
        funcVG=VGroup(K2aB[0].shift([3,2,0]),funcVG).scale(2)
        speckles=ImageMobject("PureRGBNoiseCirc").scale(0.14).shift([-3,2,0])
        speckles2=speckles.copy().shift([1,0,0])
        speckles3=speckles.copy().shift([0.5,r3/2,0])
        qm=TextMobject("?").scale(1.8).shift([0.5,0.3,0])
        speckleVG=VGroup(qm,K3a).shift([-3,2,0]).scale(2)
        speckleG=Group(speckles,speckles2,speckles3).scale(2)
        self.add(NP)
        self.add(speckles,speckles2,speckles3,speckleVG)
        self.add(funcVG)
        self.bring_to_front(K2aB[0])
        self.add(TextMobject("Hadwiger-Nelson\\\\Problem").shift([-3.5,-2,0]).scale(1.7))
        self.add(TextMobject("Why tiles?").shift([3.5,-2,0]).scale(2.5))
        #Save via -s
        
class TestZone(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.5,
    }
    def construct(self):
        self.add(NP)
        self.activate_zooming(animate=False)
        arc0=ArcBetweenPoints(np.array([2,2,0]),np.array([2,-2,0]),stroke_width=0,angle=0)
        arc1=ArcBetweenPoints(np.array([2,-2,0]),np.array([-2,-2,0]),stroke_width=0,angle=0)
        arc2=ArcBetweenPoints(np.array([-2,-2,0]),np.array([-2,2,0]),stroke_width=0,angle=0)
        arc3=ArcBetweenPoints(np.array([-2,2,0]),np.array([2,2,0]),stroke_width=0,angle=0)
        arc4=ArcBetweenPoints(np.array([1,1,0]),np.array([-1,1,0]),stroke_width=0,angle=0)
        arc5=ArcBetweenPoints(np.array([-1,1,0]),np.array([-1,-1,0]),stroke_width=0,angle=0)
        arc6=ArcBetweenPoints(np.array([-1,-1,0]),np.array([1,-1,0]),stroke_width=0,angle=0)
        arc7=ArcBetweenPoints(np.array([1,-1,0]),np.array([1,1,0]),stroke_width=0,angle=0)
        AP=ArcPolygon(arc0,arc1,arc2,arc3,arc5,arc6,arc7,arc4,arc0,
                      fill_opacity=0.5,color=RED,stroke_width=3.0,stroke_color=GREEN)
        #self.play(ShowCreation(AP),run_time=13,rate_func=linear)
        #self.wait(2)
        #p=Polygon([1,1,0],[1,-1,0],[-1,-1,0],[-1,1,0]).scale(1)
        #p2=p.copy().flip(RIGHT)
        #p2=Polygon([1,1,0],[-1,1,0],[-1,-1,0],[1,-1,0]).scale(1)
        p=RegularPolygon(4).flip(RIGHT).scale(0.5)
        EX=ExclusionZone(p,fill_opacity=0.5,color=RED,stroke_width=3,stroke_color=GREEN)
        #EX2=ExclusionZone(p2,fill_opacity=1,color=RED,stroke_width=3,stroke_color=GREEN)

        self.play(ShowCreation(p),run_time=2,rate_func=linear)
        self.play(ShowCreation(EX),run_time=6,rate_func=linear)

        #self.play(ShowCreation(EX.get_ExZone()),fill_opacity=1),run_time=6,rate_func=linear)
        #self.play(ShowCreation(Arc(0,-math.pi/2,radius=1,fill_opacity=1).move_arc_center_to([0,0,0])),
        #          run_time=3,rate_func=linear)
        #self.remove(p)
        #self.play(ShowCreation(p2),run_time=2,rate_func=linear)
        self.wait(2)
        
        for i in range(3):
            print("pre change")
            print(i)
            i=-(i+1)
            print("post change")
            print(i)

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
            if nr.get_tex_string() is not ".":
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
