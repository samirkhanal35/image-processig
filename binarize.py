def binarize(img,h,w):
    import numpy as np
    img2=np.zeros((h,w,1),np.uint8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            gray=img[i,j]
            if gray<=128:
                img2[i,j]=0
            else:
                img2[i,j]=255
    return img2
        
