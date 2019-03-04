def grayscale(img,h,w):
    import numpy as np
    
    img2=np.zeros((w,h,1),np.uint8)
    for i in range(0,h):
        for j in range(0,w):
            img2[j,i]=int(0.07*img[i,j][2]+0.72*img[i,j][1]+0.21*img[i,j][0])
    return img2
    
    
