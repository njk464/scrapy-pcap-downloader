#!/bin/bash
cd pcaps/full

# specify the path here
PATH="/home/nkantor/pcaps/"

CP=/bin/cp 

for filename in *; do
	$CP $filename $PATH
done