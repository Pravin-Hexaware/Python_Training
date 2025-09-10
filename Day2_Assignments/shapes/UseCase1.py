import circle as cs
import rectangle as rs

radius=int(input("Enter the radius:"))
print(cs.area(radius))
print(cs.perimeter(radius))

length,width=list(map(int,input("Enter the values of length and width:").split()))
print(rs.area(length,width))
print(rs.perimeter(length,width))