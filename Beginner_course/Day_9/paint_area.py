import math
h = float(input("Please enter the heigth(in m)"));
l= float(input("Please enter the widht (in m)"))
coverage =5
def area_paint(coverage,height,width):
    numbers_of_can = (height*width)/coverage;
    return numbers_of_can
numbers_of_can = area_paint(coverage=coverage,height=h,width=l);
print(f'No. of can required to paint the wall is {math.ceil(numbers_of_can)}')

