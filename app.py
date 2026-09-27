from transformers import pipeline
import gradio as gr

model = pipeline("text-generation")

def predict(prompt):
    summary = model(prompt) [0] ["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder = "Enter text block to summarize", lines=4)
    gr.Interface(fn=predict, inputs= textbox, outputs= "text")

  demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
