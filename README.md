# notepad extension
adds dummy textbox to oobabooga web_ui

Purpose: save or edit parts of generated text you want to keep, without switching between browser and text editor

https://github.com/oobabooga/text-generation-webui

The box automatically saves anything you write or paste in it to file keep.txt in text-generation-webui
And read it back next time you run it. Works in all interface mode - especially useful in --notebook 

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
