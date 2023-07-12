import torch
import gradio as gr
from pytorch_lightning import LightningModule
import torchvision.transforms as T
import torch.nn.functional as F

def main() :
    ckpt_path = "model/model.script.pt"

    print("Running Demo")

    print("Instantiating scripted model: {}".format(ckpt_path))
    model = torch.jit.load(ckpt_path)

    print(f"Loaded Model: {model}")

    transforms = T.Compose(
            [T.ToTensor(), 
             T.Resize((32, 32)),
             T.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
        )

    def predict(image):
        if image is None:
            return None
        image = transforms(image).unsqueeze(0)
        # image = torch.tensor(image[None, None, ...], dtype=torch.float32)
        logits = model(image)
        preds = F.softmax(logits, dim=1).squeeze(0).tolist()
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