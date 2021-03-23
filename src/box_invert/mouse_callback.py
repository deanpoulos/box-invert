from box_invert import *
from box_invert.find_contours import paint_contours, get_contours

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
img = None

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img

    if event == cv2.EVENT_LBUTTONDOWN and flags == cv2.EVENT_FLAG_SHIFTKEY+1:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP and flags == cv2.EVENT_FLAG_SHIFTKEY+1:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
        else:
            cv2.circle(img,(x,y),5,(255,255,255),-1)


    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,0,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,0),-1)

    elif event == cv2.EVENT_MBUTTONDOWN:
        ix,iy = x,y

    elif event == cv2.EVENT_MBUTTONUP:
        from box_invert import smart_invert
        curr_img = smart_invert.img.copy().astype(np.uint8)
        mask = np.zeros(curr_img.shape).astype(np.uint8)
        masked_img = np.zeros(curr_img.shape).astype(np.uint8)
        cv2.rectangle(mask,(ix,iy),(x,y),(255,255,255),-1)
        for i in range(curr_img.shape[0]):
            for j in range(curr_img.shape[1]):
                if mask[i][j][2] == 255: masked_img[i][j] = curr_img[i][j]
                
        contours = get_contours(masked_img)
        cv2.fillPoly(img, pts =contours, color=(0,0,0))
