## 🏋️ Reporte Semanal de Aforo y Uso del Gimnasio

### 📌 ¿Qué hace el proyecto?
Automatiza la generación del informe semanal de uso del gimnasio para optimizar la capacidad de las instalaciones y conocer el comportamiento de los usuarios.

### 📊 Métricas que analiza:
- **Picos de asistencia:** Horarios y días con mayor flujo de usuarios.
- **Áreas más utilizadas:** Zonas con mayor demanda (mancuernas, cardio, salones grupales).
- **Permanencia promedio:** Tiempo medio que pasa un afiliado en la instalación por sesión.

### 🛠️ ¿Qué usamos y cómo?
- **Python (Pandas):** Procesa los registros de entrada/salida para calcular el tiempo de permanencia y las horas pico.
- **FastAPI / Express:** Expone los endpoints para consultar los consolidados semanales.
- **Chart.js / Tailwind CSS:** Renderiza gráficos interactivos del aforo en el panel de administración.
- **Cron Jobs / Tareas programadas:** Ejecutan la consolidación de datos automáticamente cada domingo a medianoche.
