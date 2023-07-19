for k in range(31,101):    
    s='7'*k    
    while '777' in s:    
        s=s.replace('777','1',1)    
        s=s.replace('111','7',1)    
    if s=='17':    
        print(k)    
        break    


