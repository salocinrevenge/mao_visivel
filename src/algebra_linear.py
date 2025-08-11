def toIsometric(x,y):
    return (x+y, (x-y)/2)

def fromIsometric(x,y):
    return ((2*y + x)/2, -(2*y - x)/2) # adicionei o menos ao resolver as contas