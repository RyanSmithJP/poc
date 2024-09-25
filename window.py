import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
def drawWindow():
    #Initilise GLFW and Window
    if not glfw.init():
        print("Failed to initialise GLFW")
        raise Exception("GLFW could not be initialised")
    window = glfw.create_window(600,600,"Track Sim",None,None) #Parameters: lxw,title,fullscreen?,share_resources?
    point_size = 20
    myCursor = MyCursor(point_size)
    if not window:
        glfw.terminate()
        print("Window can't be created")
        exit()

    def onInit():
        glfw.make_context_current(window) #OpenGL can use this now
        glClearColor(1,1,1,1)
        glViewport(0,0,600,600)
        glMatrixMode(GL_PROJECTION) #2D axis
        glLoadIdentity()
        gluOrtho2D(0, 600, 600, 0)  #Set up a 2D orthographic projection for drawing points
        glColor3f(1,0,0)
        glPointSize(point_size)
        glEnable(GL_POINT_SMOOTH) #Circle points

        glLineWidth(5.0)

        glfw.set_cursor_enter_callback(window,myCursor.cursorCallback)
        glfw.set_cursor_pos_callback(window,myCursor.cursorPosCallback)
        glfw.set_mouse_button_callback(window,myCursor.drawPoint)

    onInit()
    #Loop window
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #Clear window
        # if(myCursor.myCursor==True):
        #     print("y")
        #Draw points then lines
        lastPoint = None
        glBegin(GL_POINTS)
        for i in myCursor.points:
            glVertex2f(i[0],i[1])
        glEnd()
        glBegin(GL_LINES)
        for i in myCursor.points:
            if lastPoint:
                glVertex2f(lastPoint[0],lastPoint[1])
                glVertex2f(i[0],i[1])
            lastPoint = i
        if(myCursor.complete_track==True):
            glVertex2f(myCursor.points[-1][0],myCursor.points[-1][1]) #most recent point
            glVertex2f(myCursor.points[0][0],myCursor.points[0][1]) #connected to starting point
        glEnd()
        glfw.poll_events() #Input
        glfw.swap_buffers(window) #Prevents flickering
    #Close on exit
    glfw.terminate()
class MyCursor:
    def __init__(self,point_size):
        self.myCursor=False
        self.xpos = 0
        self.ypos = 0
        self.points = [] #List of co-ords
        self.point_size = point_size
        self.complete_track = False
    def cursorCallback(self,window,entered): #If cursor on screen
        if(entered):
            self.myCursor=True
        else:
            self.myCursor=False
    def cursorPosCallback(self,window,x,y):
        self.xpos=x
        self.ypos=y
    def drawPoint(self,window,button,action,mods):
        #if pressed on first point, complete track
        if(button==glfw.MOUSE_BUTTON_LEFT 
        and len(self.points)>0 
        and self.xpos >= (self.points[0][0] -self.point_size/2) and self.xpos <= (self.points[0][0] + self.point_size/2) 
        and self.ypos >= (self.points[0][1] -self.point_size/2) and self.ypos <= (self.points[0][1] + self.point_size/2)
        and action==glfw.PRESS):
            self.complete_track = True
        #else add to list
        elif(self.complete_track==False and button==glfw.MOUSE_BUTTON_LEFT and action==glfw.PRESS):
            print(self.xpos," ",self.ypos)
            glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #Clear window
            self.points.append((self.xpos,self.ypos))
            # if(myCursor.myCursor==True):
            #     print("y")