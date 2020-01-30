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

cPrototype = {"stroke_width":3,"stroke_color":BLUE,"fill_opacity":1,"color": PURPLE}
cArc = {"stroke_width":0,"stroke_color":BLUE,"fill_opacity":0,"color": PURPLE}
cArc2 = {"stroke_width":3,"stroke_color":YELLOW,"fill_opacity":0,"color": PURPLE}
cArc3 = {"stroke_width":5,"stroke_color":"#ff0000","fill_opacity":0,"color": PURPLE}
cExclusion = {"stroke_width":3,"stroke_color":GREEN,"fill_opacity":0.5,"color": RED}

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
pRMTriangle=ArcPolygon(arc0,arc1,arc2,**cPrototype).shift([-0.5,-r3/6,0])

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
pGreyPent=ArcPolygon(arc0,arc1,arc2,arc3,arc4,**cPrototype).move_to([0,0,0])


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
        def update_AP(mob,alpha):
            arcs=pTriangle.get_arcs()
            new_mob=ArcPolygon(*arcs,**pTriangle.CONFIG).move_to([0,0,0])
            mob.become(new_mob)
        def update_EX(mob,alpha,tile):
            new_mob=ExclusionZone(pTriangle,**mob.__dict__)
            print(tile)
            mob.become(new_mob)
            
        self.add(NP)
        self.activate_zooming(animate=False)
        EX=ExclusionZone(pTriangle,fill_opacity=0.5,color=GREEN,stroke_width=2,stroke_color=BLUE)
        self.play(ShowCreation(pTriangle),run_time=2,rate_func=linear)
        self.play(ShowCreation(EX),run_time=2,rate_func=linear)
        #self.play(ShowCreation(EX.get_preDual()),run_time=2,rate_func=linear)
        self.wait(1)

        self.play(Transform(pTriangle,pRMTriangle),
                  UpdateFromAlphaFuncArg(EX,update_EX,"test"),run_time=5)
        #self.play(UpdateFromAlphaFunc(EX,update_EX2),run_time=13)
        
        self.wait(3)

class S0_TriangleGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        self.add(NP)
        t=Tiling(pTriangle,
                 [[Mobject.shift,np.array([0.5,0,0]),Mobject.rotate,math.pi]],
                 [[Mobject.shift,np.array([0,r3/2,0]),Mobject.rotate,math.pi]],range(-6,6),range(-1,2))
        v=t.get_VGroup()
        self.play(ShowCreation(v),run_time=5)
        self.play(ApplyMethod(v.scale,0.5))
        self.wait()
        
class S0_SquareGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        self.add(NP)
        t=Tiling(pSquare,
                 [[Mobject.shift,np.array([1/r2,0,0])]],
                 [[Mobject.shift,np.array([0,1/r2,0])]],range(-6,6),range(-1,1))
        v=t.get_VGroup()
        self.play(ShowCreation(pHexagon),run_time=1)
        #self.play(ApplyMethod(v.scale,0.5))
        #self.play(ApplyMethod(t.get_dict()[0][-1].shift,[1,1,0]))
        #self.play(ApplyMethod(v.scale,2))
        #self.play(ShowCreation(pSquare))
        self.wait(2)
        
class S0_HexagonGrid(ZoomedScene):
    CONFIG = {
        "zoomed_display_corner": [0,0,0],
        "zoomed_display_height": FRAME_HEIGHT,
        "zoomed_display_width": FRAME_WIDTH,
        "zoom_factor": 0.6,
    }
    def construct(self):
        def update_EX(mob,alpha,tile):
            new_mob=ExclusionZone(tile,**mob.__dict__)
            mob.become(new_mob)
        self.add(NP)
        t=Tiling(pHexagon,[[Mobject.shift,np.array([r3/2,0,0])]],
                          [[Mobject.shift,np.array([r3/4,0.75,0])],[Mobject.shift,np.array([-r3/4,0.75,0])]],range(-7,7),range(-4,4))
        self.activate_zooming(animate=False)
        v=t.get_VGroup()
        self.play(ShowCreation(v),run_time=10,rate_func=linear)
        EX=ExclusionZone(t.get_dict()[0][0],**cExclusion)
        self.play(ShowCreation(EX),run_time=5)


        
        self.play(ApplyMethod(v.scale,0.8),
                  UpdateFromAlphaFuncArg(EX,update_EX,t.get_dict()[0][0]),run_time=5)

        
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
