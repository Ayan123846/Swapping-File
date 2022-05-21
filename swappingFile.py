print("By Mohd. Ayan")
print("To Ms. Rahat Shaikh")
print("Hi there,")
print("Wanna swap your files?? You are just at the right place!! Just enter the name of your any 2 files and watch our magic on your files!")

def swapFileData():

    file1 = input("Enter your first file name:- ")
    file2 = input("Enter your second file name:- ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

swapFileData()   