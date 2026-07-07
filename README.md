# Sales & Profitability Analysis

**Power BI | DAX | Data Modeling | Business Intelligence**

Proyecto de portfolio basado en un dataset sintético diseñado para simular el comportamiento de una empresa retail con venta de productos de tecnología a través de canales físico y online.

El objetivo del análisis es entender cómo evolucionó el negocio entre 2023 y 2025, identificar las causas del deterioro en la rentabilidad y detectar oportunidades de mejora a nivel canal, categoría, producto y cliente.

---

## Business Context

La empresa presenta una dinámica particular: el volumen de pedidos se mantiene relativamente estable, pero la rentabilidad cae con fuerza entre 2024 y 2025. A su vez, el negocio muestra cambios en la composición del revenue, presión sobre los costos, variaciones en el mix de categorías y señales de deterioro en la base de clientes.

Este proyecto busca responder cuatro preguntas clave:

1. ¿Qué pasó con el negocio?
2. ¿Por qué cayó la rentabilidad?
3. ¿Dónde conviene intervenir?
4. ¿Qué hacer con la base de clientes?

El análisis está organizado en cuatro dashboards complementarios:

- **Executive Overview**: evolución general del negocio.
- **Profitability Diagnosis**: explicación de la caída de margen y de la estructura de costos.
- **Product Performance**: análisis a nivel SKU para detectar productos rentables y no rentables.
- **Customer Retention**: evolución de clientes nuevos, retenidos, perdidos y de alto valor.

---

## Main Insights

### 1. La rentabilidad cae mucho más rápido que las ventas

Entre 2024 y 2025 el **Revenue Neto** cae, pero la **Ganancia Neta** se contrae en una proporción mucho mayor. Esto indica que el negocio no solo vendió menos, sino que perdió eficiencia económica.

### 2. El negocio mantiene el volumen de pedidos, pero reduce el valor promedio por venta

La cantidad de pedidos no cae al mismo ritmo que el revenue. Sin embargo, el **ticket promedio** baja de forma importante, lo que sugiere un cambio en el mix de productos, una mayor presión promocional o una mayor participación de productos de menor valor unitario.

### 3. El canal online gana protagonismo, pero con menor rentabilidad

El canal online absorbe una mayor parte de la actividad comercial y se convierte en el principal motor de ganancia neta. Sin embargo, su margen también se deteriora, lo que muestra crecimiento en volumen pero presión sobre la rentabilidad.

### 4. El aumento del costo de mercadería explica gran parte del deterioro

La principal causa de la caída del margen no parece ser el descuento comercial. El factor más relevante es el aumento del costo relativo de mercadería, que comprime el margen en ambos canales.

### 5. La rentabilidad cambia por categoría y por producto

Telefonía y Accesorios continúan siendo categorías relevantes, pero el comportamiento no es homogéneo. Algunas líneas sostienen la ganancia, mientras que otras —especialmente TV y Video y parte de Computación— muestran un deterioro notable.

### 6. Los productos no rentables se concentran en el canal online

A nivel SKU aparecen productos con margen negativo principalmente en el canal online. Esto convierte al análisis de producto en una pieza clave para detectar oportunidades de corrección y priorizar decisiones.

### 7. La fidelización mejora en volumen, pero la captación se debilita

La cantidad de clientes retenidos aumenta, pero los clientes nuevos disminuyen de forma clara. Al mismo tiempo, cae la tasa de retención y sube la pérdida de clientes. La lectura correcta no es “fidelización o captación”, sino una combinación: **priorizar la retención en el corto plazo y mejorar la adquisición con foco en calidad de cliente**.

---

## Dashboard 1 — Executive Overview

Este dashboard resume la evolución general del negocio y responde qué ocurrió entre 2024 y 2025.

### Hallazgos principales

- El **Revenue Bruto** y el **Revenue Neto** se reducen respecto del año anterior.
- La **Ganancia Neta** cae en una proporción mucho mayor que las ventas.
- El **margen neto** se reduce de forma significativa.
- El **ticket promedio** baja con fuerza.
- Los **pedidos** no muestran una caída equivalente al revenue.
- El canal **online** gana peso frente al físico.

### Lectura de negocio

La empresa no enfrenta solamente una pérdida de volumen: enfrenta una pérdida de eficiencia. El negocio sigue vendiendo, pero vende peor, con menor valor por pedido y menor capacidad de transformar ventas en utilidad.

---

## Dashboard 2 — Profitability Diagnosis

Este dashboard busca explicar por qué cayó la rentabilidad y cómo se compone el margen.

### Hallazgos principales

- El **costo de mercadería** aumenta como porcentaje del Revenue Neto.
- Los **descuentos** no muestran un crecimiento suficiente como para explicar por sí solos la caída del margen.
- Los **costos logísticos** tienen mayor impacto en el canal online.
- La estructura de rentabilidad se deteriora con fuerza en 2025.
- Algunas categorías muestran una caída mucho más fuerte que otras.
- El gráfico de estructura histórica se deja sin segmentación por año para preservar el contexto temporal y facilitar la lectura de largo plazo.

### Lectura de negocio

La caída de rentabilidad responde principalmente a una compresión de márgenes provocada por costos crecientes. Esto sugiere presión en abastecimiento, pricing o mix de productos, más que una política promocional agresiva.

---

## Dashboard 3 — Product Performance

Este dashboard baja al nivel de SKU para identificar qué productos generan valor y cuáles destruyen rentabilidad.

### Hallazgos principales

- La concentración del Top 5 de productos baja, lo que indica una cartera más distribuida.
- Los productos no rentables aparecen al profundizar por canal, especialmente en **online**.
- **Accesorios** concentra una combinación interesante: alto volumen, buena ganancia total y también heterogeneidad interna en rentabilidad.
- El comportamiento por categoría es muy distinto entre líneas, lo que confirma que no todas aportan de la misma manera.

### Lectura de negocio

El análisis de producto permite pasar del diagnóstico general a la acción concreta. No alcanza con saber que el margen cayó: también hace falta identificar qué SKUs sostienen el negocio y cuáles deben revisarse, ajustarse o discontinuarse.

---

## Dashboard 4 — Customer Retention

Este dashboard analiza la salud de la base de clientes y permite entender si el negocio solo pierde rentabilidad o también deteriora su relación con los clientes.

### Hallazgos principales

- Los **clientes activos** crecen, pero los **clientes nuevos** caen.
- La **retención absoluta** mejora levemente en volumen, pero la **tasa de retención** baja.
- La **pérdida de clientes** aumenta.
- Los **clientes de alto valor** disminuyen en cantidad.
- Una parte muy grande del revenue sigue concentrada en clientes retenidos / de mayor valor.

### Lectura de negocio

La base de clientes muestra señales mixtas. El negocio logra retener una cantidad importante de clientes, pero pierde capacidad de atraer nuevos y aumenta la salida de clientes. En términos de decisión, esto sugiere una estrategia doble:

- **prioridad de corto plazo:** fidelizar y proteger la base actual, que sostiene la mayor parte del revenue;
- **prioridad de mediano plazo:** mejorar la adquisición de clientes nuevos, pero con foco en calidad y potencial de valor.

---

## Business Recommendations

### Prioridad alta

- Revisar la estructura de costos de mercadería en las categorías con peor desempeño.
- Auditar los productos con margen negativo en el canal online.
- Analizar si algunos SKUs deben ser reformulados, re-preciados o discontinuados.
- Proteger la base de clientes retenidos, ya que concentra la mayor parte del revenue.

### Prioridad media

- Optimizar la logística del canal online.
- Revisar el mix de productos para recuperar ticket promedio.
- Profundizar el análisis de categorías con caída fuerte de margen.
- Diseñar acciones para recuperar clientes nuevos con foco en calidad, no solo volumen.

### Prioridad estratégica

- Potenciar las categorías más rentables sin concentrar excesivamente el negocio en pocos productos.
- Usar el análisis de rentabilidad para guiar decisiones de pricing, promociones y surtido.
- Construir una estrategia combinada de fidelización y captación para sostener crecimiento futuro.

---

## Portfolio Value

Este proyecto no está pensado solo para mostrar visualizaciones, sino para demostrar una forma de pensar como analista.

La secuencia de análisis es clara:

1. Qué pasó con el negocio.
2. Por qué pasó.
3. Dónde actuar.
4. A qué clientes priorizar.

Esa narrativa vuelve al portfolio más fuerte, porque transforma un dashboard en un caso de estudio de negocio.

---

## Data Engineering Pipeline

Antes del análisis en Power BI, el dataset fue procesado mediante un pipeline ETL en Python con las siguientes etapas:

- **main**
- **extract**
- **inspect**
- **clean**
- **transform**
- **load**

Durante este proceso se unificaron **Pedidos** y **Detalle Pedidos** para construir un modelo analítico con:

- una **tabla de hechos**;
- varias **dimensiones**;
- estructura preparada para análisis en Power BI;
- validaciones de calidad de datos;
- reglas de negocio consistentes.

> El proyecto de ETL puede publicarse en un repositorio separado para documentar el proceso técnico con más detalle.

---

## Conclusions

El proyecto muestra que el negocio crece en complejidad más que en eficiencia. La empresa mantiene actividad comercial, pero enfrenta una caída fuerte en la rentabilidad impulsada por mayor costo de mercadería, menor ticket promedio, deterioro de algunas categorías clave y señales mixtas en la base de clientes.

La principal fortaleza del análisis es que no se limita a describir gráficos: conecta la evolución del negocio con sus causas y con acciones concretas para mejorar el rendimiento.

---

## Tech Stack

- Power BI
- DAX
- Power Query
- Data Modeling
- Synthetic Data Design
- Python ETL
- GitHub Documentation

---

## Notes

- El proyecto fue construido sobre un dataset sintético diseñado con reglas de negocio para simular un escenario retail realista.
- Algunas visualizaciones históricas se mantienen sin segmentación para preservar contexto temporal y facilitar la lectura comparativa.
- La hoja de clientes se incorpora para complementar el análisis comercial con una mirada de fidelización y retención.

---

## Screenshots

> Insertar aquí las capturas principales de cada dashboard.

- Executive Overview
- Profitability Diagnosis
- Product Performance
- Customer Retention










# 🛒 TechnoShop: End-to-End Retail Data Analytics

## 📋 Resumen Ejecutivo
Este proyecto es un análisis de datos completo para TechnoShop, un comercio de retail tecnológico multicanal. El objetivo principal fue diagnosticar la reciente caída estructural de rentabilidad (2023-2025) y entender el comportamiento de retención de clientes. 

A pesar de sostener el volumen de ventas (+3% interanual), el margen neto cayó severamente. A través de este pipeline de datos, se demostró que la causa no es una crisis de demanda, sino un incremento del **Costo de Mercadería** combinado con políticas logísticas ineficientes para productos de ticket bajo en el canal Online (el actual motor de crecimiento del negocio).

## 🛠️ Arquitectura y Stack Tecnológico
El proyecto abarca todo el ciclo de vida del dato, diseñado bajo un enfoque pragmático y orientado a resultados:

1. **Ingeniería de Datos (Python & Pandas):** Desarrollo de un pipeline ETL modular (`extract.py`, `inspect.py`, `clean.py`, `transform.py`, `load.py`). Se priorizó la velocidad de transformación y limpieza mediante Pandas, omitiendo validaciones estrictas de esquemas (schema validation) para acelerar el flujo de análisis y el cruce dimensional.
2. **Exploración y Validación (SQL):** Uso de SQLite para auditar las tablas dimensionales y de hechos (`dim_clientes`, `dim_productos`, `fact_pedidos_final`) antes de su ingesta visual.
3. **Business Intelligence (Power BI):** Modelado de datos y desarrollo de un dashboard analítico para la toma de decisiones gerenciales.

---

## 📊 Insights Clave de Negocio

### 1. La Paradoja de Rentabilidad y el Motor Online
Entre 2024 y 2025, el margen neto cayó del 33% al 21% (Físico) y del 30% al 15% (Online). Sin embargo, el canal Online generó **$47,971 de ganancia neta en 2025**, casi el doble que el canal Físico. Online se ha convertido indiscutiblemente en la fuente principal de crecimiento y volumen, aunque con un margen porcentual más ajustado que requiere optimización.

![Dashboard Ejecutivo](powerbi/01_dashboard_ejecutivo.png)

### 2. Causa Raíz: Inflación de Proveedores y Pisos de Envío
El % Costo de Mercadería (COGS) subió ~13 puntos (llegando al 78% del revenue). Los costos logísticos se mantuvieron marginales a nivel general, descartando crisis operativas. 
El hallazgo más crítico: **el mismo producto rinde distinto según el canal**. Un accesorio de $15 absorbe un costo fijo de envío de $10 en la web, destruyendo el margen (más del 50% de su valor), mientras que en una notebook de $1,600 el envío es insignificante. Esto genera márgenes negativos en productos económicos vendidos online de forma unitaria.

![Diagnóstico de Rentabilidad](powerbi/02_diagnostico_rentabilidad.png)

### 3. Salud del Catálogo: Alerta en Computación
La categoría *Computación* sufrió la peor combinación posible: perdió volumen y rentabilidad simultáneamente (de 135 pedidos a 27% de margen en 2024, a 77 pedidos y 9% de margen en 2025). El traslado de costos a precio final volvió productos clave (como MacBook Air) menos accesibles, comprimiendo el revenue. *Accesorios* tomó el liderazgo en ganancia gracias al volumen, aunque presenta alta variabilidad interna de márgenes.

![Performance de Productos](powerbi/03_performance_productos.png)

### 4. Fuga de Clientes de Alto Valor
La concentración de ingresos supera el principio de Pareto: **el 20% de los clientes genera el 73% del revenue neto**. El riesgo principal radica en que, en 2025, la tasa de pérdida de clientes (50.94%) superó a la de retención. El segmento "Perdido" es ya el más numeroso de la base histórica. El desafío no es atraer, sino retener a los perfiles de alto valor.

![Clientes Retención](powerbi/04_retencion_clientes.png)

---

## 💡 Acciones Estratégicas Recomendadas

* **Rediseñar Políticas de Envío Online:** Implementar mínimos de compra libre de envío o costos escalonados por ticket para evitar que productos económicos (accesorios, Chromecast) operen con margen negativo al venderse de forma unitaria.
* **Auditoría de Pricing en Computación:** Revisar urgente el traslado de precios al consumidor. La compresión de la MacBook Air indica que la estrategia actual de reprecio destruye volumen sin compensar en margen.
* **Depuración de la Categoría Accesorios:** Segmentar por margen individual. Potenciar los SKUs estrella y aplicar estrategias de *bundling* (combos), reprecio o descontinuación a los de peor desempeño.
* **Programa de Retención de Alto Valor:** Priorizar la retención sobre la adquisición. Diseñar acciones de fidelización dirigidas al segmento "En Riesgo", ya que la pérdida de un solo cliente del Top 20% impacta severamente en la rentabilidad general.
