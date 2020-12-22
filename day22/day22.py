p1='''9
2
6
3
1'''.splitlines()

p2='''5
8
4
7
10'''.splitlines()


p1 = '''4
14
5
49
3
48
41
39
18
15
46
23
32
16
19
27
47
17
29
26
33
6
10
38
45'''.splitlines()

p2 = '''1
24
7
44
20
40
42
50
37
21
43
9
12
8
34
13
28
36
25
35
22
2
11
30
31'''.splitlines()

p1 = list(map(int, p1))
p2 = list(map(int, p2))

#! ########### PART 1 ############
while len(p1) > 0 and len(p2) > 0:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
if len(p1) > 0:
   result = sum([(i + 1) * c for i, c in enumerate(p1[::-1])])
else:
   result = sum([(i + 1) * c for i, c in enumerate(p2[::-1])])
print (f"Part 1 result = {result}") #34127
        
#! ########### PART 2 ############
p1 = list(map(int, p1))
p2 = list(map(int, p2))
