

def get_zones(A):
    rdl = int(((A*A)/20)**0.5)
    rll = A-int(A/3)
    rcl = int(A/3)
    RD = ((0,rdl),(0,rdl))
    RL = ((0,rll),(A-1,A-1))
    RC = ((rcl,rcl),(2*rcl,2*rcl))
    
