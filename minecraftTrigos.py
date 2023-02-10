import math
print('set defualt blocks travleend (recomended 20)')
blocks = input()
while True:
    for x in range(0, 999):
        print('enter degree:')
        degree = input()
        final = float(blocks)/(math.cos(float(degree) * math.pi/180))
        
        print(str('about ') + str(final) + str(' blocks away from the end portal.'))
