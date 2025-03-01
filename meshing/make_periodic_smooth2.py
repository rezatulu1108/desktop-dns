import numpy as np

def make_periodic_smooth2(blk,next_block,next_patch,nbnow,pitch):
    ng=1
    up = {}
    dn = {}
    
    f1 = 0.5 #16.0/30.0
    f2 = 0.0 #-1.0/30.0
    f0 = 0.95
    f1 = f1*(1.0-f0)
    f2 = f2*(1.0-f0)
    
    ib=nbnow
    im_next_block=next_block[ib]['im']
    ip_next_block=next_block[ib]['ip']
    jm_next_block=next_block[ib]['jm']
    jp_next_block=next_block[ib]['jp']
    im_next_patch=next_patch[ib]['im']
    ip_next_patch=next_patch[ib]['ip']
    jm_next_patch=next_patch[ib]['jm']
    jp_next_patch=next_patch[ib]['jp']

    if (im_next_block != 0):
        if (im_next_patch == 1):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset = pitch
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[im_next_block]['x'][1,:]
            yup=blk[im_next_block]['y'][1,:] + yoffset
            xup2=blk[im_next_block]['x'][2,:]
            yup2=blk[im_next_block]['y'][2,:] + yoffset
            
            xnow = blk[ib]['x'][0,:]
            ynow = blk[ib]['y'][0,:]

            blk[ib]['x'][0,:]= xnow*f0 + \
            (xup + blk[ib]['x'][1,:])*f1+(xup2 + blk[ib]['x'][2,:])*f2 
            blk[ib]['y'][0,:]= ynow*f0 + \
            (yup + blk[ib]['y'][1,:])*f1+(yup2 + blk[ib]['y'][2,:])*f2 
            
            blk[im_next_block]['x'][0,:]=blk[ib]['x'][0,:]
            blk[im_next_block]['y'][0,:]=blk[ib]['y'][0,:] - yoffset
            
        if (im_next_patch == 2):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][-1,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][-1,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[im_next_block]['x'][-2,:]
            yup=blk[im_next_block]['y'][-2,:] + yoffset
            xup2=blk[im_next_block]['x'][-3,:]
            yup2=blk[im_next_block]['y'][-3,:] + yoffset
            
            xnow = blk[ib]['x'][0,:]
            ynow = blk[ib]['y'][0,:]

            blk[ib]['x'][0,:]= xnow*f0 + \
            (xup + blk[ib]['x'][1,:])*f1+(xup2 + blk[ib]['x'][2,:])*f2 
            blk[ib]['y'][0,:]= ynow*f0 + \
            (yup + blk[ib]['y'][1,:])*f1+(yup2 + blk[ib]['y'][2,:])*f2 

            blk[im_next_block]['x'][-1,:]=blk[ib]['x'][0,:]
            blk[im_next_block]['y'][-1,:]=blk[ib]['y'][0,:] - yoffset
            
        if (im_next_patch == 3):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[im_next_block]['x'][:,1])
            yup=np.transpose(blk[im_next_block]['y'][:,1]) + yoffset
            
            xup2=np.transpose(blk[im_next_block]['x'][:,2])
            yup2=np.transpose(blk[im_next_block]['y'][:,2]) + yoffset
            
            xnow = blk[ib]['x'][0,:]
            ynow = blk[ib]['y'][0,:]

            blk[ib]['x'][0,:]= xnow*f0 + \
            (xup + blk[ib]['x'][1,:])*f1+(xup2 + blk[ib]['x'][2,:])*f2 
            blk[ib]['y'][0,:]= ynow*f0 + \
            (yup + blk[ib]['y'][1,:])*f1+(yup2 + blk[ib]['y'][2,:])*f2 
            
            blk[im_next_block]['x'][:,0]=np.transpose(blk[ib]['x'][0,:])
            blk[im_next_block]['y'][:,0]=np.transpose(blk[ib]['y'][0,:]) - yoffset
            
        if (im_next_patch == 4):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,-1]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[im_next_block]['y'][0,-1]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[im_next_block]['x'][:,-2])
            yup=np.transpose(blk[im_next_block]['y'][:,-2]) + yoffset
            
            xup2=np.transpose(blk[im_next_block]['x'][:,-3])
            yup2=np.transpose(blk[im_next_block]['y'][:,-3]) + yoffset
            
            xnow = blk[ib]['x'][0,:]
            ynow = blk[ib]['y'][0,:]

            blk[ib]['x'][0,:]= xnow*f0 + \
            (xup + blk[ib]['x'][1,:])*f1+(xup2 + blk[ib]['x'][2,:])*f2 
            blk[ib]['y'][0,:]= ynow*f0 + \
            (yup + blk[ib]['y'][1,:])*f1+(yup2 + blk[ib]['y'][2,:])*f2 
            
            blk[im_next_block]['x'][:,-1]=np.transpose(blk[ib]['x'][0,:])
            blk[im_next_block]['y'][:,-1]=np.transpose(blk[ib]['y'][0,:]) - yoffset
    
    if (ip_next_block != 0):
        if (ip_next_patch == 1):
            yoffset=0.0
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset = pitch
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[ip_next_block]['x'][1,:]
            yup=blk[ip_next_block]['y'][1,:] + yoffset

            xup2=blk[ip_next_block]['x'][2,:]
            yup2=blk[ip_next_block]['y'][2,:] + yoffset
            
            xnow = blk[ib]['x'][-1,:]
            ynow = blk[ib]['y'][-1,:]

            blk[ib]['x'][-1,:]= xnow*f0 + \
            (xup + blk[ib]['x'][-2,:])*f1+(xup2 + blk[ib]['x'][-3,:])*f2 
            blk[ib]['y'][-1,:]= ynow*f0 + \
            (yup + blk[ib]['y'][-2,:])*f1+(yup2 + blk[ib]['y'][-3,:])*f2 

            blk[ip_next_block]['x'][0,:]=blk[ib]['x'][-1,:]
            blk[ip_next_block]['y'][0,:]=blk[ib]['y'][-1,:] - yoffset
            
        if (ip_next_patch == 2):
            yoffset=0.0
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][-1,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][-1,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[ip_next_block]['x'][-2,:]
            yup=blk[ip_next_block]['y'][-2,:] + yoffset
            xup2=blk[ip_next_block]['x'][-3,:]
            yup2=blk[ip_next_block]['y'][-3,:] + yoffset

            xnow = blk[ib]['x'][-1,:]
            ynow = blk[ib]['y'][-1,:]

            blk[ib]['x'][-1,:]= xnow*f0 + \
            (xup + blk[ib]['x'][-2,:])*f1+(xup2 + blk[ib]['x'][-3,:])*f2 
            blk[ib]['y'][-1,:]= ynow*f0 + \
            (yup + blk[ib]['y'][-2,:])*f1+(yup2 + blk[ib]['y'][-3,:])*f2 

            blk[ip_next_block]['x'][-1,:]=blk[ib]['x'][-1,:]
            blk[ip_next_block]['y'][-1,:]=blk[ib]['y'][-1,:] - yoffset
            
        if (ip_next_patch == 3):
            yoffset=0.0
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[ip_next_block]['x'][:,1])
            yup=np.transpose(blk[ip_next_block]['y'][:,1]) + yoffset
            xup2=np.transpose(blk[ip_next_block]['x'][:,2])
            yup2=np.transpose(blk[ip_next_block]['y'][:,2]) + yoffset

            xnow = blk[ib]['x'][-1,:]
            ynow = blk[ib]['y'][-1,:]

            blk[ib]['x'][-1,:]= xnow*f0 + \
            (xup + blk[ib]['x'][-2,:])*f1+(xup2 + blk[ib]['x'][-3,:])*f2 
            blk[ib]['y'][-1,:]= ynow*f0 + \
            (yup + blk[ib]['y'][-2,:])*f1+(yup2 + blk[ib]['y'][-3,:])*f2 

            blk[ip_next_block]['x'][:,0]=np.transpose(blk[ib]['x'][-1,:])
            blk[ip_next_block]['y'][:,0]=np.transpose(blk[ib]['y'][-1,:]) - yoffset
            
        if (ip_next_patch == 4):
            yoffset=0.0
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,-1]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][-1,0] - blk[ip_next_block]['y'][0,-1]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[ip_next_block]['x'][:,-2])
            yup=np.transpose(blk[ip_next_block]['y'][:,-2]) + yoffset
            xup2=np.transpose(blk[ip_next_block]['x'][:,-3])
            yup2=np.transpose(blk[ip_next_block]['y'][:,-3]) + yoffset

            xnow = blk[ib]['x'][-1,:]
            ynow = blk[ib]['y'][-1,:]

            blk[ib]['x'][-1,:]= xnow*f0 + \
            (xup + blk[ib]['x'][-2,:])*f1+(xup2 + blk[ib]['x'][-3,:])*f2 
            blk[ib]['y'][-1,:]= ynow*f0 + \
            (yup + blk[ib]['y'][-2,:])*f1+(yup2 + blk[ib]['y'][-3,:])*f2 

            blk[ip_next_block]['x'][:,-1]=np.transpose(blk[ib]['x'][-1,:])
            blk[ip_next_block]['y'][:,-1]=np.transpose(blk[ib]['y'][-1,:]) - yoffset
    
    if (jm_next_block != 0):
        if (jm_next_patch == 1):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset = pitch
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[jm_next_block]['x'][1,:])
            yup=np.transpose(blk[jm_next_block]['y'][1,:]) + yoffset
            xup2=np.transpose(blk[jm_next_block]['x'][2,:])
            yup2=np.transpose(blk[jm_next_block]['y'][2,:]) + yoffset

            xnow = blk[ib]['x'][:,0]
            ynow = blk[ib]['y'][:,0]

            blk[ib]['x'][:,0]= xnow*f0 + \
            (xup + blk[ib]['x'][:,1])*f1+(xup2 + blk[ib]['x'][:,2])*f2 
            blk[ib]['y'][:,0]= ynow*f0 + \
            (yup + blk[ib]['y'][:,1])*f1+(yup2 + blk[ib]['y'][:,2])*f2 

            
            blk[jm_next_block]['x'][0,:]=np.transpose(blk[ib]['x'][:,0])
            blk[jm_next_block]['y'][0,:]=np.transpose(blk[ib]['y'][:,0]) - yoffset
            
        if (jm_next_patch == 2):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][-1,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][-1,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[jm_next_block]['x'][-2,:])
            yup=np.transpose(blk[jm_next_block]['y'][-2,:]) + yoffset
            xup2=np.transpose(blk[jm_next_block]['x'][-3,:])
            yup2=np.transpose(blk[jm_next_block]['y'][-3,:]) + yoffset

            xnow = blk[ib]['x'][:,0]
            ynow = blk[ib]['y'][:,0]

            blk[ib]['x'][:,0]= xnow*f0 + \
            (xup + blk[ib]['x'][:,1])*f1+(xup2 + blk[ib]['x'][:,2])*f2 
            blk[ib]['y'][:,0]= ynow*f0 + \
            (yup + blk[ib]['y'][:,1])*f1+(yup2 + blk[ib]['y'][:,2])*f2 
            
            blk[jm_next_block]['x'][-1,:]=np.transpose(blk[ib]['x'][:,0])
            blk[jm_next_block]['y'][-1,:]=np.transpose(blk[ib]['y'][:,0]) - yoffset
            
        if (jm_next_patch == 3):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[jm_next_block]['x'][:,1]
            yup=blk[jm_next_block]['y'][:,1] + yoffset
            xup2=blk[jm_next_block]['x'][:,2]
            yup2=blk[jm_next_block]['y'][:,2] + yoffset

            xnow = blk[ib]['x'][:,0]
            ynow = blk[ib]['y'][:,0]

            blk[ib]['x'][:,0]= xnow*f0 + \
            (xup + blk[ib]['x'][:,1])*f1+(xup2 + blk[ib]['x'][:,2])*f2 
            blk[ib]['y'][:,0]= ynow*f0 + \
            (yup + blk[ib]['y'][:,1])*f1+(yup2 + blk[ib]['y'][:,2])*f2 

            blk[jm_next_block]['x'][:,0]=blk[ib]['x'][:,0]
            blk[jm_next_block]['y'][:,0]=blk[ib]['y'][:,0] - yoffset
            
        if (jm_next_patch == 4):
            yoffset=0.0
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,-1]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,0] - blk[jm_next_block]['y'][0,-1]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[jm_next_block]['x'][:,-2]
            yup=blk[jm_next_block]['y'][:,-2] + yoffset
            xup2=blk[jm_next_block]['x'][:,-3]
            yup2=blk[jm_next_block]['y'][:,-3] + yoffset

            xnow = blk[ib]['x'][:,0]
            ynow = blk[ib]['y'][:,0]

            blk[ib]['x'][:,0]= xnow*f0 + \
            (xup + blk[ib]['x'][:,1])*f1+(xup2 + blk[ib]['x'][:,2])*f2 
            blk[ib]['y'][:,0]= ynow*f0 + \
            (yup + blk[ib]['y'][:,1])*f1+(yup2 + blk[ib]['y'][:,2])*f2 

            blk[jm_next_block]['x'][:,-1]=blk[ib]['x'][:,0]
            blk[jm_next_block]['y'][:,-1]=blk[ib]['y'][:,0] - yoffset
    
    if (jp_next_block != 0):
        if (jp_next_patch == 1):
            yoffset=0.0
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset = pitch
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[jp_next_block]['x'][1,:])
            yup=np.transpose(blk[jp_next_block]['y'][1,:]) + yoffset
            xup2=np.transpose(blk[jp_next_block]['x'][2,:])
            yup2=np.transpose(blk[jp_next_block]['y'][2,:]) + yoffset

            xnow = blk[ib]['x'][:,-1]
            ynow = blk[ib]['y'][:,-1]

            blk[ib]['x'][:,-1]= xnow*f0 + \
            (xup + blk[ib]['x'][:,-2])*f1+(xup2 + blk[ib]['x'][:,-3])*f2 
            blk[ib]['y'][:,-1]= ynow*f0 + \
            (yup + blk[ib]['y'][:,-2])*f1+(yup2 + blk[ib]['y'][:,-3])*f2 

            blk[jp_next_block]['x'][0,:]=np.transpose(blk[ib]['x'][:,-1])
            blk[jp_next_block]['y'][0,:]=np.transpose(blk[ib]['y'][:,-1]) - yoffset
            
        if (jp_next_patch == 2):
            yoffset=0.0
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][-1,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][-1,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=np.transpose(blk[jp_next_block]['x'][-2,:])
            yup=np.transpose(blk[jp_next_block]['y'][-2,:]) + yoffset
            xup2=np.transpose(blk[jp_next_block]['x'][-3,:])
            yup2=np.transpose(blk[jp_next_block]['y'][-3,:]) + yoffset

            xnow = blk[ib]['x'][:,-1]
            ynow = blk[ib]['y'][:,-1]

            blk[ib]['x'][:,-1]= xnow*f0 + \
            (xup + blk[ib]['x'][:,-2])*f1+(xup2 + blk[ib]['x'][:,-3])*f2 
            blk[ib]['y'][:,-1]= ynow*f0 + \
            (yup + blk[ib]['y'][:,-2])*f1+(yup2 + blk[ib]['y'][:,-3])*f2 

            blk[jp_next_block]['x'][-1,:]=np.transpose(blk[ib]['x'][:,-1])
            blk[jp_next_block]['y'][-1,:]=np.transpose(blk[ib]['y'][:,-1]) - yoffset
            
        if (jp_next_patch == 3):
            yoffset=0.0
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,0]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,0]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[jp_next_block]['x'][:,1]
            yup=blk[jp_next_block]['y'][:,1] + yoffset           
            xup2=blk[jp_next_block]['x'][:,2]
            yup2=blk[jp_next_block]['y'][:,2] + yoffset

            xnow = blk[ib]['x'][:,-1]
            ynow = blk[ib]['y'][:,-1]

            blk[ib]['x'][:,-1]= xnow*f0 + \
            (xup + blk[ib]['x'][:,-2])*f1+(xup2 + blk[ib]['x'][:,-3])*f2 
            blk[ib]['y'][:,-1]= ynow*f0 + \
            (yup + blk[ib]['y'][:,-2])*f1+(yup2 + blk[ib]['y'][:,-3])*f2 

            blk[jp_next_block]['x'][:,0]=blk[ib]['x'][:,-1]
            blk[jp_next_block]['y'][:,0]=blk[ib]['y'][:,-1] - yoffset
            
        if (jp_next_patch == 4):
            yoffset=0.0
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,-1]) > 0.1*pitch):
                yoffset=pitch
            if ((blk[ib]['y'][0,-1] - blk[jp_next_block]['y'][0,-1]) < -0.1*pitch):
                yoffset=- pitch
            xup=blk[jp_next_block]['x'][:,-2]
            yup=blk[jp_next_block]['y'][:,-2] + yoffset
            xup2=blk[jp_next_block]['x'][:,-3]
            yup2=blk[jp_next_block]['y'][:,-3] + yoffset

            xnow = blk[ib]['x'][:,-1]
            ynow = blk[ib]['y'][:,-1]

            blk[ib]['x'][:,-1]= xnow*f0 + \
            (xup + blk[ib]['x'][:,-2])*f1+(xup2 + blk[ib]['x'][:,-3])*f2 
            blk[ib]['y'][:,-1]= ynow*f0 + \
            (yup + blk[ib]['y'][:,-2])*f1+(yup2 + blk[ib]['y'][:,-3])*f2 
            
            blk[jp_next_block]['x'][:,-1]=blk[ib]['x'][:,-1]
            blk[jp_next_block]['y'][:,-1]=blk[ib]['y'][:,-1] - yoffset
            
    return blk