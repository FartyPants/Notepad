# notepad extension
adds a very simple notepad box to oobabooga web_ui
https://github.com/oobabooga/text-generation-webui

Purpose: a multiple-notepad for text you want to keep saved across sessions, without switching between browser and some text editor

The box automatically saves anything you write or paste to files: notepad[nr].txt in text-generation-webui folder
And read it back next time you run it. Works in all interface mode - especially useful in --notebook to save parts of the genrated text or whatever else you need. You either need this or not.

![image](https://github.com/FartyPants/Notepad/assets/23346289/80176d55-4897-444d-bda4-e556d8b4ee04)

The extension can be installed by cloning this repository inside the ../text-generation-webui/extensions folder:

```
cd PATH_TO_text-generation-webui/extensions
```
then clone this repo
```
git clone https://github.com/FartyPants/Notepad
```

If you want to always load the extension on start add

 --extensions Notepad
 
 into your webui.py
