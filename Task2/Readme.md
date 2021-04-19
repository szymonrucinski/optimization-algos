# Metoda quasi-Newtona w wersji Davidon-Fletcher-Powell (DFP)

### GUI:
Wybór kryterium stopu:
- [ ]  Podaj liczbę iteracji.
- [ ]  Brak znaczących postępów w kolejnych iteracjach, gdzie pojęcie "postępu" jest zależne od implementowanego wariantu.
### Wprowadzanie danych:
- [ ]  Wprowadz funkcję o liczbie argumentów równej 2 tylko w GUI
### Wykresy:
- [ ] Narysuj wykres funkcji
- [ ] Wyniki pośrednie powinny być wyświetlane w GUI albo na konsoli.
- [ ] Zaznacz na wykresie poszczególne etapy znajdowania rozwiązania
- [ ]  Ponadto program powinien umożliwiać kliknięcie dowolnego miejsca na wykresie i odczytanie dokładnych współrzędnych punktu wraz z wartością funkcji we wskazanym punkcie.

### Co robi i jak działa algorytm???
### Hessian:
Macierz cząstkowych pochodnych, fukcji f.
### Motywacja:
Oszacowanie Hessiana jest niepraktycznego i zajmuje bardzo dużo czasu.
### Pomysł:
Użyj aproksymacji w celu oszacowania "inverse Hessian"

https://github.com/Rachnog/Optimization-Algorithms/blob/master/Davidson-Fletcher-Powell.py