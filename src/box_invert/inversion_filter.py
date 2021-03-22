from box_invert import *

def apply(src, inversion_mask=None):
    """
    Apply a clean inversion of white and black image elements, with exception
    of regions defined in the inversion mask.

    """
    res = src.copy()

    b = cv2.getTrackbarPos(B,'image')
    w = cv2.getTrackbarPos(W,'image')
    k = cv2.getTrackbarPos(K,'image')

    # select black and white elements
    mask_b_txt = 255 - cv2.threshold(res, b, 255, cv2.THRESH_BINARY)[1][:,:,0] 
    mask_w_txt = cv2.threshold(res, w, 255, cv2.THRESH_BINARY)[1][:,:,0] 

    # create mask for black and white elmements
    mask = (np.logical_or(mask_b_txt==255, mask_w_txt==255) * 255)

    # if "closing" morphological filter kernel-size is non-zero
    if k != 0:
        # apply filter to close out small noise features in mask
        kernel = np.ones((k,k),np.uint8)
        mask = cv2.dilate(mask.astype(np.uint8),kernel,iterations = 1)
        mask = cv2.erode(mask.astype(np.uint8),kernel,iterations = 1)

    # remove user-drawn regions from mask
    if type(inversion_mask) != type(None):
        mask = np.logical_and(mask==255, inversion_mask==255) * 255

    # invert image where mask is defined
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            res[i][j] = 255 - res[i][j] if mask[i][j] else res[i][j]

    return res
