import pymem.process

pm = pymem.Pymem("cs2.exe")

client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll


# these integers will get outdated sometime, so make sure to get the correct offsets
dwLocalPlayerPawn = 24286024
m_flFlashMaxAlpha = 5320

player = pm.read_longlong(client + dwLocalPlayerPawn)


def enable():
    pm.write_int(player + m_flFlashMaxAlpha, 0)


def disable():
    pm.write_int(player + m_flFlashMaxAlpha, 1132396544)


# just a simple code to test it, do whatever you want with the functions
if __name__ == '__main__':
    while True:
        enable()
        input()
        disable()
        input()
