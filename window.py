import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
def drawWindow():
    #Initilise GLFW and Window
    if not glfw.init():
        print("Failed to initialise GLFW")
        raise Exception("GLFW could not be initialised")
    window = glfw.create_window(600,600,"Track Sim",None,None) #Parameters: lxw,title,fullscreen?,share_resources?
    myCursor = MyCursor()
    if not window:
        glfw.terminate()
        print("Window can't be created")
        exit()

    glfw.make_context_current(window) #OpenGL can use this now
    glClearColor(1,1,1,1)
    glViewport(0,0,600,600)
    glMatrixMode(GL_PROJECTION) #2D axis
    glLoadIdentity()
    gluOrtho2D(0, 600, 600, 0)  #Set up a 2D orthographic projection for drawing points
    glColor3f(1,0,0)
    glPointSize(50.0)

    glfw.set_cursor_enter_callback(window,myCursor.cursorCallback)
    glfw.set_cursor_pos_callback(window,myCursor.cursorPosCallback)
    glfw.set_mouse_button_callback(window,myCursor.drawPoint)

    #Loop window
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #Clear window
        # if(myCursor.myCursor==True):
        #     print("y")
        glBegin(GL_POINTS)
        glVertex2f(25,25)
        glEnd()
        glfw.poll_events() #Input
        glfw.swap_buffers(window) #Prevents flickering
    #Close on exit
    glfw.terminate()
class MyCursor:
    def __init__(self):
        self.myCursor=False
        self.xpos = 0
        self.ypos = 0
    def cursorCallback(self,window,entered): #If cursor on screen
        if(entered):
            self.myCursor=True
        else:
            self.myCursor=False
    def cursorPosCallback(self,window,x,y):
        self.xpos=x
        self.ypos=y
    def drawPoint(self,window,button,action,mods):
        if(button==glfw.MOUSE_BUTTON_LEFT and action==glfw.PRESS):
            print(self.xpos," ",self.ypos)
            glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #Clear window
            # if(myCursor.myCursor==True):
            #     print("y")
            # glColor3f(1,0,0)
            # glBegin(GL_POINTS)
            # glVertex2f(100,50)
            # glEnd()