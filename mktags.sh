#!/usr/bin/env sh

echo Writing tags.txt
awk 'BEGIN { ORS=" " } { print $1 }' doc/tags | fold -sw 78 > doc/tags.txt
