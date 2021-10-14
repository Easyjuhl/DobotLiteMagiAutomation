from serial.tools import list_ports

import pydobot

def pick(offx, offy):
    device.suck(False)

    device.move_to(240, 0, 140, 80, wait=True) #Startposition

    device.move_to(300 + offx, -80 + offy, 140, 80, wait=True)

    device.move_to(270 + offx, -130 + offy, -40, 80, wait=True)

    device.suck(True)

    device.move_to(270 + offx, -130 + offy, 40, 80, wait=True)

    device.move_to(240, 0, 140, 80, wait=True)


def place(offx, offy):
    device.move_to(300, 80, 140, 80, wait=True)

    device.move_to(270 + offx, 130 - offy, 40, 80, wait=True)

    device.move_to(270 + offx, 130 - offy, -40, 80, wait=True)

    device.suck(False)

    device.move_to(240 + offx, 0 - offy, 140, 80, wait=True)


available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[0].device

device = pydobot.Dobot(port=port, verbose=False)

def orderhandler(order):
    rednr=0
    greennr=0
    bluenr=0
    yellownr=0

    placement = 0

    for brik in order:
        placement += 1
        if brik=="0":
            pass

        elif brik=="1":
            pick(0,20*rednr)
            rednr += 1
            if placement < 5:
                place(20*(placement-1),0)
            elif placement < 9:
                place(20*(placement-5),20)
            elif placement < 13:
                place(20*(placement-9),40)
            else:
                place(20*(placement-13),60)

        elif brik=="2":
            pick(20,20*greennr)
            greennr += 1
            if placement < 5:
                place(20*(placement-1),0)
            elif placement < 9:
                place(20*(placement-5),20)
            elif placement < 13:
                place(20*(placement-9),40)
            else:
                place(20*(placement-13),60)


        elif brik=="3":
            pick(40,20*bluenr)
            bluenr += 1
            if placement < 5:
                place(20*(placement-1),0)
            elif placement < 9:
                place(20*(placement-5),20)
            elif placement < 13:
                place(20*(placement-9),40)
            else:
                place(20*(placement-13),60)

        elif brik=="4":
            pick(60,20*yellownr)
            yellownr += 1
            if placement < 5:
                place(20*(placement-1),0)
            elif placement < 9:
                place(20*(placement-5),20)
            elif placement < 13:
                place(20*(placement-9),40)
            else:
                place(20*(placement-13),60)

orderhandler("0110133140040440")

device.close()
