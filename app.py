import streamlit as st 
import pandas as pd

# Configuracion de la aplicacion 
st.set_page_config(
    page_title="Monitoreo de ventas",
    page_icon="📊",
    layout="wide"
)

st.title("📊Sistema de monitoreo de ventas")
st.write("Administracion y analisis de informacion comercial")

# Datos del ejemplo
datos={
    "Producto": [
        "Laptop","Mouse", "Teclado",
        "Monitor", "Laptop", "Mouse",
        "Monitor", "Teclado"
    ],
    "Cantidad": [2, 10, 5, 3, 1, 8, 4, 6],
    "Precio" : [12000, 150, 350, 2800, 12000, 150, 2800, 350]
}
df = pd.DataFrame(datos)

# Calcular ingresos 
df["Total"] = df ["Cantidad"] * df ["Precio"]

#Administracion de datos
st.header("1. Administracion de datos")

df=st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True
)

# Actualizar cálculos
df["Cantidad"] = pd.to_numeric(
    df["Cantidad"], errors="coerce"
).fillna(0)

df["Precio"] = pd.to_numeric(
    df["Precio"], errors="coerce"
).fillna(0)

df["Total"] = df["Cantidad"] * df["Precio"]

# Indicadores
st.header("2. Indicadores de ventas")

col1, col2, col3 = st.columns(3)

col1.metric("Productos registrados", len(df))
col2.metric("Unidades vendidas", int(df["Cantidad"].sum()))
col3.metric("Ingresos totales", f"${df['Total'].sum():,.2f}")

# Reporte gráfico
st.header("3. Reporte gráfico")

ventas = df.groupby("Producto")["Total"].sum()

st.subheader("Ingresos por producto")
st.bar_chart(ventas)

unidades = df.groupby("Producto")["Cantidad"].sum()

st.subheader("Cantidad de productos vendidos")
st.line_chart(unidades)

# Tabla de resultados
st.header("4. Reporte de resultados")
st.dataframe(df, use_container_width=True)

# Descargar reporte
csv = df.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="Descargar reporte CSV",
    data=csv,
    file_name="reporte_ventas.csv",
    mime="text/csv"
)