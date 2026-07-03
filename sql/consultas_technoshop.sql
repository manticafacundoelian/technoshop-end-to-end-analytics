SELECT
    cliente_id,
    MIN(fecha_pedido) AS primera_compra,
    MAX(fecha_pedido) AS ultima_compra,
    COUNT(DISTINCT pedido_id) AS pedidos
FROM fact_pedidos_final
WHERE estado_pedido = 'Entregado'
GROUP BY cliente_id
ORDER BY ultima_compra;

WITH UltimaCompraPorCliente AS (
    SELECT 
        cliente_id,
        strftime('%Y', MAX(fecha_pedido)) AS anio_ultima_compra
    FROM fact_pedidos_final
    WHERE estado_pedido = 'Entregado'
    GROUP BY cliente_id
)
SELECT 
    anio_ultima_compra,
    COUNT(*) AS clientes
FROM UltimaCompraPorCliente
GROUP BY anio_ultima_compra
ORDER BY anio_ultima_compra DESC;

SELECT
    COUNT(*) AS clientes_perdidos
FROM (
    SELECT
        cliente_id,
        MAX(fecha_pedido) AS ultima_compra
    FROM fact_pedidos_final
    WHERE estado_pedido='Entregado'
    GROUP BY cliente_id
)
WHERE ultima_compra < '2025-01-01';

SELECT
    COUNT(*) AS clientes,
    strftime('%Y', ultima_compra) AS anio_ultima_compra
FROM (
    SELECT
        cliente_id,
        MAX(fecha_pedido) AS ultima_compra
    FROM fact_pedidos_final
    WHERE estado_pedido='Entregado'
    GROUP BY cliente_id
)
GROUP BY anio_ultima_compra
ORDER BY anio_ultima_compra;

SELECT
    COUNT(*) AS filas,
    COUNT(DISTINCT pedido_id) AS pedidos_unicos
FROM fact_pedidos_final;

SELECT
    cliente_id,
    COUNT(DISTINCT pedido_id) AS pedidos
FROM fact_pedidos_final
WHERE estado_pedido='Entregado'
GROUP BY cliente_id
ORDER BY pedidos DESC
LIMIT 20;

SELECT
count(DISTINCT cliente_id) as cleintes
FROM dim_clientes;

SELECT COUNT(*) AS clientes_no_activos
FROM dim_clientes
WHERE cliente_id NOT IN (
    SELECT DISTINCT cliente_id 
    FROM fact_pedidos_final 
    WHERE estado_pedido = 'Entregado'
);

SELECT COUNT(*) AS nunca_compraron_nada
FROM dim_clientes
WHERE cliente_id NOT IN (
    SELECT DISTINCT cliente_id 
    FROM fact_pedidos_final
);

SELECT cliente_id, estado_pedido, COUNT(*) AS cantidad_pedidos
FROM fact_pedidos_final
WHERE cliente_id NOT IN (
    SELECT DISTINCT cliente_id 
    FROM fact_pedidos_final 
    WHERE estado_pedido = 'Entregado'
)
GROUP BY cliente_id, estado_pedido;

WITH PrimerasComprasClientes AS (
    SELECT 
        cliente_id,
        MIN(fecha_pedido) AS primera_fecha_historica
    FROM fact_pedidos_final
    WHERE estado_pedido = 'Entregado'
    GROUP BY cliente_id
)
SELECT COUNT(DISTINCT cliente_id) AS total_clientes_nuevos_2025
FROM PrimerasComprasClientes
WHERE primera_fecha_historica BETWEEN '2025-01-01' AND '2025-12-31';

WITH HistorialPorCliente AS (
    SELECT 
        cliente_id,
        MAX(CASE WHEN fecha_pedido BETWEEN '2023-01-01' AND '2023-12-31' THEN 1 ELSE 0 END) AS compro_2023,
        MAX(CASE WHEN fecha_pedido BETWEEN '2024-01-01' AND '2024-12-31' THEN 1 ELSE 0 END) AS compro_2024,
        MAX(CASE WHEN fecha_pedido BETWEEN '2025-01-01' AND '2025-12-31' THEN 1 ELSE 0 END) AS compro_2025
    FROM fact_pedidos_final
    WHERE estado_pedido = 'Entregado'
    GROUP BY cliente_id
)
SELECT 
    -- RETENIDOS: Compró en 2024 y mantuvo la constancia en 2025
    SUM(CASE WHEN compro_2024 = 1 AND compro_2025 = 1 THEN 1 ELSE 0 END) AS sql_clientes_retenidos_2025,
    
    -- REACTIVADOS: Compró en 2023, se enfrió en 2024 (0) y regresó en 2025
    SUM(CASE WHEN compro_2023 = 1 AND compro_2024 = 0 AND compro_2025 = 1 THEN 1 ELSE 0 END) AS sql_clientes_reactivados_2025
FROM HistorialPorCliente;

SELECT COUNT(*) AS clientes_registrados_sin_compra
FROM dim_clientes
WHERE cliente_id NOT IN (
    SELECT DISTINCT cliente_id 
    FROM fact_pedidos_final 
    WHERE estado_pedido = 'Entregado'
);


