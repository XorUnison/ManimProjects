#This file contains all my custom classes, as well as a bunch of more complex objects such as graphs

from big_ol_pile_of_manim_imports import *
from scipy.spatial import distance
import cmath
import numpy as np

#===SVG Class===
class NewSVGMO(SVGMobject):
    def __init__(self,config,mode="plain",dir_path="K:\ManimMedia\designs\svg_images",**kwargs):
        digest_config(self,config,kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(dir_path,"%s_%s.svg" % (self.file_name_prefix, mode))
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" % (self.file_name_prefix, mode))
            print(svg_file)
            svg_file = os.path.join(FILE_DIR,"PiCreatures_plain.svg",)
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)

#===Intersections===
#This method gets the intersections between two circles
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d

        return (np.array([x3,y3,0]),np.array([x4,y4,0]))

#===Shoelace===
#This can calculate areas, but in here it's used for its ability to determine curve orientation
def shoelace(x_y, absoluteValue = False, orientation = True):
    x = x_y[:,0]
    y = x_y[:,1]
    result = 0.5 * np.array(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    if absoluteValue:
        return abs(result)
    else:
        if orientation:
            if result>0:
                return "CW"
            else:
                return "CCW"
        else:
            return result
    
#===Graph===
#This class is for proper visual representaiton of graphs for graph theory
class Graph():
    def __init__(self,graph,line_config,**kwargs):
        self.graph = graph
        self.line_config = line_config
        self.kwargs=kwargs
        if kwargs.get('annulus', False):
            self.annulus=True
        else:
            self.annulus=False
    def makeGraph(self):
        self.circleArr=[] #Lines and Circles are put into 2 arrays to make sure the vertices...
        self.lineArr=[]   #... are drawn on top of the lines and never the other way around
        self.annulusArr=[]#And annuluses for representing embedded graphs
        for vertex,attributes in self.graph.items():
            if self.annulus:
                a=Annulus(inner_radius=self.kwargs["inner_radius"],
                          outer_radius=self.kwargs["outer_radius"],
                          color=self.kwargs["color"],
                          fill_opacity=self.kwargs["fill_opacity"]).shift(attributes[0])
                self.annulusArr.append(a)
            else:
                c=Circle(**attributes[2])
                c.scale(attributes[2]["height"]/2)
                c.shift(attributes[0]) #Applies all the necessary attributes to the circle
                self.circleArr.append(c)
            for connectedVertex in attributes[1]:
                if connectedVertex > vertex: #Makes sure no lines are drawn double
                    l=Line(attributes[0],self.graph[connectedVertex][0],**self.line_config)
                    self.lineArr.append(l)
    def returnVGroup(self):
        self.makeGraph()
        return VGroup(*self.lineArr,*self.circleArr)
    def returnVertices(self):
        self.makeGraph()
        return VGroup(*self.circleArr)
    def returnAnnuluses(self):
        self.makeGraph()
        return VGroup(*self.annulusArr)

#===ArcPolygon===
class ArcPolygon(VMobject):
    CONFIG = {"color": BLUE}
    def __init__(self,*arcs,**kwargs):
        self.arcs=[*arcs]
        #Most of the init method here is built from the round_corners in Polygon
        VMobject.__init__(self, **kwargs)
        for arc1, arc2 in adjacent_pairs(arcs):
            self.append_points(arc1.points)
            line = Line(arc1.get_end(), arc2.get_start())
            # Make sure anchors are evenly distributed
            len_ratio = line.get_length() / arc1.get_arc_length()
            if math.isnan(len_ratio) or math.isinf(len_ratio):
                continue
            line.insert_n_curves(
                int(arc1.get_num_curves() * len_ratio)
            )
            self.append_points(line.get_points())
        self.orientation=shoelace(self.get_vertices(),False,True)
            
    def get_vertices(self):
        return self.get_start_anchors()
    def get_arcs(self):
        return self.arcs
    def get_orientation(self):
        return self.orientation
    def force_orientation(self,orientation):
        if not(orientation=="CW" or orientation=="CCW"):
            raise ValueError('Invalid input for ArcPolygon.force_orientation| Use "CW" or "CCW"')
        if not(self.orientation==orientation):
            #Since we already assured the input is CW or CCW, and the orientations don't match,
            #we just reverse.
            reversed_points=self.get_points()[::-1]
            self.clear_points()
            self.append_points(reversed_points)
            self.orientation=orientation

#===Exclusion Zone===
class ExclusionZone(VMobject):#Work in progress
    #The working principle behind this class isn't exactly trivial.
    #It takes in an ArcPolygon and reads out its arcs, and from there makes the Exclusion zone
    #
    #The Exclusion Zone is made of two boundaries
    #The outer boundary is made by expanding the ArcPolygon by a width of 1
    #The inner boundary then has to run in reverse to the outer boundary, calculated opposite to...
    #...the outer boundary on the inside
    
    def __init__(self,ArcPolygon,**kwargs):
        VMobject.__init__(self, **kwargs)
        ArcPolygon=ArcPolygon.copy().force_orientation("CW")#
        
    def deprecated(self):
        points=shape.get_vertices()
        pLen=len(points)
        pRange=range(pLen)
        for i in pRange:
            print(i)
        #We need to get the orientation first, since we're afterwards adding the first element...
        #At the end again for ease of processing
        orientation=shoelace(points)
        points=np.vstack((points,points[0]))
        #The outer boundary is made via the input points and the lines made by connecting them.
        #This means one Arc object is created for every input point, its angles determined...
        #...via the angles towards the previous and next point.
        EXarcsOuter=[]
        for i in pRange:
            #print(points[i])
            #The angle output we need to determine from what we have is as follows:
            #Point 1[1,1,0]
            #pi/2 | -pi/2
            #Point 2[1,-1,0]
            #0 | -pi/2
            #Point 3[-1,-1,0]
            #-pi/2 | -pi/2
            #Point 4[-1,1,0]
            #-pi | -pi/2
            if orientation=="CW":
                if i==0:
                    #print("Starting angle0")
                    #points[-2] because the first point as appended to the end of the points array
                    a1=Line(points[-2],points[i]).get_angle()+math.pi/2
                    #print(round(math.degrees(a1)))
                    a2=Line(points[i],points[i+1]).get_angle()+math.pi/2-a1
                    #print("Line direction0")
                    #print(round(math.degrees(Line(points[i],points[i+1]).get_angle()+math.pi/2)))
                else:
                    #print("Starting angle")
                    a1=a1+a2
                    #print(round(math.degrees(a1)))
                    a2=Line(points[i],points[i+1]).get_angle()+math.pi/2
                    #print("Line direction")
                    #print(round(math.degrees(a2)))
                    a2=Line(points[i],points[i+1]).get_angle()+math.pi/2-a1
                    #print(round(math.degrees(a2)))
                    a2=a2%(-math.pi*2)#This is patchwork solution for now, probably not final
            else:#CCW - the angle offset needs to be reversed to still point outside
                if i==0:#points[-2] because the first point as appended to the end of the points array
                    a1=Line(points[-2],points[i]).get_angle()-math.pi/2
                    a2=Line(points[i],points[i+1]).get_angle()-math.pi/2-a1
                else:
                    a1=a1+a2
                    a2=Line(points[i],points[i+1]).get_angle()-math.pi/2
                    a2=Line(points[i],points[i+1]).get_angle()-math.pi/2-a1
                    a2=a2%(math.pi*2)#This is patchwork solution for now, probably not final
            arc=Arc(a1,a2,radius=1).move_arc_center_to(points[i])
            #print(arc)
            EXarcsOuter.append(arc)

        
        EXarcsInner=[]
        for i in pRange:
            #print(points[-i])
            i=-(i+1)
            if orientation=="CW":
                if i==-1:
                    #print("Starting angle Inner0")
                    #points[-2] because the first point as appended to the end of the points array
                    a1=Line(points[1],points[i]).get_angle()+math.pi/2
                    #print(round(math.degrees(a1)))
                    a2=Line(points[i],points[-2]).get_angle()+math.pi/2-a1
                    #print("Line direction Inner0")
                    #print(round(math.degrees(Line(points[i],points[i+1]).get_angle()+math.pi/2)))
                else:
                    #print("Starting angle Inner")
                    a1=a1+a2
                    #print(round(math.degrees(a1)))
                    a2=Line(points[i],points[i-1]).get_angle()+math.pi/2
                    #print("Line direction Inner")
                    #print(round(math.degrees(a2)))
                    a2=Line(points[i],points[i-1]).get_angle()+math.pi/2-a1
                    #print(round(math.degrees(a2)))
                    a2=a2%(-math.pi*2)#This is patchwork solution for now, probably not final
            arc=Arc(a1,a2,radius=1).move_arc_center_to(points[i])
            EXarcsInner.append(arc)
            #print(arc)
            
        ExZone=ArcPolygon(*EXarcsOuter)
        InZone=ArcPolygon(*EXarcsInner)
        #self.ExZone=ExZone
        #,**APkwargs)
        #Last, the simple center tile
        #Tile=ArcPolygon(*arcs,**APkwargs)
        self.append_points(ExZone.get_points())
        #self.append_points(InZone.get_points())
            
    def get_vertices(self):
        return self.get_start_anchors()
    #def get_ExZone(self):
    #    return self.ExZone

#===Measure Bar===
class MeasureBar():
    def __init__(self,mbH,mbW,sW,leftKwargs,rightKwargs,**kwargs):
        self.mbH=mbH #These two variables define the measure bar width and height
        self.mbW=mbW
        self.sW=sW #Used for stroke width
        self.leftKwargs=leftKwargs
        self.rightKwargs=rightKwargs

    def assembleMeasureBar(self):
        #[0]: Frame - Top
        #[1]: Black foundation - Back
        #[2][0]: Bar - Left Center
        #[2][1-n]: Subsequent bar states
        #[3][0]: XBar - Right Center
        #[3][1-n]: Subsequent bar states

        #The first rectangle is the outer frame
        self.frame=Rectangle(height=self.mbH,width=self.mbW,stroke_color=WHITE,fill_opacity=0.0,
                        stroke_width=self.sW)
        #The second rectangle is the black back, the filling is between these two
        self.back=Rectangle(height=self.mbH,width=self.mbW,stroke_color=RED,fill_opacity=1.0,
                       color=BLACK)
        self.leftArr=[] #Will contain the initial bar and transformations for the left
        self.rightArr=[]#Will contain the initial bar and transformations for the right

        for kwargs in self.leftKwargs:
            #print(kwargs)
            self.leftArr.append(Rectangle(**kwargs).shift(kwargs["offset"]))
        for kwargs in self.rightKwargs:
            #print(kwargs)
            self.rightArr.append(Rectangle(**kwargs).shift(kwargs["offset"]))
            
        return VGroup(self.frame,self.back,VGroup(*self.leftArr),VGroup(*self.rightArr))

#================================
#Objects from this point onwards
#================================

#===Root variables===
r3=math.sqrt(3)
r5=math.sqrt(5)
r11=math.sqrt(11)
r15=math.sqrt(15)
r33=math.sqrt(33)
r55=math.sqrt(55)
r165=math.sqrt(165)
r11s3=math.sqrt(11/3)

#===Configs===
cBlue = {"color" : BLUE}
cGreen = {"color" : GREEN}
cGGreen = {"color" : "#00FF00"}
cRed = {"color" : RED}
cRRed = {"color" : "#ff0000"}
cYellow = {"color" : YELLOW}
cPurple = {"color" : PURPLE}
cCyan = {"color" : "#00ffff"}
cOrange = {"color" : ORANGE}
cBlack = {"color" : BLACK}
cGray = {"color" : GRAY}

stroke0={"stroke_width" : 0}
stroke2={"stroke_width" : 1.8}
stroke200={"stroke_width" : 20}
height0p25 ={"height" : 0.25}
height0p05 ={"height" : 0.05}
height1 ={"height":1}
hexBase = {
    "stroke_color" : WHITE,
    "fill_opacity" : 1,
    **height0p25
}
hexBaseTiny = {
    "stroke_color" : WHITE,
    "fill_opacity" : 1,
    **height0p05
}
traceBase = {
    "file_name_prefix": "Ex",
    "stroke_color" : WHITE,
    **stroke2
}
areaBase = {
    "stroke_color" : GRAY,
    "fill_opacity" : 1,
    **height0p25
}
exBaseB = {
    "file_name_prefix": "Ex",
    "fill_opacity" : 1,
    **stroke0,
    **cBlue
}
exBaseG = {
    "file_name_prefix": "Ex",
    "fill_opacity" : 1,
    **stroke0,
    **cGreen
}
exBaseGr = {
    "file_name_prefix": "Ex",
    "fill_opacity" : 1,
    **stroke0,
    **cGray
}
exBaseR = {
    "file_name_prefix": "Ex",
    "fill_opacity" : 1,
    **stroke0,
    **cRed
}

msBase = {
    "stroke_color" : WHITE,
    "fill_opacity" : 1,
    "height":0.05,
    "stroke_width" : 1
}
mscBase = {
    "stroke_color" : "#00ffff",
    "fill_opacity" : 1,
    "height":0.05,
    **stroke2
}

lineConfig = {
    "color" : "#ff0000",
    "stroke_width": 3,
}
lineConfigR = {
    "color" : RED,
    "stroke_width": 5,
}
lineConfigG = {
    "color" : GREEN,
    "stroke_width": 5,
}
lineConfigB = {
    "color" : "#0000ee",
    "stroke_width": 5,
}
lineConfig553 = {
    "color" : GRAY,
    "stroke_width": 0.5,
}

#These are used for the hexagons in the upper bound explanation
cBlueSt = {**cBlue,**stroke2,**hexBase}
cGreenSt = {**cGreen,**stroke2,**hexBase}
cGGreenSt = {**cGGreen,**stroke2,**hexBase}
cRedSt = {**cRed,**stroke2,**hexBase}
cRRedSt = {**cRRed,**stroke2,**hexBase}
cTBlueSt = {**cBlue,**stroke2,**hexBaseTiny}
cTGreenSt = {**cGreen,**stroke2,**hexBaseTiny}
cTRedSt = {**cRed,**stroke2,**hexBaseTiny}
cYellowSt = {**cYellow,**stroke2,**hexBase}
cPurpleSt = {**cPurple,**stroke2,**hexBase}
cCyanSt = {**cCyan,**stroke2,**hexBase}
cOrangeSt = {**cOrange,**stroke2,**hexBase}
cBlackSt = {**cBlack,**stroke2,**hexBase}
cEmptySt = {**cBlack,**stroke2,**hexBase,"fill_opacity":0}

cYellowStSmall = {"stroke_color":WHITE,"fill_opacity":1,"height":0.1,**cYellow,**stroke2,}

cBlueMS = {"color" : "#0000ff",**stroke2,**msBase}
cGreenMS = {**cGreen,**stroke2,**msBase}
cRedMS = {**cRRed,**stroke2,**msBase}
cYellowMS = {**cYellow,**stroke2,**msBase}
cPurpleMS = {**cPurple,**stroke2,**msBase}
cWhiteMS = {"color" : WHITE,**stroke2,**msBase}
cOl = {**cBlack,**stroke2,**mscBase}


hexagons=[]
hexagons.append(RegularPolygon(6,**cBlue,**stroke2,**hexBase).scale(0.5))
hexagons.append(RegularPolygon(6,**cPurple,**stroke2,**hexBase).scale(0.5).shift([0,r3*0.5,0]))
hexagons.append(RegularPolygon(6,**cGray,**stroke2,**hexBase).scale(0.5).shift([0,r3*0.5,
0]).rotate((np.pi)/3,about_point=[0,0,1]))
hexagons.append(RegularPolygon(6,**cRRed,**stroke2,**hexBase).scale(0.5).shift([0,r3*0.5,0]).rotate(2*(np.pi)/3,
about_point=[0,0,1]))
hexagons.append(RegularPolygon(6,**cOrange,**stroke2,**hexBase).scale(0.5).shift([0,r3*-0.5,0]))
hexagons.append(RegularPolygon(6,**cYellow,**stroke2,**hexBase).scale(0.5).shift([0,r3*-0.5,0]).rotate((np.pi)/3,
about_point=[0,0,1]))
hexagons.append(RegularPolygon(6,**cGreen,**stroke2,**hexBase).scale(0.5).shift([0,r3*-0.5,0]).rotate(2*(np.pi)/3,
about_point=[0,0,1]))

hexagonsV=VGroup(*hexagons)

#===TexMathObjects===
xFormula = TexMobject("\mathbb{X}_{G_n}(w) = \\bigcup\limits^{}_{(a_1,  \ldots ,a_n)"+
                              " \in w} \{ (x_1, \ldots ,x_n) \in \mathbb{R}^n \mid (x_1 - a_1)^2"+
                              " + \cdots (x_n - a_n)^2 = 1  \} ").scale(0.8)
xFormula2 = TexMobject("\mathbb{X}_{G_2}(w) = \\bigcup\limits^{}_{(a_1, a_2)"+
                              " \in w} \{ (x_1, x_2) \in \mathbb{R}^2 \mid (x_1 - a_1)^2"+
                              " + (x_2 - a_2)^2 = 1  \} ").scale(0.8)
xFormula1 = TexMobject("\mathbb{X}_{G_1}(w) = \\bigcup\limits^{}_{(a)"+
                              " \in w} \{ (x) \in \mathbb{R} \mid (x - a)^2 = 1  \} ").scale(0.8)
xw = TexMobject("\mathbb{X}(w)",**cRed).scale(0.8)
w = TexMobject("w",**cGreen).scale(0.8)

w0 = TexMobject("0",**cGreen).scale(1)
x0 = TexMobject("\mathbb{X}(0)",**cRed).scale(1)
xIterM=TexMobject("\mathbb{X}^{\circ m}(w)").scale(1)
xIter2=TexMobject("\mathbb{X}^{\circ 2}(0)",**cGreen).scale(1).shift([0,2,0])
xIter3=TexMobject("\mathbb{X}^{\circ 3}(0)",**cRed).scale(1).shift([0,2,0])
xIter4=TexMobject("\mathbb{X}^{\circ 4}(0)",**cGreen).scale(1).shift([0,2,0])
xIter5=TexMobject("\mathbb{X}^{\circ 5}(0)",**cRed).scale(1).shift([0,2,0])
xIter6=TexMobject("\mathbb{X}^{\circ 6}(0)",**cGreen).scale(1).shift([0,2,0])
xIter2w=TexMobject("\mathbb{X}^{\circ 2}(w)",**cGreen).scale(1)
xIter3w=TexMobject("\mathbb{X}^{\circ 3}(w)",**cRed).scale(1)

wU0 = TexMobject("0",**cBlue).scale(1)
xUIter1=TexMobject("\mathbb{X}^{\cup\circ 1}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter2=TexMobject("\mathbb{X}^{\cup\circ 2}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter3=TexMobject("\mathbb{X}^{\cup\circ 3}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter4=TexMobject("\mathbb{X}^{\cup\circ 4}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter5=TexMobject("\mathbb{X}^{\cup\circ 5}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter6=TexMobject("\mathbb{X}^{\cup\circ 6}(0)",**cBlue).scale(1).shift([0,2,0])
xUIter7=TexMobject("\mathbb{X}^{\cup\circ 7}(0)",**cBlue).scale(1).shift([0,2,0])

#---K3ConflictMB---
def Xthird(nr):
    return 1-(2/3)**nr
mbH=0.15
mbW=0.8
sW =5
zf=0.35
K3CMB=MeasureBar(mbH,mbW,sW,
                  #Left bar entries
                  [{"height":mbH-(sW/(100/zf)),"width":0,"stroke_color":"#00FF00","fill_opacity":1.0,
                    "color":"#00FF00","stroke_width":0,"offset":[-mbW/2+(sW/(100/zf)),0,0]},
                   {"height":mbH-(sW/(100/zf)),"width":mbW/3-(sW/(100/zf)),"stroke_color":"#00FF00",
                    "fill_opacity":1.0,"color":"#00FF00","stroke_width":0,"offset":[-mbW/3,0,0]}],
                  #Right bar entries
                  [{"height":mbH-(sW/(50/zf)),"width":0,"stroke_color":"#FF0000","fill_opacity":1.0,
                    "color":"#00FF00","stroke_width":sW,"offset":[mbW/2-(sW/(100/zf)),0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW*(1/3),"stroke_color":"#FF0000",
                    "fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[mbW/3-(sW/(100/zf)),0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW*Xthird(2)-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[mbW/2-(mbW*Xthird(2))/2,0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW*Xthird(3)-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[mbW/2-(mbW*Xthird(3))/2,0,0]},
                   #Full width for the next two entries
                   {"height":mbH-(sW/(50/zf)),"width":mbW-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[0,0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#00FF00","stroke_width":sW,
                    "offset":[0,0,0]}
                   ]).assembleMeasureBar().shift([3,1.25,0])

#---K3CBMB---
mbH=0.15
mbW=0.8
sW =5
zf=0.35
K3CBMB=MeasureBar(mbH,mbW,sW,
                  #Left bar entries
                  [],
                  #Right bar entries
                  [{"height":mbH-(sW/(50/zf)),"width":0,"stroke_color":"#FF0000","fill_opacity":1.0,
                    "color":"#0000FF","stroke_width":sW,"offset":[mbW/2,0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW-(sW/(50/zf)),
                    "stroke_color":"#FF0000","fill_opacity":1.0,"color":"#0000FF","stroke_width":sW,
                    "offset":[0,0,0]}
                   ]).assembleMeasureBar().shift([3,1,0])
#---K3CRMB---
mbH=0.15
mbW=0.8
sW =5
zf=0.35
K3CRMB=MeasureBar(mbH,mbW,sW,
                  #Left bar entries
                  [],
                  #Right bar entries
                  [{"height":mbH-(sW/(50/zf)),"width":0,"stroke_color":"#0000FF","fill_opacity":1.0,
                    "color":"#FF0000","stroke_width":sW,"offset":[mbW/2,0,0]},
                   {"height":mbH-(sW/(50/zf)),"width":mbW-(sW/(50/zf)),
                    "stroke_color":"#0000FF","fill_opacity":1.0,"color":"#FF0000","stroke_width":sW,
                    "offset":[0,0,0]}
                   ]).assembleMeasureBar().shift([3,0.75,0])

#---K3MB---
mbH=0.15
mbW=0.8
sW =5
zf=0.35
K3MB=MeasureBar(mbH,mbW,sW,
                #Left bar entries
                [{"height":mbH-(sW/(100/zf)),"width":0,"stroke_color":"#00FF00","fill_opacity":1.0,
                "color":"#00FF00","stroke_width":0,"offset":[-mbW/2,0,0]},
                {"height":mbH-(sW/(100/zf)),"width":mbW/3,"stroke_color":"#00FF00","fill_opacity":1.0,
                "color":"#00FF00","stroke_width":0,"offset":[-mbW/3,0,0]},
                {"height":mbH-(sW/(100/zf)),"width":0,"stroke_color":"#FF0000","fill_opacity":1.0,
                "color":"#FF0000","stroke_width":0,"offset":[0,0,0]},
                {"height":mbH-(sW/(100/zf)),"width":mbW/3,"stroke_color":"#FF0000",
                "fill_opacity":1.0,"color":"#FF0000","stroke_width":0,"offset":[0,0,0]},
                {"height":mbH-(sW/(100/zf)),"width":0,"stroke_color":"#0000FF","fill_opacity":1.0,
                "color":"#0000FF","stroke_width":0,"offset":[mbW/2,0,0]},
                {"height":mbH-(sW/(100/zf)),"width":mbW/3,"stroke_color":"#0000FF","fill_opacity":1.0,
                "color":"#0000FF","stroke_width":0,"offset":[mbW/3,0,0]},
                 #This next entry is for a full green measure bar
                {"height":mbH-(sW/(100/zf)),"width":mbW-(sW/(100/zf)),"stroke_color":"#00FF00",
                "fill_opacity":1.0,"color":"#00FF00","stroke_width":0,"offset":[0,0,0]},
                 #This entry is for an almost empty measure bar
                {"height":mbH-(sW/(100/zf)),"width":mbW/30-(sW/(100/zf)),"stroke_color":"#00FF00",
                "fill_opacity":1.0,"color":"#00FF00","stroke_width":0,
                 "offset":[(-mbW+mbW/30)/2,0,0]}],
                #Right bar entries, unused here
                []).assembleMeasureBar().shift([2,1.25,0])


                  
#---MoserSpindle---
n0=[0,0,0]#BottomLeft
n1=[1,0,0]#BottomRight
n2=[(9+r33)/12,(3*r11+r3)/12,0]#FarRight
n3=[(9-r33)/12,(3*r11-r3)/12,0]#Left
n4=[(3-r33)/12,(3*r11+r3)/12,0]#FarLeft
n5=[(3+r33)/12,(3*r11-r3)/12,0]#Right
n6=[0.5,r11/2,0]#Top
g={0:[n0,[1,4,5],cRedSt],1:[n1,[0,2,3],cYellowSt],2:[n2,[1,3,6],cGreenSt],
3:[n3,[1,2,6],cBlueSt],4:[n4,[0,5,6],cBlueSt],5:[n5,[0,4,6],cGreenSt],6:[n6,[2,3,4,5],cRedSt]}

MS=Graph(g,lineConfig).returnVGroup()
gm={0:[n5,[1,2],cYellowStSmall],1:[n4,[0,2],cYellowStSmall],2:[n6,[0,1],cYellowStSmall]}
MSmark=Graph(gm,lineConfig).returnVertices()

MSa=Graph(g,lineConfig,annulus=True,inner_radius=0.235/2,outer_radius=0.26/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()
MSax=Graph(g,lineConfig,annulus=True,inner_radius=1-0.26/2,outer_radius=1+0.26/2,
          fill_opacity=0.3,color=RED).returnAnnuluses()
gGray={0:[n0,[1,4,5],{**cRedSt,"stroke_color" : GRAY}],1:[n1,[0,2,3],
{**cYellowSt,"stroke_color" : GRAY}],2:[n2,[1,3,6],{**cGreenSt,"stroke_color" : GRAY}],
3:[n3,[1,2,6],{**cBlueSt,"stroke_color" : GRAY}],4:[n4,[0,5,6],{**cBlueSt,"stroke_color" : GRAY}],
5:[n5,[0,4,6],{**cGreenSt,"stroke_color" : GRAY}],6:[n6,[2,3,4,5],{**cRedSt,"stroke_color" : GRAY}]}
MSaColored=Graph(gGray,lineConfig).returnVertices()

#---K2---
n0=[0,0,0]#Left
n1=[1,0,0]#Right
g={0:[n0,[1],cGreenSt],1:[n1,[0],cRedSt]}
gc={0:[n0,[1],cBlackSt],1:[n1,[0],cBlackSt]}
K2=Graph(g,lineConfig).returnVGroup()
K2c=Graph(gc,lineConfig).returnVGroup()
K2a=Graph(gc,lineConfig,annulus=True,inner_radius=0.255/2,outer_radius=0.29/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()
K2aB=Graph(gc,lineConfig,annulus=True,inner_radius=0.95/2,outer_radius=1/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()
        
#---K3---
n0=[0,0,0]#BottomLeft
n1=[1,0,0]#BottomRight
n2=[0.5,r3/2,0]#Top
g={0:[n0,[1,2],cGreenSt],1:[n1,[0,2],cRedSt],2:[n2,[0,1],cBlueSt]}
gc={0:[n0,[1,2],cBlackSt],1:[n1,[0,2],cBlackSt],2:[n2,[0,1],cBlackSt]}
ge={0:[n0,[1,2],cEmptySt],1:[n1,[0,2],cEmptySt],2:[n2,[0,1],cEmptySt]}
gAlt={0:[n0,[1,2],cGGreenSt],1:[n1,[0,2],cPurpleSt],2:[n2,[0,1],cCyanSt]}
K3=Graph(g,lineConfig).returnVGroup()
K3c=Graph(gc,lineConfig).returnVGroup()
K3e=Graph(ge,lineConfig).returnVGroup()
K3AltColors=Graph(gAlt,lineConfig).returnVGroup()
K3a=Graph(gc,lineConfig,annulus=True,inner_radius=0.255/2,outer_radius=0.29/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()
K3aB=Graph(gc,lineConfig,annulus=True,inner_radius=0.95/2,outer_radius=1/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()

#---K3aux---
#This one here uses complex functions to determine coordinates
n0=(1/math.sqrt(3))*cmath.exp((complex(0,1)*0*2*cmath.pi)/3)
n1=(1/math.sqrt(3))*cmath.exp((complex(0,1)*1*2*cmath.pi)/3)
n2=(1/math.sqrt(3))*cmath.exp((complex(0,1)*2*2*cmath.pi)/3)
g={0:[[float(n0.real),float(n0.imag),0],[1,2],cTBlueSt],
   1:[[float(n1.real),float(n1.imag),0],[0,2],cTGreenSt],
   2:[[float(n2.real),float(n2.imag),0],[0,1],cTRedSt]}
K3C=Graph(g,lineConfig).returnVGroup()
K3Cpoints=Graph(g,lineConfig).returnVertices()
K3Ca=Graph(g,lineConfig,annulus=True,inner_radius=0.235/2,outer_radius=0.26/2,
          fill_opacity=1,color=GRAY).returnAnnuluses()

#---H553---
#Raw vertex coordinates
h553pre=[[0,0,0],
[1,0,0],
[-1/2,r3/2,0],
[-1/2,-r3/2,0],
[-1,0,0],
[1/2,-r3/2,0],
[1/2,r3/2,0],
[r11s3/2,-1/(2*r3),0],
[(3 - r33)/12,(r3 + 3*r11)/12,0],
[(-3 - r33)/12,(r3 - 3*r11)/12,0],
[-r11s3/2,1/(2*r3),0],
[(-3 + r33)/12,(-r3 - 3*r11)/12,0],
[(3 + r33)/12,(-r3 + 3*r11)/12,0],
[r11s3/2,1/(2*r3),0],
[5/6,-r11/6,0],
[(5 - r33)/12,(-5*r3 - r11)/12,0],
[(-3 + r33)/12,(r3 + 3*r11)/12,0],
[(3 + r33)/12,(r3 - 3*r11)/12,0],
[-5/6,r11/6,0],
[-5/6,-r11/6,0],
[(-5 + r33)/12,(5*r3 + r11)/12,0],
[(-3 - r33)/12,(-r3 + 3*r11)/12,0],
[-r11s3/2,-1/(2*r3),0],
[(3 - r33)/12,(-r3 - 3*r11)/12,0],
[(5 - r33)/12,(15 + r33)/(12*r3),0],
[(-5 - r33)/12,-(-15 + r33)/(12*r3),0],
[(3*r5 + 7*r33)/48,(-7*r3 + 3*r55)/48,0],
[(-3*r5 - 7*r33)/48,(7*r3 - 3*r55)/48,0],
[(21 + 3*r5 + 7*r33 - 3*r165)/96,(-7*r3 + 21*r11 + 3*r15 + 3*r55)/96,0],
[(-21 - 3*r5 - 7*r33 + 3*r165)/96,(7*r3 - 21*r11 - 3*r15 - 3*r55)/96,0],
[(21 - 3*r5 - 7*r33 - 3*r165)/96,(7*r3 + 21*r11 + 3*r15 - 3*r55)/96,0],
[(-21 + 3*r5 + 7*r33 + 3*r165)/96,(3*r11*(-7 + r5) - r3*(7 + 3*r5))/96,0],
[(21 + 3*r5 - 7*r33 + 3*r165)/96,-(7 - 3*r5 + 7*r33 + r165)/(32*r3),0],
[(-21 - 3*r5 + 7*r33 - 3*r165)/96,(7 - 3*r5 + 7*r33 + r165)/(32*r3),0],
[(-3*r5 + 7*r33)/48,(7 + r165)/(16*r3),0],
[(3*r5 - 7*r33)/48,-(7 + r165)/(16*r3),0],
[(-21 + 3*r5 - 7*r33 - 3*r165)/96,-(7 + 3*r5 - 7*r33 + r165)/(32*r3),0],
[(21 - 3*r5 + 7*r33 + 3*r165)/96,(7 + 3*r5 - 7*r33 + r165)/(32*r3),0],
[(-7 + r33)/12,(r3 - r11)/12,0],
[(7 - r33)/12,(-r3 + r11)/12,0],
[(5 - r33)/12,(3*r3 - r11)/12,0],
[(-5 + r33)/12,(-3*r3 + r11)/12,0],
[1/6,(-6 + r33)/(6*r3),0],
[-1/6,1/r3 - r11/6,0],
[(6 - r33)/18,-(-4 + r33)/(6*r3),0],
[(7 - r33)/12,(r3 - r11)/12,0],
[(-7 + r33)/12,(-r3 + r11)/12,0],
[1/6,1/r3 - r11/6,0],
[(5 - r33)/12,(-9 + r33)/(12*r3),0],
[(-5 + r33)/12,-(-9 + r33)/(12*r3),0],
[(6 - r33)/6,1/(2*r3),0],
[1/6,(3*r3 - 2*r11)/6,0],
[-1/6,(-3*r3 + 2*r11)/6,0],
[(9 - r33)/12,(-5*r3 + 3*r11)/12,0],
[(3 - r33)/12,(7*r3 - 3*r11)/12,0],
[(-3 + r33)/12,(-7*r3 + 3*r11)/12,0],
[(3 - r33)/12,(-7*r3 + 3*r11)/12,0],
[(-6 + r33)/6,-1/(2*r3),0],
[(4 - r33)/6,(-2*r3 + r11)/6,0],
[(-9 + r33)/12,(-5 + r33)/(4*r3),0],
[(-6 + r33)/6,1/(2*r3),0],
[(-3 + r33)/12,-(-7 + r33)/(4*r3),0],
[(-5 + r33)/6,-(-3 + r33)/(6*r3),0],
[(-9 + r33)/12,-(-5 + r33)/(4*r3),0],
[(9 - r33)/12,-(-5 + r33)/(4*r3),0],
[-1/6,(9 - 2*r33)/(6*r3),0],
[(5 - r33)/12,(-r3 - r11)/12,0],
[(-5 + r33)/12,(-r3 - r11)/12,0],
[(5 - r33)/12,(r3 + r11)/12,0],
[(-5 + r33)/12,(r3 + r11)/12,0],
[-1/3,(-r3 + r11)/6,0],
[(-3 - r33)/36,(13*r3 - 3*r11)/36,0],
[(3 + r33)/36,(-13*r3 + 3*r11)/36,0],
[(-1 + r33)/12,(3*r3 - r11)/12,0],
[(-1 + r33)/12,(-3*r3 + r11)/12,0],
[(1 - r33)/12,(-3*r3 + r11)/12,0],
[(-21 + r33)/36,(5*r3 - 3*r11)/36,0],
[(9 - r33)/18,2/(3*r3),0],
[1/3,(r3 - r11)/6,0],
[(21 - r33)/36,(-5*r3 + 3*r11)/36,0],
[(1 - r33)/12,(3*r3 - r11)/12,0],
[(21 - r33)/36,-(-5 + r33)/(12*r3),0],
[(-21 + r33)/36,(-5 + r33)/(12*r3),0],
[-1/3,-(-3 + r33)/(6*r3),0],
[(-9 + r33)/18,2/(3*r3),0],
[(-3 - r33)/36,(-13 + r33)/(12*r3),0],
[(3 + r33)/36,-(-13 + r33)/(12*r3),0],
[(-7 + r33)/12,(5*r3 - r11)/12,0],
[1/3,(3*r3 - r11)/6,0],
[(11 - r33)/12,-(-3 + r33)/(12*r3),0],
[(3 - r33)/12,(-r3 + r11)/4,0],
[(-3 + r33)/12,(r3 - r11)/4,0],
[(-3 + r33)/12,(-r3 + r11)/4,0],
[(3 - r33)/6,0,0],
[(-3 + r33)/6,0,0],
[(-6 + r33)/9,(r3 - 3*r11)/18,0],
[(3 - r33)/12,-(-3 + r33)/(4*r3),0],
[-1/3,-(-9 + r33)/(6*r3),0],
[(-11 + r33)/12,-(-3 + r33)/(12*r3),0],
[((-7 + 3*r5)*(r3 - r11))/(32*r3),((7 + r5)*(-3 + r33))/(32*r3),0],
[(-7*(-3 + r33))/48,(r15 - r55)/16,0],
[(7*(-3 + r33))/48,(-r15 + r55)/16,0],
[-((-7 + 3*r5)*(r3 - r11))/(32*r3),-((7 + r5)*(-3 + r33))/(32*r3),0],
[-((7 + 3*r5)*(-3 + r33))/96,((-7 + r5)*(r3 - r11))/32,0],
[((7 + 3*r5)*(-3 + r33))/96,-((-7 + r5)*(r3 - r11))/32,0],
[(-7 + r33)/12,(-15 + r33)/(12*r3),0],
[(7 - r33)/12,-(-15 + r33)/(12*r3),0],
[(1 - r33)/12,(-r3 - r11)/12,0],
[r11s3/6,-5/(6*r3),0],
[-1/6,-r11/6,0],
[(-1 + r33)/12,(-r3 - r11)/12,0],
[1/6,r11/6,0],
[(1 - r33)/12,(r3 + r11)/12,0],
[1/6,-r11/6,0],
[(-1 + r33)/12,(r3 + r11)/12,0],
[(1 + r33)/12,(-r3 + r11)/12,0],
[(-1 - r33)/12,(r3 - r11)/12,0],
[-1/6,r11/6,0],
[(-1 - r33)/12,(-r3 + r11)/12,0],
[(1 + r33)/12,(r3 - r11)/12,0],
[0,1/r3,0],
[-1/2,1/(2*r3),0],
[-1/2,-1/(2*r3),0],
[0,-(1/r3),0],
[1/2,1/(2*r3),0],
[1/2,-1/(2*r3),0],
[-r5/8,7/(8*r3),0],
[(-7 - r5)/16,(7 - 3*r5)/(16*r3),0],
[(-7 + r5)/16,-(7 + 3*r5)/(16*r3),0],
[(7 - r5)/16,(7 + 3*r5)/(16*r3),0],
[r5/8,-7/(8*r3),0],
[(7 + r5)/16,(-7 + 3*r5)/(16*r3),0],
[(15 + r33)/36,(5*r3 - 3*r11)/36,0],
[(-15 - r33)/36,(-5*r3 + 3*r11)/36,0],
[(15 - r33)/36,(-5*r3 - 3*r11)/36,0],
[(-15 + r33)/36,(5*r3 + 3*r11)/36,0],
[r11s3/6,5/(6*r3),0],
[-r11s3/6,-5/(6*r3),0],
[(15 + r33)/36,(-5*r3 + 3*r11)/36,0],
[-r11s3/6,5/(6*r3),0],
[(-15 - r33)/36,(5*r3 - 3*r11)/36,0],
[(-15 + r33)/36,-(5 + r33)/(12*r3),0],
[(15 - r33)/36,(5 + r33)/(12*r3),0],
[(-2 + r33)/6,(-2*r3 + r11)/6,0],
[(-13 + r33)/12,(-9 + r33)/(12*r3),0],
[1/3,1/r3 - r11/3,0],
[-1/3,1/r3 - r11/3,0],
[(11 - r33)/12,-(-15 + r33)/(12*r3),0],
[(-11 + r33)/12,-(-15 + r33)/(12*r3),0],
[-1/6,2/r3 - r11/6,0],
[1/6,2/r3 - r11/6,0],
[2/3,(-r3 + r11)/6,0],
[(1 + r33)/12,(-5*r3 + r11)/12,0],
[(-7 + r33)/12,(-3*r3 - r11)/12,0],
[-2/3,(r3 - r11)/6,0],
[(-7 + r33)/12,(3*r3 + r11)/12,0],
[(7 - r33)/12,(3*r3 + r11)/12,0],
[-2/3,(-r3 + r11)/6,0],
[(1 + r33)/12,-(-15 + r33)/(12*r3),0],
[2/3,-(-3 + r33)/(6*r3),0],
[(7 - r33)/12,-(9 + r33)/(12*r3),0],
[(-1 - r33)/12,-(-15 + r33)/(12*r3),0],
[(3 - 5*r33)/36,-(-7 + r33)/(12*r3),0],
[(-9 - r33)/36,(5 - 3*r33)/(12*r3),0],
[(3 - r33)/6,-(1/r3),0],
[(9 - r33)/12,(r3 - 3*r11)/12,0],
[(-9 + r33)/12,(r3 - 3*r11)/12,0],
[(9 - r33)/12,(-r3 + 3*r11)/12,0],
[(-3 + r33)/6,-(1/r3),0],
[(-3 + r33)/6,1/r3,0],
[(-9 + r33)/12,(-r3 + 3*r11)/12,0],
[2/3,(-3*r3 + r11)/6,0],
[(-3 - r33)/12,(-5*r3 + 3*r11)/12,0],
[(3 + r33)/12,(5*r3 - 3*r11)/12,0],
[(3 + r33)/12,(-5*r3 + 3*r11)/12,0],
[(-21 - 6*r5 + 7*r33)/48,(14 - 3*r5 + r165)/(16*r3),0],
[(-63 + 3*r5 + 7*r33 - 3*r165)/96,(-7*r3 + 21*r11 - 9*r15 + 3*r55)/96,0],
[(-13 + r33)/12,(-r3 - r11)/12,0],
[-2/3,(3*r3 - r11)/6,0],
[(13 - r33)/12,-(3 + r33)/(12*r3),0],
[(-13 + r33)/12,(3 + r33)/(12*r3),0],
[2/3,-(-9 + r33)/(6*r3),0],
[(3 - r33)/6,1/r3,0],
[(-3 - r33)/12,-(-5 + r33)/(4*r3),0],
[(-5 + r33)/12,-(-21 + r33)/(12*r3),0],
[(21 + 15*r5 + 7*r33 - 3*r165)/96,(-35 + 3*r5 + 7*r33 + r165)/(32*r3),0],
[(21 - 6*r5 - 7*r33)/48,-(-14 - 3*r5 + r165)/(16*r3),0],
[(-21 - 15*r5 - 7*r33 + 3*r165)/96,-(-35 + 3*r5 + 7*r33 + r165)/(32*r3),0],
[(63 + 3*r5 - 7*r33 - 3*r165)/96,-(7 - 9*r5 - 7*r33 + r165)/(32*r3),0],
[(-63 - 3*r5 + 7*r33 + 3*r165)/96,(7 - 9*r5 - 7*r33 + r165)/(32*r3),0],
[(-3 + r33)/12,(11*r3 - 3*r11)/12,0],
[((7 + r5)*(-3 + r33))/32,((-7 + 3*r5)*(-3 + r33))/(32*r3),0],
[(1 - r33)/12,(-7*r3 + r11)/12,0],
[-1/6,(-r3 + 2*r11)/6,0],
[(-1 + r33)/6,(-r3 + r11)/6,0],
[(11 - r33)/12,-(9 + r33)/(12*r3),0],
[(-2 + r33)/6,-r11/6,0],
[-5/6,1/r3 - r11/6,0],
[-1/6,(3 - 2*r33)/(6*r3),0],
[5/6,1/r3 - r11/6,0],
[(2 - r33)/6,-r11/6,0],
[(1 - r33)/6,(r3 - r11)/6,0],
[1/6,(3 - 2*r33)/(6*r3),0],
[(3 - r33)/36,-(-23 + r33)/(12*r3),0],
[(-1 + r33)/12,-(-21 + r33)/(12*r3),0],
[(-1 + r33)/6,-(-3 + r33)/(6*r3),0],
[(-5 + r33)/6,(r3 + r11)/6,0],
[-2/3,1/r3 - r11/3,0],
[(-1 + r33)/6,-(-9 + r33)/(6*r3),0],
[(1 - r33)/6,-(-9 + r33)/(6*r3),0],
[(5 - r33)/6,-(3 + r33)/(6*r3),0],
[(-5 + r33)/6,(-r3 - r11)/6,0],
[2/3,1/r3 - r11/3,0],
[(-1 - r33)/12,(-5*(-3 + r33))/(12*r3),0],
[(6 - r33)/6,-r3/2,0],
[(-6 + r33)/6,r3/2,0],
[(-15 + r33)/12,-(-3 + r33)/(4*r3),0],
[(-3 - r33)/12,-(-9 + r33)/(4*r3),0],
[(-6 + r33)/6,-r3/2,0],
[(6 - r33)/6,r3/2,0],
[(15 - r33)/12,-(-3 + r33)/(4*r3),0],
[(-5 - r33)/12,(-r3 + r11)/12,0],
[-1/3,(r3 + r11)/6,0],
[1/3,(-r3 - r11)/6,0],
[(5 + r33)/12,(-r3 + r11)/12,0],
[-1/3,(-r3 - r11)/6,0],
[(1 + r33)/12,(3*r3 + r11)/12,0],
[(1 + r33)/12,(-3*r3 - r11)/12,0],
[(-1 - r33)/12,(-3*r3 - r11)/12,0],
[(-21 - r33)/36,(-5*r3 - 3*r11)/36,0],
[(21 + r33)/36,(5*r3 + 3*r11)/36,0],
[(-9 - r33)/18,2/(3*r3),0],
[(-3 + r33)/36,(-13*r3 - 3*r11)/36,0],
[(3 - r33)/36,(13*r3 + 3*r11)/36,0],
[(5 + r33)/12,(r3 - r11)/12,0],
[1/3,(r3 + r11)/6,0],
[(-5 - r33)/12,(r3 - r11)/12,0],
[(-3 + r33)/36,(13 + r33)/(12*r3),0],
[(-1 - r33)/12,(9 + r33)/(12*r3),0],
[(9 + r33)/18,2/(3*r3),0],
[(-21 - r33)/36,(5 + r33)/(12*r3),0],
[(3 - r33)/36,-(13 + r33)/(12*r3),0],
[(1 - r33)/12,(5*r3 + r11)/12,0],
[(-1 + r33)/12,(-5*r3 - r11)/12,0],
[2/3,(r3 + r11)/6,0],
[(7 + r33)/12,-(-9 + r33)/(12*r3),0],
[-2/3,(3 + r33)/(6*r3),0],
[-2/3,-(3 + r33)/(6*r3),0],
[(-7 - r33)/12,-(-9 + r33)/(12*r3),0],
[(-7 - r33)/12,(-9 + r33)/(12*r3),0],
[1/6,1/r3 + r11/6,0],
[(-7 - r33)/12,(-r3 - r11)/12,0],
[-1/6,-(1/r3) - r11/6,0],
[(5 + r33)/12,(3*r3 + r11)/12,0],
[(5 + r33)/12,(-3*r3 - r11)/12,0],
[(-5 - r33)/12,(3*r3 + r11)/12,0],
[(-7 - r33)/12,(r3 + r11)/12,0],
[(7 + r33)/12,(-r3 - r11)/12,0],
[1/6,-(6 + r33)/(6*r3),0],
[(-5 - r33)/12,-(9 + r33)/(12*r3),0],
[(6 + r33)/18,(4 + r33)/(6*r3),0],
[(-9 - 2*r33)/18,1/(6*r3),0],
[1,-(1/r3),0],
[-1,-(1/r3),0],
[1,1/r3,0],
[(-1 + r33)/6,(-r3 - r11)/6,0],
[(-1 - r33)/6,(r3 - r11)/6,0],
[(1 + r33)/6,(-r3 + r11)/6,0],
[(1 - r33)/6,(r3 + r11)/6,0],
[0,2/r3,0],
[-1/3,-r11/3,0],
[1/3,r11/3,0],
[-1,1/r3,0],
[0,-2/r3,0],
[(-1 + r33)/6,(3 + r33)/(6*r3),0],
[1/3,-r11/3,0],
[-1/3,r11/3,0],
[(1 - r33)/6,-(3 + r33)/(6*r3),0],
[(-1 - r33)/6,(-3 + r33)/(6*r3),0],
[(1 + r33)/6,-(-3 + r33)/(6*r3),0],
[(-7 + r5)/8,-(7 + 3*r5)/(8*r3),0],
[-r5/4,7/(4*r3),0],
[(7 + r5)/8,(-7 + 3*r5)/(8*r3),0],
[-1/2,1/r3 - r11/2,0],
[1/2,1/r3 - r11/2,0],
[(-7 - 2*r5 + r165)/16,-(-14 + 3*r5 + 7*r33)/(16*r3),0],
[(7 - 5*r5 - 7*r33 + r165)/32,(35 + 3*r5 - 7*r33 - 3*r165)/(32*r3),0],
[(21 - r5 - 7*r33 - r165)/32,(7 + 9*r5 + 7*r33 - 3*r165)/(32*r3),0],
[(15 - r33)/12,(r3 + 3*r11)/12,0],
[(3 - r33)/6,2/r3,0],
[(-3 + r33)/6,-2/r3,0],
[(-15 + r33)/12,(-r3 - 3*r11)/12,0],
[(-15 + r33)/12,(1 + r33)/(4*r3),0],
[(-3 + r33)/6,2/r3,0],
[(9 + r33)/12,-(-7 + r33)/(4*r3),0],
[(15 - r33)/12,-(1 + r33)/(4*r3),0],
[(-9 - r33)/12,-(-7 + r33)/(4*r3),0],
[(-9 - r33)/12,(-7 + r33)/(4*r3),0],
[-1,-(-3 + r33)/(2*r3),0],
[(-9 + r33)/12,(-r3 - r11)/4,0],
[(9 - r33)/12,(r3 + r11)/4,0],
[(-9 + r33)/12,(3 + r33)/(4*r3),0],
[(9 + r33)/12,(-r3 + r11)/4,0],
[(-9 - r33)/12,(r3 - r11)/4,0],
[-7/6,r11/6,0],
[-r11s3/2,r3/2,0],
[-r11s3/2,-r3/2,0],
[7/6,r11/6,0],
[(2 + r33)/6,1/r3 - r11/6,0],
[(-7 - r33)/12,(7*r3 - r11)/12,0],
[(7 + r33)/12,(-7*r3 + r11)/12,0],
[r11s3/2,-r3/2,0],
[(-2 + r33)/6,1/r3 + r11/6,0],
[-2/3,r11/3,0],
[(-2 - r33)/6,(-2*r3 + r11)/6,0],
[(2 + r33)/6,(-2*r3 + r11)/6,0],
[(-7 + r33)/12,-(21 + r33)/(12*r3),0],
[(7 - r33)/12,(21 + r33)/(12*r3),0],
[2/3,-r11/3,0],
[-7/6,-r11/6,0],
[(-39 + r33)/36,(-13*r3 - 3*r11)/36,0],
[(-39 - r33)/36,(13*r3 - 3*r11)/36,0],
[(-9 - r33)/12,(-3 + r33)/(4*r3),0],
[(9 - r33)/12,(-r3 - r11)/4,0],
[(-2 - r33)/6,1/r3 - r11/6,0],
[7/6,-r11/6,0],
[(-7 + r33)/12,(21 + r33)/(12*r3),0],
[(7 - r33)/12,-(21 + r33)/(12*r3),0],
[r11s3/2,r3/2,0],
[(-7 - r33)/12,(-21 + r33)/(12*r3),0],
[(7 + r33)/12,-(-21 + r33)/(12*r3),0],
[(-2 + r33)/6,-(6 + r33)/(6*r3),0],
[r11s3/6,13/(6*r3),0],
[(9 + r33)/12,-(-3 + r33)/(4*r3),0],
[(-39 + r33)/36,(13*r3 + 3*r11)/36,0],
[(-63 - 9*r5 - 7*r33 + 3*r165)/96,-(-21 + 9*r5 + 7*r33 + r165)/(32*r3),0],
[(-9*r5 + 7*r33)/48,(21 + r165)/(16*r3),0],
[(9*r5 - 7*r33)/48,-(21 + r165)/(16*r3),0],
[(63 + 9*r5 + 7*r33 - 3*r165)/96,(-21 + 9*r5 + 7*r33 + r165)/(32*r3),0],
[(9*r5 + 7*r33)/48,(-21 + r165)/(16*r3),0],
[(-9*r5 - 7*r33)/48,-(-21 + r165)/(16*r3),0],
[(-63 + 9*r5 - 7*r33 - 3*r165)/96,-(21 + 9*r5 - 7*r33 + r165)/(32*r3),0],
[(63 - 9*r5 - 7*r33 - 3*r165)/96,(21 + 9*r5 + 7*r33 - r165)/(32*r3),0],
[(-63 + 9*r5 + 7*r33 + 3*r165)/96,(-21 - 9*r5 - 7*r33 + r165)/(32*r3),0],
[(63 - 9*r5 + 7*r33 + 3*r165)/96,(21 + 9*r5 - 7*r33 + r165)/(32*r3),0],
[(63 + 9*r5 - 7*r33 + 3*r165)/96,-(21 - 9*r5 + 7*r33 + r165)/(32*r3),0],
[(-63 - 9*r5 + 7*r33 - 3*r165)/96,(21 - 9*r5 + 7*r33 + r165)/(32*r3),0],
[-2/3,-r11/3,0],
[0,(-1 + r33)/(2*r3),0],
[(-1 + r33)/4,(r3 - 3*r11)/12,0],
[(1 - r33)/4,(-r3 + 3*r11)/12,0],
[(1 - r33)/4,-(-1 + r33)/(4*r3),0],
[0,-(-1 + r33)/(2*r3),0],
[-(r5*(-1 + r33))/16,(-7*(r3 - 3*r11))/48,0],
[-((-7 + r5)*(-1 + r33))/32,-((7 + 3*r5)*(r3 - 3*r11))/96,0],
[((7 + r5)*(r3 - 3*r11))/(32*r3),-((-7 + 3*r5)*(-1 + r33))/(32*r3),0],
[-((7 + r5)*(r3 - 3*r11))/(32*r3),((-7 + 3*r5)*(-1 + r33))/(32*r3),0],
[((-7 + r5)*(-1 + r33))/32,((7 + 3*r5)*(r3 - 3*r11))/96,0],
[(r5*(-1 + r33))/16,(7*(r3 - 3*r11))/48,0],
[(-11 - r33)/12,-(-9 + r33)/(12*r3),0],
[(1 + r33)/6,(-r3 - r11)/6,0],
[(-1 - r33)/6,-(3 + r33)/(6*r3),0],
[1/6,-(3 + 2*r33)/(6*r3),0],
[-5/6,-(6 + r33)/(6*r3),0],
[(1 + r33)/6,(3 + r33)/(6*r3),0],
[(11 + r33)/12,-(-9 + r33)/(12*r3),0],
[(6*r5 + 7*r33 - 3*r165)/48,(-14 + 7*r33 + r165)/(16*r3),0],
[(-21 + 3*r5 + 7*r33 - 3*r165)/48,(-7 - 3*r5 + 7*r33 + r165)/(16*r3),0],
[(21 - 3*r5 - 14*r33)/48,(7 + 3*r5 - 2*r165)/(16*r3),0],
[(-21 + 3*r5 + 14*r33)/48,(-7 - 3*r5 + 2*r165)/(16*r3),0],
[(21 + 3*r5 - 14*r33)/48,-(7 - 3*r5 + 2*r165)/(16*r3),0],
[(-21 - 3*r5 + 14*r33)/48,(7 - 3*r5 + 2*r165)/(16*r3),0],
[(-6*r5 - 7*r33 + 3*r165)/48,-(-14 + 7*r33 + r165)/(16*r3),0],
[(21 - 3*r5 - 7*r33 + 3*r165)/48,-(-7 - 3*r5 + 7*r33 + r165)/(16*r3),0],
[(-6*r5 + 7*r33 + 3*r165)/48,(14 - 7*r33 + r165)/(16*r3),0],
[(21 + 3*r5 - 7*r33 - 3*r165)/48,-(7 - 3*r5 - 7*r33 + r165)/(16*r3),0],
[(-21 - 3*r5 + 7*r33 + 3*r165)/48,(7 - 3*r5 - 7*r33 + r165)/(16*r3),0],
[(-7 - r33)/12,(-5*r3 - r11)/12,0],
[(-11 - r33)/12,(3 + r33)/(12*r3),0],
[(7 + r33)/12,(5*r3 + r11)/12,0],
[-1/3,(3*r3 + r11)/6,0],
[1/3,(-3*r3 - r11)/6,0],
[(11 + r33)/12,(r3 + r11)/12,0],
[(3 + r33)/12,(r3 + r11)/4,0],
[(-3 - r33)/12,(r3 + r11)/4,0],
[(-3 - r33)/6,0,0],
[(3 + r33)/6,0,0],
[(-9 + r33)/36,(13 + 3*r33)/(12*r3),0],
[(-7 - r33)/12,(15 + r33)/(12*r3),0],
[(-3 - r33)/12,-(3 + r33)/(4*r3),0],
[(3 + r33)/12,-(3 + r33)/(4*r3),0],
[-((-7 + 3*r5)*(r3 + r11))/(32*r3),((7 + r5)*(3 + r33))/(32*r3),0],
[(-7*(3 + r33))/48,(-r15 - r55)/16,0],
[(7*(3 + r33))/48,(r15 + r55)/16,0],
[((-7 + 3*r5)*(r3 + r11))/(32*r3),-((7 + r5)*(3 + r33))/(32*r3),0],
[((7 + 3*r5)*(3 + r33))/96,((-7 + r5)*(3 + r33))/(32*r3),0],
[-((7 + 3*r5)*(3 + r33))/96,-((-7 + r5)*(r3 + r11))/32,0],
[(-11 - r33)/12,-(3 + r33)/(12*r3),0],
[-3/2,-1/(2*r3),0],
[3/2,1/(2*r3),0],
[-1,-2/r3,0],
[1,2/r3,0],
[-1/2,5/(2*r3),0],
[-1,2/r3,0],
[-3/2,1/(2*r3),0],
[(-3 + r33)/12,(5*r3 + 3*r11)/12,0],
[(3 - r33)/12,(5*r3 + 3*r11)/12,0],
[(-3 + r33)/12,(-5*r3 - 3*r11)/12,0],
[(3 - r33)/12,(-5*r3 - 3*r11)/12,0],
[(3 + r33)/6,-(1/r3),0],
[(-9 - r33)/12,(r3 + 3*r11)/12,0],
[(9 + r33)/12,(-r3 - 3*r11)/12,0],
[(3 + r33)/6,1/r3,0],
[(-3 - r33)/6,-(1/r3),0],
[(9 + r33)/12,(r3 + 3*r11)/12,0],
[(-21 - 15*r5 + 7*r33 - 3*r165)/96,(35*r3 + 21*r11 - 3*r15 + 3*r55)/96,0],
[(-63 - 3*r5 - 7*r33 - 3*r165)/96,(7*r3 + 21*r11 - 9*r15 - 3*r55)/96,0],
[(21 - 6*r5 + 7*r33)/48,(14 + 3*r5 + r165)/(16*r3),0],
[(5 + r33)/12,(-7*r3 - r11)/12,0],
[(-5 - r33)/12,(7*r3 + r11)/12,0],
[-2/3,(-3*r3 - r11)/6,0],
[2/3,(3*r3 + r11)/6,0],
[(-3 - r33)/6,1/r3,0],
[(-13 - r33)/12,(-3 + r33)/(12*r3),0],
[(13 + r33)/12,-(-3 + r33)/(12*r3),0],
[(-5 - r33)/12,-(21 + r33)/(12*r3),0],
[(5 + r33)/12,(21 + r33)/(12*r3),0],
[(-9 - r33)/12,-(1 + r33)/(4*r3),0],
[-2/3,(9 + r33)/(6*r3),0],
[(21 + 6*r5 + 7*r33)/48,(-14 + 3*r5 + r165)/(16*r3),0],
[(-21 - 6*r5 - 7*r33)/48,-(-14 + 3*r5 + r165)/(16*r3),0],
[(63 - 3*r5 + 7*r33 - 3*r165)/96,(7 + 9*r5 + 7*r33 + r165)/(32*r3),0],
[(-21 + 15*r5 + 7*r33 + 3*r165)/96,(-35 - 3*r5 - 7*r33 + r165)/(32*r3),0],
[(-63 + 3*r5 - 7*r33 + 3*r165)/96,-(7 + 9*r5 + 7*r33 + r165)/(32*r3),0],
[(21 - 15*r5 - 7*r33 - 3*r165)/96,(35 + 3*r5 + 7*r33 - r165)/(32*r3),0],
[1/2,r11/2,0],
[(-15 + r33)/12,(5*r3 + 3*r11)/12,0],
[(15 - r33)/12,(-5*r3 - 3*r11)/12,0],
[-1/2,r11/2,0],
[(-1 + r33)/4,(r3 + r11)/4,0],
[(1 + r33)/4,(-r3 + r11)/4,0],
[0,r3,0],
[(-15 - r33)/12,(5*r3 - 3*r11)/12,0],
[(-1 - r33)/4,(r3 - r11)/4,0],
[-1/2,-r11/2,0],
[(-1 + r33)/4,(-r3 - r11)/4,0],
[-r11s3/2,5/(2*r3),0],
[(-1 - r33)/4,(-3 + r33)/(4*r3),0],
[(1 + r33)/4,-(-3 + r33)/(4*r3),0],
[(1 - r33)/4,-(3 + r33)/(4*r3),0],
[(1 - r33)/4,(r3 + r11)/4,0],
[1/2,-r11/2,0],
[(-7 - 3*r5 - 7*r33 + r165)/32,(7*r3 - 7*r11 - r15 - 3*r55)/32,0],
[(-7 - 3*r5 + 7*r33 - r165)/32,(21 - 3*r5 + 7*r33 + 3*r165)/(32*r3),0],
[(7 + 3*r5 - 7*r33 + r165)/32,-(21 - 3*r5 + 7*r33 + 3*r165)/(32*r3),0],
[(7 + 3*r5 + 7*r33 - r165)/32,(-7*r3 + 7*r11 + r15 + 3*r55)/32,0],
[(-7 + 3*r5 - 7*r33 - r165)/32,-(21 + 3*r5 - 7*r33 + 3*r165)/(32*r3),0],
[(7 - r165)/16,(7*r11 + r15)/16,0],
[(7 - 3*r5 + 7*r33 + r165)/32,(21 + 3*r5 - 7*r33 + 3*r165)/(32*r3),0],
[(-7 + r165)/16,(-7*r11 - r15)/16,0],
[(-7 + 3*r5 + 7*r33 + r165)/32,(-(r3*(7 + r5)) + r11*(-7 + 3*r5))/32,0],
[(7 + r165)/16,(-7*r11 + r15)/16,0],
[(7 - 3*r5 - 7*r33 - r165)/32,(7*r3 + 7*r11 + r15 - 3*r55)/32,0],
[(-7 - r165)/16,(7*r11 - r15)/16,0],
[(15 + r33)/12,(-r3 + 3*r11)/12,0],
[(9 - r33)/12,(7*r3 + 3*r11)/12,0],
[(-9 + r33)/12,(-7*r3 - 3*r11)/12,0],
[(-15 - r33)/12,(r3 - 3*r11)/12,0],
[(-9 + r33)/12,(7 + r33)/(4*r3),0],
[(15 + r33)/12,-(-1 + r33)/(4*r3),0],
[(3 + r33)/6,2/r3,0],
[(-3 - r33)/6,2/r3,0],
[(-15 - r33)/12,(-1 + r33)/(4*r3),0],
[(9 - r33)/12,-(7 + r33)/(4*r3),0],
[(-7*r11s3)/8,-r55/8,0],
[(r11s3*(7 - 3*r5))/16,(r11*(7 + r5))/16,0],
[(r11s3*(7 + 3*r5))/16,(r11*(-7 + r5))/16,0],
[(-1 - r33)/4,(r3 + 3*r11)/12,0],
[0,-(1 + r33)/(2*r3),0],
[0,(1 + r33)/(2*r3),0],
[(1 + r33)/4,(-r3 - 3*r11)/12,0],
[(-1 - r33)/4,-(1 + r33)/(4*r3),0],
[((-7 + r5)*(1 + r33))/32,-((7 + 3*r5)*(r3 + 3*r11))/96,0],
[-(r5*(1 + r33))/16,(7*(r3 + 3*r11))/48,0],
[(r5*(1 + r33))/16,(-7*(r3 + 3*r11))/48,0],
[((7 + r5)*(r3 + 3*r11))/(32*r3),((-7 + 3*r5)*(1 + r33))/(32*r3),0],
[-((7 + r5)*(1 + r33))/32,-((-7 + 3*r5)*(1 + r33))/(32*r3),0],
[(-6 - r33)/6,1/(2*r3),0],
[(6 + r33)/6,-1/(2*r3),0],
[(-3 - r33)/12,(7*r3 + 3*r11)/12,0],
[(9 + r33)/12,(5*r3 + 3*r11)/12,0],
[(-9 - r33)/12,(-5*r3 - 3*r11)/12,0],
[(-21 - 21*r5 - 7*r33 - 3*r165)/96,(49*r3 + 21*r11 - 3*r15 - 3*r55)/96,0],
[(3 + r33)/12,(-7*r3 - 3*r11)/12,0],
[1/6,(-3*r3 - 2*r11)/6,0],
[-1/6,(3*r3 + 2*r11)/6,0],
[(-4 - r33)/6,-(1/r3) - r11/6,0],
[(9 + r33)/12,(-5*r3 - 3*r11)/12,0],
[(3 + r33)/12,(7 + r33)/(4*r3),0],
[(-6 - r33)/6,-1/(2*r3),0],
[(-3 - r33)/12,-(7 + r33)/(4*r3),0],
[(-9 - r33)/12,(5 + r33)/(4*r3),0],
[(-42 + 3*r5 - 7*r33)/48,(-7*r3 - 6*r15 - 3*r55)/48,0],
[(63 + 15*r5 + 7*r33 + 3*r165)/96,(-35 + 9*r5 - 7*r33 + r165)/(32*r3),0],
[(6 + r33)/6,1/(2*r3),0],
[(5 + r33)/6,(3 + r33)/(6*r3),0],
[(3 + r33)/6,-(-1 + r33)/(2*r3),0],
[(-3 - r33)/6,(-1 + r33)/(2*r3),0],
[r11s3,1/r3,0],
[-r11s3,-(1/r3),0],
[(3 + r33)/6,(-r3 + 3*r11)/6,0],
[r11s3,-(1/r3),0],
[-r11s3,1/r3,0],
[(-3 + r33)/6,(-r3 - 3*r11)/6,0],
[(3 - r33)/6,(r3 + 3*r11)/6,0],
[(3 - r33)/6,(-r3 - 3*r11)/6,0],
[(-3 + r33)/6,(r3 + 3*r11)/6,0],
[(-3 - r33)/6,(r3 - 3*r11)/6,0],
[(-21 + 3*r5 - 7*r33 - 3*r165)/48,-(7 + 3*r5 - 7*r33 + r165)/(16*r3),0],
[(21 - 3*r5 - 7*r33 - 3*r165)/48,(7*r3 + 21*r11 + 3*r15 - 3*r55)/48,0],
[(-21 + 3*r5 + 7*r33 + 3*r165)/48,(3*r11*(-7 + r5) - r3*(7 + 3*r5))/48,0],
[(21 - 3*r5 + 7*r33 + 3*r165)/48,(7 + 3*r5 - 7*r33 + r165)/(16*r3),0],
[(-3*r5 - 7*r33)/24,(7*r3 - 3*r55)/24,0],
[(3*r5 + 7*r33)/24,(-7*r3 + 3*r55)/24,0],
[(21 + 3*r5 + 7*r33 - 3*r165)/48,(-7*r3 + 21*r11 + 3*r15 + 3*r55)/48,0],
[(3*r5 - 7*r33)/24,-(7 + r165)/(8*r3),0],
[(-3*r5 + 7*r33)/24,(7 + r165)/(8*r3),0],
[(-21 - 3*r5 + 7*r33 - 3*r165)/48,(7 - 3*r5 + 7*r33 + r165)/(16*r3),0],
[(-21 - 3*r5 - 7*r33 + 3*r165)/48,(7*r3 - 21*r11 - 3*r15 - 3*r55)/48,0],
[(21 + 3*r5 - 7*r33 + 3*r165)/48,-(7 - 3*r5 + 7*r33 + r165)/(16*r3),0],
[(5 + r33)/12,-(-15 + r33)/(12*r3),0],
[(9 + r33)/36,(5 - 3*r33)/(12*r3),0],
[(-5 + r33)/12,(-21 + r33)/(12*r3),0],
[(6 + r33)/18,-(4 + r33)/(6*r3),0],
[(11 + r33)/12,-(3 + r33)/(12*r3),0],
[(-9 + r33)/36,-(13 + 3*r33)/(12*r3),0],
[(13 + r33)/12,(-r3 + r11)/12,0],
[(-7 + 2*r5 + r165)/16,(-14*r3 - 21*r11 - 3*r15)/48,0],
[(-21 + r5 - 7*r33 - r165)/32,(-7*r3 + 21*r11 - 9*r15 - 9*r55)/96,0],
[(-21 - r5 - 7*r33 + r165)/32,(7*r3 - 21*r11 - 9*r15 - 9*r55)/96,0],
[(7 + 5*r5 + 7*r33 + r165)/32,(-35*r3 - 21*r11 + 3*r15 + 9*r55)/96,0],
[(-6*r5 - 7*r33 - 3*r165)/48,(14*r3 + 21*r11 - 3*r55)/48,0],
[(-6*r5 + 7*r33 - 3*r165)/48,(14*r3 + 21*r11 + 3*r55)/48,0],
[(6*r5 - 7*r33 + 3*r165)/48,(-14*r3 - 21*r11 - 3*r55)/48,0],
[(6*r5 + 7*r33 + 3*r165)/48,(-14*r3 - 21*r11 + 3*r55)/48,0],
[(-21 - 3*r5 - 7*r33 - 3*r165)/48,(7*r3 + 21*r11 - 3*r15 - 3*r55)/48,0],
[(21 - 3*r5 + 7*r33 - 3*r165)/48,(7*r3 + 21*r11 + 3*r15 + 3*r55)/48,0],
[(-21 + 3*r5 - 7*r33 + 3*r165)/48,(-7*r3 - 21*r11 - 3*r15 - 3*r55)/48,0],
[(21 + 3*r5 + 7*r33 + 3*r165)/48,(-7*r3 - 21*r11 + 3*r15 + 3*r55)/48,0],
[(-21 + 3*r5 - 14*r33)/48,-(7 + 3*r5 + 2*r165)/(16*r3),0],
[(-21 - 3*r5 - 14*r33)/48,-(-7 + 3*r5 + 2*r165)/(16*r3),0],
[(21 + 3*r5 + 14*r33)/48,(-7 + 3*r5 + 2*r165)/(16*r3),0],
[-((7 + r5)*(3 + r33))/32,-((-7 + 3*r5)*(r3 + r11))/32,0]]
g553={}

#Colorlists
listYellow=[4,6,5,10,11,12,15,17,18,21,25,26,35,80,85,86,101,104,118,121,129,131,134,138,148,157,161,
            165,168,172,178,180,183,185,191,197,202,201,209,214,211,218,217,223,221,228,225,226,227,
            232,230,231,239,236,243,244,248,249,253,256,255,258,260,264,265,274,273,272,278,275,284,
            286,287,288,293,290,296,295,304,309,307,312,314,318,322,321,323,324,328,331,330,335,346,
            350,357,362,364,370,378,379,381,383,390,392,396,401,414,426,425,434,439,449,453,459,463,
        475,484,488,489,491,492,495,511,514,517,521,524,529,533,532,530,537,540,545,548,546,552,551]
listRed=[2,1,9,7,13,14,19,22,29,33,30,37,42,53,55,64,74,73,78,79,84,89,94,99,103,110,115,119,124,125,
         126,132,141,140,143,151,152,159,171,173,174,175,176,179,181,188,194,195,196,199,205,207,208,
         212,216,224,220,229,234,237,238,242,240,246,245,251,257,259,263,266,268,276,277,279,281,280,
         282,285,289,292,298,297,301,303,306,305,313,319,320,329,339,337,351,356,361,368,373,372,374,
         377,380,384,388,387,394,398,397,395,402,403,407,413,419,428,427,430,433,438,436,446,450,451,
         455,456,460,466,473,474,478,490,494,498,510,513,522,526,531,538,541,542,]
listBlue=[24,27,28,31,36,38,43,44,41,48,45,51,57,58,56,59,62,63,65,66,67,72,75,76,83,91,93,95,96,98,
          100,105,107,109,113,116,122,123,127,133,139,137,144,142,145,146,154,153,160,163,164,166,
          177,186,187,192,198,203,200,210,213,241,250,267,269,271,294,300,302,308,315,317,326,334,
          336,343,341,344,345,348,358,367,366,369,365,371,376,375,382,386,391,399,405,406,410,412,
          418,422,424,421,429,431,432,435,437,442,440,441,445,454,458,461,465,468,467,471,472,479,
          477,482,481,485,493,497,496,500,504,507,508,509,506,512,516,515,519,528,536,550,]
listGreen=[3,8,16,20,23,32,34,39,40,46,49,47,54,52,50,61,60,68,69,70,71,77,82,81,88,87,90,92,97,102,
           106,108,112,111,114,117,120,128,130,135,136,149,147,150,155,156,158,162,169,167,170,182,
           184,189,190,193,204,206,219,215,222,233,235,247,252,254,262,261,270,283,291,299,310,311,
           316,327,325,333,332,338,340,342,349,347,354,352,353,359,355,360,363,385,389,393,404,400,
           409,408,411,416,415,417,423,420,443,444,447,448,452,457,462,464,469,470,476,483,480,487,
           486,499,501,502,503,505,518,520,523,527,525,534,535,539,544,543,547,549,]

for i in range(len(h553pre)):
    connectedVertices=[]
    for k in range(i,len(h553pre)):
        d=distance.euclidean(h553pre[i], h553pre[k])
        #print(d)
        if d>0.9999999 and d<1.0000001:
            connectedVertices.append(k)
    if i in   listYellow:
        color=cYellowMS
        
    elif i in listRed:
        color=cRedMS
        
    elif i in listGreen:
        color=cGreenMS
        
    elif i in listBlue:
        color=cBlueMS
    else:
        color=cWhiteMS
    g553[i]=[h553pre[i],connectedVertices,color]# This finally assembles the graph base data
H553=Graph(g553,lineConfig553).returnVGroup()
H553Vert=Graph(g553,lineConfig553).returnVertices()

#Here we make the separate vertices available by color
arr=[]
for i in listYellow:
    arr.append(H553Vert[i])
H553Y=VGroup(*arr)
arr=[]
for i in listRed:
    arr.append(H553Vert[i])
H553R=VGroup(*arr)
arr=[]
for i in listBlue:
    arr.append(H553Vert[i])
H553B=VGroup(*arr)
arr=[]
for i in listGreen:
    arr.append(H553Vert[i])
H553G=VGroup(*arr)
