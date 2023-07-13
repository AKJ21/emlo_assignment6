FROM python:3.9-slim-buster

WORKDIR /workspace

RUN pip3 install \
    torch==2.0.1 \
    torchvision==0.15.2 \
    gradio==3.36.1 \
    && rm -rf /root/.cache/pip

COPY gradio_demo.py .

COPY /model/model.script.pt ./model/

COPY /sample ./sample/

CMD ["python3", "gradio_demo.py"]