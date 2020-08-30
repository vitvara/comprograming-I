# define x0y0 - x2y2
x0, x1, x2 = 1, 4, 4
y0, y1, y2 = 1, 1, 5

# x-x y-y to know length
pre_a1, pre_a2 = x0 - x1, y0 - y1
pre_b1, pre_b2 = x1 - x2, y1 - y2
pre_c1, pre_c2 = x2 - x0, y2 - y0

# add length to list
list_pre_length = [pre_a1, pre_a2, pre_b1, pre_b2, pre_c1, pre_c2]
# an empty list that wait for append
list_length = []

for i in range(0, 6):
    if i not in [1, 3, 5]:
        # calculate to right angle
        tri = ((list_pre_length[i]) ** 2 + (list_pre_length[i + 1]) ** 2) ** (1 / 2)
        # append right angle size to list
        list_length.append(tri)

# make element in list into int
a = list_length[0]
b = list_length[1]
c = list_length[2]
# calculate s
s = 0.5 * (a + b + c)

# calculate area
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
print(area)
