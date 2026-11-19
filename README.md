# 🏥 Gestión de pacientes UCI en Chile

Programa de consola en **Python** que analiza los datos públicos de pacientes en Unidades de Cuidados Intensivos (UCI) por región de Chile, durante la pandemia de COVID-19.

## ✨ Funcionalidades

El programa muestra un menú con estas opciones:

1. **Gráfico de las últimas dos semanas** de una región, en modo acumulativo o no acumulativo
2. **Análisis estadístico por región** (promedio, mediana y moda)
3. **Listado de regiones** con su código
4. **Regiones con el máximo y el mínimo** de pacientes UCI registrados

Se puede elegir la región por nombre o por código, y el programa valida lo que se ingresa.

## 🛠️ Tecnologías

- Python 3
- `statistics` (biblioteca estándar)
- `matplotlib` para los gráficos
- Datos en CSV (`UCI_std.csv`)

## 🚀 Cómo ejecutarlo

```bash
git clone https://github.com/idkferr/Proyecto-Python-.git
cd Proyecto-Python-
pip install matplotlib
python pacientesUCI.py
```

En Windows también se puede abrir con `pacientesUCII.bat`.

## 📁 Archivos

| Archivo | Contenido |
|---|---|
| `pacientesUCI.py` | Programa principal |
| `UCI_std.csv` | Datos de pacientes UCI por región y fecha |
| `diagrama Alto Nivel.jpeg` | Diagrama de alto nivel del programa |

## 👥 Contexto

Proyecto del curso *Fundamentos de Programación* (2021), mi primer proyecto en Python.
