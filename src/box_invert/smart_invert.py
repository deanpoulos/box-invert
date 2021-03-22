from box_invert import *
import box_invert.mouse_callback as mouse
from box_invert.inversion_filter import apply
from box_invert.find_contours import paint_contours

src = cv2.imread(sys.argv[1])

mouse.img = np.ones((src.shape[0], src.shape[1])) * 255

cv2.namedWindow('image')

def create_trackbars():
    # create empty function for trackbar callback
    def nothing(x): 
        pass

    # create trackbars for parameter change
    cv2.createTrackbar(B,'image',108,255,nothing)
    cv2.createTrackbar(W,'image',190,255,nothing)
    cv2.createTrackbar(K,'image',3,10,nothing)
    cv2.createTrackbar(C,'image',0,1,nothing)
    cv2.createTrackbar(T,'image',0,255,nothing)
    cv2.createTrackbar(I,'image',0,1,nothing)

create_trackbars()

cv2.setMouseCallback('image', mouse.draw_circle)

while(1):
    # apply filter to image and show
    img = apply(src, mouse.img)
    if cv2.getTrackbarPos(C, 'image') == 1:
        paint_contours(img)
    if cv2.getTrackbarPos(I, 'image') == 1:
        img = 255 - img

    cv2.imshow('image',img)

    # wait for user-exit
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'): 
        mode = not mode
    elif k == 27: 
        break

cv2.destroyAllWindows()