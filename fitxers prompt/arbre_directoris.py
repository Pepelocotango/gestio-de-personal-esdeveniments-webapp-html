#!/usr/bin/env python3
import os

def arbre_simple(directori):
    for arrel, dirs, fitxers in os.walk(directori):
        nivell = arrel.replace(directori, '').count(os.sep)
        indent = ' ' * 4 * nivell
        print(f"{indent}{os.path.basename(arrel)}/")
        subindent = ' ' * 4 * (nivell + 1)
        for f in fitxers:
            print(f"{subindent}{f}")

if __name__ == "__main__":
    arbre_simple(os.getcwd())


# per executar la ordre : python3 arbre_directoris.py #
