
# Imports
import datetime
import os
from tensorboard import program
from torch.utils.tensorboard import SummaryWriter
from ultralytics import YOLO
import argparse
import yaml

# Defaults
default_config_ = "default_config.yaml"

# Parser Setup
def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default=default_config_, help='Path to training config')
    return parser

# Main Func
def main_func(args):
    # Initialize config
    with open(args.config, 'r') as file:
        conf = yaml.safe_load(file)

    # Initialize Tensorboard
    log_dir = os.path.join(conf['project'], conf['name'])
    if os.path.exists(log_dir):
        ad_num = 2
        while os.path.exists(log_dir+str(ad_num)):
            ad_num+=1
        log_dir = log_dir+str(ad_num)
    tb = program.TensorBoard()
    tb.configure(argv=[None, '--logdir', log_dir, '--port', '6006', '--bind_all'])
    url = tb.launch()
    print(f"Tensorboard started listening to {log_dir} and broadcasting on {url}")

    # Load Model
    model = YOLO(conf['model'])

    # Do Training
    model.train(cfg=args.config, data=conf['data'])

    # Kill TensorBoard
    tb.kill()

# Main func wrapper
if __name__ == "__main__":
    args = init_parser().parse_args()
    main_func(args)
    print("Done!")
