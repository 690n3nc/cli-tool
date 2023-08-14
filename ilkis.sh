#!/bin/bash

stampoftime=$(date +"%s")

echo -e "$stampoftime\n-\n-\nlog of update, upgrade prompt on:\n$(date --date=@$stampoftime)\n-\n-" > ~/.cli-tool/ilkis_logs/$stampoftime.ilkis


sudo apt update -y 2> ~/.cli-tool/ilkis_logs/.$stampoftime.ilkis1;

sudo apt upgrade -y 2> ~/.cli-tool/ilkis_logs/.$stampoftime.ilkis2;

sudo apt dist-upgrade -y 2> ~/.cli-tool/ilkis_logs/.$stampoftime.ilkis3;


cat ~/.cli-tool/ilkis_logs/.$stampoftime.ilkis[1,2,3] | tee -a ~/.cli-tool/ilkis_logs/$stampoftime.ilkis

rm ~/.cli-tool/ilkis_logs/.$stampoftime.ilkis[1,2,3]


echo -e "-\n-\n$(date --date=@$stampoftime), log is created\nunder ilkis_logs.\n"

