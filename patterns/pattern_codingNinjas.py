N = 10

for x in range(0, N):
    calculated = N - x;"""print("\n\n",calculated,"\n\n")"""
    spaces = N - calculated;"""print("\n\n",spaces,"\n\n")"""
    for y in range(0, N):
        if (spaces!=0):
            print(" ", end = "");spaces = spaces - 1;continue;
        if (calculated!=0):
            print("*", end = "");calculated = calculated - 1;
    print()
