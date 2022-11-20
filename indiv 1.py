#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pink(func):

    def pnk(text, chars=" !?"):

        print(text)

        h = ''.join(map(lambda x: x if x not in chars else '-', func(text)))
        print(h)
        while '--' in h:
            h = h.replace('--', '-')
        print(h)
        return h


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
    s = 'Я щ --- ! ? - ?помню чудное мгновенье: Передо мной явилась ты, \
    Как мимолетное виденье,\
     Как гений чистой красоты.'

    x = wrapper(s)
