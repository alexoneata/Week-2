bookcover = input("please enter the cover type (soft/hard):")

if bookcover == "soft":
    bound= input("is it perfect bound?")
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive")

