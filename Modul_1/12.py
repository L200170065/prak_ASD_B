import random

print ("Game tebak angka")

z = 0
ronde = 1
jawaban = random.randint(0,100)
i=0
while z <= 1:
    i=i+1
    inp = int(input("Masukkan tebakan ke-{0} :".format(i)))
    if inp < jawaban:
        print ("Itu terlalu kecil. Coba lagi")
        ronde = ronde + 1
        
    elif inp == jawaban:
        print ("Ya. Anda benar")
        
        z = z+1
        ronde = ronde + 1
    else:
        print ("Itu terlalu besar. Coba lagi")
        ronde = ronde + 1
