import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")
loop = True

while loop:
    masukan = input("masukan input nyalakan/matikan: ")

    if (masukan == "nyalakan"):
        board.digital[13].write(1)
    elif (masukan == "matikan"):
        board.digital[13].write(0)
    else:
        loop = False




 