

i = 0
a = [1, 5, 7, 9, 4, 6]

def swap(a, c, d):
    a[c], a[d] = a[d], a[c]

while (i<len(a)-1):
    j = i + 1
    while (j<len(a)):
        if a[i] > a[j]:
            # a[i], a[j] = a[j], a[i]
            swap(a, i, j)
        j = j + 1
    i = i + 1
print(a)

# j = i + 1;
# while (j<len(a))
# if a[i]<a[j] then
# swap(a[i], a[j]);
# end if
# end while
# i = i + 1;
# end while
