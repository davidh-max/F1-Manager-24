"""Cálculos de pista con las vueltas observadas de cada tanda."""
from statistics import linear_regression, mean, pstdev


def analizar_tanda(tanda):
    vueltas = tanda.get('vueltas') or []
    numeros = [v['numero'] for v in vueltas]
    if any(type(n) is not int or n < 1 for n in numeros):
        raise ValueError('Los números de vuelta deben ser enteros positivos')
    if len(set(numeros)) != len(numeros):
        raise ValueError('Hay números de vuelta duplicados en la tanda')

    muestra = {}
    excluidas = {}
    for vuelta in vueltas:
        numero = vuelta['numero']
        tiempo = vuelta.get('tiempo_ms')
        if tiempo is not None and (type(tiempo) is not int or tiempo <= 0):
            raise ValueError(f'Vuelta {numero}: tiempo_ms debe ser un entero positivo')
        motivo = vuelta.get('exclusion_ritmo') or ('sin tiempo' if tiempo is None else None)
        if motivo:
            excluidas[numero] = motivo
        else:
            muestra[numero] = tiempo

    indices = sorted(muestra)
    tiempos = [muestra[numero] for numero in indices]
    tendencia = None
    if len(tiempos) >= 4:
        tendencia = round(linear_regression(indices, tiempos).slope / 1000, 4)

    return {
        'estado': 'CALCULADO',
        'vueltas_utilizadas': indices,
        'vueltas_excluidas': excluidas,
        'mejor_vuelta_ms': min(tiempos) if tiempos else None,
        'ritmo_medio_ms': round(mean(tiempos), 1) if tiempos else None,
        'dispersion_ms': round(pstdev(tiempos), 1) if len(tiempos) >= 2 else None,
        'tendencia_ritmo_s_por_vuelta': tendencia,
        'metodo': 'Regresión lineal sobre el número real de vuelta, con al menos cuatro tiempos útiles',
        'limitaciones': (
            'Tendencia neta del ritmo. Combustible, tráfico, temperatura y pista pueden influir. '
            'Comprueba la comparabilidad y documenta las exclusiones antes de interpretarla.'
        ),
    }
