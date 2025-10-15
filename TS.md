Кароя делай новую прилу.
Внутри пока что три аппы
projects
buildings
properties


Корневые файлы типо settings urls выносишь в папку config рядом с другими прилами


В projects делаешь модель Project
Это будет типо ЖК.
Поля там 
name,
slug
type - тут делаешь селект и варианты селекты выносишь в константу в файле constants
Ну и пока что все

В Buildings делаешь следующие модели, разнося их в разные файлы моделей в папке models
Building - Корпус
Поля 
project
number 
commission_date - срок сдачи

Section - Секция/Подьезд
project
building 
number
floor_count

Floor - этаж
project 
building 
section
number




Properties - Объекты собственности
Делаешь модель Property
project
building 
section
floor
number 
area
price
status - в константу выносишь селекты ( В продаже, продано, забронировано)
type - в константу выносишь селекты ( Квартира, апартаменты, парковочное место, коммерческое помещение)



А, и ко всем моделям докинь поле is_active - Активно тупо булевое