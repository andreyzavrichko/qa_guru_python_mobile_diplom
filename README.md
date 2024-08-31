# Приложение color note
## :cherry_blossom:	Содержание
> ➠ [Используемые технологии](#Используемые-технологии)
>
> ➠ [Описание проекта](#Описание-проекта)
>
> ➠ [Особенности реализации тестового проекта](#Особенности-реализации-тестового-проекта)
>
> ➠ [Список проверок](#Список-проверок)
>
> ➠ [Ограничения проекта](#Ограничения-проекта)
>
> ➠ [Этапы реализации](#Этапы-реализации)

## Используемые технологии
![This is an image](/design/icons/tech.png)
## Описание проекта
- Учебный проект реализации автотестирования мобильного приложения.<br/>
- В качестве объекта тестирование выбрано мобильное приложение для учета личных заметок **Color-note**.<br/>
- ColorNote — это простой блокнот. Он предоставляет возможность легкого и простого пользования блокнотом при написании заметок, напоминаний, email, сообщений, перечней дел и покупок. <br/>
<a target="_blank" href="https://play.google.com/store/apps/details?id=com.socialnmobile.dictapps.notepad.color.note"> Подробнее о приложении по ссылке</a></br></br>
<img src="/design/images/page1.png"> <img src="/design/images/page2.png"> </br>
<img src="/design/images/page4.png"> <img src="/design/images/page5.png"> </br>

## Особенности реализации тестового проекта
- [x] Были созданы тест-кейсы в **Allure TestOps** для дальнейшей автоматизации.</br>
- [x] Для описания шагов тест-кейсов в java-коде использован степовой подход.</br>
- [x] Реализована возможность настройки параметров запуска через **Jenkins**

## Список проверок
#### Список проверок, реализованных в автотестах
- [x] Проверка экранов Onboarding
- [x] Проверка экрана создания записки
- [x] Проверка меню More
- [x] Проверка экрана смены тем
- [x] Проверка экрана Поиска
- [x] Проверка экрана Настроек
- [x] Проверка добавления создания записки
- [x] Проверка Туториала
- [x] Проверка создания чек-листа
- [x] Проверка экрана Архив
- [x] Проверка экрана Корзины
- [x] Проверка календаря
- [x] Проверка сортировки
- [x] Проверка меню
- [x] Проверка экрана Цвета

## Ограничения проекта
Файл apk взят из открытого источника. Приложение установлено на сервер Browserstack. <br/>
Также реализован локальный прогон тестов.

#### Пример запуска из командной строки
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=local_emulator
```
Для запуска в эмуляторе необходимо:
- Запустить девайс Android Virtual Device
- Запустить Appium Server
- Запустить команду для запуска тестов

Тесты запускаются по <a target="_blank" href="http://localhost:4723/wd/hub">адресу</a>
## Этапы реализации

### 1. Формирование тест-кейсов в Allure Test Ops
<img src="/design/images/manual_list.png"><br/></br>

### 2. Структура проекта
- Папка **utils** - файлы для выбора девайса, прикрепления результатов выполнения тестов
- Папка **tests** - файлы с тестами
- Папка **apk** - файл с тестируемым приложением
- Файлы **.env** - конфигурационные файлы
- Файл **config.py** - основной конфигурационный файл
- Файл **pytest.ini** - конфигурационный файл Pytest
- Файл **requirements.txt** - подключение библиотек

<img src="/design/images/str.png">

### 3. Настройка сборки
<a target="_blank" href="https://jenkins.autotests.cloud/job/014_azavrichko-mobile_diplom"> Ссылка на сборку в Jenkins</a><br/><br/> 
<img src="/design/images/jenkins.png">


### 4. Результат выполнения
Итоговые результаты сгруппированы в Dashboard для удобства локализации дефектов по основным функциям приложения.<br/><br/>  
<img src="/design/images/dashboard1.png">
<img src="/design/images/dashboard2.png">

### Пример видеозаписи прохождения теста на эмуляторе мобильного устройства
![This is an image](/design/images/mobile_test.gif)

### Пример выполнения теста в **Browserstack**
<img src="/design/images/browserstack.png">

### Пример результата теста в **Allure Report**
<img src="/design/images/allureReport.png">

### Пример результатов теста в **Allure Report** по времени
<img src="/design/images/time.png">

### Пример результатов теста в **Allure Report** по Timeline
<img src="/design/images/timeline.png">

### Пример дашборда в **Allure TestOps**
<img src="/design/images/testops_dashboards.png">

### Пример запуска в **Allure TestOps**
<img src="/design/images/run.png">

### 5. Оповещения
После выполнения тестов, приходят оповещения в **telegram** <br/></br>
<img src="/design/images/telegram.png">


:heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
:blue_heart: <a target="_blank" href="https://t.me/qa_automation">t.me/qa_automation</a>
