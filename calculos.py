#Funcion con parametros y con retorno
def es_surfeable(altura):
    return altura >= 1.5

#Funcion con parametros y sin retorno
def alertar_viento_peligroso(nudos_viento):
    if nudos_viento > 20:
        print("[ALERTA CRITICA]: Viento peligroso, peligro de corriente")
    else:
        print("Condiciones de viento dentro del limite")

#Funcion sin parametros y con retorno
def obtener_temperatura_limite_traje():
    obtener_temperatura_limite_traje = 13
    return obtener_temperatura_limite_traje

#Funcion sin parametros y sin retorno
def mostrar_advertencia_marejada():
    print("---------------------------------")
    print("AVISO DE LA ARMADA: MAREJADAS ACTIVAS")
    print("---------------------------------")