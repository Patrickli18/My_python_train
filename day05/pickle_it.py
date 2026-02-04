# Pickle IT
import pickle , shelve

print("Picklig lists...")
variety = ["sweet","hot","dill"]
shape = ["whole","spear","chip"]
brand = ["Claussen","Vlasic","Mt. Olive"]
f = open("day05/pickles.dat","wb")
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()


print("\nUnpickling lists...")
f = open("day05/pickles.dat","rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
f.close()


print(variety)
print(shape)
print(brand)

print("\nShelving lists...")
s = shelve.open("day05/pickles2.dat")
s["variety"] = ["sweet","hot","dill"]
s["shape"] = ["whole","spear","chip"]
s["brand"] = ["Claussen","Vlasic","Mt. Olive"]
s.sync()
print("\nRetrieing lists from shelf...")
print("brand - ",s["brand"])
print("shape - ",s["shape"])
print("variety - ",s["variety"])
s.close()

input("\n\nPress Enter to exit." )