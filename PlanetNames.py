def planet(id):
    planets={1:'Mercury',2:'Venus',3:'Earth',4:'Mars',5:'jupiter',6:'saturn',7:'uranus',8:'neptune',9:'pluto'}
    return planets[id]
id=int(input('Enter planet ID'))
p=planet(id)
print('planet name is:',p)