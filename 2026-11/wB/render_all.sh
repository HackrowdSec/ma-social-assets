#!/bin/sh
cd "$(dirname "$0")"
for k in 02-0700 02-0900 02-1300 02-1500 02-1700 02-1900 03-0700 03-0900 03-1300 03-1500 03-1700 03-1900 04-0700 04-0900 04-1300 04-1500 04-1700 04-1900 05-0700 05-0900 05-1300 05-1500 05-1700 05-1900 06-0700 06-0900 06-1300 06-1500 06-1700 06-1900 07-0700 07-0900 07-1300 07-1500 07-1700 07-1900 08-0700 08-0900 08-1300 08-1500 08-1700 08-1900; do
  while ! grep -qE "^$k (OK|NEEDS LOOK)" gen_audio.log; do sleep 20; done
  grep -q "^$k NEEDS LOOK" gen_audio.log && { echo "$k AUDIO NEEDS LOOK"; continue; }
  for a in v p; do
    python3 -I build_v2.py $k $a > build-$k-$a.log 2>&1 || { echo "$k-$a BUILD FAIL: $(tail -1 build-$k-$a.log)"; continue; }
    for try in 1 2; do
      (cd out/$k-$a && timeout 900 npx hyperframes render --skill=hyperframes --quiet -o ../../final/wB-$k-$a.mp4 . > ../../render-$k-$a.err 2>&1)
      [ -f final/wB-$k-$a.mp4 ] && break
    done
    echo "$k-$a $(ffprobe -v error -show_entries format=duration -of csv=p=0 final/wB-$k-$a.mp4 2>/dev/null || echo RENDER FAIL)"
  done
done
echo ALLDONE
