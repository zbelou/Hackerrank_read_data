# The first line contains two space-separated integers denoting the respective values of s and t. 
# The second line contains two space-separated integers denoting the respective values of a and b. 
# The third line contains two space-separated integers denoting the respective values of m and n. 
# The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a. 
# The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

# Sample input
7 11
5 15
3 2
-2 2 1
5 -6

s,t = [int(points) for points in input().strip().split(' ')]
a,b = [int(points) for points in input().strip().split(' ')]
m,n = [int(points) for points in input().strip().split(' ')]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]