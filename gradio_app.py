import gradio as gr
import requests

FASTAPI_URL = "http://localhost:8000/verify"

def process_file(file):
    if file is None:
        return "No file uploaded"
    
    with open(file.name, "rb") as f:
        files = {"file": (file.name, f)}
        response = requests.post(FASTAPI_URL, files=files)
        
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

with gr.Blocks() as demo:
    gr.Markdown("## Document Verification System")

    with gr.Row():
        file_input = gr.File(label="Upload Document", type="filepath")
        output = gr.JSON(label="Verification Result")

    submit_btn = gr.Button("Verify Document")
    submit_btn.click(fn=process_file, inputs=file_input, outputs=output)

if __name__ == "__main__":
    demo.launch()