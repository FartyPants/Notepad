# notepad extension
adds a notepad box to oobabooga web_ui

Purpose: a simple notepad for text you want to keep, without switching between browser and text editor

https://github.com/oobabooga/text-generation-webui

The box automatically saves anything you write or paste in it to file keep.txt in text-generation-webui
And read it back next time you run it. Works in all interface mode - especially useful in --notebook to save parts of the genrated text or whatever.

The extension can be installed by cloning this repository inside the ../text-generation-webui/extensions folder:

```
cd PATH_TO_text-generation-webui/extensions
```
then clone this repo
```
git clone https://github.com/FartyPants/Notepad
```

You can always load the extension if you add

 --extensions Notepad
 
 into your webui.py
