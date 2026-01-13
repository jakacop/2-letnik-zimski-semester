def napolni_seznam(m, n):
    sez = []
    for i in range(m, n + 1):
        sez.append(i)
    return sez

nas_seznam = napolni_seznam(42, 65)

def vsota_seznama():
    return print(f"Ustvarjen seznam dolžine {len(nas_seznam)} z vsoto {sum(nas_seznam)} je: {nas_seznam}.")

vsota_seznama()