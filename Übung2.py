# 1) Regular Expression Modul importieren
import re

# 2) Einen regular Expression erschaffen

reg_exp = "Mir geht es [a-z]*"
# [] Zeichen die in dem Wort vorkommen dürfen [abc]
# oder auch [a-c]
# * gibt an, dass die Zeichen kein, oder so oft wie man will verwendet
# werden dürfen

# [a-z]* sagt also, dass die Buchstaben a-z so oft verwendet werden
# können, wie man will.


# 3) Text angeben, der durchsucht werden soll
text = "Mir geht es gut. Mir geht es schlecht."

# METHODEN
# re.match(regulärer Ausdruck, TextDerDurchsuchtWird)
# gibt ein Objekt mit wahr, falsch aus, ob sich der gesuchte Begriff
# in dem Text befindet
ist_die_suche_erfolgreich = re.match(reg_exp,text)
if ist_die_suche_erfolgreich:
    print("Jap der gesuchte Begriff ist dadrin")

# Das Problem dabei ist, wir haben nur untersucht, ob der Begriff
# überhaupt dabei ist, aber nicht, wie oft und welche Treffer genau

# a)
# Dafür verwenden wir zunächst
# re.compile(regExp)
# Diese Methode übersetzt den regulären Ausdruck in ein für den
# Computer verständlicheres Objekt hier Muster oder Pattern genannt

pattern = re.compile(reg_exp)

# b)
# patter.findall()
# Ein Objekt, dass alle Suchtreffer als Liste speichert

such_treffer = pattern.findall(text)

# c)
# die Suchtreffer in dem Text ausgeben lassen:
# enumerate nummeriert hier einfach nur die Treffer mit einem index durch
for index, treffer in enumerate(such_treffer):
    print(f"{index} : {treffer}")

""" Gibt:
0 : Mir geht es gut
1 : Mir geht es schlecht
aus."""

# Verschiedene Gruppensuchentreffer finden
# Wenn man nach mehreren Sachen in einem Text sucht kann man Gruppen
# definieren
# z.B. 