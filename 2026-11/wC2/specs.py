# Week C, Mon 9 to Sun 15 Nov beats for build_v2.py. Cloud and identity.
# Anchors: plain words only (no digits, apostrophes, hyphens), never the clip's first word, searched in order.
SPECS = {
    # MON 9
    "09-0700": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("The bucket", "was public."), ("ui", ["company-exports", "Access: Public", "invoices_2026.csv  ·  passports.zip"], [1])),
        ("stmt", "No hack needed", ("No hack", "needed.")),
        ("list", "Public buckets usually", "How it happens", [("quick fix", "A quick fix during testing"), ("website asset", "A website asset folder"), ("old bucket", "An old bucket, older defaults")]),
        ("list", "Turn on public", "The fix", [("Turn on public", "Block public access, account-wide"), ("signed links", "Short-lived signed links"), ("scan for anything", "Scan for public, daily")]),
    ]},
    "09-0900": {"kicker": "CLOUD SECURITY", "cta": True, "beats": [
        ("hook", None, ("The cloud didn't", "secure that."), ("ui", ["Shared responsibility", "Provider: data centres, hardware", "You: identity, config, data, code"], [2])),
        ("stmt", "That is the", ("Where many breaches", "start.")),
        ("list", "You own your", "Your side", [("identities and permissions", "Identities and permissions"), ("your configuration", "Configuration"), ("network rules", "Network rules"), ("your data", "Data and code")]),
        ("stmt", "Know which side", ("Know your side.", "Name an owner.")),
    ]},
    "09-1300": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("Keys that", "never expire."), ("code", ["AccessKeyId: AKIA...7Q", "Created: 2023-03-14", "Last used: today", "Expires: never"], [1, 3])),
        ("stmt", "get copied", ("Copied into scripts,", "laptops, chats.")),
        ("stmt", "expire on their", ("Short-lived credentials", "expire on their own.")),
        ("list", "Use roles for", "Replace them", [("Use roles for", "Roles for workloads"), ("for people", "SSO for people"), ("rotate them", "Rotate the rest"), ("delete the ones", "Delete unused keys")]),
    ]},
    "09-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("A day in", "cloud security."), ("ui", ["Today", "09:30  Review Terraform PR", "14:00  Tune alerts", "16:00  Fix wide permissions"], [1, 2, 3])),
        ("stmt", "Less hacking than", ("Less hacking.", "More building.")),
        ("list", "Reviewing infrastructure changes", "The work", [("Reviewing infrastructure", "Review infra changes"), ("Tuning alerts", "Tune alerts"), ("Fixing permissions", "Fix wide permissions"), ("Helping developers", "Secure defaults for devs")]),
        ("stmt", "The best ones", ("Read code. Explain risk.", "Automate the boring.")),
    ]},
    "09-1700": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("Open to the", "whole internet."), ("code", ["Inbound rule", "Port: 5432 (PostgreSQL)", "Source: 0.0.0.0/0"], [2])),
        ("stmt", "Rules that allow", ("Fine for websites.", "Not for databases.")),
        ("stmt", "Automated scanners find", ("Scanners find them", "within minutes.")),
        ("list", "Allow only the", "The fix", [("Allow only", "Allow only known addresses"), ("behind a", "Admin behind a VPN"), ("alert whenever", "Alert on open sensitive ports")]),
    ]},
    "09-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Your oldest", "key?"), ("ui", ["Access keys", "Oldest key created", "? days ago"], [2])),
        ("stmt", "A week A", ("A week? A year?", "Older than staff?")),
        ("stmt", "Check today and", ("Check today.", "Tell me the number.")),
    ]},
    # TUE 10
    "10-0700": {"kicker": "DEVSECOPS", "cta": False, "beats": [
        ("hook", None, ("The pipeline has", "prod keys."), ("code", ["deploy.yml", "env:", "  AWS_ROLE: prod-admin", "on: push  (any branch)"], [2, 3])),
        ("stmt", "So anyone who", ("Control the pipeline,", "control production.")),
        ("stmt", "An attacker who", ("Edit a workflow.", "Inherit production.")),
        ("list", "Protect the main", "Protect it", [("Protect the main", "Protect main, require reviews"), ("Pin", "Pin actions to exact versions"), ("Separate build", "Separate build from deploy"), ("deploy step only", "Least privilege for deploy")]),
    ]},
    "10-0900": {"kicker": "DEVSECOPS", "cta": True, "beats": [
        ("hook", None, ("No secrets", "in CI."), ("code", ["permissions:", "  id-token: write", "# no AWS_SECRET_ACCESS_KEY", "# short-lived token per job"], [1, 2])),
        ("stmt", "With workload identity", ("Workload identity:", "no stored secrets.")),
        ("stmt", "Your CI system", ("A signed token in.", "Temporary credentials out.")),
        ("list", "Set it up", "Do this", [("Set it up", "Set up workload identity"), ("scope the trust", "Trust one repo, one branch"), ("delete the old", "Delete the old keys")]),
    ]},
    "10-1300": {"kicker": "KUBERNETES", "cta": False, "beats": [
        ("hook", None, ("Three Kubernetes", "settings."), ("code", ["securityContext:", "  privileged: true", "  runAsUser: 0"], [1, 2])),
        ("list", "Access control", "Get these right first", [("Access control", "Access control (RBAC)"), ("Pod security", "Pod security: no root"), ("Network policies", "Network policies")]),
        ("stmt", "By default every", ("By default, every pod", "talks to every pod.")),
        ("stmt", "Get these", ("These three first.", "Then the fancy stuff.")),
    ]},
    "10-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Which cloud for", "your career?"), ("ui", ["Pick one", "AWS", "Azure", "Google Cloud"], [1, 2, 3])),
        ("stmt", "Less than you", ("The ideas", "transfer.")),
        ("list", "Identity networking logging", "Same everywhere", [("Identity", "Identity"), ("networking", "Networking"), ("logging", "Logging"), ("encryption", "Encryption")]),
        ("stmt", "Pick the cloud", ("Go deep on one.", "Learn the others' names.")),
    ]},
    "10-1700": {"kicker": "CONTAINERS", "cta": False, "beats": [
        ("hook", None, ("Your container", "runs as root."), ("code", ["FROM node:14", "# base image: 2 years old", "USER root"], [0, 2])),
        ("stmt", "If an attacker", ("Break in as root,", "start with full power.")),
        ("stmt", "Old base images", ("Old images ship", "known vulnerabilities.")),
        ("list", "Run as a", "The fix", [("Run as a", "Run as non-root"), ("small regularly", "Small, updated base images"), ("Scan images", "Scan in the pipeline"), ("rebuild on", "Rebuild on a schedule")]),
    ]},
    "10-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Who can deploy", "to prod?"), ("ui", ["Deploy access", "Everyone", "Only the pipeline", "One laptop"], [1, 2, 3])),
        ("stmt", "The answer tells", ("The answer", "tells you a lot.")),
        ("stmt", "What is it", ("What is it", "for you?")),
    ]},
    # WED 11
    "11-0700": {"kicker": "IDENTITY", "cta": False, "beats": [
        ("hook", None, ("Single sign-on,", "single failure."), ("ui", ["Sign in", "Continue with SSO", "Or use password"], [2])),
        ("list", "Common mistakes", "Common mistakes", [("local password", "Local password still allowed"), ("identity provider signed", "Signer not checked"), ("by email address", "Users matched by email"), ("And sessions", "App sessions outlive SSO")]),
        ("list", "Enforce single", "Do this", [("Enforce single", "Enforce SSO everywhere"), ("validate every", "Validate every response"), ("stable", "Link by a stable ID")]),
    ]},
    "11-0900": {"kicker": "IDENTITY", "cta": True, "wordfix": {"lever": "leaver", "Levers": "Leavers"}, "beats": [
        ("hook", None, ("They left.", "Access didn't."), ("ui", ["Leaver: J. Okafor", "Left: 3 months ago", "Last login: yesterday"], [2])),
        ("stmt", "is the identity", ("Joiner. Mover. Leaver.", "Every stage leaks.")),
        ("list", "Joiners get copied", "Where it leaks", [("Joiners", "Joiners copy a colleague's access"), ("Movers", "Movers keep old access"), ("keep accounts", "Leavers keep side accounts")]),
        ("list", "Drive access from", "The fix", [("Drive access", "Drive access from HR"), ("Disable everything", "Disable all on the last day"), ("every quarter", "Review every quarter")]),
    ]},
    "11-1300": {"kicker": "IDENTITY", "cta": False, "beats": [
        ("hook", None, ("The login that", "skips MFA."), ("ui", ["Sign-in log", "IMAP  ·  basic auth", "MFA: not required"], [1, 2])),
        ("stmt", "Older protocols like", ("Old protocols can't", "ask for MFA.")),
        ("stmt", "an attacker with", ("Stolen password", "walks past MFA.")),
        ("list", "Block legacy authentication", "The fix", [("Block legacy", "Block legacy auth"), ("Check your", "Check sign-in logs first"), ("Then require", "Require MFA for every app")]),
    ]},
    "11-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("AppSec", "from zero."), ("ui", ["Security programme", "Tools: 0", "Apps known: ?"], [2])),
        ("stmt", "Start with knowing", ("Not tools first.", "Know what you have.")),
        ("list", "First list your", "In order", [("First list", "List apps and owners"), ("Second fix", "Fix the basics"), ("Third add", "Pipeline checks devs trust"), ("Fourth train", "Train on real bugs")]),
        ("stmt", "Then measure", ("Fewer repeat bugs", "means it works.")),
    ]},
    "11-1700": {"kicker": "IDENTITY", "cta": False, "wordfix": {"to,": "two,"}, "beats": [
        ("hook", None, ("The emergency", "account."), ("ui", ["SSO status", "Identity provider: DOWN", "Admins: locked out"], [1, 2])),
        ("stmt", "With a", ("A break-glass account.", "For that moment.")),
        ("list", "Do it safely", "Do it safely", [("Do it safely", "Two, cloud-only"), ("strong", "Phishing-resistant keys"), ("Alert every time", "Alert on every use"), ("test them", "Test every few months")]),
    ]},
    "11-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Same day or", "same month?"), ("ui", ["Leaver access removed", "Same day", "Same week", "Same month"], [1, 2, 3])),
        ("stmt", "Be honest", ("Be", "honest.")),
        ("stmt", "What happens in", ("What happens", "in your team?")),
    ]},
    # THU 12
    "12-0700": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("From reader", "to admin."), ("code", ["role: ReadOnly", "  -> assume: DeployRole", "  -> pass role to new function", "  -> function runs as Admin"], [3])),
        ("stmt", "That is privilege", ("Privilege escalation", "by role chaining.")),
        ("stmt", "No single permission", ("No single step", "looks dangerous.")),
        ("list", "Map who can", "The fix", [("Map who", "Map who can assume what"), ("pass roles", "Map who can pass roles"), ("Remove the paths", "Remove unneeded paths"), ("alert on", "Alert on unusual assumptions")]),
    ]},
    "12-0900": {"kicker": "ZERO TRUST", "cta": True, "beats": [
        ("hook", None, ("Inside isn't", "trusted."), ("ui", ["Request", "From: office network", "Trusted? Not by default"], [2])),
        ("stmt", "In the old", ("The old model:", "a castle with walls.")),
        ("stmt", "Today staff work", ("Staff anywhere. Apps in the cloud.", "No walls.")),
        ("list", "Zero trust checks", "Every request", [("Who is this", "Who is this?"), ("device healthy", "Is the device healthy?"), ("reach this", "Should they reach this, now?")]),
        ("stmt", "Start with identity", ("Start with identity.", "Then devices, then segments.")),
    ]},
    "12-1300": {"kicker": "LOGGING", "cta": False, "beats": [
        ("hook", None, ("Turn these logs", "on today."), ("ui", ["Incident", "\"Who changed this?\"", "Logs: disabled"], [2])),
        ("list", "Turn these on", "Turn on", [("First your cloud", "Control-plane logs, every region"), ("Second", "Identity sign-in logs"), ("Third network", "Network flow logs"), ("Fourth access", "Storage access logs")]),
        ("stmt", "Send them to", ("A separate account.", "Kept for months.")),
    ]},
    "12-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("A real security", "incident."), ("ui", ["Alert  ·  02:14", "Login from new country", "Severity: unknown"], [1])),
        ("stmt", "Rarely a movie", ("Rarely a movie hacker.", "Usually an alert.")),
        ("list", "A login from", "What it looks like", [("A login from", "A login from somewhere new"), ("A spike", "A spike in failed passwords"), ("A key used", "A key used from a new place")]),
        ("stmt", "The job is", ("Real or noise?", "Then contain.")),
        ("stmt", "Good runbooks and", ("Runbooks and calm", "beat fast typing.")),
    ]},
    "12-1700": {"kicker": "SECRETS", "cta": False, "beats": [
        ("hook", None, ("Env vars aren't", "a vault."), ("code", ["Error 500  ·  debug page", "DATABASE_URL=postgres://admin:", "STRIPE_KEY=sk_live_..."], [1, 2])),
        ("stmt", "They show up", ("Crash reports. Debug pages.", "Logs.")),
        ("list", "A secrets manager", "A secrets manager", [("stores secrets", "Encrypted storage"), ("controls who", "Access per secret"), ("logs every", "Every read logged"), ("rotation simple", "Easy rotation")]),
        ("stmt", "secrets from the", ("Load at runtime.", "Rotate on a schedule.")),
    ]},
    "12-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Where do", "secrets live?"), ("ui", ["Production secrets", "Secrets manager", "Env vars", "A shared doc"], [1, 2, 3])),
        ("stmt", "Where are yours", ("Where are", "yours?")),
    ]},
    # FRI 13
    "13-0700": {"kicker": "CLOUD SECURITY", "cta": False, "wordfix": {"Everyone": "Every one", "everyone": "every one"}, "beats": [
        ("hook", None, ("Unlucky? Or", "misconfigured?"), ("ui", ["Friday 13", "Bucket: public", "MFA on admin: off"], [1, 2])),
        ("list", "A storage bucket", "Not bad luck", [("A storage bucket", "Public storage"), ("A database", "Database open to all"), ("An access key", "Key in a public repo"), ("Logging switched", "Logging switched off"), ("An admin account", "Admin without MFA")]),
        ("stmt", "configuration choice", ("configuration choice", "a choice.")),
        ("stmt", "Bad luck is", ("Bad luck, you can't prevent.", "These, you can.")),
    ]},
    "13-0900": {"kicker": "DEVSECOPS", "cta": True, "beats": [
        ("hook", None, ("Catch it", "in the PR."), ("code", ['resource "aws_db_instance" {', "  publicly_accessible = true", "}", "! scan: public database"], [1, 3])),
        ("stmt", "Infrastructure as code", ("Scan the code", "before it deploys.")),
        ("list", "Public storage open", "It flags", [("Public storage", "Public storage"), ("open ports", "Open ports"), ("missing encryption", "Missing encryption"), ("wide permissions", "Wide permissions")]),
        ("stmt", "Start with a", ("Block only serious issues", "at first.")),
    ]},
    "13-1300": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("The link that", "never expires."), ("code", ["https://files.example.com/", "  contract.pdf?signature=...", "  &expires=31536000  (1 year)"], [2])),
        ("stmt", "Signed links are", ("Signed links: good.", "No public storage.")),
        ("stmt", "But a", ("A long-lived link", "works for anyone.")),
        ("list", "Keep expiry short", "Do this", [("Keep expiry", "Minutes, not months"), ("Generate links", "Check access first"), ("never sign", "Never sign with a powerful key")]),
    ]},
    "13-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("The cloud", "interview."), ("ui", ["Interview", "\"A key leaked an hour ago.\"", "\"What do you do first?\""], [1, 2])),
        ("list", "First fundamentals", "What it tests", [("First fundamentals", "Fundamentals"), ("Second scenarios", "Scenarios"), ("Third communication", "Communication")]),
        ("stmt", "talking through", ("Practise scenarios", "out loud.")),
        ("stmt", "Certifications get you", ("Certs get you in the room.", "Reasoning gets the offer.")),
    ]},
    "13-1700": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("The bill spotted", "the attack."), ("ui", ["Billing alert", "Compute: +4,800% today", "Region: never used before"], [1, 2])),
        ("stmt", "Stolen cloud credentials", ("Stolen keys", "mine crypto.")),
        ("stmt", "The data was", ("The data was safe.", "The invoice wasn't.")),
        ("list", "Set budget alerts", "Do this", [("budget alerts", "Budget + anomaly alerts"), ("Restrict which", "Restrict regions and sizes"), ("treat a sudden", "Spend spike = security alert")]),
    ]},
    "13-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Biggest cloud", "surprise?"), ("ui", ["Your biggest surprise", "A bill", "An exposed resource", "A forgotten service"], [1, 2, 3])),
        ("stmt", "Share it so", ("Share it,", "so others don't repeat it.")),
    ]},
    # SAT 14
    "14-0700": {"kicker": "DNS", "cta": False, "beats": [
        ("hook", None, ("The subdomain", "they claimed."), ("code", ["promo.example.com", "  CNAME -> old-promo.cloudapp.net", "  (resource deleted)"], [1, 2])),
        ("stmt", "That is a", ("A subdomain", "takeover.")),
        ("stmt", "Your DNS still", ("DNS points to", "something you deleted.")),
        ("stmt", "An attacker creates", ("Same name.", "Their page. Your domain.")),
        ("list", "When you delete", "The fix", [("When you delete", "Delete DNS first"), ("Review DNS", "Review records regularly")]),
    ]},
    "14-0900": {"kicker": "EMAIL SECURITY", "cta": True, "beats": [
        ("hook", None, ("Anyone can send", "as you."), ("ui", ["Inbox", "From: ceo@yourcompany.com", "\"Urgent wire transfer\""], [1, 2])),
        ("stmt", "records do the", ("Three records", "do the work.")),
        ("list", "SPF lists the", "The three", [("SPF lists", "SPF: who may send"), ("DKIM signs", "DKIM: signed messages"), ("DMARC tells", "DMARC: what to do on fail")]),
        ("list", "Start DMARC at", "Roll it out", [("Start DMARC", "Monitor"), ("fix your", "Fix legit senders"), ("quarantine", "Quarantine"), ("reject", "Reject")]),
    ]},
    "14-1300": {"kicker": "OPERATIONS", "cta": False, "beats": [
        ("hook", None, ("Expired", "at midnight."), ("ui", ["Your connection is not private", "NET::ERR_CERT_DATE_INVALID", "Expired: today, 00:00"], [1, 2])),
        ("stmt", "Certificate lifetimes are", ("Certificates are", "getting shorter.")),
        ("ui", "Since March this", ["Max certificate lifetime", "Mar 2026: 200 days", "Mar 2027: 100 days", "Mar 2029: 47 days"], [1, 3]),
        ("list", "Automate renewal for", "Do this", [("Automate renewal", "Automate every renewal"), ("Monitor expiry", "Alert weeks ahead"), ("keep a list", "List every certificate")]),
    ]},
    "14-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Build", "this lab."), ("ui", ["Cloud lab", "Budget alert: $10", "App + storage + database"], [1, 2])),
        ("stmt", "Set a spending", ("Budget alert", "first.")),
        ("stmt", "Then misconfigure it", ("Then break it", "on purpose.")),
        ("list", "Use free tools", "Then", [("Use free tools", "Scan with free tools"), ("Fix each", "Fix each issue"), ("write up", "Write it up"), ("delete everything", "Delete everything")]),
    ]},
    "14-1700": {"kicker": "CLOUD SECURITY", "cta": False, "beats": [
        ("hook", None, ("The admin page", "was public."), ("ui", ["admin.example.com", "Database dashboard", "Login  ·  open to the internet"], [2])),
        ("stmt", "Exposed admin consoles", ("First thing", "attackers scan for.")),
        ("stmt", "Even with a", ("A password invites", "guessing.")),
        ("list", "Keep admin interfaces", "The fix", [("Keep admin", "Off the public internet"), ("behind a", "Behind a VPN or proxy"), ("Require MFA", "Require MFA"), ("scan your", "Scan your own ranges")]),
    ]},
    "14-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("p=none, quarantine", "or reject?"), ("code", ["_dmarc.yourdomain.com", '"v=DMARC1; p=?"'], [1])),
        ("stmt", "None only monitors", ("None monitors.", "Reject stops spoofing.")),
        ("stmt", "Check your domain", ("Check today.", "Where are you?")),
    ]},
    # SUN 15
    "15-0700": {"kicker": "RANSOMWARE", "cta": False, "beats": [
        ("hook", None, ("The attacker deleted", "backups."), ("ui", ["Backup vault", "Recovery points: 0", "Deleted by: admin, 02:51"], [1, 2])),
        ("stmt", "Many ransomware groups", ("Backups go first.", "That's the point.")),
        ("list", "Keep backups in", "Protect them", [("separate account", "A separate account"), ("immutable", "Immutable until a set date"), ("Restrict who", "Restrict policy changes"), ("alert on any", "Alert on deletion attempts")]),
    ]},
    "15-0900": {"kicker": "CLOUD SECURITY", "cta": True, "beats": [
        ("hook", None, ("Small accounts,", "small blast."), ("ui", ["Organization", "prod  ·  dev  ·  logs  ·  security", "Guardrails: on"], [1, 2])),
        ("stmt", "Separate accounts create", ("One account:", "one mistake, everything.")),
        ("list", "Production development logging", "Separate accounts", [("Production", "Production"), ("development", "Development"), ("logging", "Logging"), ("security", "Security")]),
        ("stmt", "organization features", ("Guardrails across", "every account.")),
    ]},
    "15-1300": {"kicker": "IDENTITY", "cta": False, "beats": [
        ("hook", None, ("No owner.", "Full access."), ("ui", ["svc-integration", "Role: Owner", "Created by: (left 2024)"], [1, 2])),
        ("stmt", "Nobody knows what", ("Nobody knows what uses it.", "Nobody dares turn it off.")),
        ("list", "Give every service", "The fix", [("Give every", "An owner and a purpose"), ("Scope its", "Scoped permissions"), ("credentials where", "Short-lived credentials"), ("disable it", "Unclaimed? Disable and watch")]),
    ]},
    "15-1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Teach one", "person."), ("ui", ["Mentoring", "Pair on a code review", "Walk through a finding"], [1, 2])),
        ("stmt", "Mentoring juniors makes", ("Teaching shows you", "your own gaps.")),
        ("list", "Start small", "Start small", [("Pair on", "Pair on a review"), ("Walk them", "Walk through a finding"), ("Share the", "Share resources"), ("Let them present", "Let them present")]),
        ("stmt", "One person you", ("Help one today.", "They help others tomorrow.")),
    ]},
    "15-1700": {"kicker": "IDENTITY", "cta": False, "beats": [
        ("hook", None, ("Start with", "admins."), ("ui", ["Sign in", "Use a passkey", "Password: disabled"], [1, 2])),
        ("stmt", "Start small with", ("Start with the accounts", "that matter most.")),
        ("list", "Your administrators", "In order", [("Your administrators", "Admins first"), ("sensitive data", "Then sensitive-data access"), ("rest of the", "Then everyone")]),
        ("stmt", "Each step removes", ("Fewer passwords", "to phish.")),
    ]},
    "15-1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("One week.", "What first?"), ("ui", ["One week to fix", "One thing", "Why?"], [1])),
        ("stmt", "Not a wish", ("Not a wish list.", "One thing.")),
        ("stmt", "What would it", ("What would it be,", "and why?")),
    ]},
}
