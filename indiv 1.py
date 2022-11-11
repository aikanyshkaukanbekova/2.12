#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pink(func):
    import re

    def pnk(chars=" !?"):

        print(chars)

        h = func(s)
        rx = re.compile('[ !?]')
        hh = rx.sub('-', h)
        print(hh)
        ch = re.sub(r'-+', '-', hh)
        print(ch)

    return pnk


@pink
def wrapper(text):
    p = text.lower()
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
         'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
         'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
         'я': 'ya'}
    return p.translate({ord(key): t[key] for key in t})


if __name__ == "__main__":
    s = 'Б щ --- ! ? - ?Барабанщик сильно занят, Барабанщик барабанит: \
    – Та-ра-ра, та-ра-ра,\
     На прогулку нам пора!'

    x = wrapper(s)