regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  message("Calculating incidence")

  if (cases < 0) {
    stop("Cases cannot be negative")
  }

  if (population < 0) {
    stop("Population cannot be negative")
  }

  if (population == 0) {
    warning("Population is zero. Incidence rate cannot be calculated.")
    return(NA)
  }

  if (cases == 0) {
    message("No cases reported in region")
  }

  rate <- cases / population * 100000

  message("Incidence rate for is ", round(rate, 2))

  return(rate)
}

classify_risk <- function(rate) {
  risk_level <- ifelse(rate > 50, "high", "low")

  return(risk_level)
}

regions$incidence_rate <- mapply(calculate_incidence, regions$cases, regions$population)
regions$risk <- classify_risk(regions$incidence_rate)

print(regions)
