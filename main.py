import time
import os
os.system('cls')
os.system('color 9')
print("""
 __   __  _______  ______   _______    _______  __   __    __   __  __   __  __    _  _______  __   __  ___  
|  |_|  ||   _   ||      | |       |  |  _    ||  | |  |  |  |_|  ||  | |  ||  |  | ||       ||  | |  ||   | 
|       ||  |_|  ||  _    ||    ___|  | |_|   ||  |_|  |  |       ||  | |  ||   |_| ||  _____||  |_|  ||   | 
|       ||       || | |   ||   |___   |       ||       |  |       ||  |_|  ||       || |_____ |       ||   | 
|       ||       || |_|   ||    ___|  |  _   | |_     _|  |       ||       ||  _    ||_____  ||       ||   | 
| ||_|| ||   _   ||       ||   |___   | |_|   |  |   |    | ||_|| ||       || | |   | _____| ||   _   ||   | 
|_|   |_||__| |__||______| |_______|  |_______|  |___|    |_|   |_||_______||_|  |__||_______||__| |__||___| 
""")
print("1. Input 2 numbers and find shape")
print("2. Check if shape is a polyhedra ")
choice = input("Select: (1 or 2) ")
if choice == "1":
    donthave = input("What don't you have? (verticies, edges, faces): ")
    if donthave == "verticies" or donthave == "Verticies":
        e = int(input("How many edges? "))
        f = int(input("How many faces? "))
        v = 2 + e - f
        if v >= 0:
            if str(v) == "1":
                print("There is 1 vertex in this shape.")
                if f == 4 and e == 6:
                    print("This shape is a Tetrahedron!")
                elif f == 5 and e == 9:
                    print("This shape is a Triangular prism!")
                elif f == 6 and e == 12:
                    print("This shape is a Cube!")
                elif f == 7 and e == 15:
                    print("This shape is a Pentagonal prism!")  
                elif f == 8 and e == 12:
                    print("This shape is a Octahedron!")
                elif f == 8 and e == 18:
                    print("This shape is a Truncated tetrahedron!")
                elif f == 10 and e == 16:
                    print("This shape is a Square antiprism!")  
                elif f == 10 and e == 24:
                    print("This shape is a Octagonal prism!")
                elif f == 12 and e == 20:
                    print("This shape is a Pentagonal antiprism!")
                elif f == 12 and e == 30:
                    print("This shape is a Dodecahedron or Decagonal prism!")  
                elif f == 14 and e == 24:
                    print("This shape is a Cuboctahedron or Hexagonal antiprism!")
                elif f == 14 and e == 36:
                    print("This shape is a Truncated octahedron or Dodecagonal prism or Truncated cube!")
                elif f == 18 and e == 32:
                    print("This shape is a Octagonal antiprism!")  
                elif f == 20 and e == 30:
                    print("This shape is a Icosahedron!")
                elif f == 22 and e == 40:
                    print("This shape is a Decagonal antiprism!")
                elif f == 26 and e == 48:
                    print("This shape is a Rhombicuboctahedron or Dodecagonal antiprism!")
                elif f == 26 and e == 72:
                    print("This shape is a Truncated cuboctahedron!")  
                elif f == 32 and e == 60:
                    print("This shape is a Icosidodecahedron!")
                elif f == 32 and e == 90:
                    print("This shape is a Truncated icosahedron!")
                elif f == 38 and e == 60:
                    print("This shape is a Snub cube!")  
                elif f == 62 and e == 120:
                    print("This shape is a Rhombicosidodecahedron!")
                elif f == 62 and e == 180:
                    print("This shape is a Truncated icosidodecahedron!")
                elif f == 92 and e == 150:
                    print("This shape is a Snub dodecahedron!")  
            else:
                print("There are " + str(v)  + " verticies in this shape.")
            if v - e + f == 2:
                if f == 1:
                    print("This shape is a Tetrahedron!")
                elif f == 2:
                    print("This shape is a cube!")
                elif f == 3:
                    print("This shape is a octahedron!")
                elif f == 4:
                    print("This shape is a dodecahedron!")
                elif f == 5:
                    print("This shape is a icosahedron!")
                elif f == 6:
                    print("This shape is a truncated tetrahedron!")
                elif f == 7:
                    print("This shape is a cuboctahedron!")
                elif f == 8:
                    print("This shape is a truncated cube!")
                elif f == 9:
                    print("This shape is a truncated octahedron!")
                elif f == 10:
                    print("This shape is a small rhombicuboctahedron!")
                elif f == 11:
                    print("This shape is a great rhombicuboctahedron!")
                elif f == 12:
                    print("This shape is a icosidodecahedron!")
                elif f == 13:
                    print("This shape is a truncated dodecahedron!")
                elif f == 14:
                    print("This shape is a truncated icosahedron!")
                elif f == 15:
                    print("This shape is a left snub cube!")
                elif f == 16:
                    print("This shape is a right snub cube!")
                elif f == 17:
                    print ("This shape is a small rhombicosidodecahedron!")
                elif f == 18:
                    print("This shape is a great rhombicosidodecahedron!")
                elif f == 19:
                    print("This shape is a left snub dodecahedron!")
                elif f == 20:
                    print("This shape is a right snub dodecahedron!")
                
            else:
                print("This shape is not a polyhedra! ")
        else:
            print("This is not a real shape.")
        time.sleep(10)

    elif donthave == "edges" or donthave == "Edges":
        v = int(input("How many verticies? "))
        f = int(input("How many faces? "))
        e = 2 - v - f
        if e >= 0:
            if str(e) == "1":
                print("There is 1 edge in this shape.")
                if f == 4 and e == 6:
                    print("This shape is a Tetrahedron!")
                elif f == 5 and e == 9:
                    print("This shape is a Triangular prism!")
                elif f == 6 and e == 12:
                    print("This shape is a Cube!")
                elif f == 7 and e == 15:
                    print("This shape is a Pentagonal prism!")  
                elif f == 8 and e == 12:
                    print("This shape is a Octahedron!")
                elif f == 8 and e == 18:
                    print("This shape is a Truncated tetrahedron!")
                elif f == 10 and e == 16:
                    print("This shape is a Square antiprism!")  
                elif f == 10 and e == 24:
                    print("This shape is a Octagonal prism!")
                elif f == 12 and e == 20:
                    print("This shape is a Pentagonal antiprism!")
                elif f == 12 and e == 30:
                    print("This shape is a Dodecahedron or Decagonal prism!")  
                elif f == 14 and e == 24:
                    print("This shape is a Cuboctahedron or Hexagonal antiprism!")
                elif f == 14 and e == 36:
                    print("This shape is a Truncated octahedron or Dodecagonal prism or Truncated cube!")
                elif f == 18 and e == 32:
                    print("This shape is a Octagonal antiprism!")  
                elif f == 20 and e == 30:
                    print("This shape is a Icosahedron!")
                elif f == 22 and e == 40:
                    print("This shape is a Decagonal antiprism!")
                elif f == 26 and e == 48:
                    print("This shape is a Rhombicuboctahedron or Dodecagonal antiprism!")
                elif f == 26 and e == 72:
                    print("This shape is a Truncated cuboctahedron!")  
                elif f == 32 and e == 60:
                    print("This shape is a Icosidodecahedron!")
                elif f == 32 and e == 90:
                    print("This shape is a Truncated icosahedron!")
                elif f == 38 and e == 60:
                    print("This shape is a Snub cube!")  
                elif f == 62 and e == 120:
                    print("This shape is a Rhombicosidodecahedron!")
                elif f == 62 and e == 180:
                    print("This shape is a Truncated icosidodecahedron!")
                elif f == 92 and e == 150:
                    print("This shape is a Snub dodecahedron!")
                    
            else:
                print("There are " + str(e)  + " edges in this shape.")
                if f == 1:
                    print("This shape is a Tetrahedron!")
                elif f == 2:
                    print("This shape is a cube!")
                elif f == 3:
                    print("This shape is a octahedron!")
                elif f == 4:
                    print("This shape is a dodecahedron!")
                elif f == 5:
                    print("This shape is a icosahedron!")
                elif f == 6:
                    print("This shape is a truncated tetrahedron!")
                elif f == 7:
                    print("This shape is a cuboctahedron!")
                elif f == 8:
                    print("This shape is a truncated cube!")
                elif f == 9:
                    print("This shape is a truncated octahedron!")
                elif f == 10:
                    print("This shape is a small rhombicuboctahedron!")
                elif f == 11:
                    print("This shape is a great rhombicuboctahedron!")
                elif f == 12:
                    print("This shape is a icosidodecahedron!")
                elif f == 13:
                    print("This shape is a truncated dodecahedron!")
                elif f == 14:
                    print("This shape is a truncated icosahedron!")
                elif f == 15:
                    print("This shape is a left snub cube!")
                elif f == 16:
                    print("This shape is a right snub cube!")
                elif f == 17:
                    print ("This shape is a small rhombicosidodecahedron!")
                elif f == 18:
                    print("This shape is a great rhombicosidodecahedron!")
                elif f == 19:
                    print("This shape is a left snub dodecahedron!")
                elif f == 20:
                    print("This shape is a right snub dodecahedron!")
        else:
            print("This is not a real shape.")
        time.sleep(10)
        
    elif donthave == "faces" or donthave == "Faces":
        v = int(input("How many verticies? "))
        e = int(input("How many edges? "))
        f = 2 - v + e
        if f >= 0:
            if str(f) == "1":
                print("There is 1 face in this shape.")
            else:
                print("There are " + str(f)  + " faces in this shape.")
            if v - e + f == 2:      
                if f == 4 and e == 6:
                    print("This shape is a Tetrahedron!")
                elif f == 5 and e == 9:
                    print("This shape is a Triangular prism!")
                elif f == 6 and e == 12:
                    print("This shape is a Cube!")
                elif f == 7 and e == 15:
                    print("This shape is a Pentagonal prism!")  
                elif f == 8 and e == 12:
                    print("This shape is a Octahedron!")
                elif f == 8 and e == 18:
                    print("This shape is a Truncated tetrahedron!")
                elif f == 10 and e == 16:
                    print("This shape is a Square antiprism!")  
                elif f == 10 and e == 24:
                    print("This shape is a Octagonal prism!")
                elif f == 12 and e == 20:
                    print("This shape is a Pentagonal antiprism!")
                elif f == 12 and e == 30:
                    print("This shape is a Dodecahedron or Decagonal prism!")  
                elif f == 14 and e == 24:
                    print("This shape is a Cuboctahedron or Hexagonal antiprism!")
                elif f == 14 and e == 36:
                    print("This shape is a Truncated octahedron or Dodecagonal prism or Truncated cube!")
                elif f == 18 and e == 32:
                    print("This shape is a Octagonal antiprism!")  
                elif f == 20 and e == 30:
                    print("This shape is a Icosahedron!")
                elif f == 22 and e == 40:
                    print("This shape is a Decagonal antiprism!")
                elif f == 26 and e == 48:
                    print("This shape is a Rhombicuboctahedron or Dodecagonal antiprism!")
                elif f == 26 and e == 72:
                    print("This shape is a Truncated cuboctahedron!")  
                elif f == 32 and e == 60:
                    print("This shape is a Icosidodecahedron!")
                elif f == 32 and e == 90:
                    print("This shape is a Truncated icosahedron!")
                elif f == 38 and e == 60:
                    print("This shape is a Snub cube!")  
                elif f == 62 and e == 120:
                    print("This shape is a Rhombicosidodecahedron!")
                elif f == 62 and e == 180:
                    print("This shape is a Truncated icosidodecahedron!")
                elif f == 92 and e == 150:
                    print("This shape is a Snub dodecahedron!")       
        else:
            print("This is not a real shape.")
        time.sleep(10)

elif choice == "2":
    v = int(input("How many verticies? ")) #Asks user for number of verticies
    e = int(input("How many edges? ")) #Asks user for number of edges
    f = int(input("How many faces? ")) #Ask user for number of faces
    if v - e + f == 2: #Checks if it is a polyhedra
        print("This is a polyhedra!") #Says that it is a polyhedra
        if f == 4 and e == 6:
            print("This shape is a Tetrahedron!")
        elif f == 5 and e == 9:
            print("This shape is a Triangular prism!")
        elif f == 6 and e == 12:
            print("This shape is a Cube!")
        elif f == 7 and e == 15:
            print("This shape is a Pentagonal prism!")  
        elif f == 8 and e == 12:
            print("This shape is a Octahedron!")
        elif f == 8 and e == 18:
            print("This shape is a Truncated tetrahedron!")
        elif f == 10 and e == 16:
            print("This shape is a Square antiprism!")  
        elif f == 10 and e == 24:
            print("This shape is a Octagonal prism!")
        elif f == 12 and e == 20:
            print("This shape is a Pentagonal antiprism!")
        elif f == 12 and e == 30:
            print("This shape is a Dodecahedron or Decagonal prism!")  
        elif f == 14 and e == 24:
            print("This shape is a Cuboctahedron or Hexagonal antiprism!")
        elif f == 14 and e == 36:
            print("This shape is a Truncated octahedron or Dodecagonal prism or Truncated cube!")
        elif f == 18 and e == 32:
            print("This shape is a Octagonal antiprism!")  
        elif f == 20 and e == 30:
            print("This shape is a Icosahedron!")
        elif f == 22 and e == 40:
            print("This shape is a Decagonal antiprism!")
        elif f == 26 and e == 48:
            print("This shape is a Rhombicuboctahedron or Dodecagonal antiprism!")
        elif f == 26 and e == 72:
            print("This shape is a Truncated cuboctahedron!")  
        elif f == 32 and e == 60:
            print("This shape is a Icosidodecahedron!")
        elif f == 32 and e == 90:
            print("This shape is a Truncated icosahedron!")
        elif f == 38 and e == 60:
            print("This shape is a Snub cube!")  
        elif f == 62 and e == 120:
            print("This shape is a Rhombicosidodecahedron!")
        elif f == 62 and e == 180:
            print("This shape is a Truncated icosidodecahedron!")
        elif f == 92 and e == 150:
            print("This shape is a Snub dodecahedron!")  
    else: #Else statement that occurs when it is not a polyhedra
        print("This is not a polyhedra!") #Says that it is not a polyhedra
    time.sleep(10)

