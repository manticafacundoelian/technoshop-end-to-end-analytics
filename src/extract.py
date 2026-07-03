import pandas as pd
import logging
import os

logger = logging.getLogger(__name__)

def _read_csv_safe(filename):
    """Función helper interna para leer un archivo de forma segura."""
    path = os.path.join('data', 'raw', filename)
    try:
        df = pd.read_csv(path)
        logger.info(f"[EXTRACT] EXTRACCION EXITOSA: '{filename}'. Filas: {len(df)}")
        return df
    except FileNotFoundError:
        logger.error(f"[EXTRACT] Error: No se encontró el archivo en {path}")
        return None
    except Exception as e:
        logger.error(f"[EXTRACT] Error inesperado al extraer {filename}: {e}")
        return None

def extract_all_data(): 
    """Lee todos los archivos del modelo TechnoShop y los devuelve en orden."""
    logger.info("[EXTRACT] Iniciando lectura masiva del catálogo de TechnoShop")

    # Mapeo exacto de tus 4 nuevas tablas
    pedidos_df = _read_csv_safe('fact_pedidos.csv')
    detalle_df = _read_csv_safe('fact_detalle_pedidos.csv')
    clientes_df = _read_csv_safe('dim_clientes.csv')
    productos_df = _read_csv_safe('dim_productos.csv')

    return pedidos_df, detalle_df, clientes_df, productos_df
