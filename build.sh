#!/usr/bin/env sh
set -eu
rm -rf dist
mkdir -p dist
cp index.html styles.css app.js analytics.js dist/
cp -R public/. dist/
printf '%s\n' 'Static build ready in dist/'
