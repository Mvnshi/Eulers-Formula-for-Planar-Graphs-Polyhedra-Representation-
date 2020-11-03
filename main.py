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
    if donthave == "verticies" or "Verticies":
        e = int(input("How many edges? "))
        f = int(input("How many faces? "))
        v = 2 + e - f
        if v >= 0:
            if str(v) == "1":
                print("There is 1 vertex in this shape.")
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

    elif donthave == "edges" or "Edges":
        v = int(input("How many verticies? "))
        f = int(input("How many faces? "))
        e = 2 - v - f
        if e >= 0:
            if str(e) == "1":
                print("There is 1 edge in this shape.")
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
    elif donthave == "faces" or "Faces":
        v = int(input("How many verticies? "))
        e = int(input("How many edges? "))
        f = 2 - v + e
        if f >= 0:
            if str(f) == "1":
                print("There is 1 face in this shape.")
            else:
                print("There are " + str(f)  + " faces in this shape.")
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




elif choice == "2":
    v = int(input("How many verticies? ")) #Asks user for number of verticies
    e = int(input("How many edges? ")) #Asks user for number of edges
    f = int(input("How many faces? ")) #Ask user for number of faces

    if v - e + f == 2: #Checks if it is a polyhedra
        print("This is a polyhedra!") #Says that it is a polyhedra
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
    else: #Else statement that occurs when it is not a polyhedra
        print("This is not a polyhedra!") #Says that it is not a polyhedra
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
    time.sleep(10)

