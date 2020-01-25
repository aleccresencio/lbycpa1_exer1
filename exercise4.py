
#allows loop to go back to here
while True:
    print("\n******Formula Selection Screen******\n")
    print("Select the formula you want to use: ")
    print("[1]Kinematic Formula")
    print("[2]Newton's Law of Cooling formula")
    print("[0]Quit")
    #accept choice from user
    formu = int(input("\nType the number of the formula you want to use: \n"))
    
    #asks user on what variable to solve   
    if formu == 1:
        
        while True:
            print("\n******Variable Selection Screen******\n")
            print("[1]Vo = initial velocity")
            print("[2]a = acceleration")
            print("[3]x = final distance")
            print("[4]xo = initial distance")
            print("[5]Vf = final velocity")
            print("[0]Go back to formula screen")
            
            var = int(input("\nType the number of the variable you want to solve: \n"))
            
        #accept variable input from user
            if var == 1:
                Vf = float(input("Input final velocity: "))
                acc = float(input("Input acceleration: "))
                x = float(input("Input final distance: "))
                xo = float(input("Input initial distance: "))
                #compute using formula
                d = x - xo
                e = 2 * acc * d
                f = Vf ** 2 - e
                g = f ** .5
                while True:
                    print("\nThe initial velocity is:\n", g, "m/s")
                    print("[1]Go back to variable screen")
                    
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")



            if var == 2:
                Vf = float(input("Input final velocity: "))
                Vox = float(input("Input initial velocity: "))
                x = float(input("Input final distance: "))
                xo = float(input("Input initial distance: "))

                d = x - xo
                e = 2 * d
                f = Vf ** 2 - Vox ** 2
                g = f / e
                while True:
                    print("\nThe acceleration is:\n", g, "m/s**2")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 3:
                Vf = float(input("Input final velocity: "))
                Vox = float(input("Input initial velocity: "))
                acc = float(input("Input acceleration: "))
                xo = float(input("Input initial distance: "))

                d = 2 * acc
                e = Vf ** 2 - Vox ** 2
                f = e / d
                g = f + xo
                while True:
                    print("\nThe final distance is:\n", g, "m")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 4:
                Vf = float(input("Input final velocity: "))
                acc = float(input("Input acceleration: "))
                Vox = float(input("Input initial velocity: "))
                x = float(input("Input final distance: "))

                d = 2 * acc
                e = -Vf ** 2 + Vox ** 2
                f = e / d
                g = f + x
                while True:
                    print("\nThe initial distance is:\n", g, "m")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 5:
                Vox = float(input("Input initial velocity: "))
                acc = float(input("Input acceleration: "))
                x = float(input("Input final distance: "))
                xo = float(input("Input initial distance: "))

                d = x - xo
                e = d * 2 * acc
                f = Vox ** 2 + e
                g = f ** .5
                while True:
                    print("\nThe final velocity is:\n", g, "m/s")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 0:
                break

            else:
                print("Invalid answer")

           

    if formu == 2:

        while True:
            print("\n******Variable Selection Screen******\n")
            print("[1]q = heat transferred per unit time")
            print("[2]A = heat transfer area of the surface")
            print("[3]hc = convective heat transfer coefficient")
            print("[4]dT = temperature difference")
            print("[0]Go back to formula screen")
            
            var = int(input("\nType the number of the variable you want to solve: \n"))
            
        #accept variable input from user
            if var == 1:
                A = float(input("Input heat transfer area of the surface: "))
                hc = float(input("Input convective heat transfer coefficient: "))
                dT = float(input("Input temperature difference: "))

                z = hc * A * dT
                while True:
                    print("\nThe heat transferred per unit time is:\n", z, "W")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 2:
                q = float(input("Input heat transferred per unit time: "))
                hc = float(input("Input convective heat transfer coefficient: "))
                dT = float(input("Input temperature difference: "))

                z = q * hc * dT
                while True:
                    print("\nThe heat transfer area of the surface is:\n", z, "m**2")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 3:
                q = float(input("Input heat transferred per unit time: "))
                A = float(input("Input heat transfer area of the surface: "))
                dT = float(input("Input temperature difference: "))

                z = q * A * dT
                while True:
                    print("\nThe convective heat transfer coefficient is:\n", z, "W/(m**2k)")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")

            if var == 4:
                q = float(input("Input heat transferred per unit time: "))
                A = float(input("Input heat transfer area of the surface: "))
                hc = float(input("Input convective heat transfer coefficient: "))
            
                z = q * A * hc
                while True:
                    print("\nThe temperature difference is:\n", z, "K")
                    print("[1]Go back to variable screen")
                        
                    ans = int(input("Input choice here:"))

                    if ans == 1:
                        break
                    else:
                        print("Invalid answer")
        
            if var == 0:
                break

            else:
                print("Invalid answer")

    if formu == 0:
        break

    else:
        print("You have entered an invalid key")
        





