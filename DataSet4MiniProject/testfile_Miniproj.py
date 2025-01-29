#!/home/ia97tafa/verbitpy/bin/python3

fname="Gr1_MatPt1.dat"
with open(fname,'r') as file:
    for ix,line in enumerate(file):
        if ix==0:
            Vol=line.split(':')[1].strip()
            #print(f"{line.split(':')[1].strip()}")
        else:
            #print(line)
        #with open('input.txt', 'r') as f:
            l = [[float(num) for num in line.split(' ')] for line in file]
            #print(l)

print(f"The Atomic Volume: {Vol}\n Matrix: {l}")
    

