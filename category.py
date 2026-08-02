def get_category(title):

    title = title.lower()


    if any(word in title for word in [
        "sign",
        "signed",
        "transfer",
        "join",
        "deal",
        "contract"
    ]):
        return "🔄 Transfer News"


    if any(word in title for word in [
        "goal",
        "brace",
        "beat",
        "defeat",
        "match",
        "win",
        "draw",
        "score"
    ]):
        return "⚽ Match Report"


    if any(word in title for word in [
        "fifa",
        "world cup",
        "uefa",
        "champions league"
    ]):
        return "🌍 FIFA / UEFA"


    if any(word in title for word in [
        "injury",
        "injured",
        "suspended",
        "suspension"
    ]):
        return "🏥 Injury / Suspension"


    if any(word in title for word in [
        "tactic",
        "formation",
        "coach",
        "manager",
        "strategy"
    ]):
        return "🧠 Tactical Analysis"


    if any(word in title for word in [
        "performance",
        "season",
        "record",
        "stats"
    ]):
        return "📊 Player Performance"


    return "⚽ Football News"
