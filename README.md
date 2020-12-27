# algorithm-lab
1. clone my repository: 
(if you are working with a console)
```
https://github.com/Maria-Sparrow/algorithm-lab.git
```
* or download and extract it;

2. open command prompt and switch the directory to **/algorithm-lab**:
```
cd algorithm-lab
```
* if you decided to download and extract it to, let us say, D:/projects, you would do it like that:
```
D:
```
```
cd projects/algorithm-lab
```


3. if you do not have Phyton 3+ installed, you must use the console:
```
python main.py
```

***
Iндiана Джонс i останнiй прямокутний обхiд Код задачi: IJONES 
В пошуках Святого Грааля Iндiана Джонс зiткнувся з небезпечним випробуванням. Йому потрiбно пройти крiзь прямокутний коридор, який складається з крихких плит (пригадайте сцену з фiльму «Iндiана Джонс i останнiй хрестовий похiд»). На кожнiй плитi написана одна лiтера: 
a a a 
c a b 
d e f 
Можна починати з будь-якої плити в найлiвiшому стовпцi. Виходом iз коридору є верхня права та нижня права плити (для прикладу вище — a та f). 
Iндiана спритний, i може переходити не лише на сусiдню плиту, а й перестрибувати через кiлька плит. Проте, щоб не провалитися крiзь пiдлогу, вiн повинен дотримуватися таких правил: 
1. Пiсля кожного кроку Iндiана повинен опинятися правiше, нiж був перед цим. a a a 
c a b 
d e f 
2. Завжди можна переходити на одну плиту праворуч. 
a a a 
c a b 
d e f 
3. Крiм руху на одну плиту праворуч, можна перестрибувати, проте лише на ту саму лiтеру. Наприклад, з лiтери a можна перестрибнути на будь-яку iншу лiтеру a за умови, що ми цим ходом просунемося правiше. 
a a a 
c a b 
d e f 

Для заданого коридору, пiдрахуйте, скiльки всього iснує способiв пройти його успiшно. 
Вхiднi данi 
Вхiдний файл ijones .in складається з H + 1 рядкiв. 
• Перший рядок мiстить два числа W i H, роздiленi пробiлом: W — ширина коридору, H — висота коридору, 1  W, H  2000. 
• Кожен з наступних H рядкiв мiстить слово довжиною W символiв, яке складається з малих латинських лiтер вiд a до z. 
Вихiднi данi 
Вихiдний файл ijones .out повинен мiстити одне цiле число — кiлькiсть рiзних шляхiв для виходу з коридору. 
# Див. приклади нижче # 

Приклад 1 
ijones .in 
3 3 
aaa 
cab 
def 
ijones .out 
5 
Пояснення: Iснує 3 варiанти обходу, якщо починати з лiтери a, i по одному варiанту, якщо починати з лiтери c або d. 
Приклад 2 
ijones .in 
10 1 
abcdefaghi 
ijones .out 
2 
Приклад 3 
ijones .in 
7 6 
aaaaaaa 
aaaaaaa 
aaaaaaa 
aaaaaaa 
aaaaaaa 
aaaaaaa 
ijones .out 
201684 
