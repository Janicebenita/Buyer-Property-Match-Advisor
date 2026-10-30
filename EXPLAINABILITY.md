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

This repository is a declarative OpenGAP worker package: `agent.yaml` defines its interface and constraints, `SOUL.md` defines its operating principles, and this document explains its matching rationale and review boundaries. `README.md` provides the supported use case and reviewer-facing setup information.

No live listing feed, valuation model, transaction API, or autonomous purchase action is implemented. A conforming host must supply the buyer requirements and listing evidence, expose the comparison to the user, and require human verification before any consequential step.
