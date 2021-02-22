from time_conv import *
from bpm import *
from dataset import get_dataset
from conf import conf

df = get_dataset(conf)

start_sec = 0
end_sec = df.end.max()

df = time_filter(df, start_sec, end_sec)

print(
	"Number of premature P waves {}".format(
		len(get_waves_with_tags(df, "P", ["premature"]))
	)
)

print(
	"Number of premature QRS waves {}".format(
		len(get_waves_with_tags(df, "QRS", ["premature"]))
	)
)

print(
	"Mean heart rate: {:.3f}".format(
		get_mean_bpm(df, start_sec, end_sec)
	)
)

val, occ_time = get_bpm_min(df, start_sec, end_sec)
t = sec_to_date_time(date_time_to_sec(conf["start_recording_date_time"]) + occ_time * 60)
print("Minimum heart rate: {} at {}".format(val, t))

val, occ_time = get_bpm_max(df, start_sec, end_sec)
t = sec_to_date_time(date_time_to_sec(conf["start_recording_date_time"]) + occ_time * 60)
print("Maximum heart rate: {} at {}".format(val, t))