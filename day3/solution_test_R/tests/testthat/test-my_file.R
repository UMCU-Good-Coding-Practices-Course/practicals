source("my_file.R")

test_that("calculate_incidence works", {
  expect_equal(calculate_incidence(5, 1e6), 0.5)
  expect_equal(calculate_incidence(0, 1), 0)
  expect_true(is.na(calculate_incidence(0, 0)))
})

# test_that("classify_risk works", {
#   expect_equal(classify_risk(NA_real_), "unknown")
#   expect_equal(classify_risk(5), "low")
#   expect_equal(classify_risk(50), "low")
#   expect_equal(classify_risk(100), "high")
# })