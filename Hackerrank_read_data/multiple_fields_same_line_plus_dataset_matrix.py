# The first line contains 2 space-separated integers, F (the number of observed features) and N (the number of rows/houses for which Charlie has noted both the features and price per square foot). 
# The N subsequent lines each contain F+1 space-separated floating-point numbers describing a row in the table; the first elements are the noted features for a house, and the very last element is its price per square foot.
# The next line (following the table) contains a single integer, T, denoting the number of houses for for which Charlie noted features but does not know the price per square foot. 
# The T subsequent lines each contain F space-separated floating-point numbers describing the features of a house for which pricing is not known.

# Sample input
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

features, rows = map(int, input().split()) # Read in first line F & N
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split())) # Create elements list for independent variables. This creates a list of all dependent variables from all observations until we get to 4
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

new_rows = int(input()) # Read in line 15 to show prediction data set will have 4 observations
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split())) # Same logic as above but don't need to limit to first 2 observations since there are only 2 (dependent variables, this is what we predict)
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)