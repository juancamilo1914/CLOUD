unidad_origen = print(float("ingrese la unidad: "))

def convertir_unidades(cantidad, unidad_origen, unidad_destino):
    conversiones = {
        "Bits": 1,
        "Bytes": 8,
        "Kb": 1024,
        "MB": 1024 * 1024,
        "GB": 1024 * 1024 * 1024
    }

    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        return "Unidad no válida. Las unidades válidas son: Bits, Bytes, Kb, MB, GB."

    factor_conversion = conversiones[unidad_origen] / conversiones[unidad_destino]
    resultado = cantidad * factor_conversion

    return f"{cantidad} {unidad_origen} son:\n{resultado} {unidad_destino}"
