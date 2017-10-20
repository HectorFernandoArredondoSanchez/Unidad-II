def gastos_operacion(gastos_ventas: float, gastos_admon: float, gastos: float, productos_financieros: float) -> float:
    """Obtiene los gastos de operacion"""
    return gastos_ventas + gastos_admon + (gastos - productos_financieros)


def utilidad_operacion(utilidad_bruta: float, gastos_operacion: float) -> float:
    """Calcula la utilidad de operacion"""
    return utilidad_bruta - gastos_operacion
