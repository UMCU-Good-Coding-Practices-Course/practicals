import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


reports = [
    {"location": "North", "cases": 120, "population": 500000},
    {"location": "South", "cases": 85, "population": 250000},
    {"location": "East", "cases": 0, "population": 0},
    {"location": "West", "cases": 200, "population": 800000},
]


def calculate_incidence(cases, population, location):
    """Compute incidence per 100k people"""
    logging.info("Calculating incidence for location: %s", location)

    if cases < 0:
        logging.error("Cases cannot be negative in location: %s", location)
        raise ValueError("Cases cannot be negative")

    if population < 0:
        logging.error("Population cannot be negative in location: %s", location)
        raise ValueError("Population cannot be negative")

    if population == 0:
        logging.warning(
            "Population is zero in location: %s. Incidence cannot be calculated.",
            location
        )
        return None

    if cases == 0:
        logging.info("No cases reported in location: %s", location)

    incidence = cases / population * 100000

    logging.info("Incidence for %s is %.2f", location, incidence)

    return incidence


def classify_risk(incidence, location):
    logging.info("Classifying risk for location: %s", location)

    if incidence is None:
        logging.warning("Risk level is unknown for location: %s", location)
        return "unknown"

    if incidence > 50:
        logging.info("Risk level for %s is high", location)
        return "high"
    else:
        logging.info("Risk level for %s is low", location)
        return "low"

if __name__ == "__main__":
    for report in reports:
        incidence = calculate_incidence(
            report["cases"],
            report["population"],
            report["location"]
        )

        risk = classify_risk(incidence, report["location"])

        print(report["location"] + ": " + risk + " risk")