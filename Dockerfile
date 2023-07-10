FROM python:3.9-slim-buster

WORKDIR /workspace

RUN pip3 install \
    torch==1.11 \
    torchvision==0.12.0 \
    --index-url https://download.pytorch.org/whl/cpu \
    pytorch-lightning==1.7.0 \
    einops==0.3.3 \
    && rm -rf /root/.cache/pip

COPY gradio.py .

COPY /outputs/model.script.pt model/

EXPOSE 8080

CMD ["python3", "gradio.py"]