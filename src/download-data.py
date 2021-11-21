# author : Group 30 - Block 3 - MDS UBC 
# date : 2021-11-19

'''Downloads csv data from a web url and saves it to a local filepath as csv file format

Usage: download_data.py --url=<url> --out_file=<out_file>

Options:
--url=<url>             URL from where to download the data (must be in standard csv format)
--out_file=<out_file>   Path (including filename) of where to locally write the file
'''

import pandas as pd
import os
from docopt import docopt

opt = docopt(__doc__)

def main(url, out_file):
  data = pd.read_csv(url)
  try:
    data.to_csv(out_file, index = False)
  except:
     os.makedirs(os.path.dirname(out_file))
     data.to_csv(out_file, index = False)

if __name__ == "__main__":
  main(opt["--url"], opt["--out_file"])