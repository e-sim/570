#!/bin/sh
#author: Erica Sim

while read curr; do
	RESULT="$(echo $curr | carmel -sliq $1 2>&1 | tail -n 1)"
	if [[ $RESULT =~ .*Empty.* ]] #stderr says "Empty or invalid..." w/ no match
	then
		echo "$curr => no" 
	else
		echo "$curr => yes"
	fi
done < $2