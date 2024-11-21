if(len(adresses) == 0):
    print("Attention, tu as retiré toutes les adresses !")

assert(adresses == [24, 3, 23], "Tu as retiré la mauvaise adresse !")
assert(len(adresses) == 3, "Tu as retiré la mauvaise adresse !")
assert(adresses.count(14) == 0, "Tu as retiré la mauvaise adresse !")