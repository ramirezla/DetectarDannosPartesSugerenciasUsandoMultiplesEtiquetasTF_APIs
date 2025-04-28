# Documentación del Proyecto: Preparación de Datos para Detección de Daños con Múltiples Etiquetas

---

## 1. Introducción y Marco Teórico

Este proyecto tiene como objetivo preparar y procesar datos para un sistema de detección de daños en partes de vehículos utilizando múltiples etiquetas. Se trabaja con imágenes y etiquetas que describen las piezas del vehículo, tipos de daño y sugerencias de reparación o reemplazo.

El enfoque multi-etiqueta permite clasificar simultáneamente múltiples daños y partes afectadas en una imagen, lo que es fundamental para aplicaciones en seguros y evaluación de siniestros automotrices.

---

## 2. Descripción de los Datos

### 2.1 Piezas del Vehículo

Listado completo de las piezas consideradas en el proyecto:

- Antiniebla delantero derecho
- Antiniebla delantero izquierdo
- Capó
- Cerradura capo
- Cerradura maletero
- Cerradura puerta
- Espejo lateral derecho
- Espejo lateral izquierdo
- Faros derecho
- Faros izquierdo
- Guardabarros delantero derecho
- Guardabarros delantero izquierdo
- Guardabarros trasero derecho
- Guardabarros trasero izquierdo
- Luz indicadora delantera derecha
- Luz indicadora delantera izquierda
- Luz indicadora trasera derecha
- Luz indicadora trasera izquierda
- Luz trasera derecho
- Luz trasera izquierdo
- Maletero
- Manija derecha
- Manija izquierda
- Marco de la ventana
- Marco de las puertas
- Moldura capó
- Moldura puerta delantera derecha
- Moldura puerta delantera izquierda
- Moldura puerta trasera derecha
- Moldura puerta trasera izquierda
- Parabrisas delantero
- Parabrisas trasero
- Parachoques delantero
- Parachoques trasero
- Puerta delantera derecha
- Puerta delantera izquierda
- Puerta trasera derecha
- Puerta trasera izquierda
- Rejilla, parrilla
- Rueda
- Tapa de combustible
- Tapa de rueda
- Techo
- Techo corredizo
- Ventana delantera derecha
- Ventana delantera izquierda
- Ventana trasera derecha
- Ventana trasera izquierda
- Ventanilla delantera derecha
- Ventanilla delantera izquierda
- Ventanilla trasera derecha
- Ventanilla trasera izquierda

### 2.2 Tipos de Daño

- Abolladura
- Deformación
- Desprendimiento
- Fractura
- Rayón
- Rotura

### 2.3 Sugerencias

- Reparar
- Reemplazar

---

## 3. Librerías y Configuración del Entorno

Para la preparación y análisis de datos se utilizan las siguientes librerías de Python:

- pandas
- numpy
- scikit-learn
- imblearn
- iterative-stratification
- matplotlib
- scikit-multilearn
- liac-arff

Instalación recomendada:

```bash
pip install --upgrade pip
pip install pandas scikit-learn imblearn iterative-stratification matplotlib scikit-multilearn liac-arff
```

---

## 4. Preparación y Limpieza de Datos

- Se realiza la lectura del archivo CSV con los datos originales.
- Limpieza y estandarización de texto (minúsculas, eliminación de espacios).
- Manejo de valores compuestos en la columna "Tipos de Daño" (por ejemplo, "Abolladura-dent").
- Mapeo de texto a valores numéricos para piezas, daños y sugerencias con manejo de errores.
- Consolidación de etiquetas por imagen para facilitar el procesamiento multi-etiqueta.

---

## 5. Codificación y Consolidación de Etiquetas

- Se codifican las etiquetas de daños, partes y sugerencias en valores numéricos.
- Se agrupan las etiquetas por imagen para obtener listas consolidadas.
- Se guardan los datos procesados en archivos CSV para su uso posterior.

---

## 6. Análisis de Distribución y Manejo de Clases Raras

- Se analiza la distribución de clases multi-etiqueta para identificar clases con pocas muestras.
- Se establecen umbrales para considerar una clase como rara.
- Se agrupan las clases raras bajo una categoría "Otras" para mejorar la robustez del modelo.
- Se actualizan los diccionarios de etiquetas para incluir estas nuevas categorías.
- Se generan archivos de soporte con ejemplos y estadísticas de clases raras.

---

## 7. División de Datos para Entrenamiento, Validación y Prueba

- Se utiliza la técnica de estratificación multilabel para mantener la distribución de clases en los conjuntos.
- División recomendada:
  - 70% entrenamiento
  - 15% validación
  - 15% prueba
- Se guardan los conjuntos en archivos CSV separados.
- Se almacenan metadatos para reproducibilidad y trazabilidad.

---

## 8. Mejores Prácticas y Sugerencias

- Mantener la reproducibilidad mediante el uso de semillas aleatorias y guardado de metadatos.
- Analizar y manejar clases raras para evitar sesgos en el modelo.
- Utilizar técnicas de estratificación multilabel para preservar la distribución de etiquetas.
- Documentar claramente cada paso del procesamiento para facilitar mantenimiento y mejoras.
- Realizar análisis exploratorios para entender la distribución y calidad de los datos.

---

## 9. Conclusiones

La preparación cuidadosa y estructurada de los datos es fundamental para el éxito de modelos de detección multi-etiqueta. Este proyecto proporciona un pipeline completo desde la limpieza, codificación, análisis, agrupamiento de clases raras y división estratificada, asegurando datos de calidad para el entrenamiento y evaluación.

---

## 10. Bibliografía

- Documentación oficial de pandas, scikit-learn, imblearn y matplotlib.
- Artículos y recursos sobre clasificación multilabel y estratificación multilabel.
- Referencias específicas pueden añadirse según fuentes utilizadas.

---

## 11. Extras

### Mapa Mental (Mind Map)

> [Incluir aquí un diagrama o enlace a un mapa mental que resuma el flujo del proyecto]

### Imágenes y Gráficos

> [Incluir gráficos de distribución de clases, diagramas de flujo y otros recursos visuales relevantes]

---

*Fin de la documentación del proyecto.*
