import sys
from random import choice

N_ZONES = 10
N_DEVICES = 100

for i in range(N_ZONES):
    sys.stdout = open("Z"+str(i)+".txt", "w+")

    for j in range(N_DEVICES):
        print("{ \"Z"+str(i)+"U"+str(j)+"\", \"P"+str(j) +"\", \""+choice(["carro", "moto", "aviao", "comboio"])+"\"}.")

    sys.stdout.close()