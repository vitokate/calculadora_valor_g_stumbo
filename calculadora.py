# Calculadora de valor g para el metodo de Stumbo
# Válida solo en el dominio 10°C ≤ z ≤ 111°C, fh/U ≥ 0.3 y 0.4 ≤ Jc ≤ 2


import numpy as np

# Coeficientes de la Tabla 1 para el polinomio H
coefficients_H = {
    'aA': -0.004402, 'aB': 0.048989, 'aC': -0.162490, 'aD': 0.160914,
    'bA': 0.014952, 'bB': -0.136467, 'bC': 0.355817, 'bD': -0.128237,
    'cA': -0.411237, 'cB': 1.373832, 'cC': -1.310923, 'cD': 0.038973,
    'dA': -0.032731, 'dB': 0.252513, 'dC': -0.697395, 'dD': 1.614456
}

# Coeficientes de la Tabla 2 para el polinomio K
coefficients_K = {
    'pP': -2.1736e-5, 'pQ': 3.6527e-5, 'pR': -4.6221e-3,
    'qP': -1.0870e-4, 'qQ': 7.0356e-3, 'qR': -7.0012e-2,
    'rP': 8.7693e-5, 'rQ': 1.6666e-2, 'rR': 0.2322
}

# Función para calcular los polinomios H y K
def calculate_polynomials(u, y, Jc):
    H = (coefficients_H['aA']*u**3 + coefficients_H['aB']*u**2 + coefficients_H['aC']*u + coefficients_H['aD']) + \
        (coefficients_H['bA']*u**3 + coefficients_H['bB']*u**2 + coefficients_H['bC']*u + coefficients_H['bD'])*y + \
        (coefficients_H['cA']*u**3 + coefficients_H['cB']*u**2 + coefficients_H['cC']*u + coefficients_H['cD'])*y**2 + \
        (coefficients_H['dA']*u**3 + coefficients_H['dB']*u**2 + coefficients_H['dC']*u + coefficients_H['dD'])*y**3

    K = 1 / (1 + (Jc - 0.4)*(coefficients_K['pP']*u**2 + coefficients_K['pQ']*u + coefficients_K['pR']) *
             (coefficients_K['qP']*u**2 + coefficients_K['qQ']*u + coefficients_K['qR']) *
             (coefficients_K['rP']*u**2 + coefficients_K['rQ']*u + coefficients_K['rR']))

    return H, K

# Función para calcular g
def calculate_g(Z, Jc, fh_U, gamma=2.718281828459045):
    # Asegurarse de que fh/U y Z son positivos
    if fh_U <= 0 or Z <= 0:
        raise ValueError("fh/U y Z deben ser mayores que cero para calcular el logaritmo.")

    # Convertir a logaritmos
    u = np.log(fh_U)
    y = np.log(Z)

    # Calcular los polinomios H y K
    H, K = calculate_polynomials(u, y, Jc)

    # Calcular g usando la ecuación dada
    g = (Z / 2.3) * np.exp(-gamma - (2.3 / fh_U)) * H * K
    return g

# Uso de ejemplo de la función
# Recuerda únicamente dividir por 1.8 al pasar de °F a °C
Z_input = 10  # Temperatura en °C
Jc_input = 1.64  # Valor de Jc
fh_U_input = 0.536  # Valor de fh/U

# Calcular el valor de g
g_calculated = calculate_g(Z_input, Jc_input, fh_U_input)
print(f'El valor calculado de g es: {g_calculated}')