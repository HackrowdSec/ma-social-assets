"""Voice B narration with a transcript check; retries with another seed if the take is garbled."""
import difflib, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "audio")
S = json.load(open(os.path.join(HERE, "scripts.json")))
INSTRUCT = "male, middle-aged, moderate pitch, american accent"
NUM = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "10": "ten", "15": "fifteen", "90": "ninety"}
def norm(t):
    t = re.sub(r"[^a-z0-9 ]", " ", t.lower())
    return " ".join(NUM.get(w, w) for w in t.split())
def run(*a): return subprocess.run(a, capture_output=True, text=True)
for k in (sys.argv[1:] or S):
    open(f"{A}/txt-{k}.txt", "w").write(S[k])
    ok = False
    for seed in (11, 12, 13):
        r = run("curl", "-s", "--fail-with-body", "-m", "600", "http://localhost:3900/generate", "-F", f"text=<{A}/txt-{k}.txt",
                "-F", "language=en", "-F", f"instruct={INSTRUCT}", "-F", f"seed={seed}", "-o", f"{A}/raw-{k}.wav")
        if r.returncode: print(k, seed, "GEN FAIL", r.stdout[:200], flush=True); continue
        run("ffmpeg", "-v", "error", "-y", "-i", f"{A}/raw-{k}.wav", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", f"{A}/v-{k}.wav")
        run("curl", "-s", "-m", "300", "http://localhost:3900/v1/audio/transcriptions", "-F", f"file=@{A}/v-{k}.wav", "-F", "model=whisper-1",
            "-F", "language=en", "-F", "response_format=verbose_json", "-F", "timestamp_granularities[]=word", "-o", f"{A}/t-{k}.json")
        try: txt = json.load(open(f"{A}/t-{k}.json"))["text"]
        except Exception: txt = ""
        ratio = difflib.SequenceMatcher(None, norm(S[k]), norm(txt)).ratio()
        print(k, "seed", seed, "match", round(ratio, 3), "|", txt[:90], flush=True)
        if ratio >= 0.9:
            ok = True; json.dump({"seed": seed, "match": ratio}, open(f"{A}/meta-{k}.json", "w")); break
    print(k, "OK" if ok else "NEEDS LOOK", flush=True)
print("ALLDONE", flush=True)
