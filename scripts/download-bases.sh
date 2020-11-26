#!/bin/bash
links="links-download.txt"

while IFS= read -r line
    do
        wget "$line" -P ../download/
    done < "$links"
