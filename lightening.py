#Lightning.py
#Amanda Hansford
#9/11/17

def lightening():
    y = float(input("How many seconds ago did you see the lightening: "))
    x = float(input("How many seconds ago did you hear the thunder: "))

    x=y-x

    print("So there was a", x, "second gap.")
    
    x= 1100*x
    z= x/5280

    print("That means the storm is about", z, "miles away.")

lightening()
