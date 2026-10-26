"""Mon 26 Oct explainer videos: faceless, paper-and-maroon personal look, VoiceStudio narration.

Run: python3 -I build_videos.py <key> <aspect>   (key: 0700..1900, aspect: v=1080x1920, p=1080x1350)
Writes a HyperFrames project to out/<key>-<aspect>/ (index.html + assets/).
Beats are timed to the narration via word timestamps in audio/t-<key>.json.
"""
import html
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INK, DEEP, TEXT, BODY, MUTED, PAPER = "#8B1419", "#5E1015", "#17130F", "#2A241E", "#6A5F52", "#EFE7D6"

SPECS = {
    "0700": {
        "kicker": "API SECURITY", "cta": False,
        "beats": [
            ("title", None, ("The bug that leaks", "other customers' data.")),
            ("code", "A user opens", ["GET /api/invoices/1042", "200 OK  your invoice"], []),
            ("code", "They change it", ["GET /api/invoices/1043", "200 OK  someone else's invoice"], [1]),
            ("stmt", "No hacking tools", ("No tools.", "Just a number.")),
            ("stmt", "It happens because", ("Logged in", "is not allowed.")),
            ("code", "On every request", ["invoice = load(id)", "if invoice.owner != user.id:", "    return 403"], [1, 2]),
            ("stmt", "Then write a test", ("Test it with two users.", "Every release.")),
        ],
    },
    "0900": {
        "kicker": "EU FINTECH", "cta": True,
        "beats": [
            ("title", None, ("DORA, in plain words", "for engineers.")),
            ("stmt", "The Digital Operational", ("In force since", "January 2025.")),
            ("list", "In plain words", "Prove you can", [("withstand", "Withstand"), ("respond", "Respond"), ("recover", "Recover")]),
            ("stmt", "including incidents at", ("Including incidents at", "your suppliers.")),
            ("list", "For engineers that", "Three habits", [("Know which", "Map critical systems"), ("Test recovery", "Test recovery for real"), ("And treat", "Exit plans for third parties")]),
            ("stmt", "Teams that already", ("Mostly evidence,", "or a lot of work.")),
        ],
    },
    "1300": {
        "kicker": "PAYMENTS", "cta": False, "wordfix": {"1.": "One.", "2.": "Two.", "3.": "Three.", "4.": ""},
        "beats": [
            ("title", None, ("Is that webhook", "really from them?")),
            ("code", "How do you know", ["POST /webhooks/payments", '{ "event": "order.paid",', '  "order": "A-2291" }'], [1]),
            ("code", "If you do not check", ["anyone can send:", '{ "event": "order.paid" }', "goods shipped. for free."], [2]),
            ("list", "Three checks fix", "Three checks", [("Verify the signature", "Verify the signature"), ("Check the amount", "Match amount and currency"), ("Make the handler", "Safe to run twice")]),
            ("stmt", "Signature amount idempotency", ("Signature. Amount.", "Idempotency.")),
        ],
    },
    "1500": {
        "kicker": "CAREER", "cta": True,
        "beats": [
            ("title", None, ("Juniors report findings.", "Seniors report decisions.")),
            ("stmt", "An executive does", ("They don't need", "the severity score.")),
            ("list", "They need three", "What leaders need", [("What could happen", "Business impact"), ("How likely", "Likelihood and cost"), ("And the options", "Options and effort")]),
            ("stmt", "Then make a", ("Recommend.", "Then let them choose.")),
            ("stmt", "The goal is", ("Every risk,", "carried on purpose.")),
        ],
    },
    "1700": {
        "kicker": "MOBILE SECURITY", "cta": False,
        "beats": [
            ("title", None, ("Your mobile app", "is not a safe.")),
            ("code", "App files can", ["$ unzip app.apk", "res/values/strings.xml", '  PAYMENT_SECRET = "a9f3..."'], [2]),
            ("list", "So API keys", "Never in the app", [("API keys", "API keys"), ("admin tokens", "Admin tokens"), ("payment secrets", "Payment secrets")]),
            ("stmt", "Everything sensitive stays", ("Secrets stay", "on the server.")),
            ("list", "If a key has", "Already shipped?", [("Rotate it", "Rotate it"), ("restrict it", "Restrict it"), ("move that work", "Move it server side")]),
        ],
    },
    "1900": {
        "kicker": "QUESTION", "cta": False, "tail": 2.2,
        "beats": [
            ("title", None, ("5 findings.", "Time to fix 2.")),
            ("stmt", "which ones go", ("Which go", "first?")),
            ("stmt", "My rule is", ("Anything touching another", "user's data or money.")),
            ("stmt", "What is yours", ("What's", "yours?")),
        ],
    },
}

SIZES = {"v": (1080, 1920), "p": (1080, 1350)}


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower())


def find(words, phrase):
    toks = [norm(t) for t in phrase.split()]
    ws = [norm(w["word"]) for w in words]
    for i in range(len(ws) - len(toks) + 1):
        if ws[i : i + len(toks)] == toks:
            return words[i]["start"]
    raise SystemExit(f"phrase not found: {phrase!r}")


def caption_groups(words, maxw=4):
    groups, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        gap = words[i + 1]["start"] - w["end"] if i + 1 < len(words) else 9
        if len(cur) >= maxw or gap >= 0.15 or re.search(r"[.?!:]$", w["word"]):
            groups.append(cur)
            cur = []
    if cur:
        groups.append(cur)
    return groups


def build(key, aspect):
    W, H = SIZES[aspect]
    spec = SPECS[key]
    t = json.load(open(os.path.join(HERE, "audio", f"t-{key}.json")))
    words = [w for w in t["words"] if w["word"].strip()]
    fix = spec.get("wordfix", {})
    words = [dict(w, word=fix.get(w["word"].strip(), w["word"])) for w in words if fix.get(w["word"].strip(), w["word"]) != ""]
    audio_len = float(t.get("duration") or words[-1]["end"])
    tail = spec.get("tail", 3.0)
    total = round(audio_len + tail, 2)

    out = os.path.join(HERE, "out", f"{key}-{aspect}")
    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "assets", "fonts"))
    shutil.copy(os.path.join(HERE, "audio", f"v-{key}.wav"), os.path.join(out, "assets", "voice.wav"))
    for f in ("lora-normal.ttf", "lora-italic.ttf"):
        shutil.copy(os.path.join(HERE, "kit", f), os.path.join(out, "assets", "fonts", f))

    v = aspect == "v"
    # layout band: vertical keeps words between 168 and 1330 px
    top = 300 if v else 150
    band = 800 if v else 900
    cap_top = 1150 if v else 1140
    pad = 100
    title_fs = 104 if v else 88
    stmt_fs = 96 if v else 80
    code_fs = 44 if v else 38
    list_fs = 56 if v else 48
    cap_fs = 50 if v else 44

    starts = []
    for b in spec["beats"]:
        starts.append(0.0 if b[1] is None else round(find(words, b[1]) - 0.15, 2))
    ends = starts[1:] + [round(audio_len + 0.2, 2)]

    els, tw = [], []
    for i, (b, s, e) in enumerate(zip(spec["beats"], starts, ends)):
        bid = f"b{i}"
        dur = round(e - s, 2)
        kind = b[0]
        if kind in ("title", "stmt"):
            roman, ital = b[2]
            fs = title_fs if kind == "title" else stmt_fs
            inner = (
                (f'<div style="width:64px;height:3px;background:{INK};margin-bottom:34px"></div>' if kind == "title" else "")
                + f'<div class="ln" style="font:700 {fs}px/1.04 Lora;letter-spacing:-0.02em;color:{TEXT}">{html.escape(roman)}</div>'
                + f'<div class="ln" style="font:700 italic {fs}px/1.08 Lora;letter-spacing:-0.02em;color:{INK};margin-top:8px">{html.escape(ital)}</div>'
            )
        elif kind == "code":
            lines, hot = b[2], b[3]
            rows = "".join(
                f'<div class="ln" style="font:500 {code_fs}px/1.55 \'JetBrains Mono\';white-space:pre;font-variant-ligatures:none;color:{INK if j in hot else TEXT}">{html.escape(l)}</div>'
                for j, l in enumerate(lines)
            )
            inner = f'<div style="background:#F7F1E6;border:2px solid {TEXT};border-radius:14px;padding:40px 44px;box-shadow:10px 10px 0 {INK}">{rows}</div>'
        elif kind == "list":
            head, items = b[2], b[3]
            rows = f'<div style="font:600 {int(list_fs*0.5)}px Poppins;letter-spacing:.24em;text-transform:uppercase;color:{MUTED};margin-bottom:34px">{html.escape(head)}</div>'
            for j, (ph, label) in enumerate(items):
                rows += (
                    f'<div id="{bid}i{j}" class="li" style="display:flex;align-items:baseline;gap:28px;margin-top:22px;opacity:0">'
                    f'<span style="font:700 italic {list_fs}px Lora;color:{INK};min-width:56px">{j+1}</span>'
                    f'<span style="font:600 {list_fs}px/1.2 Poppins;color:{TEXT}">{html.escape(label)}</span></div>'
                )
                at = max(round(find(words, ph) - s - 0.1, 2), 0.2)
                tw.append(f'tl.fromTo("#{bid}i{j}",{{opacity:0,x:-30}},{{opacity:1,x:0,duration:0.35,ease:"power3.out"}},{s + at});')
            inner = rows
        els.append(
            f'<div id="{bid}" class="clip beat" data-start="{s}" data-duration="{dur}" data-track-index="2" '
            f'style="position:absolute;left:{pad}px;right:{pad}px;top:{top}px;height:{band}px;display:flex;flex-direction:column;justify-content:center;z-index:3"><div id="{bid}c">{inner}</div></div>'
        )
        if i == 0:
            tw.append(f'tl.fromTo("#{bid}c",{{opacity:1,y:0}},{{opacity:1,y:0,duration:0.01}},0);')
        else:
            tw.append(f'tl.fromTo("#{bid}c",{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.45,ease:"power3.out"}},{s});')
        tw.append(f'tl.to("#{bid}c",{{opacity:0,duration:0.2,ease:"power2.in"}},{round(e - 0.22, 2)});')

    # end card
    es = round(audio_len + 0.2, 2)
    ed = round(total - es, 2)
    cta = (
        f'<div style="font:500 {38 if v else 34}px/1.4 Poppins;color:{BODY};margin-top:40px">Open to security roles<br>in Europe and the UK</div>'
        if spec["cta"] else ""
    )
    els.append(
        f'<div id="end" class="clip" data-start="{es}" data-duration="{ed}" data-track-index="2" '
        f'style="position:absolute;left:{pad}px;right:{pad}px;top:{top}px;height:{band}px;display:flex;flex-direction:column;justify-content:center;z-index:3"><div id="endc">'
        f'<div style="width:64px;height:3px;background:{INK};margin-bottom:30px"></div>'
        f'<div style="font:700 {64 if v else 56}px Poppins;letter-spacing:.12em;color:{TEXT}">MICHAEL<br>ADEYANJU</div>'
        f'<div style="font:600 {28 if v else 26}px Poppins;letter-spacing:.22em;text-transform:uppercase;color:{INK};margin-top:22px">AppSec · Product Security</div>'
        f'{cta}'
        f'<div style="font:300 {40 if v else 36}px Poppins;color:{MUTED};margin-top:40px">michaeladeyanju.com</div>'
        f"</div></div>"
    )
    tw.append(f'tl.fromTo("#endc",{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.5,ease:"power3.out"}},{es});')

    # captions
    caps = []
    for gi, g in enumerate(caption_groups(words)):
        gs = round(max(g[0]["start"] - 0.05, 0.1), 2)
        ge = round(g[-1]["end"] + 0.1, 2)
        if ge > es:
            ge = es
        if ge - gs < 0.25:
            continue
        txt = " ".join(w["word"].strip() for w in g)
        caps.append(
            f'<div id="c{gi}" class="clip cap" data-start="{gs}" data-duration="{round(ge-gs,2)}" data-track-index="4" '
            f'style="position:absolute;left:0;right:0;top:{cap_top}px;text-align:center;z-index:6;overflow:visible">'
            f'<span id="c{gi}t" style="display:inline-block;font:600 {cap_fs}px/1.25 Poppins;color:{TEXT};background:rgba(239,231,214,.88);'
            f'padding:10px 26px;border-radius:10px;border-bottom:4px solid {INK};max-width:{W-2*pad}px">{html.escape(txt)}</span></div>'
        )
        tw.append(f'tl.fromTo("#c{gi}t",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.12,ease:"power2.out"}},{gs});')

    noise = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" preserveAspectRatio="none" '
        f'style="position:absolute;inset:0;mix-blend-mode:multiply;opacity:.30;z-index:1"><filter id="nq" filterUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">'
        f'<feTurbulence type="fractalNoise" baseFrequency="0.82" numOctaves="4" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>'
        f'<rect width="100%" height="100%" filter="url(#nq)" opacity="0.42"/></svg>'
    )
    chrome = (
        f'<div id="rule" style="position:absolute;left:56px;top:{140 if v else 64}px;bottom:{140 if v else 64}px;width:2px;background:{INK};opacity:.55;z-index:2"></div>'
        f'<div id="kick" style="position:absolute;left:{pad}px;top:{200 if v else 70}px;font:700 22px Poppins;letter-spacing:.34em;color:{INK};z-index:2">'
        f'{html.escape(spec["kicker"])} <span style="color:{MUTED}">/ MICHAEL ADEYANJU</span></div>'
        f'<div id="glow" style="position:absolute;width:{int(W*1.2)}px;height:{int(W*1.1)}px;right:-{int(W*0.45)}px;bottom:-{int(W*0.4)}px;'
        f'background:radial-gradient(circle closest-side,rgba(139,20,25,.11) 0%,rgba(139,20,25,.04) 54%,rgba(139,20,25,0) 100%);z-index:0"></div>'
    )
    tw.append(f'tl.fromTo("#glow",{{x:0,y:0}},{{x:-60,y:-40,duration:{total},ease:"none"}},0);')

    doc = f"""<!doctype html>
<html>
<head><meta charset="utf-8">
<style>
@font-face{{font-family:Lora;src:url('assets/fonts/lora-normal.ttf');font-weight:400 700;font-style:normal}}
@font-face{{font-family:Lora;src:url('assets/fonts/lora-italic.ttf');font-weight:400 700;font-style:italic}}
*{{margin:0;padding:0;box-sizing:border-box}}
#bg{{position:absolute;inset:0;background:{PAPER}}}
</style></head>
<body>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="{W}" data-height="{H}" style="position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:Poppins">
<div id="bg"></div>
{noise}
{chrome}
{''.join(els)}
{''.join(caps)}
<audio id="voice" class="clip" src="assets/voice.wav" data-start="0" data-duration="{round(audio_len,2)}" data-track-index="8" data-volume="1"></audio>
</div>
<script>
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tw)}
window.__timelines["main"] = tl;
</script>
</body></html>
"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(doc)
    print(out, total)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
