#!/bin/bash

split -n l/2 --numeric-suffixes=1 hugefile1.txt hugefile1_2_ --additional-suffix=.txt
split -n l/2 --numeric-suffixes=1 hugefile2.txt hugefile2_2_ --additional-suffix=.txt
split -n l/10 --numeric-suffixes=1 hugefile1.txt hugefile1_10_ --additional-suffix=.txt
split -n l/10 --numeric-suffixes=1 hugefile2.txt hugefile2_10_ --additional-suffix=.txt



