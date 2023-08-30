
👀👌XPath

#Селекторы
Селекторы-потомки
h1	//h1	
div p	//div//p	
ul > li	//ul/li	
ul > li > a	//ul/li/a	 
div > *	//div/*	 
:root	/	
:root > body	/body	 

Селекторы атрибутов
#id	//*[@id="id"]	
.class	//*[@class="class"] …вроде как	 
input[type="submit"]	//input[@type="submit"]	 
a#abc[for="xyz"]	//a[@id="abc"][@for="xyz"]	
a[rel]	//a[@rel]	 
a[href^='/']	//a[starts-with(@href, '/')]	
a[href$='pdf']	//a[ends-with(@href, '.pdf')]	 
a[href*='://']	//a[contains(@href, '://')]	 
a[rel~='help']	//a[contains(@rel, 'help')] ... вроде как	 

Селекторы порядка
ul > li:first-of-type	//ul/li[1]	
ul > li:nth-of-type(2)	//ul/li[2]	 
ul > li:last-of-type	//ul/li[last()]	 
li#id:first-of-type	//li[1][@id="id"]	
a:first-child	//*[1][name()="a"]	 
a:last-child	//*[last()][name()="a"]	 

Братья и сестры
h1 ~ ul	//h1/following-sibling::ul	
h1 + ul	//h1/following-sibling::ul[1]	 
h1 ~ #id	//h1/following-sibling::[@id="id"]	 

jQuery
$('ul > li').parent()	//ul/li/..	
$('li').closest('section')	//li/ancestor-or-self::section	 
$('a').attr('href')	//a/@href	
$('span').text()	//span/text()	 

Другие вещи
h1:not([id])	//h1[not(@id)]	
Совпадение текста	//button[text()="Submit"]	
Совпадение текста (подстрока)	//button[contains(text(),"Go")]	 
Арифметика	//product[@price > 2.50]	 
Имеет дочерние элементы	//ul[*]	 
Имеет дочерние элементы (определенные)	//ul[li]	 
Или логика	//a[@name or @href]	
Объединение (объединяет результаты)	//a | //div	

Проверка класса
//div[contains(concat(' ',normalize-space(@class),' '),' foobar ')]
В Xpath нет оператора “проверить, является ли список частью списка, разделенного пробелами”, поэтому это обходной путь (Источник).

#Выражения
Шаги и оси
//	ul	/	a[@id='link']
Ось	Шаг	Ось	Шаг
Префиксы
Префикс	Пример	Что
//	//hr[@class='edge']	Где угодно
./	./a	Относительный
/	/html/body/div	Корень
Начните свое выражение с любого из них.

Оси
Ось	Пример	Что
/	//ul/li/a	Дочерний элемент
//	//[@id="list"]//a	Потомок
Разделяйте свои шаги с помощью /. Используйте two (//), если вы не хотите выбирать прямых дочерних элементов.

Шаги
//div
//div[@name='box']
//[@id='link']
Шаг может иметь имя элемента (div) и предикаты ([...]). Оба являются необязательными. Они также могут быть этими другими элементами:

//a/text()     #=> "Go home"
//a/@href      #=> "index.html"
//a/*          #=> All a's child elements
#Предикаты
Предикаты
//div[true()]
//div[@class="head"]
//div[@class="head"][@id="top"]
Ограничивает набор узлов, только если выполняется какое-либо условие. Они могут быть объединены в цепочку.

Операторы
# Comparison
//a[@id = "xyz"]
//a[@id != "xyz"]
//a[@price > 25]
# Logic (and/or)
//div[@id="head" and position()=2]
//div[(x and y) or not(z)]
Используйте операторы сравнения и логики для создания условий.

Использование узлов
# Use them inside functions
//ul[count(li) > 2]
//ul[count(li[@class='hide']) > 0]
# This returns `<ul>` that has a `<li>` child
//ul[li]
Вы можете использовать узлы внутри предикатов.

Индексирование
//a[1]                  # first <a>
//a[last()]             # last <a>
//ol/li[2]              # second <li>
//ol/li[position()=2]   # same as above
//ol/li[position()>1]   # :not(:first-of-type)
Использовать [] с числом, или last() или position().

Порядок цепочки
a[1][@href='/']
a[@href='/'][1]
Порядок важен, эти два отличаются.

Вложенные предикаты
//section[.//h1[@id='hi']]
Это возвращает <section> если у него есть <h1> потомок с id='hi'.

#Функции
Функции узла
name()                     # //[starts-with(name(), 'h')]
text()                     # //button[text()="Submit"]
                           # //button/text()
lang(str)
namespace-uri()
count()                    # //table[count(tr)=1]
position()                 # //ol/li[position()=2]
Логические функции
not(expr)                  # button[not(starts-with(text(),"Submit"))]
Строковые функции
contains()                 # font[contains(@class,"head")]
starts-with()              # font[starts-with(@class,"head")]
ends-with()                # font[ends-with(@class,"head")]
concat(x,y)
substring(str, start, len)
substring-before("01/02", "/")  #=> 01
substring-after("01/02", "/")   #=> 02
translate()
normalize-space()
string-length()
Преобразование типов
string()
number()
boolean()
#Оси
Использование осей
//ul/li                       # ul > li
//ul/child::li                # ul > li (same)
//ul/following-sibling::li    # ul ~ li
//ul/descendant-or-self::li   # ul li
//ul/ancestor-or-self::li     # $('ul').closest('li')
Этапы выражения разделяются символом /, обычно используемым для выбора дочерних узлов. Это не всегда верно: вы можете указать другую “ось” с помощью ::.

//	ul	/child::	li
Ось	Шаг	Ось	Шаг
Дочерняя ось
# both the same
//ul/li/a
//child::ul/child::li/child::a
child:: является осью по умолчанию. Это заставляет //a/b/c работать.

# both the same
# this works because `child::li` is truthy, so the predicate succeeds
//ul[li]
//ul[child::li]
# both the same
//ul[count(li) > 2]
//ul[count(child::li) > 2]
Ось "Потомок" или "я"
# both the same
//div//h4
//div/descendant-or-self::h4
// является сокращением от оси descendant-or-self:: .

# both the same
//ul//[last()]
//ul/descendant-or-self::[last()]
Другие оси
Ось	Сокращение	Примечания
ancestor	 	 
ancestor-or-self	 	 
attribute	@	@href является сокращением от attribute::href
child	 	div является сокращением от child::div
descendant	 	 
descendant-or-self	//	// является сокращением от /descendant-or-self::node()/
namespace	 	 
self	.	. является сокращением от self::node()
parent	..	.. является сокращением от parent::node()
following	 	 
following-sibling	 	 
preceding	 	 
preceding-sibling	 	 
Вы можете использовать другие оси.

Объединения
//a | //span
Используйте | для объединения двух выражений.

#Еще примеры
Примеры
//*                 # all elements
count(//*)          # count all elements
(//h1)[1]/text()    # text of the first h1 heading
//li[span]          # find a <li> with an <span> inside it
                    # ...expands to //li[child::span]
//ul/li/..          # use .. to select a parent
Найдите родителя
//section[h1[@id='section-name']]
Находит<section>, который непосредственно содержит h1#section-name

//section[//h1[@id='section-name']]
Находит, <section> который содержит h1#section-name. (То же, что и выше, но использует потомка-или-себя вместо дочернего элемента)

Ближайший
./ancestor-or-self::[@class="box"]
Работает так же, как в jQuery $().closest('.box').

Атрибуты
//item[@price > 2*@discount]
Находит <item> и проверяет его атрибуты


