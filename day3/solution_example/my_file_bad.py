# Debugging exercise: outbreak report

reports = [
    {"location": "North", "cases": 120, "population": 500000},
    {"location": "South", "cases": 85, "population": 250000},
    {"location": "East", "cases": 0, "population": 0},
    {"location": "West", "cases": "200", "population": 800000},
]


def calculate_incidence(cases, population):
    incidence = cases / population * 100000
    return incidence


def classify_risk(incidence):
    if incidence > 50:
        return "high"
    else:
        return "low"

if __name__ == "__main__":
    for report in reports:
        incidence = calculate_incidence(report["cases"], report["population"])
        risk = classify_risk(incidence)

        print(report["location"] + ": " + risk + " risk")