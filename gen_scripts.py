from urllib.request import urlopen, Request
import json
import argparse

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('outputtype', choices=["macos", "ahk"])
    p.add_argument('-f', '--file')
    return p.parse_args()

def get_words():
    with urlopen(Request(
        "https://api.linku.la/v1/",
        headers={'User-Agent' : 'Mozilla'})) as r:
        if r.status == 200:
            return json.loads(r.read().decode('utf-8'))
        else:
            exit(1)

get_ucsur = lambda words: (
        (word, chr(int(words[word]['representations']['ucsur'][2:], 16)))
        for word in filter(lambda x: 'ucsur' in words[x]['representations'],  
                           words))

def ahk_script(words):
        return """; ahk script 4.0 from nasin-nanpa

#Requires AutoHotkey v2.0+
#SingleInstance force
#Hotstring O

Hotstring("EndChars", "``")

""" + "\n".join(["::" + i[0] + "::{U+" + str(hex(ord(i[1])))[2:].upper() + "} ; " +  i[1]
                 for i in sorted(words, key=lambda x: len(x[0]), reverse=True)]) +"""
::[::{U+F1990} ; cartouche start
::]::{U+F1991} ; cartouche end

::=::{U+200D} ; default zero width joiner
::+::{U+F1996} ; scaling joiner
::-::{U+F1995} ; stacking joiner

::(::{U+F1997} ; start left-combining (normal) long glyph
::)::{U+F1998} ; end left-combining (normal) long glyph
::_::{U+F1999} ; container extender

::{::{U+F199A} ; start right-combining (reversed) long glyph
::}::{U+F199B} ; end right-combining (reversed) long glyph

::.::{U+F199C} ; sitelen pona full stop
::`:::{U+F199D} ; sitelen pona colon


::`s`s::{U+3000} ; logograph fullwidth space
::<::{U+300C} ; 「 start quote
::>::{U+300D} ; 」 end quote


::~~::{U+FE01} ; variation selector 2
::~::{U+FE00} ; variation selector 1
"""


def mac_os_plugin(words):
    return """METHOD: TABLE
ENCODE: Unicode
PROMPT: sitelen pona (UCSUR)
DELIMITER: ,
VERSION: 3.2
MAXINPUTCODE: 15
VALIDINPUTKEY: aeioujklmnpstw[_].:/+{}

BEGINCHARACTER
[ 󱦐
] 󱦑
_ 󱦒
pi_ 󱦓
___ 󱦔
- ‍
^ 󱦕
+ 󱦖
( 󱦗
) 󱦘
__ 󱦙
{ 󱦚
} 󱦛
. 󱦜
: 󱦝
te 「
to 」
< 「
> 」""" + "\n".join((f"{i[0]} {i[1]}" for i in words)) + "\nENDCHARACTER"


if __name__ == "__main__":
    words = get_words()
    args = parse_args()
    match args.outputtype: 
        case "macos":
            text = mac_os_plugin(get_ucsur(words))
        case "ahk":
            text = ahk_script(get_ucsur(words))
    if args.file:
        with open(args.file, 'w') as f:
            f.write(text)
    else:
        print(text)
