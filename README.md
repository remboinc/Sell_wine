# Одностраничный сайт по продаже вина

Сайт магазина авторского вина "Новое русское вино".
![Сайт по продаже вина.png](%D0%A1%D0%B0%D0%B9%D1%82%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B5%20%D0%B2%D0%B8%D0%BD%D0%B0.png)
## Запуск

- Склонируйте репозиторий
```
git clone https://github.com/remboinc/Sell_wine.git
```
- Создайте виртуальное окружение в директории проекта
```
python3.10 -m venv env
```

- Активируйте виртуальное окружение
На Windows:
```
env\Scripts\activate
```
На macOS и Linux:
```
source env/bin/activate
```

- Перейдите в директорию проекта и установите зависимости
```
cd wine
pip install -r requirements.txt
```

- Запустите рендеринг шаблона сайта из директории `wine/`  
```
python3 main.py
```
- Откройте появившийся файл index.html в браузере по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Подготовка файла к загрузке товаров на сайт

В репозитории в папке `wine/` есть файл с одноименным названием `wine.xlsx`. Он создан для примера. Скопируйте его и заполните своими данными. Важно не менять заголовки основных полей -- "Категория", "Цена" и так далее. Данные в них можно менять. 

ВАЖНО! У созданного файла должно быть расширение `xlsx`. 

| Категория                 | Название                   | Сорт             | Цена        | Картинка                | Акция        |
|---------------------------|----------------------------|------------------|-------------|-------------------------|--------------|
| Ваше название категории 1 | Наименование вашего вина 1 | Сорт винограда 1 | Ваша цена 1 | Название_картинки.png 1 | Ваша акция 1 |
| Ваше название категории 2 | Наименование вашего вина 3 | Сорт винограда 4 | Ваша цена 2 | Название_картинки.png 2 | Ваша акция 2 |
| Ваше название категории 3 | Наименование вашего вина 5 | Сорт винограда 6 | Ваша цена 3 | Название_картинки.png 3 | Ваша акция 3 |

После подготовки эксель документа, создайте в директории проекта файл `.env` и пропишите в переменной `FILE` путь к файлу.
```
FILE=path/to/file.xlsx
```
### Выгружаем картинки
Картинки лежат по адресу `wine/images`. Загрузите в папку собственные изображения и пропишите их названия и расширения в таблице.