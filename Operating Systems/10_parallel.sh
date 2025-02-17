#!/bin/bash
set -x
set -e
set -u

start_time=$SECONDS


for i in {1..10}; do
	num=$(printf "%02d" $i)
	python3 parallel_processing.py hugefile1_10_"$num".txt hugefile2_10_"$num".txt totalfile_10_"$num".txt &
done

wait 

cat totalfile_10_*.txt > totalfileB.txt

end_time=$SECONDS
diff=$((end_time-start_time))

echo "Processing 10 parallel takes: $diff seconds.

