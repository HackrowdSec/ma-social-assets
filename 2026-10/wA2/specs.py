# Week A, Thu 29 Oct to Sun 1 Nov beats for build_v2.py
SPECS = {
    # THU 29
    "29-0700": {"kicker": "PAYMENTS", "cta": False, "beats": [
        ("hook", None, ("Send", "minus 500."), ("code", ['POST /transfer', '{ "to": "you",', '  "amount": -500 }'], [2])),
        ("stmt", "In some apps", ("The money moves", "the wrong way.")),
        ("ui", "A transfer of", ["Transfer", "From you to me: -500", "Result: 500 moves to you"], [2]),
        ("stmt", "The same trick", ("Quantities. Refunds.", "Tips.")),
        ("list", "Validate every amount", "Validate on the server", [("positive", "Positive"), ("within limits", "Within limits"), ("right currency", "Right currency"), ("right decimals", "Right decimals")]),
        ("stmt", "Never trust the", ("Never trust the client's", "sign, size or format.")),
    ]},
    "29-0900": {"kicker": "ACCOUNT TAKEOVER", "cta": True, "beats": [
        ("hook", None, ("Your OTP went to", "their phone."), ("ui", ["SMS", "Your code is 482 913", "Delivered to: new SIM"], [2])),
        ("stmt", "That is a", ("The login wasn't", "the weak link.")),
        ("stmt", "Recovery was", ("Recovery was.", "")),
        ("ui", "Attackers move your", ["Number moved", "To: attacker's SIM", "Password reset by text"], [1, 2]),
        ("list", "Use an authenticator", "Three defences", [("Use an authenticator", "Authenticator app or passkeys"), ("Add a", "Cooling-off after a number change"), ("watch for", "Flag new device + new number")]),
    ]},
    "29-1300": {"kicker": "PAYMENTS", "cta": False, "beats": [
        ("hook", None, ("Pressed pay", "twice?"), ("ui", ["Checkout", "Pay EUR 49.00", "Charged twice"], [2])),
        ("stmt", "Without an idempotency", ("Without an idempotency key,", "maybe.")),
        ("code", "The fix the", ["POST /payments", "Idempotency-Key: 8f2c-41a0", '-> first result stored'], [1]),
        ("code", "If the same", ["same key again?", "-> return stored result", "-> no second charge"], [1, 2]),
        ("stmt", "Same request same", ("Same request.", "Same answer.")),
    ]},
    "29-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Findings that", "get fixed."), ("ui", ["Security finding", "Severity: High", "Developer: \"what do I change?\""], [2])),
        ("stmt", "Most security findings", ("Hard to read,", "not hard to fix.")),
        ("list", "A finding", "Four parts", [("Where it is", "Where: the exact request"), ("What an attacker", "Impact: one sentence"), ("How to reproduce", "Reproduce in five minutes"), ("And the fix", "The fix, with code")]),
        ("stmt", "If a developer", ("Reproducible before the coffee cools?", "Fixed this sprint.")),
    ]},
    "29-1700": {"kicker": "MOBILE SECURITY", "cta": False, "beats": [
        ("hook", None, ("New phone, same day?", "Flag it."), ("ui", ["Account activity", "New device: Pixel, 09:12", "Number changed, 09:20"], [1, 2])),
        ("stmt", "In mobile banking", ("One of the clearest", "takeover signals.")),
        ("stmt", "Device binding ties", ("Device binding:", "accounts on known devices.")),
        ("list", "When a new", "New device? Step up", [("confirm on the old", "Confirm on the old device"), ("verify identity", "Verify identity"), ("or hold", "Hold high-risk actions")]),
        ("stmt", "Real users barely", ("Real users barely notice.", "Attackers hit a wall.")),
    ]},
    "29-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Which second", "factor?"), ("ui", ["Your users' MFA", "SMS code", "Authenticator app", "Passkey"], [3])),
        ("list", "SMS is easy", "Trade-offs", [("SMS is easy", "SMS: easy, interceptable"), ("Authenticator apps", "Apps: stronger"), ("Passkeys resist", "Passkeys: phishing-resistant")]),
        ("stmt", "What do you", ("What do you use?", "What's stopping you?")),
    ]},
    # FRI 30
    "30-0700": {"kicker": "BUSINESS LOGIC", "cta": False, "beats": [
        ("hook", None, ("Skip step 2.", "Get step 3."), ("ui", ["Checkout", "1  Cart", "2  Payment  (skipped)", "3  Confirmed"], [2, 3])),
        ("stmt", "In some apps", ("Confirmed", "without payment.")),
        ("stmt", "That is a", ("A logic flaw.", "Scanners rarely find it.")),
        ("code", "The fix the", ["order.state == 'PAID'", "  -> allow confirm", "else -> 409"], [0]),
        ("stmt", "Test it by", ("Call every step", "out of order.")),
    ]},
    "30-0900": {"kicker": "FINTECH", "cta": True, "beats": [
        ("hook", None, ("Fraud and security,", "one table."), ("ui", ["Two teams", "Security: odd login, Monday", "Fraud: loss, Tuesday"], [1, 2])),
        ("stmt", "Attackers like that", ("Attackers live", "in the gap.")),
        ("list", "Three things to", "Share", [("Login and device", "Login and device signals"), ("Known bad", "Known bad accounts and cards"), ("And alerts", "Alerts, both ways")]),
        ("stmt", "When fraud and", ("Same events.", "Same attacker, caught earlier.")),
    ]},
    "30-1300": {"kicker": "API SECURITY", "cta": False, "beats": [
        ("hook", None, ("Make yourself", "admin."), ("code", ["PATCH /me", '{ "name": "Ana",', '  "isAdmin": true }'], [2])),
        ("stmt", "If your code", ("Every field copied in?", "Now you're admin.")),
        ("stmt", "That is mass", ("Mass", "assignment.")),
        ("code", "The fix allow", ["ALLOWED = {'name', 'email'}", "data = {k: v for k, v in body.items()", "        if k in ALLOWED}"], [0]),
        ("stmt", "And test by", ("Send fields", "the form never shows.")),
    ]},
    "30-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Ten bugs.", "Time for two."), ("ui", ["Findings", "10 open", "Sprint capacity: 2"], [2])),
        ("list", "First anything", "Fix first", [("another user's", "Cross-user data or money"), ("without logging", "Reachable without login"), ("easy to exploit", "Easy to exploit at scale")]),
        ("stmt", "Everything else gets", ("Everything else:", "a date and an owner.")),
        ("stmt", "Severity scores help", ("Scores help.", "Business impact decides.")),
    ]},
    "30-1700": {"kicker": "FRAUD", "cta": False, "beats": [
        ("hook", None, ("One person.", "Fifty accounts."), ("ui", ["New sign-ups, last hour", "50 accounts", "1 device  1 card"], [2])),
        ("stmt", "Referral and promo", ("Fraud that looks", "like growth.")),
        ("list", "The signals are", "Signals", [("Same device", "Same device"), ("Same bank", "Same card or account"), ("Same address", "Same address pattern"), ("Signups", "Bursts of sign-ups")]),
        ("list", "Limit rewards per", "Controls", [("Limit rewards", "Cap per device and card"), ("Pay rewards only", "Pay after a real transaction"), ("review bursts", "Review bursts before payout")]),
    ]},
    "30-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Strangest fraud", "you've seen?"), ("ui", ["This year", "The obvious ones", "The weird ones"], [2])),
        ("stmt", "Not the obvious", ("Not the obvious.", "The clever, slow, weird ones.")),
        ("stmt", "Share one without", ("Share one.", "No names.")),
    ]},
    # SAT 31
    "31-0700": {"kicker": "HALLOWEEN", "cta": False, "beats": [
        ("hook", None, ("Nobody knows", "who deployed it."), ("ui", ["Server: test-old-2", "Owner: unknown", "Last patched: 2023"], [1, 2])),
        ("stmt", "No owner no", ("No owner. No updates.", "Still connected.")),
        ("stmt", "Every forgotten test", ("A door someone else", "might find first.")),
        ("list", "The fix is", "The boring fix", [("owner tag", "Every resource has an owner"), ("gets flagged", "Untagged gets flagged"), ("once a month", "Monthly: switch off the unclaimed")]),
    ]},
    "31-0900": {"kicker": "AWARENESS MONTH", "cta": True, "beats": [
        ("hook", None, ("Five habits.", "All year."), ("ui", ["October", "Awareness month: over", "The habits: not over"], [2])),
        ("list", "habits worth keeping", "Keep these", [("multi-factor", "MFA on every admin"), ("Rotate secrets", "Rotate shared secrets"), ("Test your backups", "Restore a backup"), ("Remove access", "Remove leavers' access"), ("an attacker would", "Review one feature a month")]),
        ("stmt", "None of them", ("None are new.", "All of them work.")),
    ]},
    "31-1300": {"kicker": "API SECURITY", "cta": False, "beats": [
        ("hook", None, ("The API nobody", "remembers."), ("code", ["GET /v1/users   200 OK", "GET /test/export  200 OK", "owner: ???"], [1, 2])),
        ("stmt", "Old versions test", ("Old versions. Test endpoints.", "Forgotten tools.")),
        ("list", "Start with an", "Inventory from", [("your gateway", "The gateway"), ("your code", "The code"), ("traffic logs", "The traffic")]),
        ("stmt", "Anything live that", ("Owned,", "or switched off.")),
    ]},
    "31-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Your portfolio is", "your notes."), ("ui", ["Write-ups", "Lab 1: IDOR in a test app", "Lab 2: JWT misconfig"], [1, 2])),
        ("list", "A short post", "Each write-up", [("what you tested", "What you tested"), ("what you found", "What you found"), ("how it's fixed", "How it's fixed")]),
        ("stmt", "Hiring managers can't", ("They can't see study hours.", "They can see write-ups.")),
        ("stmt", "And writing clearly", ("Clear writing is", "half the job.")),
    ]},
    "31-1700": {"kicker": "AUTHENTICATION", "cta": False, "beats": [
        ("hook", None, ("Logged in", "forever."), ("ui", ["Session", "Remember me: forever", "Stolen session: works forever"], [2])),
        ("list", "Sessions should expire", "Do this", [("expire after inactivity", "Idle timeout"), ("fixed time", "Absolute lifetime"), ("Sensitive actions", "Re-auth for sensitive actions"), ("changing a password", "Password change ends all sessions")]),
        ("stmt", "Convenient for users", ("Convenient for users.", "No forever key.")),
    ]},
    "31-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("One habit for", "November."), ("ui", ["Awareness month", "Over", "Your habit: ?"], [2])),
        ("stmt", "What is one", ("What's yours?", "")),
        ("stmt", "Pick one", ("Pick one.", "Say it out loud.")),
    ]},
    # SUN 1
    "01-0700": {"kicker": "RESILIENCE", "cta": False, "beats": [
        ("hook", None, ("Have you ever", "restored it?"), ("ui", ["Backups", "Nightly: success", "Last restore test: never"], [2])),
        ("stmt", "A backup you", ("Never restored?", "That's a hope.")),
        ("list", "Once a month", "Monthly", [("restore a backup", "Restore to test"), ("time how long", "Time it"), ("check the data", "Check the data")]),
        ("stmt", "And keep at", ("One copy attackers", "can't delete.")),
    ]},
    "01-0900": {"kicker": "RANSOMWARE", "cta": True, "beats": [
        ("hook", None, ("Encrypted by", "Monday."), ("ui", ["Files", "report.xlsx.locked", "backup.tar.locked"], [1, 2])),
        ("stmt", "It starts weeks", ("It started weeks", "earlier.")),
        ("list", "For engineering teams", "The familiar defences", [("Multi-factor", "MFA on remote access"), ("Patch", "Patch the edge fast"), ("Limit who", "Limit who reaches what"), ("And backups", "Separate, tested backups")]),
    ]},
    "01-1300": {"kicker": "CYBER HYGIENE", "cta": False, "beats": [
        ("hook", None, ("admin /", "admin"), ("ui", ["Login", "Username: admin", "Password: admin   Welcome!"], [2])),
        ("stmt", "Dashboards databases routers", ("Shipped with defaults.", "Never changed.")),
        ("stmt", "Someone installs it", ("Change it later.", "Later never comes.")),
        ("list", "Make it part", "Setup checklist", [("change defaults", "Change defaults before go-live"), ("single sign-on", "Admin panels behind SSO"), ("scan for default", "Scan for default logins")]),
    ]},
    "01-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("What's the", "blast radius?"), ("ui", ["If this key leaks", "Reaches: 1 service", "Not: everything"], [1])),
        ("stmt", "If this key", ("How far can", "an attacker get?")),
        ("list", "A small blast", "Design it small", [("Separate accounts", "Separate accounts and roles"), ("Short-lived", "Short-lived credentials"), ("Limits on what", "Narrow service reach")]),
        ("stmt", "You can't stop", ("Every mistake,", "made small.")),
    ]},
    "01-1700": {"kicker": "IDENTITY", "cta": False, "beats": [
        ("hook", None, ("Codes can be", "phished."), ("ui", ["log1n-yourbank.example", "Password: ••••••", "Code: 482 913"], [0])),
        ("stmt", "A fake login", ("Relayed to the real site", "in real time.")),
        ("stmt", "Passkeys can't be", ("Passkeys are bound", "to the real site.")),
        ("stmt", "For admins and", ("Admins first.", "Then everyone.")),
    ]},
    "01-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Your biggest win", "this year?"), ("ui", ["This year", "Scariest incident", "Biggest win"], [2])),
        ("stmt", "Not the scariest", ("Not the incident.", "The win.")),
        ("stmt", "The fix the", ("The fix, the habit,", "the tool. Share it.")),
    ]},
}
