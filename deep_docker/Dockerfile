# Use an official PyTorch runtime as a parent image
FROM pytorch/pytorch:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install numpy matplotlib torch torchvision

# Define environment variable
ENV NAME World

# Mount the dataset from /datasets/ to /app/datasets/
VOLUME /app/datasets

# Run your script when the container launches
CMD python3 ./deep_sort/deep/train.py --data_dir /app/data
