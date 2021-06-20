#!/usr/bin/python3

import argparse
import os
from video2img import convert

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument(
    'video', 
    type=str, 
    help='video to convert to images'
)

parser.add_argument(
    'out_folder',
    type=str,
    nargs='?',
    help='Want a special output directory ?',
)

parser.add_argument(
    '-r', '--recurse',
    action='store_true',
    help='Do you want to recurse through folders ?',
    default=False,
    dest='recurse'
)

args = parser.parse_args()

if not os.path.exists(args.video):
    raise FileNotFoundError(args.video)
elif os.path.isdir(args.video) and not args.recurse:
    print(f"{args.video} is a folder, pass -r or --recurse to fo inside the folder.")
    exit(0)

if not args.out_folder:
    args.out_folder = 'output_'+(args.video.split('.')[0].split('/')[-1])

convert(args.video, args.out_folder, args.recurse)
