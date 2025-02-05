#!/bin/bash

# Load conda environment
source /home/naod/miniconda3/etc/profile.d/conda.sh  
conda activate w7-env  

# Run the script
/home/naod/miniconda3/envs/w7-env/bin/python /home/naod/Projects/tenx/W7/Telegram-Medical-Data-Warehouse/src/scrape.py
