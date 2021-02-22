import pandas as pd
from tempfile import NamedTemporaryFile
import csv
import numpy as np
import requests


def dump_file(conf):
	url = conf["csv_url"]
	r = requests.get(url)
	open('record.csv', 'wb').write(r.content)


def reformat_csv():
	with NamedTemporaryFile(mode='r+', delete=False) as tmp_file:
		with open('record.csv', newline='', mode='r') as csv_file:
			reader = csv.reader(csv_file, delimiter=',')
			writer = csv.writer(tmp_file, delimiter=',', lineterminator='\n')

			for row in reader:
				writer.writerow([row[0], row[1], row[2], '#'.join(row[3:])])

	return tmp_file


def get_dataset(conf):
	dump_file(conf)
	tmp_ds = reformat_csv()

	return pd.read_csv(
		tmp_ds.name,
		names=["wave", "start", "end", "tags"], 
		converters={"tags": lambda x : x.split("#")}
	)