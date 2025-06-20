g=2.5
print('outside-1:',g)
def fun():
    global g
    a=10
    g=199
    print('local:',a)
    print('global:',g)

fun()
print('outside:',g)
