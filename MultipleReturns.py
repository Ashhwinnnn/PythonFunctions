def result(mrk1,mrk2,mrk3):
    total= mrk1+ mrk2+ mrk3
    average=total/3

    if average>=45:
        grade='pass'
    else:
        grade='fail'
    return total,average,grade
    
print(result(55,60,70))