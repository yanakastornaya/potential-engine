for k in range(0,1000+1): 
    s='#'+'2'*20+'5'*k+'9'*16    
    while '#2' in s or '#5' in s or '#9' in s:    
        if '#2' in s:   
            s=s.replace('#2','55#',1)    
        if '#5' in s:
            s=s.replace('#5','5#',1)
        if '#9' in s:
            s=s.replace('#9','2#',1)
    summ=s.count('2')*2+s.count('5')*5+s.count('9')*9    
    if summ>2013:    
        print(k)    
        break    
   
