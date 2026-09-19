#!/bin/bash

filecnt=0

for file in *.*; do
    echo "FILE: $file"
    echo "Size: $(du -h $file | cut -f1)"
    stat $file | awk "NR>=5 && NR<=6"

    if test -r $file; then
        echo "Can read: True"
    else
        echo "Can read: False"
    fi
    
    if test -w $file; then
        echo "Can write: True"
    else
        echo "Can write: False"
    fi

    if test -x $file; then
        echo "Can execute: True"
    else
        echo "Can execute: False"
    fi
    echo 

    # arithmetic context not necessary
    # since the file is already 
    ((filecnt+=1))

done

echo "---------------------------"
echo "Total file count: $filecnt"