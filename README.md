# sitelen pona UCSUR guide!!!

o sitelen e sitelen pona lon ilo mute a!

## Render sitelen pona on most desktop applications!

Due to the standardization of codepoints in the UCSUR, you can now render sitelen pona on many desktop applications (Firefox, Discord, etc). In many applications all you need to do is install a UCSUR compatible sitelen pona font, and you are good to go. However there are some quirks, and you need an input engine to be able to easily input these characters, which is the purpose of this guide.

# Fonts

The current recomended fonts for sitelen pona are:

- [Fairfax HD](https://www.kreativekorp.com/software/fonts/fairfaxhd.shtml)

  ![an image preview of fairfax hd](fairfaxhd.png)
  
  This font supports the 2022-05-20 version of UCSUR. It looks a bit nasa, however it is mostly readable.

- [nasin nanpa](https://github.com/ETBCOR/nasin-nanpa)

  ![an image preview of nasin nanpa](nasinnanpa.png)
  
  This is an alternative font, actively being developed by jan Itan (`@etbcor`). It is monospace, and supports cartouches, combination glyphs, and long glyphs (pi, tawa & lon). This font supports the 2022-05-20 version of UCSUR, and is used in [*su*](https://www.amazon.com/dp/0978292375)!.

- [sitelen seli kiwen juniko (mono)](https://www.kreativekorp.com/software/fonts/sitelenselikiwen)
    
  ![an image preview of sitelen seli kiwen](sitelenselikiwen.png)
    
  This font by jan Lepeka supports the most recent version of UCSUR (2024-02-20). It's personally my favorite! There are proportional *(glyphs take up varying amounts of space)* and monospaced *(glyphs take up the same amount of space)* versions of the font. Monospaced fonts in general are recommened for sitelen pona (both of the above fonts are monospaced). **sitelen seli kiwen juniko mono**, the monospaced version of sitelen seli kiwen juniko is used in the css below, fyi.

If you are unsure of which font to pick, I would recomend nasin nanpa or sitelen seli kiwen.

Once you have installed any of these fonts you are done, in many applications sitelen pona should render correctly, with the exception of websites, as they do not fall back to sitelen pona. This is an issue, because some applications are actually websites, with a notable example being Discord. 

## Discord

Because internally the Discord application relies on electron, it does not fall back to the font you installed when sitelen pona glyphs are present, instead displaying these frustrating little squares. To fix this, sadly the only option is to modify your Discord. Currently, this modification is possible on all Desktop systems, and on Android.

### Desktop

To patch your Discord to correctly render sitelen pona on desktop, we will use the [Vencord client modification](https://vencord.dev/). Start by following the installation guide on their website to install it. After installing Vencord we need to add a CSS snippet, this is a small snippet of code that tells Vencord to use Fairfax HD or nasin nanpa when sitelen pona is present.

First go to go to Settings, then scroll down to "Vencord", click "Themes", and press "Edit QuickCSS"

Paste this snippet of code into the text box. (No need to worry about security! CSS can only change visual aspects of Discord, and cannot steal your login token or act on your behalf)

```CSS
:root {
    --font-primary: 'gg sans', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif, 'nasin-nanpa', 'Fairfax HD', 'sitelen seli kiwen mono juniko';
    --font-display: 'gg sans', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif, 'nasin-nanpa', 'Fairfax HD', 'sitelen seli kiwen mono juniko';
    --font-code: Consolas, 'Andale Mono WT', 'Andale Mono', 'Lucida Console', 'Lucida Sans Typewriter', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Liberation Mono', 'Nimbus Mono L', Monaco, 'Courier New', Courier, monospace, 'nasin-nanpa', 'Fairfax HD', 'sitelen seli kiwen mono juniko';
    --font-headline: 'ABC Ginto Nord', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif, 'nasin-nanpa', 'Fairfax HD', 'sitelen seli kiwen mono juniko';
}
```

Once you have pasted this code into the QuickCSS box, you can now exit settings, your Discord should be properly set up to render sitelen pona!

> Note: If `sitelen seli kiwen mono juniko` doesnt work for you, try using `sitelen seli kiwen mono juniko meso` or `sitelen seli kiwen mono juniko meso Regular` instead (in the CSS, replace all occurrences of it with this new text).

### Android

> I do not own an Android phone, so I cannot give an accurate guide on this section (maybe somebody fill this in with a pull request), however kulupu Mimuki (`@.mouseless`) has put together an [excellent video guide](https://cdn.discordapp.com/attachments/882652782509846548/943688987070062612/YouCut_20220217_121644150.mp4) for achieving this with [Aliucord](https://github.com/Aliucord/Aliucord).

*~ the previous text here, tan jan Lili*

There used to be a video guide for viewing sitelen pona in [Aliucord](https://github.com/Aliucord/Aliucord) by kulupu Mimuki. However, the video link is now dead, nor have I been able to get sitelen pona working in Aliucord. But [this reddit post](https://www.reddit.com/r/tokipona/comments/10bwbur/guide_on_viewing_and_rendering_sitelen_pona_on/) is a wonderful guide on how to get UCSUR sitelen pona on Android. Regarding viewing sitelen pona, here are the listed steps:

Installing the font:

1. Download [nasin-nanpa-2.5.1.otf](https://github.com/ETBCOR/nasin-nanpa/releases/download/n2.5.1/nasin-nanpa-2.5.1.otf). (Please note that the latest version will not work; the latest version of nasin nanpa now translations Latin characters as well as UCSUR, which messes things up).

2. Convert nasin-nanpa-2.5.1.otf to [nasin-nanpa-2.5.1.ttf](https://www.mediafire.com/file/pj5nmp2io9y34qt/nasin-nanpa-2.5.1.ttf/file) (If you're not sure how, skip this step or click the link).

3. Download [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2&gl=US) from the Play Store. *(Other font changing apps such as [#mono_](https://xdaforums.com/t/app-mono_-flipfont-custom-ttf-installer-v2-1-for-samsung-oneui-1-2-3-no-root.4195613/) might work instead)*

4. In the app, go to Downloads, press the + icon in the bottom right and add the font file (select "Add File"). (If you didn't convert it, the app will prompt you to install another app and you can do it there if you need).

5. Click on the font file and press Apply.

6. The app will ask you for your Android version, choose "Auto".

7. Follow the steps in the app, they vary depending on your phone, for me it involved installing a fake Samsung font.

8. Once you're done you should now be able view sitelen pona in every app.

> You should be able to read this: 󱥞󱤘󱤮󱤉󱥁

<!-- TODO: Add how this changes the OS's font & how to change it back to default -->

### Browser

If you use a web browser, you can use the [stylus extension](https://github.com/openstyles/stylus#releases) to add [the css code above](#desktop). Simply click on the extension with a discord tab open, and use the "Write new style as UserCSS" option. Be sure to write it for just "discord.com" (or "discord.com/channels", I suppose), as choosing a different URL will make it not work outside of the channel you were looking at.

<!-- TODO: iOS? -->

## Input

Now that sitelen pona is rendering properly, we need to be able to type it!

<!-- TODO: Talk abt nasin sitelen Wakalito (atleast in macOS and Linux) -->

### Windows

If you use windows, there is an [Auto Hotkey Script](https://github.com/ETBCOR/nasin-nanpa/releases/download/n2.5.1/sitelen-pona-3.0.ahk) (download with ctrl+s) by jan Itan (`@etbcor`) for input. Write the toki pona word and then a \` (the letter under escape) to convert it into sitelen pona. You can also write '\[\`' and '\]\`' for cartouches, as well as '\(\`' and '\)\`' for long glyphs. There is also a ["small" version of the script](https://github.com/ETBCOR/nasin-nanpa/releases/download/n2.5.1/stl-pon-3.0.ahk) that uses 3 letter codes for each word instead of typing the whole word. For any of this to work, you need to have [Auto Hotkey](https://www.autohotkey.com/) installed.

Other features of the script are explained near the bottom of [nasin-nanpa's releases page](https://github.com/ETBCOR/nasin-nanpa/releases/tag/n2.5.1).

The [Auto Hotkey script in this repository](/sitelen-pona-input.ahk) is the same script from nasin-nanpa, with a modification that enables multidirectional-ni, which is helpful for writing in sitelen pona.

![multidirectional ni showcase](multidir.png)

It uses the characters `^><v` for direction, similar to linja lipamanka. For exmaple, `ni>` is a rightward/east pointing ni, and `ni>^` and `ni^>` both result in a northeast pointing ni.

### macOS

<!-- Seems to work for jan Osuka so I hope this is fine. Again, I do want to add multidir ni to this... -->

jan Tepo (`@tbodt`) has made an [input plugin for macOS](https://raw.githubusercontent.com/neroist/sitelen-pona-ucsur-guide/main/sitelen-pona.inputplugin) with modifications by jan Semu (`@jmiibo`) to support the 2022-05-20 version of UCSUR (download with ctrl+s). Install it by double clicking. Then enable it in System Preferences > Keyboard > Input Sources. You'll find it listed under "Chinese, Simplified" for some reason.

### Linux

<!-- TODO: Test this... tenpo lon la mi kepeken ilo sama tawa sitelen · taso ilo ibus ala -->

The only current supported input engine for Linux is ibus, for this to work, you need both ibus, and ibus-tables installed.

jan Komi (`@cominixo`) has created an [ibus input table](https://raw.githubusercontent.com/neroist/sitelen-pona-ucsur-guide/main/tokipona.txt) (download with ctrl+s). Copy it to a directory of your choice, and then open a command line in the same directory. Run these commands to install it.

![an image of the ibus input engine in action](ibus.png)

```bash
sudo ibus-table-createdb -n /usr/share/ibus-table/tables/tokipona.db -s tokipona.txt
ibus-daemon -drxR
```

Once you have done this, open the ibus preferences, go to Input Method, click ADD and then select sitelen pona (the last option under the English category). Cartouches are typed with '\[', '\_', and '\]'. Long pi is started with 'pi_' and extended with '.

### Android

Two input engines for android exist:

- [jan Komi's (`@cominixo`)](https://github.com/cominixo/tokiponakeyboard/releases/tag/v0.1-sp) (similar apks can be found in [this reddit post](https://www.reddit.com/r/tokipona/comments/10bwbur/guide_on_viewing_and_rendering_sitelen_pona_on/))

- and [kulupu Mimuki's (`@.mouseless`)](./android_keyboard.zip) which can be used with [this app](https://play.google.com/store/apps/details?id=de.humbergsoftware.keyboarddesigner), but it requires a paid addon to import the file.

<!-- TODO: iOS? nasin sitelen Wakalito? -->

### Web

If you are on a device which cannot use these input methods for any reason, [jan Tala (`@at`)](https://github.com/DataKinds) has created a [web based converter](https://ilo-pi-sitelen-pona.glitch.me/) from sitelen Lasina to sitelen pona.

# End

This is a really huge step for toki pona, and I am extremely happy to see this happen. If you have created a font, input method, or any other resource that you want added, please create a pull request, issue, or just ping me on discord `@o.v` (jan Lili lon ma pona pi toki pona) and we can talk!
