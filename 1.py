s='а'*80    
while 'ааа' in s or 'ддд' in s:    
    if 'ддд' in s:    
        s=s.replace('ддд','а',1)    
    else:
        s=s.replace('ааа','д',1)
print(s)    
            




