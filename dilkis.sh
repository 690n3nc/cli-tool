#!/bin/bash


echo -e "-\n-\nlast 5 update(respectively):\n"
find ~/.cli-tool/ilkis_logs/ -type f -exec echo "update log file : {}" \; | sort -nr | head -n 5 

