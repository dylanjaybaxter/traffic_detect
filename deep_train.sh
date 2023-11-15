docker build -f ./deep_docker/Dockerfile \
     -t deep_trainingimage .

docker run \
    -it -p 5000:5000 -e MASTER_ADDR=localhost -e MASTER_PORT=12355 \
    -v /datasets/deepsort:/app/data \
     --gpus all \
     --ipc=host deep_trainingimage
