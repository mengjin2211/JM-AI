#!/bin/bash

start_time=$SECONDS


for i in {1..10}; do
	python3 parallel_processing.py hugefile1_10_$i.txt hugefile2_10_$i.txt totalfile_10_$i.txt &
done

wait 

cat totalfile_10_*.txt>totalfileB.txt
end_time=$SECONDS
diff=$((end_time-start_time))

echo "Processing 10 parallel takes: $diff seconds."
