# There are N rectangular buildings standing along the road next to each other. The K-th building is of size H[K] × 1.

# Because a renovation of all of the buildings is planned, we want to cover them with rectangular banners until the renovations are finished. Of course, to cover a building, the banner has to be at least as high as the building. We can cover more than one building with a banner if it is wider than 1.

# For example, to cover buildings of heights 3, 1, 4 we could use a banner of size 4×3 (i.e. of height 4 and width 3), marked here in blue:

# Buildings of sizes (3 × 1), (1 × 1), (4 × 1), covered with scaffolding of size 4×3

# We can order at most two banners and we want to cover all of the buildings. Also, we want to minimize the amount of material needed to produce the banners.

# What is the minimum total area of at most two banners which cover all of the buildings?

# Write a function:

# def solution(H)

# that, given an array H consisting of N integers, returns the minimum total area of at most two banners that we will have to order.

# Examples:

# 1. Given H = [3, 1, 4], the function should return 10. The result can be achieved by covering the first two buildings with a banner of size 3×2 and the third building with a banner of size 4×1:

# Illustration of first example

# 2. Given H = [5, 3, 2, 4], the function should return 17. The result can be achieved by covering the first building with a banner of size 5×1 and the other buildings with a banner of size 4×3:

# Illustration of second example

# 3. Given H = [5, 3, 5, 2, 1], your function should return 19. The result can be achieved by covering the first three buildings with a banner of size 5×3 and the other two with a banner of size 2×2:

# Illustration of third example

# 4. Given H = [7, 7, 3, 7, 7], your function should return 35. The result can be achieved by using one banner of size 7×5:

# Illustration of fourth example

# 5. Given H = [1, 1, 7, 6, 6, 6], your function should return 30. The result can be achieved by using banners of size 1×2 and 7×4:

# Illustration of fifth example

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..10,000].

# PLANNING

# array of area tuples - 
#     1st - just 1st, and rest, then 1st 2 and rest, etc
#     Area of banner = i (number of buildings) x H[tallest]
#     if 4 buildings ex.
#     [(A0, A1-3), (A0-1, A2-3), (A0-2, A3)]
    
#     how to find tallest in set w/ looping multiple?
#     need h1 and h2
#     dict with sorted hieghts and index?
#     ex. h1 = -1, h2 = -1
#     for dict - i in r 1 or 2?
#      -> h1 or h2
#      go down dict until h2
#      if i of h2 in r1, h2 again
     
#      so need to record range as well

def solution(H):
    # write your code in Python 3.6
    
    #edge case 1 - no buildings
    if H is None:
        return 0
    
    print("H", H)
    # 1. dict of hieghts
    # dictH = {H[i]:i for i in range(len(H))}
    dictH = {}
    for i in range(len(H)):
        if H[i] in dictH:
            dictH[H[i]].append(i)
        else:
            dictH[H[i]] = [i]
            
    print("dicH", dictH)
    
    #2. sorted heights, desc
    sortH = H
    sortH.sort(reverse=True)
    print("sortH", sortH)
    
    #3. variables for area calc,
    # range1 (start to index), range2 (i to fin), h1 (max height in range1), h2 (max height in range 2), minS (minimum sum of area range1 and area range2)
    h1 = -1
    h2 = -1
    minS = sortH[0]*len(H)
    print("minS", minS)
    
    #0 to len(H)-1
    for i in range(len(H)):
        
        # range1 = 0 -> i
        # range2 = i+1 -> len(H)
        
        #max height index
        maxI = dictH[sortH[0]][0]
        print("maxI", maxI)
        
        if maxI <= i:
            h1 = sortH[0]
            print("h1", h1)
                    
        else:
            h2 = sortH[0]
            print("h2", h2)
            
        #find other height
        #if h2 in range1, reset
        if h2 != -1 and dictH[h2] <= i:
            h2 = -1
            
        for j in range(len(H)):
            
            #temp heights until i in range2
            tempH = sortH[j]
            print("tempH", tempH)
            
            #temp height index
            for k in range(len(dictH[tempH])):
                tempI = dictH[tempH][k]
                print("tempI", tempI)
            
                if h1 == -1:
                    if tempI <= i:
                        h1 = tempH
                        print("h1", h1)
                        
                    
                if h2 == -1:
                    if tempI > i:
                        h2 = tempH
                        print("h2", h2)
                
                elif h1 != -1 and h2 != -1:
                    break
            
        
        #4. After h1 and h2, areas of banners for range1 and range2
        
        #4a - area of banner range1
        area1 = h1 * (i + 1)
        
        #4b - area of banner range2
        area2 = h2 * (len(H) - i - 1)
        
        #5 sum of 2 banners
        sumB = area1 + area2
        
        #6 if sumB < minS, set as new minumum
        if sumB < minS:
            minS = sumB
    
    #7. return min sum
    return minS
        


#TESTS

h1 = [3,1,4] #10
h2 = [5,3,2,4] #17
h3 = [5,3,5,2,1] #19
h4 = [7,7,3,7,7] #35
h5 = [1,1,7,6,6,6] #30