Data Monitor / [dm18.te-st.ru](https://dm18.te-st.ru)
==============

### Результат работы над проектом находится по адресу [piter.unionfourman.ru](https://piter.unionfourman.ru)
### Все геопривязанные данные находятся [в открытом доступе](https://maxim.nextgis.com/resource/1734)

### Директория data содержит следующие данные:
* data.csv

   Исходные статистические данные

* dictionary.csv

   Словарь описания заголовков

* districts.geojson

   Полигональный слой административных районов Санкт-Петербурга. GeoJSON в EPSG:3857, для конвертации в EPSG:4326 можно использовать утилиту ogr2ogr.
   
* result.geojson

   Итоговые геопривязанные данные. GeoJSON в EPSG:3857, для конвертации в EPSG:4326 можно использовать утилиту ogr2ogr.
   
* attach.py

  Скрипт для привязки данных из csv таблицы к районам Санкт-Петербурга
