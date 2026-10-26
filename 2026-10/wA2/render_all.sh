#!/bin/sh
cd "$(dirname "$0")"
for k in 29-0700 29-0900 29-1300 29-1500 29-1700 29-1900 30-0700 30-0900 30-1300 30-1500 30-1700 30-1900 31-0700 31-0900 31-1300 31-1500 31-1700 31-1900 01-0700 01-0900 01-1300 01-1500 01-1700 01-1900; do
  while ! grep -qE "^$k (OK|NEEDS LOOK)" gen_audio.log; do sleep 20; done
  grep -q "^$k NEEDS LOOK" gen_audio.log && { echo "$k AUDIO NEEDS LOOK"; continue; }
  for a in v p; do
    python3 -I build_v2.py $k $a > build-$k-$a.log 2>&1 || { echo "$k-$a BUILD FAIL: $(tail -1 build-$k-$a.log)"; continue; }
    for try in 1 2; do
      (cd out/$k-$a && timeout 900 npx hyperframes render --skill=hyperframes --quiet -o ../../final/wA-$k-$a.mp4 . > ../../render-$k-$a.err 2>&1)
      [ -f final/wA-$k-$a.mp4 ] && break
    done
    echo "$k-$a $(ffprobe -v error -show_entries format=duration -of csv=p=0 final/wA-$k-$a.mp4 2>/dev/null || echo RENDER FAIL)"
  done
done
echo ALLDONE
