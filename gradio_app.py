# gradio_app.py
import gradio as gr
from app.main import cancer_prediction

def predict(cell_size, cell_shape):
    return cancer_prediction(cell_size, cell_shape)

demo = gr.Interface(
    fn=predict,
    inputs=[gr.Number(label="Cell Size"), gr.Number(label="Cell Shape")],
    outputs=gr.Textbox(label="Prediction")
)

# share=True generates a public URL automatically
demo.launch(share=True)
