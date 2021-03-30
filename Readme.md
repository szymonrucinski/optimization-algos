Cel
===

<span>Celem zadania bylo zaimplementowanie oraz porównanie skuteczności
2 metod optymalizacji funkcji jednowymiarowej: metody bisekcji oraz
dychotomii.</span>

Wprowadzenie
============

<span>Celem implementacji jest znalezienie minimum funkcji w danym
przedziale czyli najmniejszej liczby w zbiorze wartości funkcji $f(x)$.
W celu znalezienia minimum wykorzystaliśmy 2 różne od siebie algorytmy:
bisekcje oraz dychotomie.</span>

Bisekcja
--------

<span>Pierwszym krokiem w metodzie bisekcji jest wyznaczenie przedziału
nieufności ${L_0= \{a,b}\}$. Wspomniany przedział dzielimy na 4
ćwiartki, wyznaczając następujące punkty:$a,x_1,x_0,x_2,b$. Gdzie
${x_0 =}$ $ \frac{a+b}{2} $</span> to środek przedziału. Następnie
liczymy wartość funkcji dla punktów $x_1, x_2, x_0$ oraz definiujemy
$\varepsilon$ dokładność wyniku.Kolejno sprawdzamy czy funkcja rośnie
lub maleje na danym odcinku porównując wartości $f(x_1),f(x_0), f(x_2)$.
W ten sposób określamy gdzie leży minimum. Jeżeli uzyskamy przedział,
który spełnia kryterium stopu $L < 2$$\varepsilon$ gdzie $L=b-a$ to
zwracamy wynik, jeżeli nie to rozpoczynamy proces od nowa.

Dychotomia
----------

<span>W metodzie dychotomii, podobnie jak przy bisekcji, najpierw
wyznaczany jest przedział ufności ${L_0= \{a,b\}}$. Następnie wyznaczany
jest środek tego przedziału ${x_0 =}$ $ \frac{a+b}{2} $ oraz punkty
$x_1$ i $x_2$, które powstają przed odjęcie i dodanie wartości
$ \delta $ podanej przez użytkownika. Porównywane są wartości funkcji w
punkcie $x_1$ oraz $x_2$, a następnie na tej podstawie określa się po
której stronie punktu $x_0$ znajduje się minimum. Drugą połowę
przedziału odrzuca się i taką samą operację powtarza się na nowym
przedziale.</span>

Opis implementacji
==================

<span>Zadanie zostało zrealizowane w języku programowania Python.
Interfejs graficzny został stworzony za pomocą wbudowanej biblioteki
Tkinter. Do prezentowania wykresów użyliśmy biblioteki matplotlib.
Użytkownik wprowadza z poziomu GUI funkcje dla, której ma być policzone
minimum oraz $\varepsilon$, liczbę interacji, metodę optymalizacji oraz
granice przedziału $a,b$.</span>

![image](Images/gui.png) ![image](Images/graph1.png)

Czerwonym punktem na wykresie zostaje oznaczone minimum czarne zaś linie
ilustrują przedziały pośrednie, wyznaczane w trakcie kolejnych iteracji.
Projekt został zrealizowany proceduralne nie obiektowo.

Materiały i metody
==================

Eksperymenty zostaly kolejno wykonane na komputerze z uzyciem
stworzonego przez nas programu komputerowego,w którym implementujemy
wyszczególnione poniżej metody minimalizacji funkcji jednej zmiennej:

1.  Bisekcja

2.  Dychotomia

Wyniki
======

W tej sekcji przedstawimy serię eksperymentów sprawdzających poprawność
działania programu, oraz jego umiejętność radzenia sobie z niepoprawnymi
danymi (na przykład z funkcjami w nieunimodalnych przedziałach).

W pierwszym eksperymencie zostały przetestowane obie metody w celu
sprawdzenia umiejętności znalezienia minimum w funkcjach kwadratowych w
przedziałach unimodalności. W pierwszej części algorytmy zostały
przetestowane dla dużej dokładności, a w drugiej dla małej dokładności.
Setup do pierwszej części został przedstawiony na Rysunku
[setup~w~ysoka~d~okladnosc].

![image](Images/kwadratowa wysoka dokładność bisekcja setup.png)
[setup~w~ysoka~d~okladnosc]

Poniżej na Rysunku [bisekcja~w~ysoka~d~okladnosc] i Rysunku
[dychotomia~w~ysoka~d~okladnosc] zostały przedstawiony wykresy
wygenerowane przez program. Zielone lub czarne kreski przedstawiają
przedziały, które były brane pod uwagę przy wyznaczaniu minimum.
Czerwone kropki lub kreski pokazują przedział ufności znalezionego
minimum.

![image](Images/kwadratowa wysoka dokładność bisekcja wykres.png)
[bisekcja~w~ysoka~d~okladnosc]

![image](Images/kwadratowa wysoka dokładność dychotomia wykres.png)
[dychotomia~w~ysoka~d~okladnosc]

Jak widać, przy wysokiej dokładności nie jesteśmy w stanie stwierdzić,
która z metod radzi sobie lepiej z wyznaczaniem minimum. Na Rysunku
[setup~m~ala~d~okladnosc] przedstawiony został setup do drugiej części
eksperymentu. Tym razem przetestowana została mała dokładność
przejawiająca się mniejszą liczbą dopuszczalnych iteracji oraz
zwiększeniem wartości epsilon. Wyniki pokazane są na Rysunkach
[bisekcja~m~ala~d~okladnosc] i [dychotomia~m~ala~d~okladnosc].

![image](Images/kwadratowa_mała_dokładność_bisekcja_setup.png)
[setup~m~ala~d~okladnosc]

![image](Images/kwadratowa mała dokładność bisekcja wykres.png)
[bisekcja~m~ala~d~okladnosc]

![image](Images/kwadratowa mała dokładność dychotomia wykres.png)
[dychotomia~m~ala~d~okladnosc]

Jak widać zmniejszenie dokładności źle wpłynęło na precyzję metody
bisekcji, jednak nie spowodowało prawie w ogóle zmiany w przypadku
dychotomii, która dosyć precyzyjnie wyznaczyła przedział ufności minimum
lokalnego.

Drugi eksperyment polegał na podaniu funkcji, która nie jest unimodalna
w przedziale. Program miał za zadanie poszukać przedziału unimodalności
w niej i wypisać go w konsoli jeśli taki występował. Na Rysunku
[setup~n~ieunimodalna] możemy zobaczyć setup eksperymentu. Podajemy
funkcję trzeciego stopnia z jednym minimum lokalnym, ale w
nieunimodalnym przedziale. Rysunek [wynik~n~ieunimodalna] przedstawia
wynik wyświetlony w konsoli po próbie znalezienia minimum w tym
przedziale.

![image](Images/nieunimodalna setup.png) [setup~n~ieunimodalna]

![image](Images/nieunimodalna wynik.png) [wynik~n~ieunimodalna]

Trzeci eksperyment sprawdzał zachowanie algorytmu kiedy podana funkcja
nie ma minimum lokalnego, czyli jest na przykład stała. Setup do tego
eksperymentu można zobaczyć na Rysunku [setup~s~tala], a wynik w konsoli
na Rysunku [wynik~s~tala].

![image](Images/stała setup.png) [setup~s~tala]

![image](Images/stała wynik.png) [wynik~s~tala]

Ostatnim eksperymentem było podanie funkcji czwartego stopnia, która
posiada 2 minima lokalne. Program niestety nie poradził sobie ze
stwierdzeniem tego, że funkcja nie jest unimodalna w tym przedziale i
obliczył jedno z ekstremów. Setup do tego eksperymentu jest
przedstawiony na Rysunku [setup~c~zwartego], a wynikowy wykres na
Rysunku [wynik~c~zwartego].

![image](Images/nieunimodalna_bład_setup.png) [setup~c~zwartego]

![image](Images/nieunimodalna błąd wykres.png) [wynik~c~zwartego]

Dyskusja
========

Pierwszy eksperyment pokazuje, że obydwie funkcje działają i znajdują
lokalne minima bez większego problemu. Przy wysokiej dokładności nie
można wskazać różnic między ich działaniem, ponieważ wyznaczone przez
nie przedziały są bardzo podobne. Różnice widać dopiero przy drugiej
części eksperymentu gdzie dokładność jest mniejsza. Obydwie metody przy
każdej iteracji odrzucają połowę przedziału, więc szerokość ostatecznych
przedziałów jest taka sama. Jednak przy małej dokładności można
zaobserwować działanie obu algorytmów. Bisekcja może odrzucić prawą,
lewą albo połowę lewej i połowę prawej strony co widać na Rysunku
[bisekcja~m~ala~d~okladnosc]. Ostateczny przedział jest 2 razy mniejszy
od poprzedniego przedziału i leży dokładnie w jego środku. Dychotomia
może odrzucić tylko lewą albo prawą połowę przedziału i to ilustruje
Rysunek [dychotomia~m~ala~d~okladnosc]. Granica ostatecznego przedziału
leżąca w punkcie $x=0,5$ jest jednocześnie granicą poprzednio
rozpatrywanego przedziału. Ten przykład pokazuje, że bisekcja może
zapewniać większą precyzję oszacowania dokładnego punktu minimum,
ponieważ dzięki niej prawdopodobieństwo, że będzie on leżał po środku
ostatniego przedziału jest większe.

Drugi oraz trzeci eksperyment pokazują prawidłowość działania algorytmu
kiedy początkowy przedział funkcji nie jest unimodalny. Algorytm po
wykryciu tego stara się znaleźć przedział unimodalności w tym zakresie
funkcji i jeśli taki znajdzie wypisuje go w konsoli.

Czwarty eksperyment pokazuje niedoskonałości programu. Algorytm
twierdzi, że przedział funkcji jest unimodalny mimo że funkcja posiada 2
minima w tym zakresie (Rysunek [wynik~c~zwartego].

Wnioski
=======

Zarówno bisekcja jak i dychotomia zapewniają bardzo podobną precyzję
wyznaczania ekstremów funkcji. Bisekcja jednak posiada możliwość
bardziej elastycznego odrzucania przedziałów przez co lepsze oszacowanie
punktu minimum na podstawie ostatniego wyznaczonego przedziału jest
bardziej prawdopodobne.

Program używając obydwu metod nie ma problemów ze znalezieniem ekstremów
w podanych funkcjach. Rzeczą, którą należałoby poprawić jest algorytm
sprawdzający czy funkcja w podanym przedziale jest unimodalna. Na chwilę
obecną funkcja nie jest w stanie określić tego ze stu-procentową
pewnością.

## *Bibliografia*
1 - Alicja Romanowicz *Minimalizacja funkcji jednej
zmiennej*, dostępny online.
<https://ftims.edu.p.lodz.pl/pluginfile.php/162148/mod_resource/content/2/Minimalizacja%20funkcji%20jednej%20zmiennej>.

2 - Douglas J. Wilde *Optimum Seeking Methods*, 1964, dostępny online.
<https://archive.org/details/optimumseekingme00wild/page/n5/mode/2up>.
