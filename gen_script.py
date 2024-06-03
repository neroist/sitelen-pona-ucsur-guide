from ruamel.yaml.scalarstring import SingleQuotedScalarString as sq
from ruamel.yaml.comments import CommentedSeq
from urllib.request import urlopen, Request
import ruamel.yaml
import argparse
import datetime
import uuid
import json
import io
import os

long_to_short = {"kijetesantakalu":"kij","nanpa":["nnp","#"],"lili":["lil","v"],"sina":["sna","b"],"wile":["wil","w"],"ijo":["ijo","0"],"wan":["wan","1"],"kin":["kin","!"],"kokosila":"kks","misikeke":"msk","mi":["mi","p"],"pi":["pi","L"],"tu":["tu","2"],"kepeken":"kpk","sitelen":"stl","monsuta":"mon","kalama":"klm","kulupu":"klp","pakala":"pkl","palisa":"pls","pimeja":"pmj","sijelo":"sjl","sinpin":"snp","soweli":"swl","namako":"nmk","kipisi":"kps","majuna":"maj","jasima":"jas","lanpan":"lan","akesi":"aks","alasa":"als","apeja":"ape","kiwen":"kwn","linja":"lnj","lukin":"lkn","monsi":"mns","nasin":"nsn","pilin":"pln","tenpo":"tnp","utala":"utl","tonsi":"tns","epiku":"epk","anpa":"anp","ante":"ant","awen":"awn","esun":"esn","insa":"ins","jaki":"jak","jelo":"jel","kala":"kal","kama":"kam","kasi":"kas","kili":"kil","kule":"kul","kute":"kut","lape":"lap","laso":"las","lawa":"law","lete":"let","lipu":"lip","loje":"loj","luka":"luk","lupa":"lup","mama":"mam","mani":"man","meli":"mel","mije":"mij","moku":"mok","moli":"mol","musi":"mus","mute":"mut","nasa":"nas","nena":"nen","nimi":"nim","noka":"nok","olin":"oln","open":"opn","pake":"pak","pali":"pal","pana":"pna","pini":"pin","pipi":"pip","poka":"pka","poki":"pki","pona":"pon","powe":"pow","sama":"sam","seli":"sli","selo":"slo","seme":"sem","sewi":"sew","sike":"sik","sona":"son","suli":"sul","suno":"sun","supa":"sup","suwi":"suw","taso":"tas","tawa":"taw","telo":"tel","toki":"tok","tomo":"tom","unpa":"unp","walo":"wal","waso":"was","wawa":"waw","weka":"wek","leko":"lek","soko":"sok","meso":"mes","ala":"ala","ale":"ale","anu":"anu","ike":"ike","ilo":"ilo","jan":"jan","ken":"ken","kon":"kon","len":"len","lon":"lon","mun":"mun","ona":"ona","pan":"pan","sin":"sin","tan":"tan","uta":"uta","oko":"oko","en":"en","jo":"jo","ko":"ko","la":"la","li":"li","ma":"ma","mu":"mu","ni":"ni","pu":"pu","te":"te","to":"to","ku":"ku","a":"a","e":"e","o":"o","n":"n","ali":"ali"}
gen_header = f"-*- Generated by {os.path.basename(__file__)} -*-"
sort_key = lambda x: len(x)


def parse_args():
    p = argparse.ArgumentParser(description="Python script to create input plugins from linku dictionary")
    p.add_argument('outputtype', choices=["macos", "ahk", "ibus", "espanso"])
    p.add_argument('-f', '--file', help="What file to output to. Uses stdout by default")
    p.add_argument('-t', '--ahk-toggle', help="Whether or not to output the toggle variant of the AHK script", action='store_true')
    p.add_argument('-e', '--end-chars', help="What end/word-separator characters to use (only supported for AHK and Espanso)")
    p.add_argument('-s', '--short', help="Whether to use short aliases for the words", action='store_true')
    return p.parse_args()


def get_words():
    request = Request("https://api.linku.la/v1/words", headers={'User-Agent' : 'Mozilla'})

    with urlopen(request) as r:
        if r.status == 200:
            return json.loads(r.read().decode('utf-8'))
        else:
            exit(1)


def get_ucsur(words) -> list:
    filter_fn = lambda x: 'ucsur' in words[x]['representations']
    result = []

    for word in filter(filter_fn, words):
        codepoint = int(words[word]['representations']['ucsur'][2:], 16)
        result.append((word, chr(codepoint)))

    return result

# TODO reduce code duplication (only if this was nim...)
def to_short(word: str) -> list[str]:
    val = long_to_short[word]

    if type(val) is str:
        return [val]

    return val


def espanso(words, short: bool = False, end_chars: str | None = "") -> str:
    def match(trigger: str, replace: str) -> dict:
        # force into double-quoted string for consistency
        if end_chars is None:
            return {"trigger": sq(trigger), "replace": sq(replace), "word": True}
        else:
            return {"trigger": sq(trigger), "replace": sq(replace), "word": True, "word_separators": list(end_chars)}

    def matches(triggers: list[str], replace: str) -> dict:
        if end_chars is None:
            return {"trigger": triggers, "replace": sq(replace), "word": True}
        else:
            return {"trigger": triggers, "replace": sq(replace), "word": True, "word_separators": list(end_chars)}

    yaml = ruamel.yaml.YAML(typ=['rt', 'string'])
    yaml.allow_unicode = True
    yaml.encoding = 'utf-8'
    yaml.default_flow_style = False
    yaml.block_seq_indent = 2
    yaml.indent = 4

    # python uses lazy evaluation, so this runs (`len()` is not defined for `None`)
    if end_chars is None or len(end_chars) == 0:
        end_chars = " "

    matches_dict = {"matches": [
        match("zz", "　"), match("  ", "　"), match("-", "‍"),  match("^", "󱦕"),  match("*", "󱦖"),
        match(":", "󱦝"),   match(".", "󱦜"),   match("[", "󱦐"),  match("]", "󱦑"),  match("<", "「"),
        match(">", "」"),  match("(", "󱦗"),   match(")", "󱦘"),  match("{", "󱦚"),  match("}", "󱦛")
    ]}

    # store len to use as a "key" when adding comments
    punctuation_len = len(matches_dict["matches"])

    for i in words:
        if short: keys = to_short(i[0])
        else: keys = [i[0]]

        if len(keys) == 1:
            matches_dict["matches"].append(matches(keys[0], i[1]))
        else:
            matches_dict["matches"].append(match(keys[0], i[1]))

    words_len = len(matches_dict["matches"])

    # use `+=` and a list if this needs to be extended
    # rather have a json array, but this works fine
    matches_dict["matches"] += [
        {"triggers": ["msa", "misonala", "misonaala"], "replace": "󱤴󱥡󱤂", "word": True, "word_separators": end_chars}
    ]

    ## sort_key = lambda x: len(x["trigger"]) if "trigger" in x else len(str(['triggers']))
    ## matches["matches"].sort(key=sort_key, reverse=True)

    # translate into `CommentedSeq` so we can add comments
    matches_dict["matches"] = CommentedSeq(matches_dict["matches"])

    # add comments
    for i in range(1, len(matches_dict["matches"])):
        matches_dict["matches"].yaml_set_comment_before_after_key(i, before='\n')

    matches_dict["matches"].yaml_set_comment_before_after_key(0, before="punctuation etc", indent=2)
    matches_dict["matches"].yaml_set_comment_before_after_key(punctuation_len, before="nimi ale", indent=2)
    matches_dict["matches"].yaml_set_comment_before_after_key(words_len, before="contractions", indent=2)

    # init stream for use with `yaml.dump`
    buf = io.BytesIO()
    yaml.dump(matches_dict, buf)

    return f"# {gen_header}\n\n" + buf.getvalue().decode() # yaml.dump_to_string(matches, add_final_eol=True)


def ibus_table(words, short: bool = False) -> str:
    def to_ibus_fmt(words):
        result = []

        for i in words:
            keys = to_short(i[0]) if short else [i[0]]
            result += [f"{key}\t{i[1]}\t1" for key in keys]

        result.sort(key=sort_key, reverse=True)
        return "\n".join(result)

    table_id = str(uuid.uuid4())
    now = datetime.datetime.now().strftime("%Y%m%d")
    table = f"""### {gen_header}

### File header must not be modified
### This file must be encoded into UTF-8.
### This table under LGPL
### comments start with ### not single #
### Derive from the format of SCIM Table, so you can modify the table from
### scim-tables' table
SCIM_Generic_Table_Phrase_Library_TEXT
VERSION_1_0

### Begin Table definition.
BEGIN_DEFINITION

### License
LICENSE = LGPL

### An unique id to distinguish this table among others.
### Use uuidgen to generate this kind of id.
UUID = {table_id}

### A unique number indicates the version of this file.
### For example the last modified date of this file.
### This number must be less than 2^32.
### Just make your table version-able
SERIAL_NUMBER = {now}

### ICON can be any format as long as your pygtk can recognized
### the most widely ones are "png" and "svg", letter one is recommended
ICON = ibus-table.svg

### The symbol to be displayed in IM switchers
SYMBOL = 󱥬

### The default name of this table, this is needed
NAME = sitelen pona 4.0

### The local names of this table, this is optional
### NAME.zh_CN = 形码
### NAME.zh_HK = 形碼
### NAME.zh_TW = 形碼

### Description
DESCRIPTION = sitelen pona input method for IBus, ported from nasin-nanpa's ahk script.

### Supported languages of this table
### sigle "zh_CN" just be recognized as zh_CN,
### but "zh_CN, zh_HK" or more zh_XX will be recognized as zh;
### and "en_US, zh_CN" will be just ignored.
LANGUAGES = en_US

### The author of this table
AUTHOR = jan Komi

### Prompt string to be displayed in the status area, CN will be replaced by
### the gettext tools in runtime as 中.
STATUS_PROMPT = toki

### Valid input chars.
VALID_INPUT_CHARS = ()*+-.:<>[]_aeijklmnopstuwz{{}}~

### Layout
LAYOUT = us

### The max number of input keys for every phrase or character.
MAX_KEY_LENGTH = 20

### Use auto_commit mode as default
AUTO_COMMIT = TRUE

### Automatically selects the first phrase when typing
AUTO_SELECT = FALSE

### Use full width punctuation by default
DEF_FULL_WIDTH_PUNCT = FALSE
### Not use full width letter by default
DEF_FULL_WIDTH_LETTER = FALSE

### Whether user are allow to define phrase, default is true
### You have to define the word construction rules below.
### For input methods which do not input phrases, set this to False
USER_CAN_DEFINE_PHRASE = FALSE

### Whether support PinYin Mode, default is true.
### this feature is just for Chinese, set it to False if your IM is not
### Chinese.
PINYIN_MODE = FALSE

### If true then the phrases' frequencies will be adjusted dynamically
### according your using frequency.
DYNAMIC_ADJUST = TRUE 

### Some characters whose frequencies should be fix all the time, e.g. 
### some punctuations
### NO_CHECK_CHARS = 

### Rules for constructing user defined phrase
### "ce" stands for "ci equal", a Chinese English :), means "phrase length
### equal to", thus ce2 -> phrase length equal to 2; and "ca" means "phrase
### length equal or above", so ca4 -> phrase length equal or above 4.
### p21 -> the 1st key of 2nd character in the phrase, and so on.
### Each rule separate via ";". 
### Example below is a complete rule-set, 
### becuase [2,2] ∩ [3,3] ∩ [4,+∞] = [2,+∞], which is the range of length
### of phrase. This have to be satisfied if you need ibus-table to build up
### your own inputed phrase via your daily using.
### RULES = ce2:p11+p12+p21+p22;ce3:p11+p21+p22+p31;ca4:p11+p21+p31+p41

### The key strokes to page up the lookup table.
### PAGE_UP_KEYS = Page_Up,KP_Page_Up,minus,comma

### The key strokes to page down.
### PAGE_DOWN_KEYS = Page_Down,KP_Page_Down,equal,period

### The key strokes to select candidiate phrases.
### Usually "1,2,3,4,5,6,7,8,9" but if this conflicts with
### characters one wants to use for input one can also
### use something like “F1,F2,F3,F4,F5,F6,F7,F8,F9”
SELECT_KEYS = 1,2,3,4,5,6,7,8,9

### The default orientation of the candidate list
### TRUE means the candidate list is vertical, FALSE means it is horizontal
ORIENTATION=TRUE

END_DEFINITION

### Begin Table data.
### Format of every line whose formated in "input_keys\\tphrase\\tfreq\\n" is an
### entry.
### From left to right, the 1st column are the input key combination that you
### entered via keyboard; the 2nd column are presented character or phrase of
### the key combination you want; the 3rd column are frequency of the character
### or phrase.
BEGIN_TABLE
"""
    table += to_ibus_fmt(words)
    table += """
[	󱦐	1
]	󱦑	1
*	‍	1
+	󱦖	1
-	󱦕	1
(	󱦗	1
)	󱦘	1
_	󱦙	1
{	󱦚	1
}	󱦛	1
.	󱦜	1
:	󱦝	1
ss	　	1
zz	　	1
<	「	1
>	」	1
~~	︁	1
~	︀	1
END_TABLE"""

    return table


def ahk_script(words, short: bool = False, toggle: bool = False, end_chars: str | None = "") -> str:
    def to_ahk_fmt(words):
        result = []

        for i in words:
            str_codepoint = str(hex(ord(i[1])))[2:].upper()
            keys = to_short(i[0]) if short else [i[0]]

            result += [f"::{key}::{{U+{str_codepoint}}} ; {i[1]}" for key in keys]

        result.sort(key=sort_key, reverse=True)
        return "\n".join(result)

    # python uses lazy evaluation, so this runs (`len()` is not defined for `None`)
    if end_chars is None or len(end_chars) == 0:
        if toggle:
            end_chars = " "
        else:
            end_chars = "``"

    if toggle:
        # ` ^42` center-aligns the string to 42 characters
        # (len of prev line minus the two spaces and semicolons)
        header = f"""
; ---- USE ALT + SPACE TO TOGGLE SCRIPT ---- ;
; {gen_header: ^42} ;

#Requires AutoHotkey v2.0+
#SingleInstance force
#Hotstring O Z

Hotstring("EndChars", "{end_chars}")

#SuspendExempt
!Space::Suspend
#SuspendExempt False

"""
    else:    
        header = f"""
; {gen_header}

#Requires AutoHotkey v2.0+
#SingleInstance force
#Hotstring O

Hotstring("EndChars", "{end_chars}")

"""
    return header.lstrip() + to_ahk_fmt(words) + """
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
::zz::{U+3000} ; logograph fullwidth space
::<::{U+300C} ; 「 start quote
::>::{U+300D} ; 」 end quote

::~~::{U+FE01} ; variation selector 2
::~::{U+FE00} ; variation selector 1
"""

# TODO update input plugin (e.g. what else uses `pi_`??)
def mac_os_plugin(words, short: bool = False) -> str:
    def to_mac_fmt(words):
        result = []

        for i in words:
            keys = to_short(i[0]) if short else [i[0]]
            result += [f"{key} {i[1]}" for key in keys]

        result.sort(key=sort_key, reverse=True)
        return "\n".join(result)

    return f"""# {gen_header}

METHOD: TABLE
ENCODE: Unicode
PROMPT: sitelen pona (UCSUR)
DELIMITER: ,
VERSION: 3.2
MAXINPUTCODE: 15
VALIDINPUTKEY: aeioujklmnpstw[_].:/+{{}}

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
{{ 󱦚
}} 󱦛
. 󱦜
: 󱦝
te 「
to 」
< 「
> 」""" + to_mac_fmt(words) + "\nENDCHARACTER"


if __name__ == "__main__":
    args = parse_args()
    words = get_words()
    encoding = "utf-8"

    match args.outputtype: 
        case "macos":
            text = mac_os_plugin(get_ucsur(words), short=bool(args.short))

            # Apple documentation says to use utf-16
            # https://support.apple.com/guide/mac-help/create-and-use-your-own-input-source-on-mac-mchlp2866/mac
            encoding = "utf-16"
        case "ahk":
            text = ahk_script(get_ucsur(words), short=bool(args.short), toggle=bool(args.ahk_toggle), end_chars=args.end_chars)
        case "ibus":
            text = ibus_table(get_ucsur(words), short=bool(args.short))
        case "espanso":
            text = espanso(get_ucsur(words), short=bool(args.short), end_chars=args.end_chars)

    if args.file:
        with open(args.file, 'w', encoding=encoding) as f:
            f.write(text)
    else:
        print(text)
