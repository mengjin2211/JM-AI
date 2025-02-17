#!/bin/bash
set -x
start_time=$SECONDS

python3 parallel_processing.py hugefile1_2_01.txt hugefile2_2_01.txt totalfile_2_01.txt &

python3 parallel_processing.py hugefile1_2_02.txt hugefile2_2_02.txt totalfile_2_02.txt &

wait
cat totalfile_2*.txt> totalfileA.txt
end_time=$SECONDS

diff=$((end_time-start_time))

echo "Processing 2 parallel takes: $diff seconds"
