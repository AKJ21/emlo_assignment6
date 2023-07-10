import torch
import gradio as gr

def main() :
    ckpt_path = "model/model.script.pt"

    print("Running Demo")

    print("Instantiating scripted model: {}".format(ckpt_path))
    model = torch.jit.load(ckpt_path)

    print(f"Loaded Model: {model}")

    def predict(image):
        if image is None:
            return None
        image = torch.tensor(image[None, None, ...], dtype=torch.float32)
        preds = model.forward_jit(image)
        preds = preds[0].tolist()
        return {str(i): preds[i] for i in range(10)}

    im = gr.Image(type="pil")

    demo = gr.Interface(
        fn=predict,
        inputs=[im],
        outputs=[gr.Label(num_top_classes=10)],
        live=True,
    )

    demo.launch(server_port=8080)

if __name__ == "__main__":
    main()