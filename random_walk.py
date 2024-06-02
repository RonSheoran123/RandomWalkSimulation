def random_walk(p_up,p_down,start,size):
    #p_up+p_down==1
    rr=np.random.random(size)
    positions=[start]
    for i in range(len(rr)):
        if rr[i]<p_up:
            positions.append(positions[i]+1)
        else:
            positions.append(positions[i]-1)
    return positions
