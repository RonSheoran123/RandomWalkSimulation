def random_walk(p_up,p_down,start,size):
    #p_up+p_down==1
    W=np.zeros(size)
    W[0]=start
    rr=np.random.random(size)
    for i in range(size-1):
        if rr[i]<p_up:
            W[i+1]=W[i]+1
        else:
            W[i+1]=W[i]-1
    return W
