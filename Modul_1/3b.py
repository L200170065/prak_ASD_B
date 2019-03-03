def jumlahHurufKonsonan(k):
    p = 0
    hkon = ["b","c","d","f","g","j","k","l","m","n","p","q","r","S","t","v","w","x","y","z"]
    for i in k:
        for z in hkon:
            if i == z:
                p = p+1
    return (len(k), p)
