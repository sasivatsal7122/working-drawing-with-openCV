'''
 written by me obviously
 ignore all the typos, i'm half asleep coding
 and commenting  this
 (try xplaining ur code in comments u'll how understand how pain in the ass it is)
'''

import cv2
import numpy as np

'''declaring global variables'''

# by default darawing is set FALSE coz 
drawing = False # its True if mouse is pressed
# initial co-ords are set to -1 which is updated with
# new cursors values during func call
ix,iy = -1,-1
'''
 in this function user can draw circles by clicking left and
 right mouse button
'''
def drawing_with_mouse_click():
    # they are default paarmeters
    # must strictly be defined
    def draw_circle(event,x,y,flags,param):
        '''
        checking wether the user is pressing left-btn,if true
        drawing a green circle using cv2.circle func 
        '''
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img,(x,y),100,(0,255,0),-1)
            cv2.putText(img, 'lft-btn clicked',(x-90,y),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1,(0, 0, 0),1)
        # checking wether the user is pressing left-btn,if true
        # drawing a green circle using cv2.circle func 
        elif event == cv2.EVENT_RBUTTONDOWN:
            cv2.circle(img,(x,y),100,(0,0,255),-1)
            cv2.putText(img, 'rgt-btn clicked',(x-90,y),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1,(0, 0, 0),1)
    
    # Create a black image of size 800x1000
    # change arguments for desired size if wanted too
    '''
    3d - array created since opencv consider an image as 3 channels
    R and G and B
    assigning all zeros in 3 channels indicates a black image
    any color can created by understanding how color codes work
    in form of arrays
    try understanding that u r brain will collapse into a black hole..jk..
    '''
    img = np.zeros((800,1000,3), np.uint8)
    
    # This names the window so we can reference it 
    cv2.namedWindow(winname='opencv is hard af!')
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('opencv is hard af!',draw_circle)

    while True: #Runs forever until we break with Esc key on keyboard
        # Shows the image window
        cv2.imshow('opencv is hard af!',img)
        '''not sure '''
        if cv2.waitKey(20) & 0xFF == 27:
            break
    # Once script is done, It closes all windows 
    # not necessay just a fail safe method
    cv2.destroyAllWindows()

'''
 took me forever to make this thing work
'''

def drawing_with_mouse():
    def draw_rectangle(event,x,y,flags,param):
        # global variables declaration
        global ix,iy,drawing,mode  
        if event == cv2.EVENT_LBUTTONDOWN:
            # remember when we set darwing false
            # When you click DOWN with left mouse button drawing is set to True
            drawing = True
            # Then we take note of where that cursor pointer was located
            ix,iy = x,y
        # this is the crucial step, here we check wether the move is moving
        # if true recatngle is created/drawn whatever
        elif event == cv2.EVENT_MOUSEMOVE:
            # since mouse is moving drawing set to true
            if drawing == True:
                # If drawing is True, it means you've already clicked on the left mouse button
                # We draw a rectangle from the previous position to the x,y where the mouse 
                # here ix,iy are previously noted co-ords
                # and x,y are just noted co-ords where cursor is in real time
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        # checking wether mouse button if lifted up
        elif event == cv2.EVENT_LBUTTONUP:
            # Once you lift the mouse button, drawing is False
            drawing = False
            # rectangle is displayed 
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            
    # Creating a black image
    '''
    here np.uint8 is given as dtype coz
    color codes in format of arrays doesnt not contain/accept
    floating values which are created by np.array method (0.)
    by setting dtype=np.uint8 integers of 8 bits are created
    (ik confusing stuff..have to live with it if u wanna learn open cv)
    '''
    img = np.zeros((800,1000,3), np.uint8)
    # This names the window so we can reference it 
    cv2.namedWindow(winname='opencv is hard af!')
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('opencv is hard af!',draw_rectangle)
    while True: #Runs forever until we break with Esc key on keyboard
        # Shows the image window
        cv2.imshow('opencv is hard af!',img)
        ''' 
        i dont know what this '0xFF == 27' is,
        copied this from stackoverflow
        #he said when esc is pressed loop terminates '''
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # xplained it before
    cv2.destroyAllWindows()

# comment one function to test
if __name__=="__main__":
   drawing_with_mouse()
   #drawing_with_mouse_click()