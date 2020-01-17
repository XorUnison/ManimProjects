#!/usr/bin/env python

from manimlib.imports import *
from Auxiliary import *

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
NPac=NumberPlane()
NPac.add_coordinates()
NLan=NumberLine().add_numbers()

class S01_Intro(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.15,
    }
    def construct(self):
        
        logoX = NewSVGMO({"file_name_prefix": "Ex","fill_opacity" : 1,"color" : WHITE},"X").scale(1.5)
        xorTheorem=TextMobject("""  Why coloring unit distance graphs \\\\
                                    in 2 or more dimensions requires tiles""").shift([0,-2.5,0])
        #HNP=TextMobject("""Hadwiger-Nelson Problem:\\\\
        #How many colors are needed to color all\\\\
        #points on the plane so that no 2 points at unit\\\\
        #distance have the same color?""")


        HNP1=TextMobject("""7 decades ago a relatively simple math\\\\
                            question was asked for the first time...""")
        HNP2=TextMobject("""What’s the lowest number of\\\\
                            colors with which we can\\\\
                            color the entire plane,\\\\
                            so that no 2 points at unit\\\\
                            distance have the same color?""")
        HNP3=TextMobject("""This number we’re looking for is\\\\
                            the chromatic number of the plane.""")
        HNP4=TextMobject("""That’s the Hadwiger-Nelson problem.""")
        
        #self.add(NP,logoX,xorTheorem)
        self.play(FadeIn(logoX),run_time=3)
        self.wait(1)
        self.play(FadeOut(logoX),run_time=1)
        self.wait(1)
        self.play(FadeIn(HNP1),run_time=2)
        self.wait(2)
        self.play(FadeOut(HNP1),run_time=2)
        self.play(ShowCreation(NPac),run_time=2)
        self.wait(2)
        self.play(FadeIn(K2))
        self.wait(2)
        bounds = TexMobject("CNP = ?").shift([5.3,2.5,0])
        self.play(FadeIn(bounds))
        self.wait(2)
        sq=Square(fill_opacity=1,fill_color=GRAY,**cGray).scale(8).shift([0,-3.7,0])
        qm=TextMobject("?").scale(3)
        self.play(FadeInFrom(sq,direction=[0,-9,0]),run_time=10)
        self.play(FadeIn(qm),run_time=3)
        self.remove(K2)
        self.wait(2)
        tiles=hexagonsV.copy()
        K3c=K3.copy()
        self.play(FadeIn(tiles.shift([-3,0,0])),run_time=2)
        self.wait(1)
        self.play(FadeIn(K3c.scale(2).shift([3,-0.5,0])),run_time=2)
        self.wait(2)
        self.play(FadeOut(qm),FadeOut(K3c),ApplyMethod(tiles.shift,[3,0,0]),
                  run_time=2)
        self.remove(bounds)
        self.wait(2)
        self.play(FadeOut(sq),FadeOut(tiles),
                  run_time=2)
        self.wait(2)
        
class S02_UpperBounds(ZoomedScene):
    #This scene is for explaining how we understand upper bounds
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.15,
    }
    def construct(self):
        hVec=[0,r3,0]+rotate_vector([0,r3*0.5,0],np.pi/3,[0,0,1])
        hexagonsV2=hexagonsV.copy().shift(hVec)
        hexagonsV3=hexagonsV.copy().shift(rotate_vector(hVec,np.pi/3,[0,0,1]))
        hexagonsV4=hexagonsV.copy().shift(rotate_vector(hVec,2*np.pi/3,[0,0,1]))
        hexagonsV5=hexagonsV.copy().shift(rotate_vector(hVec,np.pi,[0,0,1]))
        hexagonsV6=hexagonsV.copy().shift(rotate_vector(hVec,4*np.pi/3,[0,0,1]))
        hexagonsV7=hexagonsV.copy().shift(rotate_vector(hVec,5*np.pi/3,[0,0,1]))

        #Add the plane and the initial 7 hexagons
        self.add(NPac)
        self.wait(1)
        self.play(ShowCreation(hexagonsV,lag_ratio=0.8,run_time=3,rate_func=linear))
        self.wait(1)

        #This zooms in
        self.activate_zooming(animate=True)

        #Show line and brackets to explain half bounding
        self.bring_to_front(hexagonsV[0])#This facilitates correct highlighting later
        l=Line([-0.5,0,0],[0.5,0,0])
        lbracket=TexMobject("[").shift([-0.5,0,0])
        rbracket=TexMobject(")").shift([0.5,0,0])
        lnumber=TexMobject("0").shift([-0.35,-0.1,0]).scale(0.3)
        rnumber=TexMobject("1").shift([0.35,-0.1,0]).scale(0.3)
        self.play(FadeIn(l),FadeIn(lbracket),FadeIn(rbracket),FadeIn(lnumber),FadeIn(rnumber))
        self.wait(2)

        #Initiate arrows and highlight hexagons
        larrow=Arrow([0,0.3,0],[-0.5,0,0]).scale(6.2)
        rarrow=Arrow([0,0.3,0],[0.5,0,0]).scale(6.2)
        H1highlight=RegularPolygon(6,**cBlue,**stroke200,**hexBase).scale(0.5)
        H6highlight=RegularPolygon(6,**cYellow,**stroke200,**hexBase).scale(0.5).shift([0,r3*-0.5,
                                0]).rotate((np.pi)/3,about_point=[0,0,1])
        H7highlight=RegularPolygon(6,**cGreen,**stroke200,**hexBase).scale(0.5).shift([0,r3*-0.5,
                                    0]).rotate(2*(np.pi)/3,about_point=[0,0,1])
        H1=hexagonsV[0].copy()
        H6=hexagonsV[5].copy()
        H7=hexagonsV[6].copy()


        #This block is for pointing towards the points for explanation
        self.play(FadeIn(larrow),Transform(hexagonsV[0],H1highlight))
        self.wait(2)
        self.play(Transform(hexagonsV[0],H1),FadeOut(larrow),run_time=0.5)
        self.bring_to_back(hexagonsV[0])
        self.add(NP)
        self.remove(NPac)
        self.bring_to_back(NP)
        self.play(FadeIn(rarrow),Transform(hexagonsV[5],H6highlight),Transform(hexagonsV[6],H7highlight))
        self.wait(2)
        
        #This reverses the zoom
        self.play(ApplyMethod(self.foreground_mobjects[1].scale,self.zoom_factor),#Reverses the zoom...
            Transform(hexagonsV[5],H6),FadeOut(rarrow),Transform(hexagonsV[6],H7),#...and added details
            FadeOut(l),FadeOut(lbracket),FadeOut(rbracket),FadeOut(lnumber),FadeOut(rnumber))
        self.clear()
        self.setup()#Clear and Setup reset everything to a point that future zooms work again
        self.add(NP)
        self.add(hexagonsV)#Re-add previous objects to seamlessly continue
        self.wait(1)

        #Explain tiling and briefly mention periodicity
        self.play(FadeInFrom(hexagonsV2,hexagonsV2.get_center()*-1),
        FadeInFrom(hexagonsV3,hexagonsV3.get_center()*-1),
        FadeInFrom(hexagonsV4,hexagonsV4.get_center()*-1),
        FadeInFrom(hexagonsV5,hexagonsV5.get_center()*-1),
        FadeInFrom(hexagonsV6,hexagonsV6.get_center()*-1),
        FadeInFrom(hexagonsV7,hexagonsV7.get_center()*-1),
        run_time=10,lag_ratio=0.7,rate_func=linear)
        #This doesn't look as planned, but it's good in its own way
        self.wait(3)

        #ADD TRACER HERE
        tracer = NewSVGMO({"height":2,**exBaseB,**cBlack},"Tracer")
        self.play(FadeIn(tracer))
        self.play(ApplyMethod(tracer.shift,[0.5,0,0]))
        self.wait(1)
        self.play(ApplyMethod(tracer.shift,[-1,0,0]))
        self.wait(2)
        upperBoundEstablished = TexMobject("CNP \leq 7").shift([5.3,2.5,0])
        self.play(FadeOut(tracer),FadeIn(upperBoundEstablished))
        self.wait(2)

        self.play(FadeOut(hexagonsV),FadeOut(hexagonsV2),FadeOut(hexagonsV3),FadeOut(hexagonsV4),
        FadeOut(hexagonsV5),FadeOut(hexagonsV6),FadeOut(hexagonsV7),FadeOut(upperBoundEstablished),
                  run_time=3)
        self.wait(2)


class S03_LowerBounds(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [0.5,0.82,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.25,
    }
    def construct(self):
        self.add(NP)

        self.play(ShowCreation(K2,run_time=2,lag_ratio=0.5,rate_func=linear))
        self.play(ShowCreation(K3.shift([-1,1,0]),run_time=2,lag_ratio=0.5,rate_func=linear))
        self.wait(1.5)
        self.play(FadeOut(K2),FadeOut(K3))
        self.wait(1)
        self.play(ShowCreation(MS),run_time=6,lag_ratio=0.5,rate_func=linear)
        self.wait(2)
        lowerBoundOld = TexMobject("4 \leq CNP \leq 7").shift([5.3,2.5,0])
        self.play(FadeIn(lowerBoundOld))
        #self.wait(2)
        #self.play(FadeOut(lowerBoundOld))
        self.wait(5)

        pArrow1=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [(3-r33)/12,(3*r11+r3)/12,0]).scale(5)
        pArrow2=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [(3+r33)/12,(3*r11-r3)/12,0]).scale(5)
        pArrow3=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [0.5,r11/2,0]).scale(5)
        pointers=VGroup(pArrow1,pArrow2,pArrow3)
        
        self.activate_zooming(animate=True)
        self.wait(2)
        self.play(FadeIn(pointers),run_time=1)
        self.play(FadeIn(MSmark[0]))
        self.wait(1)
        self.play(FadeIn(MSmark[1]),FadeOut(MSmark[0]))
        self.wait(1)
        self.play(FadeIn(MSmark[2]),FadeOut(MSmark[1]))
        self.wait(1)
        self.play(FadeOut(MSmark[2]))
        self.wait(2)
        self.play(
            ApplyMethod(self.foreground_mobjects[1].scale_about_point,self.zoom_factor,
                        [0.5*1.35,0.82*1.35,0]),
            FadeOut(MS),FadeOut(pointers))
        self.clear()
        self.setup()#Clear and Setup reset everything to a point that future zooms work again
        self.add(NP,lowerBoundOld)
        self.wait(3)
        
class S04_LowerBounds2(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.64,
    }
    def construct(self):
        lowerBoundOld = TexMobject("4 \leq CNP \leq 7").shift([5.3,2.5,0])
        self.add(NP,lowerBoundOld)
        self.play(ShowCreation(H553),run_time=6,lag_ratio=0.5,rate_func=linear)
        self.wait(3)
        lowerBoundEstablished = TexMobject("5 \leq CNP \leq 7").shift([5.3,2.5,0])
        self.play(Transform(lowerBoundOld,lowerBoundEstablished))
        self.wait(2)
        self.play(FadeOut(lowerBoundOld))
        self.wait(2)
        self.activate_zooming(animate=True)
        self.wait(3)
        # Remove the NumberPlane for the exclusion zone explanation
        self.play(FadeOut(NP),FadeOut(H553),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]))
        
    
class S05_XFormula(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.15,
    }
    def construct(self):
        w3=w.copy()
        xw3=xw.copy()
        w4=w.copy()
        xw4=xw.copy()
        xFormulaO=xFormula.copy().shift([0,2,0])

        
        #self.add(NP)
        self.play(ShowCreation(xFormula),run_time=3)
        self.wait(0.5)
        larrow=Arrow([-5.4,-3,0],[-5.4,0,0])
        rarrow=Arrow([1.5,0,0],[1.5,-2,0])
        self.play(FadeIn(larrow),FadeIn(rarrow),run_time=2)
        self.wait(2)
        #Explain what the function is for


        #Simplify for 2 dimensions
        self.play(Transform(xFormula, xFormula2),ApplyMethod(larrow.shift,[0.9,0,0]))
        self.wait(2)



        esab = NewSVGMO({"height":2.1,**exBaseR},"SemiAnB").shift([1.5,-1.5,0])
        esab1 = NewSVGMO({"height":0.1,**exBaseG},"SemiAnB1").shift([-4.5,-1.5,0])
        #Show a point going in and a circle coming out
        self.play(ApplyMethod(larrow.shift,[0,2,0]),ApplyMethod(rarrow.shift,[0,2,0]),
                  ApplyMethod(xFormula.shift,[0,2,0]))
        self.play(FadeIn(esab),FadeIn(esab1))
        self.wait(2)

        self.bring_to_back(NP)
        #Move the point and exclusion zone into valid coordinates on a plane
        self.play(FadeIn(NP),FadeOut(xFormula),FadeOut(larrow),FadeOut(rarrow),
                  ApplyMethod(esab1.shift,[2.5,3.5,0]),ApplyMethod(esab.shift,[-3.5,3.5,0]))
        self.wait(1)
        #Add labels
        self.play(FadeIn(xw.shift([-3.5,2,0])),FadeIn(w.shift([-2.2,2,0])))
        self.wait(2)

        w2=w.copy().shift(w.get_center()+[2.2,-2,0])
        xw2=xw.copy().shift(xw.get_center()+[3.5,-2,0])
        esabPre=esab.copy()#.shift([-2,2,0])
        esab1Pre=esab1.copy()#.shift([-2,2,0])
        
        esac = NewSVGMO({"height":2.1,**exBaseR},"SemiAnC").shift([2,2,0])
        esac1 = NewSVGMO({"height":0.1,**exBaseG},"SemiAnC1").shift([2,2,0])

        self.add(w2,xw2,esab1Pre,esabPre)
        self.wait(1)
        self.play(ApplyMethod(w2.shift,[4.4,0,0]),ApplyMethod(xw2.shift,[7,0,0]),
                  ApplyMethod(esab1Pre.shift,[4,0,0]),ApplyMethod(esabPre.shift,[4,0,0]))
        self.wait(0.5)
        #Transforms and shows the 1D input
        self.play(Transform(esabPre,esac),Transform(esab1Pre,esac1),ApplyMethod(w2.shift,[0.2,0,0]),
                  ApplyMethod(xw2.shift,[0.2,0,0]))
        self.wait(2)
        #Show the tracer
        tracer=NewSVGMO({"height":2,**exBaseB,"color" : WHITE},"Tracer").scale(1.05)
        self.play(FadeIn(tracer.shift([1.78,2,0])))
        self.play(ApplyMethod(tracer.shift,[0.44,0,0]))
        self.play(FadeOut(tracer))
        self.wait(2)

        #Add second row of stuff
        annBoundary = NewSVGMO({"height":2.4,**exBaseR},"AnnBoundary")
        annBoundary1 = NewSVGMO({"height":0.48,**exBaseG},"AnnBoundary1")
        annB1f = NewSVGMO({"height":0.48,**exBaseG},"AnnBoundary1F")

        
        self.play(FadeIn(annBoundary.shift([-2,-2,0])),FadeIn(annBoundary1.shift([-2,-2,0])),
                  FadeIn(xw3.shift([-3.67,-2,0])),FadeIn(w3.shift([-2.43,-2,0])))

        self.wait(2)
        self.play(FadeIn(tracer.shift(-tracer.get_center()-[2.2,2,0])))
        #self.play(ApplyMethod(tracer.rotate,np.pi,about_point=ORIGIN,axis=RIGHT,
        #                      path_func = clockwise_path()))#[-4,-4,0]
        self.play(Rotate(tracer,np.pi,about_point=[-2,-2,0],axis=OUT))
        self.play(Rotate(tracer,np.pi,about_point=[-2,-2,0],axis=OUT))
        #self.play(Rotate(tracer,np.pi,about_point=[-2,-2,0],axis=OUT),rate_func=linear)
        #self.play(Rotate(tracer,np.pi,about_point=[-2,-2,0],axis=OUT),rate_func=linear)
        self.play(FadeOut(tracer))
        self.wait(2)
        
        annB=annBoundary.copy()
        annB1=annBoundary1.copy()
        xw4=xw3.copy()
        w4=w3.copy()

        self.add(annB,annB1,xw4,w4)
        self.play(ApplyMethod(annB.shift,[4,0,0]),ApplyMethod(annB1.shift,[4,0,0]),
                  ApplyMethod(xw4.shift,[7.34,0,0]),ApplyMethod(w4.shift,[4.86,0,0]))
        self.wait(1)
        self.play(Transform(annB1,annB1f.shift([2,-2,0])))
        self.wait(2)

        #Fade everything out to go back to the formula one last time
        self.play(FadeOut(NP),FadeOut(w),FadeOut(w2),FadeOut(w3),FadeOut(w4),FadeOut(xw),FadeOut(xw2),
                  FadeOut(xw3),FadeOut(xw4),FadeOut(annB),FadeOut(annB1),FadeOut(annB),
                  FadeOut(annBoundary),FadeOut(annBoundary1),FadeOut(esab),FadeOut(esab1),
                  FadeOut(esabPre),FadeOut(esab1Pre))

        

        self.wait(2)
        larrow2=Arrow([-5.4,0,0],[-5.4,2,0])
        self.play(FadeIn(xFormulaO),FadeIn(larrow2),FadeIn(rarrow),run_time=2)
        #-1 and 0
        self.wait(1)
        tex0 = TexMobject("0-dimensional").scale(0.8).shift([-4.5,0,0])
        tex1 = TexMobject("(1,n)-dimensional").scale(0.8).shift([-4.5,-1,0])
        texn1 = TexMobject("(n-1)-dimensional").scale(0.8).shift([1.5,0,0])
        texn = TexMobject("n-dimensional").scale(0.8).shift([1.5,-1,0])
        self.play(FadeIn(tex0),FadeIn(texn1),run_time=2)
        conversionArrow=Arrow([-2,0,0],[-1,0,0]).scale(2)
        self.play(FadeIn(conversionArrow))
        self.wait(1)
        self.play(ApplyMethod(conversionArrow.shift,[0,-1,0]),FadeIn(tex1),FadeIn(texn),run_time=2)
        self.wait(2)
        self.play(FadeOut(tex0),FadeOut(tex1),FadeOut(texn1),FadeOut(texn),FadeOut(conversionArrow)
                  ,FadeOut(xFormulaO),FadeOut(rarrow),FadeOut(larrow2))
        self.wait(2)
        #0  n-1
        #1+ n
        
        
class S06_Iteration(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.15,
    }
    def construct(self):
        l0=Line([0,0.3,0],[0,-0.3,0],**lineConfigG)
        l2=Line([2,0.2,0],[2,-0.2,0],**lineConfigG)
        lm2=Line([-2,0.2,0],[-2,-0.2,0],**lineConfigG)
        l1=Line([1,0.2,0],[1,-0.2,0],**lineConfigR)
        lm1=Line([-1,0.2,0],[-1,-0.2,0],**lineConfigR)
        l3=Line([3,0.2,0],[3,-0.2,0],**lineConfigR)
        lm3=Line([-3,0.2,0],[-3,-0.2,0],**lineConfigR)
        l4=Line([4,0.2,0],[4,-0.2,0],**lineConfigG)
        lm4=Line([-4,0.2,0],[-4,-0.2,0],**lineConfigG)
        l5=Line([5,0.2,0],[5,-0.2,0],**lineConfigR)
        lm5=Line([-5,0.2,0],[-5,-0.2,0],**lineConfigR)
        l6=Line([6,0.2,0],[6,-0.2,0],**lineConfigG)
        lm6=Line([-6,0.2,0],[-6,-0.2,0],**lineConfigG)
        
        lU0=Line([0,0.3,0],[0,-0.3,0],**lineConfigB)
        lU2=Line([2,0.2,0],[2,-0.2,0],**lineConfigB)
        lUm2=Line([-2,0.2,0],[-2,-0.2,0],**lineConfigB)
        lU1=Line([1,0.2,0],[1,-0.2,0],**lineConfigB)
        lUm1=Line([-1,0.2,0],[-1,-0.2,0],**lineConfigB)
        lU3=Line([3,0.2,0],[3,-0.2,0],**lineConfigB)
        lUm3=Line([-3,0.2,0],[-3,-0.2,0],**lineConfigB)
        lU4=Line([4,0.2,0],[4,-0.2,0],**lineConfigB)
        lUm4=Line([-4,0.2,0],[-4,-0.2,0],**lineConfigB)
        lU5=Line([5,0.2,0],[5,-0.2,0],**lineConfigB)
        lUm5=Line([-5,0.2,0],[-5,-0.2,0],**lineConfigB)
        lU6=Line([6,0.2,0],[6,-0.2,0],**lineConfigB)
        lUm6=Line([-6,0.2,0],[-6,-0.2,0],**lineConfigB)
        lU7=Line([7,0.2,0],[7,-0.2,0],**lineConfigB)
        lUm7=Line([-7,0.2,0],[-7,-0.2,0],**lineConfigB)
        
        self.play(FadeIn(NLan))
        self.wait(2)
        self.add(NL)
        self.play(FadeOut(NLan))
        
        #Explain the iteration
        #w 0
        #xw 1
        #xIter2 0,2
        #xIter3 1,3
        self.play(FadeIn(l0),FadeIn(w0.shift([0,2,0])))
        self.wait(2)
        self.play(FadeOut(l0),FadeOut(w0),FadeIn(l1),FadeIn(lm1),FadeIn(x0.shift([0,2,0])))
        self.wait(1.5)
        self.play(FadeOut(l1),FadeOut(lm1),FadeOut(x0),FadeIn(l0),FadeIn(l2),FadeIn(lm2),
                  FadeIn(xIter2))
        self.wait(5.5)
        self.play(Transform(xIter2,xIter3),FadeOut(l0),FadeOut(l2),FadeOut(lm2),
                  FadeIn(l1),FadeIn(lm1),FadeIn(l3),FadeIn(lm3))
        self.wait(1.5)
        self.play(Transform(xIter2,xIter4),FadeIn(l0),FadeIn(l2),FadeIn(lm2),
                  FadeIn(l4),FadeIn(lm4),FadeOut(l1),FadeOut(lm1),FadeOut(l3),FadeOut(lm3))
        self.wait(1.5)
        self.play(Transform(xIter2,xIter5),FadeOut(l0),FadeOut(l2),FadeOut(lm2),
                  FadeOut(l4),FadeOut(lm4),FadeIn(l1),FadeIn(lm1),FadeIn(l3),FadeIn(lm3),
                  FadeIn(l5),FadeIn(lm5))
        self.wait(1.5)
        self.play(Transform(xIter2,xIter6),FadeIn(l0),FadeIn(l2),FadeIn(lm2),
                  FadeIn(l4),FadeIn(lm4),FadeIn(l6),FadeIn(lm6),
                  FadeOut(l1),FadeOut(lm1),FadeOut(l3),FadeOut(lm3),FadeOut(l5),FadeOut(lm5))
        self.wait(1.5)
        self.play(FadeOut(xIter2),FadeOut(l0),FadeOut(l2),FadeOut(lm2),
                  FadeOut(l4),FadeOut(lm4),FadeOut(l6),FadeOut(lm6))
        self.wait(1.5)

        #Show union iteration
        self.play(FadeIn(lU0),FadeIn(wU0.shift([0,2,0])))
        self.wait(2)
        self.play(FadeOut(wU0),FadeIn(lU1),FadeIn(lUm1),FadeIn(xUIter1))
        self.wait(0.6)
        self.play(FadeIn(lU2),FadeIn(lUm2),Transform(xUIter1,xUIter2))
        self.wait(0.6)
        self.play(FadeIn(lU3),FadeIn(lUm3),Transform(xUIter1,xUIter3))
        self.wait(0.6)
        self.play(FadeIn(lU4),FadeIn(lUm4),Transform(xUIter1,xUIter4))
        self.wait(0.6)
        self.play(FadeIn(lU5),FadeIn(lUm5),Transform(xUIter1,xUIter5))
        self.wait(0.6)
        self.play(FadeIn(lU6),FadeIn(lUm6),Transform(xUIter1,xUIter6))
        self.wait(0.6)
        self.play(FadeIn(lU7),FadeIn(lUm7),Transform(xUIter1,xUIter7))
        self.wait(1.9)

        arrow=Arrow([0.1,1,0],[0.1,0,0])
        self.play(FadeIn(arrow))
        self.wait(1.2)
        lbracket=TexMobject("[").shift([0.05,-0.6,0])
        rbracket=TexMobject(")").shift([0.95,-0.6,0])
        a = TexMobject("A").shift([0.5,-0.6,0])
        b = TexMobject("B").shift([-0.5,-0.6,0])
        bA=VGroup(lbracket,rbracket,a)
        bBase=VGroup(lbracket.copy().shift([-1,0,0]),rbracket.copy().shift([-1,0,0]),b)
        bB=VGroup(bBase,bBase.copy().shift([2,0,0]))
        bA2=VGroup(bA.copy().shift([2,0,0]),bA.copy().shift([-2,0,0]))
        self.play(ApplyMethod(arrow.shift,[0.8,0,0]),FadeIn(bA))
        self.wait(2)
        self.play(FadeOut(arrow))
        self.wait(10)
        self.play(FadeIn(bB))
        self.wait(1)
        self.play(FadeIn(bA2))
        self.wait(1)
        self.play(FadeOut(bA),FadeOut(bB),FadeOut(bA2),FadeOut(lU4),FadeOut(lUm4),
                  FadeOut(lU5),FadeOut(lUm5),FadeOut(lU6),FadeOut(lUm6),FadeOut(lU7),FadeOut(lUm7),
                  FadeOut(xUIter1),FadeOut(lU3),FadeOut(lUm3),FadeOut(lU2),FadeOut(lUm2),
                  FadeOut(lU1),FadeOut(lUm1),FadeOut(lU0),FadeOut(NL))
        self.wait(2)

class S07_FiniteToInfinite(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [1.5,1,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.10,
    }
    def construct(self):
        self.play(FadeIn(NP))

        self.play(ShowCreation(K2.shift([1,1,0])),run_time=2)
                  
        self.activate_zooming(animate=True)
        self.wait(6.5)

        
        xIterRad1 = NewSVGMO({"height":0.3,**exBaseR},"Iteration1").shift([1.993,1,0])
        xIterRad2 = NewSVGMO({"height":0.3,**exBaseG},"Iteration2").shift([1.014,1,0])
        xIterRad3 = NewSVGMO({"height":0.3,**exBaseR},"Iteration3").shift([1.987,1,0])
        xFullG = NewSVGMO({"height":0.3,**exBaseG},"AnnBoundary1F").shift([1,1,0])
        xFullR = NewSVGMO({"height":0.3,**exBaseR},"AnnBoundary1F").shift([2,1,0])
        xIterCirc = Annulus(inner_radius=0.285/2,outer_radius=0.31/2,color=GRAY).shift([1,1,0])
        xIterCirc2 = Annulus(inner_radius=0.285/2,outer_radius=0.31/2,color=GRAY).shift([2,1,0])
        #This represents the expanding
        self.play(FadeIn(xIterCirc),FadeIn(xIterCirc2),FadeOut(K2))
        self.wait(10)

        #w
        dot = NewSVGMO({"height":0.1,**exBaseG},"SemiAnb1").shift([1,1,0]).scale(0.2)
        self.play(FadeIn(dot),FadeIn(w.shift([0.97,0.98,0]).scale(0.1)))
        self.wait(7)
        #X(w)
        self.bring_to_back(NP,xIterRad1)
        self.play(FadeOut(w),FadeOut(dot),FadeIn(xIterRad1),FadeIn(xw.shift([1.94,0.97,0]).scale(0.1)))
        self.wait(2)
        #Iter2
        self.bring_to_back(NP,xIterRad2)
        self.play(FadeOut(xw),FadeOut(xIterRad1),FadeIn(xIterRad2),
                  FadeIn(xIter2w.shift([1.1,0.82,0]).scale(0.1)))
        self.wait(2)
        #Iter3
        self.bring_to_back(NP,xIterRad3)
        self.play(FadeOut(xIter2w),FadeOut(xIterRad2),FadeIn(xIterRad3),
                  FadeIn(xIter3w.shift([1.92,0.82,0]).scale(0.1)))
        self.wait(2)
        #Full
        self.bring_to_back(NP,xFullG,xFullR)
        self.play(FadeOut(xIter3w),FadeOut(xIterRad3),FadeIn(xFullG),FadeIn(xFullR))
        self.wait(11)
        self.play(FadeOut(xFullG),FadeOut(xFullR),FadeOut(xIterCirc),FadeOut(xIterCirc2),FadeOut(NP),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]))
        #self.play(FadeIn(NP))

class S08_MoserSpindleExpansion(ZoomedScene):
    CONFIG = {
        "zoomed_camera_frame_starting_position": [0.5,0.82,0],
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.25,
    }
    def construct(self):
        pArrow1=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [(3-r33)/12,(3*r11+r3)/12,0]).scale(5)
        pArrow2=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [(3+r33)/12,(3*r11-r3)/12,0]).scale(5)
        pArrow3=Arrow([((3-r33)/12+(3+r33)/12+0.5)/3,((3*r11-r3)/12+(3*r11+r3)/12+r11/2)/3,0],
              [0.5,r11/2,0]).scale(5)
        pointers=VGroup(pArrow1,pArrow2,pArrow3)
        
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        firstLinks=VGroup(MS[0].copy(),MS[1].copy(),MS[2].copy())
        self.play(FadeIn(NP),FadeIn(MSa),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(2)
        self.play(FadeIn(MSax[0]))
        self.wait(1)
        self.play(FadeIn(firstLinks))
        self.wait(2)
        self.play(FadeIn(MSax[1]),FadeIn(MSax[2]),FadeIn(MSax[3])
                  ,FadeIn(MSax[4]),FadeIn(MSax[5]),FadeIn(MSax[6]))
        self.wait(1)
        self.play(FadeIn(MS))
        self.remove(firstLinks)
        self.wait(2)
        self.add(MSaColored)
        self.bring_to_back(NP,MSaColored)
        self.remove(MSax,MS)
        self.add(MSax,MS)
        self.play(FadeOut(MSax),FadeOut(MS),run_time=2)
        self.wait(2)
        self.play(FadeIn(pointers))
        self.play(FadeIn(MSmark[0]))
        self.wait(0.7)
        self.play(FadeIn(MSmark[1]),FadeOut(MSmark[0]))
        self.wait(0.7)
        self.play(FadeIn(MSmark[2]),FadeOut(MSmark[1]))
        self.wait(0.7)
        self.play(FadeOut(MSmark[2]))
        self.play(FadeOut(NP),FadeOut(MSa),FadeOut(MSaColored),FadeOut(pointers),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]))
        
class S09_ConclusionAndPatchiness(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.64,
    }
    def construct(self):
        #And now the theorem
        dbeTheorem=TextMobject("""The proven De Bruijn–Erdős theorem states that\\\\
                                    for infinite graphs with a finite chromatic number,\\\\
                                    there exists a finite subgraph with that chromatic number.\\\\""")

        interTheorem=TextMobject("""Every finite unit distance graph can be embedded\\\\
                                    and expanded in the space, yielding at least\\\\
                                    some areas that require a single continuous color.\\\\
                                    Larger single-colored areas give more efficient colorings.""")

        xorTheorem=TextMobject("""Theorem of this video:\\\\
                                    For unit distance graphs in euclidean spaces\\\\
                                    there exists a tesselation with single-colored\\\\
                                    maximum diameter Jordan-Brouwer separated spaces\\\\
                                    with the same chromatic number as the whole space.\\\\
                                    In 2 or more dimensions the use of such single-colored\\\\
                                    spaces is unavoidable.""")
        
        self.play(FadeIn(dbeTheorem))
        self.wait(10)
        self.play(FadeOut(dbeTheorem),FadeIn(interTheorem))
        self.wait(10)
        self.play(FadeOut(interTheorem),FadeIn(xorTheorem))
        self.wait(15)
        self.play(FadeOut(xorTheorem))
        self.wait(2)
        self.activate_zooming(animate=False)
        self.foreground_mobjects[1].scale_about_point(1.05,[0,0,0])
        self.play(FadeIn(NP),FadeIn(H553),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1/1.05,[0,0,0]))
        self.wait(2)
        arrow1=Arrow([1,1,0],[-0.1,-0.1,0])
        arrow2=Arrow([-1,1,0],[0.1,-0.1,0])
        arrow3=Arrow([-1,-1,0],[0.1,0.1,0])
        arrow4=Arrow([1,-1,0],[-0.1,0.1,0])
        arrows=VGroup(arrow1,arrow2,arrow3,arrow4)
        self.play(FadeIn(arrows))
        self.wait(2)
        self.play(FadeOut(arrows))
        self.wait(2)
        self.play(FadeOut(H553),FadeIn(H553B))
        self.wait(2)
        self.play(FadeOut(H553B),FadeIn(H553Y))
        self.wait(2)
        self.play(FadeOut(H553Y),FadeIn(H553G))
        self.wait(2)
        self.play(FadeOut(H553G),FadeIn(H553R))
        self.wait(2)
        self.play(FadeOut(H553R),FadeIn(H553))
        self.wait(2)
        self.play(FadeOut(H553),FadeOut(NP),
                  ApplyMethod(self.foreground_mobjects[1].scale_about_point,1.05,[0,0,0]))
        self.wait(2)


        
class S10_Endcard(ZoomedScene):
    def construct(self):
        workspace=ImageMobject("Workspace")
        workspace.scale(1/workspace.get_width()*16)
        w_w=workspace.get_width()
        print(w_w)
        self.play(FadeIn(workspace))
        self.wait(2)
        self.play(FadeOut(workspace))

class Thumbnail(ZoomedScene):
    def construct(self):
        self.add(NP)
        self.add(hexagonsV.shift([3.5,2,0]).scale(1.3))
        self.add(MS.shift([-6.5,0.5,0]))
        self.add(H553.shift([-2.5,1.5,0]).scale(0.8))
        self.add(TextMobject("Hadwiger-Nelson\\\\Problem").shift([-3.5,-2,0]).scale(1.7))
        self.add(TextMobject("Why tiles?").shift([3.5,-2,0]).scale(2.5))
        #Save via -s
        
class TestZone(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.25,
    }
    def construct(self):
        self.add(NP)
        self.add(K3Ca)
        self.add(K3Cpoints)
        self.activate_zooming(animate=False)
        #Save via -s
