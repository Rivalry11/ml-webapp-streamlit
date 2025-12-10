# Medical Insurance Cost Prediction (Streamlit + ML Model)

Este proyecto desarrolla un modelo de Machine Learning para predecir el costo del seguro médico de una persona, utilizando información demográfica y de estilo de vida. El modelo se entrena con el dataset Medical Insurance Cost de Kaggle y la aplicación web final está construida con Streamlit y desplegada en Render.

El objetivo es demostrar un flujo completo de ciencia de datos:

  1 .Exploración y análisis de datos (EDA)
  2. Entrenamiento y comparación de modelos de regresión
  3. Selección del mejor modelo y guardado con Pipeline
  4. Construcción de una aplicación interactiva
  5. Despliegue en Render para uso en la nube

## Dataset: Medical Insurance Cost

Fuente: https://www.kaggle.com/datasets/mirichoi0218/insurance

| Variable     | Tipo       | Descripción             |
| ------------ | ---------- | ----------------------- |
| **age**      | Numérica   | Edad del paciente       |
| **sex**      | Categórica | Género (male, female)   |
| **bmi**      | Numérica   | Índice de masa corporal |
| **children** | Numérica   | Número de hijos         |
| **smoker**   | Categórica | ¿Fuma? (yes/no)         |
| **region**   | Categórica | Región geográfica       |
| **charges**  | Numérica   | Costo del seguro médico |



## Análisis Exploratorio (EDA)

Entre los hallazgos principales:

  - Los fumadores presentan costos significativamente más altos.
  - BMI y edad tienen correlación positiva con el costo del seguro.
  - No hay valores nulos en el dataset.
  - Las variables categóricas requieren codificación mediante OneHotEncoder.

## Modelos Entrenados

  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - ElasticNet
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - SVR (RBF)

## Modelo seleccionado

### Random Forest Regressor, por su mejor equilibrio entre:

  - Precisión (R² alto)
  - Robustez
  - Resistencia a outliers
  - Capacidad de modelar relaciones no lineales

## Aplicación Web (Streamlit)

### Funcionalidad

El usuario ingresa:

- Edad
- BMI
- Número de hijos
- Sexo
- Fumador o no
- Región

Y la app devuelve:

👉 ### Costo estimado del seguro médico

### Ejecución local

streamlit run src/app.py 


## Despliegue en Render

### URL pública:
(agrega aquí tu enlace de Render)
➡️ https://ml-webapp-streamlit-xxxx.onrender.com

## Conclusiones

- Las características más influyentes son: smoker, age y bmi.
- Los modelos no lineales superaron claramente a los lineales.
- El Random Forest logró el mejor rendimiento general.
- Streamlit permitió crear una interfaz clara y fácil de usar.
- Render facilitó el despliegue para compartir la app públicamente.

## Contributors


This template was built as part of the [Data Science and Machine Learning Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning) by 4Geeks Academy by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Learn more about [4Geeks Academy BootCamp programs](https://4geeksacademy.com/us/programs) here.

Other templates and resources like this can be found on the school's GitHub page.
