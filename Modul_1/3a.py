def jumlahHurufVokal(k):
    p = 0
    hvok = ["a","i","u","e","o"]
    for i in k:
        for z in hvok:
            if i == z:
                p = p+1
    return (len(k), p)





