import pandas as pd
import logging
import re

logger = logging.getLogger(__name__)

def build_metric(count, total):
    pct = count / total if total > 0 else 0

    if pct == 0:
        severity = "ok"
    elif pct < 0.01:
        severity = "low"
    elif pct < 0.05:
        severity = "medium"
    else:
        severity = "high"

    return {
        "count": int(count),
        "pct": round(pct, 4),
        "severity": severity
    }

#====================================================================================================#
#                                 FUNCIONES AUXILIARES (checks)                                      #
#====================================================================================================#

#================================================================#
#             CAPA DE INTEGRIDAD TECNICA                         #
#================================================================#

#===================================================#
# FUNCION ESPACIOS EN BLANCO                        #
#===================================================#

def check_whitespace(df, nombre_tabla):
    
    logger.info(f"[INSPECT][WHITESPACE] Analizando espacios en blanco en {nombre_tabla.upper()}")
    
    result = {}
    
    total = len(df)
    
    # 1. SOLO APLICAMOS A COLUMNAS DE TEXTO
    text_cols = df.select_dtypes(include=['object', 'string']).columns
    
    for col in text_cols:
        
        # ESPACIOS AL INICIO Y AL FINAL (REPRESENTA UN FORMATO INCORRECTO)
        format_issues = df[col].str.contains(r'^\s+|\s+$', regex=True, na=False).sum()
        
        # SOLO ESPACIOS EN BLANCO/VACIOS (NULO OCULTO)
        whitespace_only = df[col].str.contains(r'^\s+$', regex=True, na=False).sum()
        
        if format_issues > 0 or whitespace_only > 0:
            result[col] = {
                "format_issues": build_metric(format_issues, total),
                "whitespace_only": build_metric(whitespace_only, total)
            }
            
            logger.warning(
                f"[INSPECT][WHITESPACE] Espacios en blanco en {nombre_tabla.upper()}.{col}: "
                f"{format_issues} Valores con espacios "
                f"{whitespace_only} Solo espacios en blanco "
            )
    
    return result

#====================================================#
# FUNCION DUPLICADOS                                 #
#====================================================#

def check_duplicates_raw(df, nombre_tabla, subset=None):

    logger.info(f"[INSPECT][DUPLICATES][RAW] Analizando duplicados crudos en {nombre_tabla.upper()}")

    result = {}

    total = len(df)

    # DUPLICADOS EXACTOS SOBRE DATOS CRUDOS (POR IGUALDAD EN TODAS LAS COLUMNAS)
    
    exact_duplicates_raw = df.duplicated().sum()

    result["exact_duplicates_raw"] = build_metric(exact_duplicates_raw, total)

    if exact_duplicates_raw > 0:
        logger.warning(
            f"[INSPECT][DUPLICATES][RAW][EXACT] Duplicados exactos crudos en {nombre_tabla.upper()}: {exact_duplicates_raw}"
        )

    
    # DUPLICADOS SEMÁNTICOS SOBRE DATOS CRUDOS (POR SUBSET SEGUN LOGICA DE NEGOCIOS) 
    
    if subset:

        total_subset_duplicates_raw = df.duplicated(subset=subset).sum()
  
        # Diferencia entre duplicados exactos y duplicados semanticos
        
        semantic_only_raw = total_subset_duplicates_raw - exact_duplicates_raw

        result["semantic_duplicates_raw_total"] = build_metric(total_subset_duplicates_raw, total)

        result["semantic_only_raw"] = build_metric(semantic_only_raw, total)

        if total_subset_duplicates_raw > 0:
            logger.warning(
                f"[INSPECT][DUPLICATES][RAW][SUBSET] Duplicados semánticos crudos en {nombre_tabla.upper()}: {total_subset_duplicates_raw} totales "
                f"({semantic_only_raw} son puramente semánticos)"
            )

    return result

def check_duplicates_normalized(df, nombre_tabla, subset=None):
    
    logger.info(f"[INSPECT][DUPLICATES][NORMALIZED] Analizando duplicados normalizados en {nombre_tabla.upper()}")

    result = {}

    total = len(df)

    # COPIA DEL DATAFRAME (PARA NO MODIFICAR ORIGINAL)
    df_norm = df.copy()

    # NORMALIZACIÓN DE COLUMNAS DE TEXTO
    
    # Solo aplicamos a columnas tipo object
    text_cols = df_norm.select_dtypes(include=['object', 'string']).columns

    for col in text_cols:
        df_norm[col] = df_norm[col].str.strip().str.lower()
    
    # DUPLICADOS EXACTOS SOBRE DATOS NORMALIZADOS (POR IGUALDAD EN TODAS LAS COLUMNAS)
    exact_duplicates_normalized = df_norm.duplicated().sum()

    result["exact_duplicates_normalized"] = build_metric(exact_duplicates_normalized, total)

    if exact_duplicates_normalized > 0:
        logger.warning(
            f"[INSPECT][DUPLICATES][NORMALIZED][EXACT] Duplicados exactos normalizados en {nombre_tabla.upper()}: {exact_duplicates_normalized}"
        )

    # DUPLICADOS SEMANTICOS SOBRE DATOS NORMALIZADOS (POR SUBSET SEGUN LOGICA DE NEGOCIOS)
    if subset:
        total_subset_duplicates_normalized = df_norm.duplicated(subset=subset).sum()

        semantic_only_normalized = total_subset_duplicates_normalized - exact_duplicates_normalized

        result["semantic_duplicates_normalized_total"] = build_metric(total_subset_duplicates_normalized, total)

        result["semantic_only_normalized"] = build_metric(semantic_only_normalized, total)

        if total_subset_duplicates_normalized > 0:
            logger.warning(
                f"[INSPECT][DUPLICATES][NORMALIZED][SUBSET] Duplicados semánticos normalizados en {nombre_tabla.upper()}: {total_subset_duplicates_normalized} totales "
                f"({semantic_only_normalized} son puramente semánticos tras normalizar)"
            )

    return result

#===================================================#
# FUNCION NULOS                                     #
#===================================================#

def check_nulls(df, nombre_tabla):

    logger.info(f"[INSPECT][NULLS] Analizando nulos en {nombre_tabla.upper()}")
    
    result = {}

    total = len(df)

    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]

    if not nulls.empty:
        result = {
            col: build_metric(count, total)
            for col, count in nulls.to_dict().items()
        }

        logger.warning(
            f"[INSPECT][NULLS] Nulos encontrados en {nombre_tabla}: "
            f"{ {col: int(count) for col, count in nulls.to_dict().items()} }"
        )
    else:
        result = {}

    return result

#===================================================#
# FUNCION CONSISTENCIA DE CASE EN CATEGORICOS       #
#===================================================#

def check_categorical_consistency(df, nombre_tabla, columns):
    logger.info(f"[INSPECT][CATEGORICAL][CONSISTENCY] Analizando consistencia en {nombre_tabla.upper()}")

    result = {}

    for col in columns:
        if col not in df.columns:
            logger.warning(f"[INSPECT][CATEGORICAL][CONSISTENCY][MISSING_COLUMN] {nombre_tabla}: {col} no existe")
            continue

        # 1. Limpieza básica y optimización: value_counts hace casi todo el trabajo duro
        series_clean = df[col].dropna().astype(str)
        if series_clean.empty:
            continue
            
        value_counts = series_clean.value_counts()
        
        # 2. Extraer valores únicos ya ordenados por frecuencia (o alfabéticamente si prefieres)
        unique_values = value_counts.index.tolist()
        
        # 3. Detectar inconsistencias de CASE de forma eficiente y segura
        # Agrupamos los ya únicos por su versión en minúsculas
        lower_seen = set()
        has_case_issue = False
        for val in unique_values:
            val_lower = val.lower()
            if val_lower in lower_seen:
                has_case_issue = True
            lower_seen.add(val_lower)

        # 4. Datos dominantes
        dominant_value = value_counts.idxmax()
        dominant_freq = int(value_counts.max()) 

        result[col] = {
            "n_unique": len(unique_values),
            "unique_values_sample": sorted(unique_values)[:20],
            "case_insensitive_unique": len(lower_seen),
            "case_variants_detected": has_case_issue,
            "dominant_value": dominant_value,
            "dominant_freq": dominant_freq
        }

        if has_case_issue:
            logger.warning(
                f"[INSPECT][CATEGORICAL CONSISTENCY] inconsistencia de case en {nombre_tabla}.{col}"
            )

    return result

#==================================================#
# FUNCION FECHA                                    #
#==================================================#

#===================================================================================================#
#                              FUNCION PRINCIPAL (inspect_data)                                     #
#===================================================================================================#

def inspect_data(pedidos_df, detalle_df, clientes_df, productos_df):

    report = {
        "fact_pedidos": {},
        "fact_detalle_pedidos": {},
        "dim_clientes": {},
        "dim_productos": {}
    }
    
    # ====================
    # ESPACIOS EN BLANCO
    # ====================
    
    report["fact_pedidos"]["whitespace"] = check_whitespace(pedidos_df, "fact_pedidos")
    report["fact_detalle_pedidos"]["whitespace"] = check_whitespace(detalle_df, "fact_detalle_pedidos")
    report["dim_clientes"]["whitespace"] = check_whitespace(clientes_df, "dim_clientes")
    report["dim_productos"]["whitespace"] = check_whitespace(productos_df, "dim_productos")

    # =====================
    # DUPLICADOS
    # =====================

    # SUBSETS PARA TABLAS DE HECHOS 
    subset_pedidos = ['cliente_id', 'fecha_pedido', 'canal_venta', 'medio_pago']
    subset_detalle = ['pedido_id', 'producto_id']
    
    # SUBSETS PARA DIMENSIONES 
    subset_clientes = ['nombre', 'apellido', 'fecha_nacimiento']
    subset_productos = ['nombre_producto', 'categoria', 'marca', 'gama']

    report["fact_pedidos"]["duplicates"] = check_duplicates_raw(pedidos_df, "fact_pedidos", subset=None)
    report["fact_pedidos"]["duplicates_normalized"] = check_duplicates_normalized(pedidos_df, "fact_pedidos", subset=None)
    report["fact_detalle_pedidos"]["duplicates"] = check_duplicates_raw(detalle_df, "fact_detalle_pedidos", subset=subset_detalle)
    report["fact_detalle_pedidos"]["duplicates_normalized"] = check_duplicates_normalized(detalle_df, "fact_detalle_pedidos", subset=subset_detalle)
    report["dim_clientes"]["duplicates"] = check_duplicates_raw(clientes_df, "dim_clientes", subset=subset_clientes)
    report["dim_clientes"]["duplicates_normalized"] = check_duplicates_normalized(clientes_df, "dim_clientes", subset=subset_clientes)
    report["dim_productos"]["duplicates"] = check_duplicates_raw(productos_df, "dim_productos", subset=subset_productos)
    report["dim_productos"]["duplicates_normalized"] = check_duplicates_normalized(productos_df, "dim_productos", subset=subset_productos)

    # =====================
    # NULOS
    # =====================

    report["fact_pedidos"]["nulls"] = check_nulls(pedidos_df, "fact_pedidos")
    report["fact_detalle_pedidos"]["nulls"] = check_nulls(detalle_df, "fact_detalle_pedidos")
    report["dim_clientes"]["nulls"] = check_nulls(clientes_df, "dim_clientes")
    report["dim_productos"]["nulls"] = check_nulls(productos_df, "dim_productos")

    # =====================
    # CONSISTENCIA CATEGORICA 
    # =====================
    
    report["fact_pedidos"]["categorical consistency"] = check_categorical_consistency(pedidos_df, "fact_pedidos", ["canal_venta", "medio_pago", "estado_pedido", "tipo_envio"])
    report["fact_detalle_pedidos"]["categorical consistency"] = {}
    report["dim_clientes"]["categorical consistency"] = check_categorical_consistency(clientes_df, "dim_clientes", ["genero", "ciudad", "provincia", "canal_adquisicion"])
    report["dim_productos"]["categorical consistency"] = check_categorical_consistency(productos_df, "dim_productos", ["categoria", "marca", "gama"])
    
    
    
    return report

