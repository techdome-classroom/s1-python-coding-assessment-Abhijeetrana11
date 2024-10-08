def decode_message(s: str, p: str) -> bool:
  
    
    def match(i, j):
        # i: index for s, j: index for p
        
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False
        if i == len(s):
            return p[j] == '*' and match(i, j + 1)
        
        if p[j] == '?' or s[i] == p[j]:
            return match(i + 1, j + 1)
        elif p[j] == '*':
            return match(i + 1, j) or match(i, j + 1)
        
        return False
    
    return match(0, 0)