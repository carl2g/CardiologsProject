import numpy as np
import pandas as pd
from filters import time_filter, get_waves_with_tags, get_waves


def get_mean_bpm(df: pd.DataFrame, start: int, end: int):
	filtered_time = time_filter(df, start, end)
	delt = (end - start) / 60000
	waves_df = get_waves(filtered_time, "QRS")
	return len(waves_df) / delt


def get_bpms(df: pd.DataFrame, start: int, end: int):
	tmp_start = start
	tmp_end = start
	bpms = []

	while tmp_start < end:
		tmp_end = tmp_start + 60000
		
		if tmp_end > end:
			tmp_end = end

		bpms.append(get_mean_bpm(df, tmp_start, tmp_end))
		tmp_start = tmp_end

	return bpms


def get_bpm_max(df: pd.DataFrame, start: int, end: int):
	bpms = get_bpms(df, start, end)
	max_bpm = max(bpms)
	return max_bpm, bpms.index(max_bpm)


def get_bpm_min(df: pd.DataFrame, start: int, end: int):
	bpms = get_bpms(df, start, end)
	min_bpm = min(bpms)
	return min_bpm, bpms.index(min_bpm)
