# sitelen pona UCSUR guide!!!

o sitelen e sitelen pona lon ilo mute a!

## Render sitelen pona on most desktop applications!

Due to the standardization of codepoints in the UCSUR, you can now render sitelen pona on many desktop applications (Firefox, Discord, etc). In many applications all you need to do is install a UCSUR compatible sitelen pona font, and you are good to go. However there are some quirks, and you need an input engine to be able to easily input these characters, which is the purpose of this guide.

# Fonts

The current recomended fonts for sitelen pona are:

- [Fairfax HD](https://www.kreativekorp.com/software/fonts/fairfaxhd.shtml)

  ![an image preview of fairfax hd](./images/fairfaxhd.png)
  
  This font supports the latest (2024-02-20) version of UCSUR. It *does not* look a bit nasa, however it is mostly readable.

- [nasin nanpa](https://github.com/ETBCOR/nasin-nanpa)

  ![an image preview of nasin nanpa](./images/nasin-nanpa.png)
  
  This is an alternative font, actively being developed by jan Itan (`@etbcor`). It is monospace, and supports cartouches, combination glyphs, and long glyphs (pi, tawa & lon). This font supports the 2024-02-20 version of UCSUR, and is used in [*su*](https://www.amazon.com/dp/0978292375)!

- [sitelen seli kiwen juniko (mono)](https://www.kreativekorp.com/software/fonts/sitelenselikiwen)
    
  ![an image preview of sitelen seli kiwen](./images/sitelenselikiwen.png)
    
  This font by jan Lepeka supports the most recent version of UCSUR (2024-02-20). It's personally my favorite! There are proportional *(glyphs take up varying amounts of space)* and monospaced *(glyphs take up the same amount of space)* versions of the font. Monospaced fonts in general are recommened for sitelen pona (both of the above fonts are monospaced). **sitelen seli kiwen juniko mono**, the monospaced version of sitelen seli kiwen juniko is used in the css below, fyi.

If you are unsure of which font to pick, I would recommend nasin nanpa.

Once you have installed any of these fonts you are done, in many applications sitelen pona should render correctly, with the exception of websites, as they do not fall back to sitelen pona. This is an issue, because some applications are actually websites, with a notable example being Discord. 

## Discord

Because internally the Discord application relies on Electron, it does not fall back to the font you installed when sitelen pona glyphs are present, instead displaying these frustrating little squares. To fix this, one option is to install a fake *Helvetica Neue* font, which will allow sitelen pona to render wherever Helvetica Neue is used, which includes Discord!

Another option is to modify your Discord. Currently, this modification is possible on all Desktop systems. **This option is dangerous, violates Discord TOS, and may result in your account being banned.**

### Font

Simply install the fake Helvetica Neue font, and it should result in Discord displaying UCSUR.

**For Windows,**

- Download and install [this font](https://github.com/ETBCOR/nasin-nanpa/releases/download/n4.0.0/nasin-nanpa-4.0.0-Helvetica.otf)

**For Linux,**

- Download the above font
- Copy the file to `~/.local/share/fonts/`

This method does not work on macOS or mobile devices. 

### Desktop

**⚠️⚠️⚠️ THIS VIOLATES DISCORD'S TOS. O SONA A ⚠️⚠️⚠️**


<details>
<summary><b>If you use BetterDiscord...</b></summary>

1. Download the sitelen pona theme: <https://raw.githubusercontent.com/neroist/sitelen-pona-ucsur-guide/main/css/sitelen-pona.theme.css>

2. In Discord, go to your BetterDiscord settings and select the `Themes` tab.

3. At the top click the "Open themes Folder" button (either as a large blue button or the small folder icon near the top)

4. Move the file you downloaded into this folder.

5. Go back to your `Themes` page and enable the theme.

</details>

To patch your Discord to correctly render sitelen pona on desktop, we will use the [Vencord client modification](https://vencord.dev/). Start by following the installation guide on their website to install it. After installing Vencord we need to add a CSS snippet, a small snippet of code that tells Vencord to use Fairfax HD or nasin nanpa when sitelen pona is present.

First go to go to Settings, then scroll down to "Vencord", click "Themes", then "Online Themes"

Paste this link into the text box:

```
https://raw.githubusercontent.com/neroist/sitelen-pona-ucsur-guide/main/css/sitelen-pona.theme.css
```

If the "Validator" section below shows that the theme is valid, you can now exit settings, and your Discord should be properly set up to render sitelen pona!

### Browser

<!-- If you use a web browser, you can use the [stylus extension](https://github.com/openstyles/stylus#releases) to add the css code above. Simply click on the extension with a discord tab open, and use the "Write new style as UserCSS" option. Be sure to write it for just "discord.com", as choosing a different URL will make it not work outside of the channel you were looking at. -->

If you use a web browser, you can use the [stylus extension](https://github.com/openstyles/stylus#releases) to help render sitelen pona. 

Simply install [this userstyle](https://userstyles.world/style/14920/sitelen-pona-o-lon-lipu-siko-a) and you're done!

### Android

[This reddit post](https://www.reddit.com/r/tokipona/comments/10bwbur/guide_on_viewing_and_rendering_sitelen_pona_on/) by jan Elijo (`u/QuantumAgain`) is a wonderful guide on how to get UCSUR on Android. Regarding viewing sitelen pona, here are the listed steps:


> :warning: **note**: this changes the system font to something else, if you want to only view sitelen pona on Discord please use Aliucord (the next section)

<details>
<summary>
  <b>List format for instructions (zFont systemwide)</b>
</summary>

Installing the font:

1. Download [nasin-nanpa-4.0.0-UCSUR.otf](https://github.com/ETBCOR/nasin-nanpa/releases/download/n4.0.0/nasin-nanpa-4.0.0-UCSUR.otf) or the latest UCSUR version from the [nasin-nanpa releases](https://github.com/ETBCOR/nasin-nanpa/releases) page.

2. Convert nasin-nanpa-4.0.0-UCSUR.otf to [nasin-nanpa-4.0.0-UCSUR.ttf](https://drive.google.com/file/d/1herShyK8TGajd10tWQqV1JOkSPVwoWyZ/view?usp=sharing) (If you're not sure how, skip this step or click the link.)

3. Download [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2&gl=US) from the Play Store. *(Other font changing apps such as [#mono_](https://xdaforums.com/t/app-mono_-flipfont-custom-ttf-installer-v2-1-for-samsung-oneui-1-2-3-no-root.4195613/) might work instead)*

4. In the app, go to Downloads, press the + icon in the bottom right and add the font file (select "Add File"). (If you didn't convert it, the app will prompt you to install another app and you can do it there if you need).

5. Click on the font file and press Apply.

6. The app will ask you for your Android version, choose "Auto".

7. Follow the steps in the app, they vary depending on your phone, for me it involved installing a fake Samsung font.

8. Once you're done you should now be able view sitelen pona in every app.

> You should be able to read this: 󱥞󱤘󱤮󱤉󱥁

</details>

> jan Nasaka (`@harger` lon ilo Siko) li pana e sona ni tawa mi. ona li pona mute a! :)

The above method may not be supported on your device. One alternative is to use the Aliucord Discord client and set a custom font. *(This method causes small font discrepancies in the Aliucord client).* The setup instructions are below:

<details>
<summary>
  <b>List format for instructions (Aliucord)</b>
</summary>

1. Install Aliucord from its [Github page](https://github.com/Aliucord/Aliucord/releases)
    * Please follow the [installation instructions](https://github.com/Aliucord/Aliucord?tab=readme-ov-file#-installation) in the readme

2. Install the Themer plugin, which will allow you to change Aliucord's font.
    * One method for doing this is pasting in the zip link (<https://github.com/Vendicated/AliucordPlugins/blob/builds/Themer.zip?raw=true>) into a Discord message, then clicking the link in Aliucord. 

3. In Aliucord, go to <kbd>User Settings</kbd>  (click your pfp in the botton right) -> <kbd>Plugin Settings</kbd> (near the bottom) -> <kbd>Themer</kbd> and toggle <kbd>Enable Custom Fonts</kbd>.

4. Click <kbd>New Theme</kbd>, enter a name for your new theme, toggle the theme, and click the pencil icon on your theme to edit it.

5. On the new menu click the <kbd>Fonts</kbd> button, then click the `*` and paste in this link: <https://github.com/ETBCOR/nasin-nanpa/releases/download/n4.0.0/nasin-nanpa-4.0.0-UCSUR.otf>.

    This is nasin-nanpa, which is the font that'll allow you to view sitelen pona

6. Click off the popup, then press the save button in the bottom right. When it prompts you to restart, restart.

7. pini a! sitelen pona la o lukin pona

</details>

### iOS

to view sitelen pona in Discord, jan Nasaka (`@harger` lon ilo Siko) has written a [bash script](https://github.com/Hargers/enmity-sp-script/blob/main/Enmity-nasin-nanpa-merge.sh) to download and merge the latest versions of the [Enmity Discord client](https://github.com/enmity-mod) and the font [nasin-nanpa](https://github.com/ETBCOR/nasin-nanpa) into a `.ipa` app file. A premerged `.ipa` file can be found [here](https://github.com/Hargers/enmity-sp-script/releases).

For installation instructions not requiring a jailbroken device, please refer to the "Sideloading Apps" section on [this page](https://ios.cfw.guide/sideloading-apps/#sideloading-apps).

## Input

Now that sitelen pona is rendering properly, we need to be able to type it!

### Windows

There are two input methods for Windows: nasin Ajemi and nasin AHK

You can download & install nasin Ajemi from [this link](https://github.com/dec32/Ajemi/releases/latest), see the [README](https://github.com/dec32/Ajemi) on how to use it. 

For nasin AHK, there is an [Auto Hotkey Script](./ahk-scripts/sitelen-pona-4.0.ahk?raw=1) (download with <kbd>Ctrl</kbd>+<kbd>S</kbd>) by jan Itan (`@etbcor`) for input. Write the toki pona word and then a \` (the letter under escape) to convert it into sitelen pona. You can also write `` [` `` and `` ]` `` for cartouches, as well as `` (` `` and `` )` `` for long glyphs. There is also a ["small" version of the script](./ahk-scripts/stl-pon-4.0.ahk?raw=1) that uses 3 letter codes for each word instead of typing the whole word.

For this of this to work, you need to have [Auto Hotkey](https://www.autohotkey.com/) installed.

Other features of the script are explained in [this README file](./ahk-scripts/README.md).

### macOS

jan Tepo (`@tbodt`) has made an [input plugin for macOS](./sitelen-pona.inputplugin?raw=1) with modifications by jan Semu (`@jmiibo`) to support UCSUR (download with <kbd>Ctrl</kbd>+<kbd>S</kbd>). Download it, then install it by double clicking. Then enable it in `System Preferences` -> `Keyboard` -> `Input Sources`. You'll find it listed under "Chinese, Simplified".

### Linux

The ~~only~~ (nasin sitelen Wakalito li lon · ilo ante kin li lon) current supported input engine for Linux is ibus, for this to work, you need both `ibus`, and `ibus-tables` installed. For installation commands/instructions, see [this page](https://github.com/ibus/ibus/wiki/ReadMe#install-binary-packages).

> During installation, regarding Ubuntu, feel free to remove `ibus-qt4` from the `apt-get insall` command, which has been removed from Ubuntu's main repository.

jan Komi (`@cominixo`) has created an [ibus input table](./ibus-tables/sitelen-pona-4.0.ibus-table?raw=1) *(click the link & download with <kbd>Ctrl</kbd>+<kbd>S</kbd>)*. Copy it to a directory of your choice, and then open a terminal in the same directory. Run these commands to install it:

```bash
sudo ibus-table-createdb -n /usr/share/ibus-table/tables/tokipona.db -s sitelen-pona-4.0.ibus-table
ibus-daemon -drxR
```

![an image of the ibus input engine in action](./images/ibus1.png)

Once you have done this, open the ibus preferences (you can do this with the `ibus-setup` command). Go to `Input Method`, click `Add` and then select `sitelen pona` (the last option under the English category).

Finally, if necessary, go to your keyboard settings in your settings application and add a "sitelen pona" input source (the name should be "English (sitelen pona)").

This should result in a new tray icon which indicates which input source you're using—English or sitelen pona. Which keybinding which allows you to switch input sources may depend on your distro. However, on Pop!_OS it is <kbd>Super</kbd> + <kbd>Space</kbd>

<details>
<summary>
  <b>List format for instructions</b>
</summary>

1. Install `ibus` and `ibus-tables`. Follow the instructions on [this page](https://github.com/ibus/ibus/wiki/ReadMe#install-binary-packages).

    - For Ubuntu, do not install the `ibus-qt4` package

2. Download the ibus input table [here](./ibus-tables/sitelen-pona-4.0.ibus-table?raw=1).

3. Copy the file to a chosen directory and open a terminal in the directory

4. Run these two commands:

```bash
sudo ibus-table-createdb -n /usr/share/ibus-table/tables/tokipona.db -s ibus-tables/sitelen-pona-4.0.ibus-table
```

```bash
ibus-daemon -drxR
```

5. Open ibus preferences (you may run the `ibus-setup` command)

6. Add the sitelen pona input method. Go to `Input Methods` -> `Add` -> `English` -> *(scroll all the way down to)* `sitelen pona`

7. If needed, go to your settings application and add a new input source of the name "English (sitelen pona)" 

    - Feel free to search for "sitelen pona" and select anything similar, if "English (sitelen pona)" is not present

8. Switch input sources (either via keybindings or the tray icon).

9. pini a!

</details>

### Espanso / nasin sitelen Wakalito

<!-- > I recommend the above methods more than this one. -->

*nasin Wakalito* is an input method for writing Toki pona words. It is available on macOS, Linux, and Windows using [Espanso](https://espanso.org/). By default, nasin Wakalito outputs words in sitelen Lasina. However, by using a modified config file, we can output UCSUR instead.

In addition, if you just need/want to use Espanso and don't like the triggers in nasin Wakalito, there is also a config file for that ([`sitelen-pona-espanso.yml`](./sitelen-pona-espanso.yml)).

nasin:

1. Install Espanso [here](https://espanso.org/install/)

2. Download a config file. There are two:

    - [This file](./wakalito-7-3-2-ucsur.yml?raw=1) uses nasin Wakalito's triggers, and outputs UCSUR

    - [This file](./sitelen-pona-espanso.yml?raw=1) uses toki pona word triggers, and outputs UCSUR

3. Copy or move the file to Espanso packages folder

    - Windows: `C:\Users\<user>\AppData\Roaming\espanso\match\packages`
	  - (<kbd>Win</kbd>+<kbd>R</kbd>, type `%appdata%` to get to `\Roaming`

    - macOS: `/Users/<user>/Library/Preferences/espanso/match/packages`
	
    - Linux: `~/.config/espanso/match/packages`

4. From where you've found your Espanso packages folder (`<wherever>/espanso/match/packages`), navigate to `<wherever>/espanso/config` and open the file `default.yml` in a text editor

5. On a new line, paste the text `toggle_key: RIGHT_ALT`, then save your changes and exit

6. Start Espanso

7. Start writing! *(When you want to toggle Espanso on/off, double tap <kbd>Alt</kbd> on the right side of your keyboard!)*

    - A table for triggers -> words can be found on sona.pona.la, [here](https://sona.pona.la/wiki/Wakalito), with a few modifications listed below. This is for the first config file, `wakalito-7-3-2-ucsur.yml`.

#### Modifications

| Character                                  | Keys on a QWERTY layout |
| -------------------------------------------| ----------------------- |
| `　` (fullwidth space)                     | `666`, `   ` (3 spaces) |
| `‍` ("-" zero width joiner)                 | `aa`                    |
| `󱦕` ("^" stacking joiner)                   | `gg`                    |
| `󱦖` ("*" scaling joiner)                    | `hh`                    |
| `󱦝` (":" sp colon)                         | `6y`                    |
| `󱦜` ("·" sp dot)                           | `3`                     |
| `󱦐` ("[" cartouche start)                  | `c1`                    |
| `󱦑` ("]" cartouche end)                    | `c2`                    |
| `「` (cjk start quote)                     | `q1`                    |
| `」` (cjk end quote)                       | `q2`                    |
| `󱦗` ("(" start left-combining long glyph)   | `b1`                    |
| `󱦘` (")" end left-combining long glyph)     | `b2`                    |
| `󱦚` ("{" start right-combining long glyph)  | `d1`                    |
| `󱦛` ("}" end left-combining long glyph)     | `d2`                    |

### Keyman

[Keyman](https://keyman.com/) is an input engine created by the Summer Institute of Linguistics, which allows for user designed input keyboards and by extension, input methods. It is available on Windows, MacOS, Linux, iOS, iPadOS, Android, and in web browser.

Installation instruction are listed below by platform:

<details>
<summary>
  <h4><b>List Android and iOS instructions</b></h4>
</summary>

1. Install the app:

- On iOS, Install Keyman [from the App Store](https://apps.apple.com/us/app/keyman/id933676545)
- On Android, install Keyman [from the Google Play Store](https://play.google.com/store/apps/details?id=com.tavultesoft.kmapro)

2. Open the app and click the <kbd>◦◦◦</kbd> button on top right corner

3. A window titled "Get Started" will open. Click the button in the middle titled "Set up Keyman as system-wide keyboard" or "Enable Keyman as system-wide keyboard"

4. On the new window, toggle Keyman as a keyboard.

    - On iOS, under the section titled "PREFERRED LANGUAGE" click <kbd>Keyboards</kbd> and toggle <kbd>Keyman</kbd>
    - On Android, toggle <kbd>Keyman</kbd>. A privacy popup will appear, regard it, then press <kbd>OK</kbd>, then <kbd>OK</kbd>

5. Navigate back to the Keyman app, click <kbd>◦◦◦</kbd> -> <kbd>Settings</kbd> -> <kbd>Installed Languages</kbd> -> <kbd>+</kbd>.

6. On the new window, click <kbd>Enter language or keyboard</kbd>, and type "Sitelen Pona"

7. An array of keyboards will populate. Click on your desired input method.

    - As of the time of writing, the keyboard `Sitelen Pona (KreativeKorp, UCSUR)` supports the most UCSUR features. 

8. On the next page, click <kbd>Install keyboard</kbd> -> <kbd>Install</kbd> -> <kbd>Done</kbd>

9. Swap to the Keyman keyboard and press the keyboard's globe icon to change to your sitelen pona input method. 

10. o sitelen pona!

</details>

<details>
<summary>
  <h4><b>List web browser instructions</b></h4>
</summary>

1. Go to the Keyman keyboard search page and search for "[Sitelen Pona](https://keyman.com/keyboards?q=sitelen%20pona)".

2. A list of keyboards will appear. Click on your desired input method.

    - For Latin keyboard input, use jan Lentan's [`Sitelen Pona (Lentan, UCSUR)`](https://keyman.com/keyboards/sp_lentan_ucsur) keyboard.

3. On the next page, click <kbd>Use keyboard online</kbd>, then, under the section titled "Browser Add-in", right click the button <kbd>Toki Pona Keyboard</kbd> and add it to your bookmarks.

4. On most pages tested, clicking your new bookmark will load your sitelen pona input method.

    - If your keyboard uses an alternate layout, you can click the button <kbd>Show On Screen Keyboard</kbd> on the edge of a focused text box to view its layout.

5. o sitelen pona!

</details>

### Android

Two input engines for android exist:

- [jan Komi's (`@cominixo`)](https://github.com/cominixo/tokiponakeyboard/releases/tag/v0.1-sp) (similar anu better APKs can be found in [this reddit post](https://www.reddit.com/r/tokipona/comments/10bwbur/guide_on_viewing_and_rendering_sitelen_pona_on/))
 
    - When trying to install the APK, if you get an error that you cannot due to "package conflicts," delete the other Toki Pona Keyboard app and try again.

- and [kulupu Mimuki's (`@.mouseless`)](./android_keyboard.zip) which can be used with [this app](https://play.google.com/store/apps/details?id=de.humbergsoftware.keyboarddesigner), but it requires a paid addon to import the file.

### iOS

Currently, the only the input method for iOS is nasin Wakalito. [nasin sitelen Wakalito](https://apps.apple.com/us/app/nasin-sitelen-wakalito/id1569543076) is an app available on iOS, iPadOS, and MacOS created by jan Likipi, kala pona Tonyu, jan Tepo, and Lipamanka. Normally, the app can only output sitelen Lasina, but with some small changes, the output can be changed to its UCSUR equivalent. The project files for this can be found [here](https://github.com/Hargers/wakalito-ios-UCSUR) and the latest prebuilt `.ipa` app file can be found [here](https://github.com/Hargers/wakalito-ios-UCSUR/releases). This fork of the app is maintained by jan Nasaka (`@harger` lon ilo Siko).

For installation instructions not requiring a jailbroken device, please refer to the "Sideloading Apps" section on [this page](https://ios.cfw.guide/sideloading-apps/#sideloading-apps).

A table for triggers -> words can be found on sona.pona.la, [here](https://sona.pona.la/wiki/Wakalito), with modifications listed below.  

<details>
<summary>
  <b>List format for modifications</b>
</summary>

#### Formatting Modifications

| Character                              | Keys on nasin Wakalito layout |
| ---------------------------------------| ----------------------------- |
| `　` (fullwidth space)                 | `-` 	                          |
| `‍` (zero width joiner)                 | `---`                         |
| `󱦕` (stacking joiner)                   | `•^>`                         |
| `󱦖` (scaling joiner)                    | `•<v`                         |
| `󱦝` (sp colon)                        | `:`                           |
| `󱦜` (sp dot)                          | `•`                           |
| `󱦐` (cartouche start)                  | `[`                           |
| `󱦑` (cartouche end)                    | `]`                           |
| `「` (cjk start quote)                 | `▢[`                         |
| `」` (cjk end quote)                   | `▢]`                         |
| `󱦗` (start left-combining long glyph)   | `[[`                          |
| `󱦘` (end left-combining long glyph)     | `]]`                          |
| `󱦚` (start right-combining long glyph)  | `[[[`                         |
| `󱦛` (end left-combining long glyph)     | `]]]`                         |

#### nimi sin Modifications

| Character          | Keys on nasin Wakalito layout |
| -------------------| ----------------------------- |
| `󱥸` (namako)      | `<v‴`, `‴<v`, `□•`, `•□`    |
| `󱦢` (majuna)      | `-‴-`, `‴--`                |
| `󱦤` (linluwi)     |  `ooo^>-`, `^>-ooo`, `\|-\|\|•••ᴗᴖ`, `\|-\|\|ᴗᴖ•••`, `\|-\|•••ᴗᴖ\|`, `\|-\|ᴗᴖ\|•••` |
| `󱦥` (kiki)      | `^>-^>-`, `-^>-^>-`, `^>^>^>^><v<v<v<v`, `^>^>^><v<v<v` |
| `󱦦` (su)          | `▢<v`                        |
| `󱦮` (owe)         | `‴o•`                        |

Additionally, triggers were removed for ASCII art, a Discord command, and words without sitelen pona characters in the font nasin-nanpa (`unu`, `Pingo`, `oke`, `mulapisu`, `kapesi`, and `isipin`).

</details>

### Web

If you are on a device which cannot use these input methods for any reason, [jan Tala (`@at`)](https://github.com/DataKinds) has created a [web based converter](https://ilo-pi-sitelen-pona.glitch.me/) from sitelen Lasina to sitelen pona.

# End

> This is a really huge step for toki pona, and I am extremely happy to see this happen. If you have created a font, input method, or any other resource that you want added, please create a pull request, issue, or just ping me on discord `@o.v` (jan Lili lon ma pona pi toki pona) and we can talk!

*~ tan jan Lili*

## ijo pona

thank you to

- jan Komi
- kulupu Mimuki
- jan Tala
- soweli pona Tesa
- mun Kekan San
- jan Tepo
- jan Itan
- jan Lili
- jan Semu
- ijo `@Qwerty-Space` (lon lipu github)
- ijo `@ReveredOxygen`
- kulupu katu
- kule Piton
- ijo `@gustav-langer`
- jan Nasaka (`@harger` lon ilo Siko)

sina ale li pona wawa a li pana sona e pona anu pali pona a (anu ni tu a a)
