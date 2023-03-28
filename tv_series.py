import pickle
import os.path
import datetime

#current year
anno_corrente = datetime.datetime.now().year

#information for the text file
titolo_file = "serie_tv_" + str(anno_corrente)
directory = "C:/Users/aless/Desktop/python/tv series/file tv series"

dizionario = {}

#check if the dictionary already exists and load it
if os.path.exists("dizionario.pickle"):
    with open("dizionario.pickle", "rb") as f:
        dizionario = pickle.load(f)

#command definition ("tv series", "vote", "pop", "pop tot" and "save")
while True:
    key = input("Inserisci una serie tv o scrivi comando: ")
    if key == "print":
        #print the table with all TV series reordered 
        dizionario_ordinato = {k: v for k, v in sorted(dizionario.items(), key=lambda item: item[1], reverse=True)}
        print("")
        print("{:<28} {:<28}".format('serie', 'voto'))
        print('-' * 34)
        for key, value in dizionario_ordinato.items():
            print("{:<28} {:<28}".format(key, value))    
    elif key == "pop":
        dizionario.popitem()
    elif key == "pop tot":
        dizionario.clear()
    elif key == "end":
        break
    elif key == "save":
        #save creates a text file containing the table ordered with all tv series
        dizionario_ordinato = {k: v for k, v in sorted(dizionario.items(), key=lambda item: item[1], reverse=True)}
        with open(os.path.join(directory, titolo_file + ".txt"), "w") as f:
            f.write("{:<28} {:<28} \n".format('serie', 'voto'))
            f.write('-' * 34 + "\n")
            for key, value in dizionario_ordinato.items():
                f.write("{:<28} {:<28} \n".format(key, value))

    else:
        value = input("voto: ")
        dizionario[key] = value

#save the updated dictionary to the file
with open("dizionario.pickle", "wb") as f:
    pickle.dump(dizionario, f)
