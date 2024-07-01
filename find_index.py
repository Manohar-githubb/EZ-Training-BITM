# s="ABABABCANFKABABCNKABABCACNDA"
s="ABABACDEABABABCABCABCABDAA"
# p="ABABCA"
p="ABCAB"
index=[]
for i in range(len(s)-len(p)):
    if s[i:i+len(p)]==p:
        index.append(i)
print(index)