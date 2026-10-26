# Wed 28 Oct beats for build_v2.py (Week A, Money moves)
SPECS = {
    "0700": {"kicker": "SECURE CODING", "cta": False, "beats": [
        ("hook", None, ("One voucher.", "Ten redemptions."), ("ui", ["Voucher SAVE50", "Single use", "Redeemed 10 times"], [2])),
        ("stmt", "And the fix", ("The fix isn't more checks.", "It's where they live.")),
        ("code", "Your code reads", ["v = get_voucher(code)", "if not v.used:", "    apply_discount()", "    v.used = True"], [1, 3]),
        ("list", "Fire 10 requests", "Ten requests at once", [("all 10 read", "All ten read: unused"), ("before any write", "Then the writes land")]),
        ("code", "The fix make", ["UPDATE vouchers SET used = true", "WHERE code = 'SAVE50'", "  AND used = false", "-- 0 rows? already used"], [2, 3]),
        ("stmt", "Then test it", ("Test with", "parallel requests.")),
    ]},
    "0900": {"kicker": "PAYMENTS COMPLIANCE", "cta": True, "beats": [
        ("hook", None, ("Shrink PCI to", "almost nothing."), ("ui", ["Checkout", "Card number  4242 •••• •••• ••••", "Hosted by your payment provider"], [2])),
        ("stmt", "Scope is every", ("Scope: every system", "that touches card data.")),
        ("stmt", "Let card numbers", ("Cards on your servers?", "Everything is in scope.")),
        ("list", "Use your payment", "Hosted fields or tokens", [("Your scope shrinks", "Smaller scope"), ("your audit gets", "Smaller audit"), ("a breach has", "Less to steal")]),
        ("stmt", "Design for scope", ("Design for scope first.", "Compliance gets cheaper.")),
    ]},
    "1300": {"kicker": "PAYMENTS", "cta": False, "beats": [
        ("hook", None, ("The refund", "nobody tests."), ("ui", ["Order #A-2291", "Paid  EUR 120.00", "Refunded  EUR 360.00"], [2])),
        ("list", "Three things to", "Check today", [("be bigger than", "Refund bigger than payment?"), ("same order be", "Same order refunded twice?"), ("refund an order", "Someone else's order?")]),
        ("stmt", "Each one is", ("Each one is", "money leaving.")),
        ("list", "Give refunds the", "Same checks as payments", [("ownership", "Ownership"), ("limits", "Limits"), ("one refund per", "One refund per order line")]),
    ]},
    "1500": {"kicker": "CAREER", "cta": True, "beats": [
        ("hook", None, ("Say no without", "blocking."), ("ui", ["Product team", "Can we launch Friday?", "Security: ..."], [1])),
        ("list", "First name the", "How to say not yet", [("First name", "Name the risk in business terms"), ("Second offer", "Offer the smallest fix"), ("Third give", "Give a date"), ("Fourth if", "Accepted? Write it down, with an owner")]),
        ("stmt", "You keep the", ("The team ships.", "The risk is a decision.")),
    ]},
    "1700": {"kicker": "PAYMENTS", "cta": False, "beats": [
        ("hook", None, ("Free money in", "the decimals."), ("code", ["transfer(0.004)  -> 0.01", "transfer(0.004)  -> 0.01", "transfer(0.004)  -> 0.01", "x 10,000"], [3])),
        ("stmt", "Currency conversion makes", ("Round trip through", "two currencies? More.")),
        ("list", "The fixes are", "The boring fixes", [("Store money as", "Integers in minor units"), ("Round once", "Round once, one rule"), ("reconcile totals", "Reconcile totals")]),
        ("stmt", "so a slow", ("Catch the slow leak", "before it adds up.")),
    ]},
    "1900": {"kicker": "QUESTION", "cta": False, "tail": 1.6, "beats": [
        ("hook", None, ("Which flow", "do you never test?"), ("ui", ["Payment flows", "Checkout  tested", "Refunds, payouts, promo codes  ?"], [2])),
        ("stmt", "Checkout gets all", ("Checkout gets", "all the attention.")),
        ("stmt", "Pick the one", ("Pick one.", "Test it this week.")),
        ("stmt", "Which one is", ("Which one", "is yours?")),
    ]},
}
