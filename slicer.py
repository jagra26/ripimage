# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:46:08 2021

@author: jagra26
"""
from alive_progress import alive_bar
#from tqdm import tqdm
from ripper import slice, save_tiles
import glob
import os
import argparse

def get_prefix(filename, foldername):
    splitedFile = filename.split("\\")
    splitedFile = splitedFile[1].split(".")
    splitedFolder = foldername.split("\\")
    return splitedFolder[-1] + "_" + splitedFile[0]
    

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="path to folder", default="testImages")
parser.add_argument("-d", "--directory", help="output directory")
parser.add_argument("-c", "--collumns", type=int, help="number of collumns", default=8)
parser.add_argument("-r", "--rows", type=int, help="number of rows", default=6)
args = parser.parse_args()

if args.directory is None:
    if not os.path.exists(args.path + "Sliced"):
        os.mkdir(args.path + "Sliced")
    directory = args.path + "Sliced"
else: directory = args.directory

files = glob.glob(args.path+"/*")

count = 1
with alive_bar(len(files)) as bar:
    for i in (range(len(files))):
        try:
            filename = files[i]
            tiles = slice(filename, col=args.collumns, row=args.rows, save=False)
            save_tiles(tiles, prefix=get_prefix(filename, args.path), directory=directory)
            bar()
        except Exception as e: print(e)
print("end")