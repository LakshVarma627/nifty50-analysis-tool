# Docker GPU Configuration

version: '3.8'

services:
  tensorflow-gpu:
    image: tensorflow/tensorflow:latest-gpu
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    volumes:
      - ./models:/models
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility
    command: bash -c "while true; do sleep 30; done"

  jupyter-gpu:
    image: jupyter/tensorflow-notebook:latest
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]
    volumes:
      - ./notebooks:/home/jovyan/work
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=compute,utility
    command: start-notebook.sh
