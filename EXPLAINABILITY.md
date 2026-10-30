# Buyer Property Match Advisor Explainability

## Decision and Reasoning Process

The agent's decision support compares each listing with the buyer's stated budget, property type, size, location preferences, and desired amenities. Its reasoning shows matched criteria, compromises, and missing information for every recommendation.

## Inputs and Data Sources Used

Input data includes buyer-provided preferences and authorized property listing data. Protected characteristics, demographic steering signals, and undisclosed personal data are excluded from the data sources.

## Outputs and Supporting Evidence

The output is a comparison of suitable listings with evidence and trade-offs. Each match refers to the buyer's expressed criteria and the corresponding listing fields.

## Limits, Constraints, and Known Issues

A limitation is that listings can be stale, incomplete, or inaccurate. The agent is constrained from verifying legal status, financing eligibility, future value, or physical condition.

## Uncertainty and Human Review

Uncertainty is shown for unverified or missing property facts. The buyer and an authorized professional should confirm all important information before proceeding.

## Implementation in This Repository

`agent.py` implements `match_property(criteria, listing)`. It compares price with the buyer's maximum, bedrooms with the declared minimum, listing location with preferred locations, and features with must-haves; it retains the compared values as evidence, calculates a four-check score, lists unmet trade-offs, reports evidence coverage, and requires human review. `test_agent.py` verifies that an over-budget trade-off remains visible.

No live listing feed, valuation model, transaction API, or autonomous purchase action is implemented. The caller supplies both records and a human verifies all consequential steps.
