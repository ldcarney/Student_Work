#Liam Carney
#Intro to AI

#Classic Traveling Saleman problem

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

np.random.seed(3202)

d=np.random.multivariate_normal([14,0], [[1,0],[0,1]],20)
d2=np.random.multivariate_normal([0,20], [[1,.8],[.8,1]],12)
d3=np.random.multivariate_normal([10,10], [[1,1],[1,1]],12)
d4=[[14,20], [0,0], [7,10]]
d5={'x': np.random.random(size=10)*(20)-3, 'y': np.random.random(size=10)*30-5}
df=pd.DataFrame(data=d, columns=['x','y'])
df = df.append(pd.DataFrame(data=d2, columns=['x','y']))
df = df.append(pd.DataFrame(data=d3, columns=['x','y']))
df = df.append(pd.DataFrame(data=d4, columns=['x','y']))
df = df.append(pd.DataFrame(data=d5, columns=['x','y']))
plt.scatter(df['x'],df['y'])
plt.show()

def add_edges(df):
    
    x_points = np.array(df["x"])
    y_points = np.array(df["y"])
    length = len(y_points)
    
    neighbors = []
    for i in range(length): 
        arr = []
        edges = {}
        temp_x = x_points[i]
        temp_y = y_points[i]
        
        for k in range(length):
            
            
            neighbor_x = x_points[k]
            neighbor_y = y_points[k]
            
            x_length = abs(neighbor_x - temp_x)
            y_length = abs(neighbor_y - temp_y)
            
            dist = np.sqrt((x_length**2)+(y_length**2))
            edges[k] = [i, k, dist]
            arr.append(dist)


        if 0.0 in arr:
            arr.remove(0.0)    
        least_1 = float(min(arr))
        arr.remove(least_1)
        least_2 = float(min(arr))

        for l in edges:
            pos = float(edges[l][2])
            if pos == least_1:
                neighbors.append([edges[l][0], edges[l][1]])
            if pos == least_2:
                neighbors.append([edges[l][0], edges[l][1]])
        
    
    lines = np.array(neighbors) 
    plt.plot(x_points[lines.T], y_points[lines.T], 'y-')
    plt.plot(x_points, y_points, 'ro') # Points 
    plt.show()
            

def distance(arr_1, arr_2):
    d = np.sqrt((arr_1[0]-arr_2[0])**2+(arr_1[1]-arr_2[1])**2)
    return d

def total_distance(city, arr):
    dist=0
    for i in range(len(city)-1):
        dist += distance(arr[city[i]],arr[city[i+1]])
    dist += distance(arr[city[-1]],arr[city[0]])
    return dist        
        
        
def reverseFunction(city, n):
    num_city = len(city)
    #Reverse half the length
    m = int((1+ ((n[1]-n[0]) % num_city))/2) 
    #Reversed by: n[0] goes to n[1], n[0]+1 goes to n[1]-1, n[0]+2 goes ton[1]-2, etc.
    #Starts at end moves to center
    
    for j in range(m):
        k = (n[0]+j) % num_city
        l = (n[1]-j) % num_city
        (city[k],city[l]) = (city[l],city[k])  # swap
    
def transpose(city, n):
    num_city = len(city)
    
    new_city=[]
    #Range n[0]...n[1]
    for j in range( (n[1]-n[0])%num_city + 1):
        new_city.append(city[(j+n[0])%num_city ])
    #Followed by n[5]...n[2]
    for j in range( (n[2]-n[5])%num_city + 1):
        new_city.append(city[(j+n[5])%num_city ])
    #Followed by n[3]...n[4]
    for j in range( (n[4]-n[3])%num_city + 1):
        new_city.append(city[ (j+n[3])%num_city ])
    return new_city
    
def Plot(city, arr, dist):
    point = [arr[city[i]] for i in range(len(city))]
    point += [arr[city[0]]]
    point = np.array(point)
    
    f2 = plt.figure()
    ax2 = f2.add_subplot()
    plt.title('Total Distance ='+str(dist))
    ax2.plot(point[:,0], point[:,1], '-o')
    plt.show()
            

coords = np.array(df)
num_city = len(coords)
max_temp_steps = num_city
#Starting temperature
temp_start = 0.2
#Rate at which temp is decreased
temp_cool = 0.9
max_steps = 100*num_city
max_accept = 10*num_city
reverse = 0.5

#Order cities are vistied - index table
city = list(range(num_city))
#Initial travel distance 
dist = total_distance(city, coords)

#Stores points of a move
n = np.zeros(6, dtype = int)

temp = temp_start

#Array of calulcated distances
histo_arr = []

for i in range(max_temp_steps):
    accepted = 0

    for k in range(max_steps):

        while True: #Finds two random cities close to each other 
            #two cities n[0] and n[1] are chosen randomly 
            n[0] = int((num_city)*np.random.rand())
            n[1] = int((num_city-1)*np.random.rand())
            if (n[1] >= n[0]):
                n[1] += 1
            if (n[1] < n[0]):
                (n[0],n[1]) = (n[1],n[0]) #swap because must be n[0] < n[1]
            m = (n[0]+num_city - n[1]-1)%num_city #number of cities not on segment n[0]...n[1]
            if m >=3:
                break

        #Want an index before and after two cities
        #Order: [n2, n0, n1, n3]
        n[2] = (n[0]-1)%num_city #one before n[0]
        n[3] = (n[1]+1)%num_city #one after n[2]

        
        
        #Reverse Method
        #Cost to reverse the path between city[n[0]]-city[n[1]]
        cost = distance(coords[city[n[2]]],coords[city[n[1]]]) + distance(coords[city[n[3]]],coords[city[n[0]]]) - distance(coords[city[n[2]]],coords[city[n[0]]]) - distance(coords[city[n[3]]],coords[city[n[1]]])

        #reverse a segment
        if cost<0 or np.exp(-cost/temp)>np.random.rand():
            accepted += 1
            dist += cost
            reverseFunction(city, n)

        
        #Transpose Method
        #Reverse proved to work better
        """
        nc = (n[1]+1+int(np.random.rand()*(m-1)))%num_city
        n[4] = nc
        n[5] =(nc+1)%num_city

        #cost to transpose
        cost = -distance(coords[city[n[1]]],coords[city[n[3]]]) - distance(coords[city[n[0]]],coords[city[n[2]]]) - distance(coords[city[n[4]]],coords[city[n[5]]])
        cost += distance(coords[city[n[0]]],coords[city[n[4]]]) + distance(coords[city[n[1]]],coords[city[n[5]]]) + distance(coords[city[n[2]]],coords[city[n[3]]])


        if cost<0 or np.exp(-cost/temp)>np.random.rand():
            accepted += 1
            dist += cost
            city = transpose(city, n)
        """
        

        if accepted>max_accept: 
            break

    #Plot
    histo_arr.append(dist)

    #The system is cooled down
    temp *= temp_cool
    #Stop if path is done changing
    if accepted == 0: break

print("The optimal path claulcated is:")
Plot(city, coords, dist)

#visualization of success times/paths of different implementations, plot of shortest path found
print("Array of total distances according to temperature and probability values: ", histo_arr)
print("Iterations: ", len(histo_arr))
f1 = plt.figure()
ax1 = f1.add_subplot()
ax1.hist(histo_arr, bins=40)
plt.title("Calculated Distance Histogram")
plt.show


Plot(city, coords, dist)



