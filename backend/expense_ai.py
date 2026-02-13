def categorize_expense(desc):
    desc = desc.lower()
    if "rent" in desc:
        return "Rent"
    if "ad" in desc or "marketing" in desc:
        return "Marketing"
    if "software" in desc or "subscription" in desc:
        return "Tools"
    if "salary" in desc:
        return "Payroll"
    return "Other"
