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
        "zoom_factor": 0.6,
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
        AP=ArcPolygon(arc0,arc1,arc2,arc3,arc5,arc6,arc7,arc4,
                      fill_opacity=0.5,color=RED,stroke_width=3.0,stroke_color=GREEN)
        arct0=ArcBetweenPoints(np.array([0.5,0.5,0]),np.array([0,0.5,0]),stroke_width=0,angle=0)
        arct1=ArcBetweenPoints(np.array([0,0.5,0]),np.array([0,0,0]),stroke_width=0,angle=0)
        arct2=ArcBetweenPoints(np.array([0,0,0]),np.array([0.5,0,0]),stroke_width=0,angle=0)
        arct3=ArcBetweenPoints(np.array([0.5,0,0]),np.array([0.5,0.5,0]),stroke_width=0,angle=0)
        AP2=ArcPolygon(arct0,arct1,arct2,arct3,
                      fill_opacity=0.5,color=RED,stroke_width=3.0,stroke_color=GREEN)

        arctr0=ArcBetweenPoints(np.array([0,0,0]),np.array([1,0,0]),stroke_width=0,angle=0)
        arctr1=ArcBetweenPoints(np.array([1,0,0]),np.array([0.5,r3/2,0]),stroke_width=0,angle=0)
        arctr2=ArcBetweenPoints(np.array([0.5,r3/2,0]),np.array([0,0,0]),stroke_width=0,angle=0)
        AP3=ArcPolygon(arctr0,arctr1,arctr2,
                      fill_opacity=0.5,color=RED,stroke_width=3.0,stroke_color=GREEN)



        
        #self.play(ShowCreation(AP),run_time=13,rate_func=linear)
        #self.wait(2)
        #p=Polygon([1,1,0],[1,-1,0],[-1,-1,0],[-1,1,0]).scale(1)
        #p2=p.copy().flip(RIGHT)
        #p2=Polygon([1,1,0],[-1,1,0],[-1,-1,0],[1,-1,0]).scale(1)
        EX=ExclusionZone(AP2,fill_opacity=0.5,color=RED,stroke_width=3,stroke_color=GREEN)
        #EX2=ExclusionZone(p2,fill_opacity=1,color=RED,stroke_width=3,stroke_color=GREEN)

        #self.play(ShowCreation(p),run_time=2,rate_func=linear)
        
        #AP.force_orientation("CW")
        #self.play(ShowCreation(AP),run_time=6,rate_func=linear)
        #AP.force_orientation("CCW")
        #self.play(ShowCreation(AP),run_time=6,rate_func=linear)

        #self.play(ShowCreation(EX.get_ExZone()),fill_opacity=1),run_time=6,rate_func=linear)
        #self.play(ShowCreation(Arc(0,-math.pi/2,radius=99999999999999999,fill_opacity=1).move_arc_center_to([0,0,0])),
        #          run_time=3,rate_func=linear)
        a=np.array([0,0,0])
        b=np.array([1.432,0,0])
        halfdist=np.linalg.norm(a-b)/2
        arcHeight=1-math.sqrt(1**2-halfdist**2)
        ang=math.acos((1-arcHeight)/1)
        ta=ArcBetweenPoints(a,b, stroke_width=2, angle=ang*2)
        #ta=ArcBetweenPoints(a,b, stroke_width=2,radius=1)
        #self.remove(p)
        #print(ta.get_arc_center())
        #print(np.linalg.norm(a-ta.get_arc_center()))
        #print(np.linalg.norm(b-ta.get_arc_center()))
        self.play(ShowCreation(AP2),run_time=2,rate_func=linear)
        self.play(ShowCreation(EX),run_time=5,rate_func=linear)
        #self.play(ShowCreation(Circle().move_to(ta.get_arc_center())),run_time=2,rate_func=linear)
        self.wait(2)

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
