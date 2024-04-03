def runner_up(a,b,c,d,e):
    pelari_tercepat = min(a,b,c,d,e)
    
    if pelari_tercepat == a:
        runner_up = min(b,c,d,e)
    elif pelari_tercepat == b:
        runner_up = min(a,c,d,e)
    elif pelari_tercepat == c:
        runner_up = min(a,b,d,e)
    elif pelari_tercepat == d:
        runner_up = min(a,b,c,e)
    elif pelari_tercepat == e:
        runner_up = min(a,b,c,d)
    
    return runner_up

runner_up(9.5,8.5,7.5,10,11)