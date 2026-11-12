"""
CLI-скрипт обработки снимков Sentinel-1.

Пайплайн:
1. Для каждого ZIP в data/incoming/:
   - SNAP GPT -> GeoTIFF в data/processing/scenes/
   - Порог -> бинарная маска
   - Векторизация -> shapefile в data/processing/parts/
2. Объединение parts/*.shp в data/current/flood_zones.shp (geopandas)
3. Запись meta.json в data/current/
4. Очистка временных файлов

TODO: реализовать на следующих этапах.
"""

if __name__ == "__main__":
    print("Скрипт обработки пока не реализован.")