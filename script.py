from pathlib import Path
import gradio as gr

def save_text_to_file(text, noteid):
    file_name = f"notebook{noteid}.txt"  # Generate the file name based on noteid
    file_path = Path(file_name)  # Specify the path and name of the output file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
       
 
def load_text(noteid):
    file_name = f"notebook{noteid}.txt"
    file_path = Path(file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            default_text = file.read()
    except FileNotFoundError:
        default_text = ""        
    
            
    return default_text

def ui():

    global noteid
    noteid = 1
    
    def save_button_click(dummy_value):
        save_text_to_file(dummy_value, noteid)
   
    def change_textbox(choice):
        global noteid
        noteid = int(choice.split()[1])
        noteid = min(max(noteid, 1), 6)
        default_text = load_text(noteid)
        return gr.update(value=default_text)
     

    default_text = load_text(noteid)    

    with gr.Accordion("Notes", open=False):
        radio = gr.Radio(["Note 1", "Note 2", "Note 3" , "Note 4", "Note 5", "Note 6"], label="Notebooks", value = "Note 1")
            
        dummy = gr.Textbox(value=default_text,label="Text:", elem_classes="textbox", lines=15)  # Set default_text as the value


    dummy.change(save_button_click, dummy)
    radio.change(fn=change_textbox, inputs=radio, outputs=dummy)
