from pathlib import Path
import gradio as gr

def save_text_to_file(text):
    file_path = Path("keep.txt")  # Specify the path and name of the output file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    
    #print("Text:", text) 
    #print("Saved file:", file_path)    

def ui():
    def save_button_click(dummy_value):
        save_text_to_file(dummy_value)

    # Read the contents of the "keep.txt" file
    file_path = Path("keep.txt")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            default_text = file.read()

    with gr.Accordion("Notes", open=False):
        dummy = gr.Textbox(value=default_text,label="Your permanent notepad", elem_classes="textbox", lines=15)  # Set default_text as the value
        #savetext = gr.Button("Save")

    dummy.change(save_button_click, dummy)
    #savetext.click(save_button_click, dummy)
