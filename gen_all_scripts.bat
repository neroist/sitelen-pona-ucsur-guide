@echo off

doskey gen_script = python gen_script.py

:: espanso
gen_script espanso -f "./sitelen-pona-espanso.yml"

:: macos input plugin
gen_script macos -f "./sitelen-pona.inputplugin"

:: ahk scripts
IF NOT EXIST "./ahk-scripts/" mkdir "./ahk-scripts/"
gen_script ahk    -f "./ahk-scripts/sitelen-pona.ahk"
gen_script ahk -t -f "./ahk-scripts/sitelen-pona-toggle.ahk"
gen_script ahk -s -f "./ahk-scripts/stl-pon.ahk"

:: ibus tables
IF NOT EXIST "./ibus-tables/" mkdir "./ibus-tables/"
gen_script ibus    -f "./ibus-tables/sitelen-pona.ibus-table"
gen_script ibus -s -f "./ibus-tables/stl-pon.ibus-table"
