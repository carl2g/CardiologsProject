import pandas as pd


def get_waves_with_tags(df, wave_type, tag):
	return df[(df.wave == wave_type) & (pd.DataFrame(df.tags.tolist()).isin(tag).any(1).values)]


def get_waves(df, wave_type):
	return df[df.wave == wave_type]


def time_filter(df, start: int, end: int):
	return df[(df.start >= start) & (df.end < end)]
