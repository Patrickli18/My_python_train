# Global Reach

def read_global():
    print("From inside the local scpe of read_global(),values is :", values)

def shadow_global():
    values = -10
    print("From inside the local scope of shadow_global(),values is :", values)

def change_global():
    global values
    values = -20
    print("From inside the local scope of change_global(),values is :", values)

values = 10
print("At the global scope,values is :", values)

read_global()
print("At the global scope,values is :", values,"\n")

shadow_global()
print("At the global scope,values is :", values,"\n")
change_global()
print("At the global scope,values is :", values,"\n")


input("\n\nPress the enter key to exit.")