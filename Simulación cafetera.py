import numpy as np
import matplotlib.pyplot as plt

# Condiciones iniciales
Tamb = 20 + 273.15     # ----> Temperatura ambiente en Kelvin
T = np.ones(2) * Tamb  # ----> Vector de temperaturas iniciales (zona inferior y superior)
Q = np.zeros(2)        # ----> Inicialización de las tasas de calor (zona inferior y superior)
m_i_inf = 3.2e-1       # ----> Masa inicial en la zona inferior (kg)
m_i_sup = 0            # ----> Masa inicial en la zona superior (kg)

# Cálculo del flujo de masa
Qin = 7.39e-5   # ----> Flujo volumétrico de entrada en m³/s
rho = 1.0e3     # ----> Densidad del agua en kg/m³
fm = rho * Qin  # ----> Flujo de masa en kg/s

# Paso de tiempo
delta = 0.01

# Definir listas para almacenar resultados
Tres = []
Qres = []
mcres = []

# Inicializar variables
i = 0
m_sup = m_i_sup

# Función cafetera
def cafetera(delta, fm, Tamb, T, Q, i, m_i_inf, m_i_sup):
    # Asignar constantes
    C = 4.183          # ----> kJ/(kg K)
    UA_inf = 3.167  # ----> Coeficiente de transferencia de calor para la zona inferior (kW/K)
    UA_sup = 3.288  # ----> Coeficiente de transferencia de calor para la zona superior (kW/K)

    # Temperaturas
    T_inf = T[0]
    T_sup = T[1]

    # Cálculos para la primera etapa (zona inferior)
    Q_inf = UA_inf * (Tamb - T_inf)
    m_inf = m_i_inf - fm * i * delta
    T_inf_new = ((Q_inf + (fm * C * T_inf)) * delta) / (m_inf * C) + T_inf

    # Cálculos para la segunda etapa (zona superior)
    Q_sup = UA_sup * (Tamb - T_sup)
    m_sup = m_i_sup + fm * i * delta
    T_sup_new = ((Q_sup + (fm * C * (T_sup - Tamb))) * delta) / (m_sup * C) + T_sup

    # Actualizar m_i_inf y m_i_sup para la próxima iteración
    m_i_inf = m_i_inf - fm * delta
    m_i_sup = m_i_sup + fm * delta

    # Almacenar las nuevas temperaturas y tasas de flujo de masa
    Tnew = np.array([T_inf_new, T_sup_new])
    Qnew = np.array([Q_inf, Q_sup])
    m_new = np.array([m_inf, m_sup])

    return Tnew, Qnew, m_new, m_inf, m_sup, m_i_inf, m_i_sup


# Implementación del bucle while
while abs(m_sup) < 3e-1:
    i += 1
    Tnew, Qnew, m_new, m_inf, m_sup, m_i_inf, m_i_sup = cafetera(delta, fm, Tamb, T, Q, i, m_i_inf, m_i_sup)

    Tres.append(Tnew)
    Qres.append(Qnew)
    mcres.append(m_new)

    Q = Qnew
    T = Tnew

# Convertir listas en arrays para facilidad en graficar
Tres = np.array(Tres)
Qres = np.array(Qres)
mcres = np.array(mcres)

# Graficar los resultados
plt.figure()
plt.plot(mcres[:, 0], label='Zona inferior')
plt.title('Masa en zona inferior del tanque')
plt.xlabel('Tiempo (s)')
plt.ylabel('Masa (kg)')
plt.legend()
plt.grid()
plt.savefig('Inferior.pdf')
plt.show()

plt.figure()
plt.plot(mcres[:, 1], label='Zona superior')
plt.title('Masa en zona superior del tanque')
plt.xlabel('Tiempo (s)')
plt.ylabel('Masa (kg)')
plt.legend()
plt.grid()
plt.savefig('Superior.pdf')
plt.show()