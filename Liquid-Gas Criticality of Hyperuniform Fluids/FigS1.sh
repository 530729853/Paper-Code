#!/bin/bash

name="Spinner-"

num=1
temp1="$name""$num"
while test -e $temp1"/FigS1.py" 
do
    cd "$temp1"
    python3 FigS1.py
    cd ../

    let num++
    temp1="$name""$num"
done
