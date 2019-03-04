def minfilter(img1,height,width):
    import numpy as np
    #import math
    a=0
    b=0
    q=[]
    img2=np.zeros((height,width,1),np.uint8)
    #img2=img1
    for d in range(1):

        for h in range(3,height,+3):
            for w in range(3,width,+3):
                q=[]
                for i in range(a,h):
                    for j in range(b,w):
                        q=[img1[i,j],img1[i,j-1],img1[i,j+1],img1[i-1,j],img1[i-1,j-1],img1[i-1,j+1],img1[i+1,j],img1[i+1,j+1],img1[i+1,j-1]]
                        img2[i,j]=int(min(q))
                
                b=w
            a=h		
    return img2
        

