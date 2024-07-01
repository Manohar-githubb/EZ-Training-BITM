#using KMP Algorithm....

def kmp(p, s):
    m = len(p)
    n = len(s)
    lps = [0] * m
    computeLPSArray(p, m, lps)
    print(lps)
    i = 0  
    j = 0  
    while i < n:
        if p[j] == s[i]:
            i += 1
            j += 1
        
        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        
        elif i < n and p[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def computeLPSArray(p, m, lps):
    length = 0  
    lps[0] = 0  
    i = 1
    
    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

if __name__ == "__main__":
    s = "ABABACDEABABABCABCABCABDAA"
    p = "ABCAB"
    kmp(p, s)