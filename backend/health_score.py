def health_score(revenue, expenses, reserve):
    score = 50
    if revenue > expenses:
        score += 20
    if reserve > expenses:
        score += 20
    if revenue > expenses * 1.5:
        score += 10
    return min(score, 100)
