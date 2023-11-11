str1 = open('k1.txt', 'r').read()
str2 = open('k2.txt', 'r').read()

durma = ["ve","veya","ile","çünkü","birkaç","böyle","falan","herkes","hiçbiri",
         "gibi","hangi","kim","şu","şey","yada","zira","zaten","yine","neyse",
         "ama","ancak","asla","az","bazı","bazısı","belki","birçok","çok","çoğu",
         "daha","değil","diğer","elbette","hiç","ise","kendi","kime","niye","önce",
         "ötürü","rağmen","şunu","şunlar","tümü","veya","yoksa","zaten","zira"]

for i in durma:
    str1 = str1.replace(i,"")
    str2 = str2.replace(i,"")

a1 = list(str1.split(" "))
print(a1)
print(len(a1))

a2 = list(str2.split(" "))
print(a2)
print(len(a2))

s1 = set(a1)
print(s1)
print(len(s1))

s2 = set(a2)
print(s2)
print(len(s2))

str = set.union(s1,s2)
print(str)
print(len(str))

fb = len(s1)+len(s2)
print("İki metin için tekil sözcük sayısı = ", fb)
ka = len(str)
print("Birleşim sonrası tekil sözcük sayısı = ", ka)
fark = fb - ka
print("Fark = ", fark)
benzeme = (fark*100)/ka
print("Benzeme oranı = %",benzeme)

