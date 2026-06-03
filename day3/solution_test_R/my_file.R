regions <- data.frame(
  region = c("North", "South", "East", "West"),
  cases = c(120, 85, 0, 200),
  population = c(500000, 250000, 0, 800000)
)

calculate_incidence <- function(cases, population) {
  if (population == 0) {
    return(NA)
  }

  rate <- cases / population * 100000
  return(rate)
}

regions$incidence_rate <- mapply(
  calculate_incidence,
  regions$cases,
  regions$population
)

regions$risk_level <- ifelse(
  regions$incidence_rate > 50,
  "high",
  "low"
)