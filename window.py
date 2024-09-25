import glfw
from OpenGL.GL import *
def drawWindow():
    #Initilise GLFW and Window
    if not glfw.init():
        print("Failed to initialise GLFW")
        raise Exception("GLFW could not be initialised")
    window = glfw.create_window(600,600,"Track Sim",None,None) #Parameters: lxw,title,fullscreen?,share_resources?
    cursor = glfw.create_standard_cursor(glfw.HRESIZE_CURSOR) #create cursor
    cursor_in_bounds = CursorInBounds()
    if not window:
        glfw.terminate()
        print("Window can't be created")
        exit()

    glfw.make_context_current(window) #OpenGL can use this now
    glClearColor(1,1,1,1)
    glViewport(0,0,600,600)

    glfw.set_cursor_enter_callback(window,cursor_in_bounds.cursorCallback)
    glfw.set_mouse_button_callback(window,drawPoint)

    #Loop window
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        # if(cursor_in_bounds.cursor_in_bounds==True):
        #     print("y")
        glfw.poll_events() #Input
        glfw.swap_buffers(window) #Prevents flickering
    #Close on exit
    glfw.terminate()
    glfw.destroy_cursor()
class CursorInBounds:
    def __init__(self):
        self.cursor_in_bounds=False
    def cursorCallback(self,window,entered): #If cursor on screen
        if(entered):
            self.cursor_in_bounds=True
        else:
            self.cursor_in_bounds=False

def drawPoint(window,button,action,mods):
    if(button==glfw.MOUSE_BUTTON_LEFT and action==glfw.PRESS):
        print("point")