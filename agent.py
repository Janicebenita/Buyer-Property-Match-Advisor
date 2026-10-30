"""Transparent buyer-to-listing comparison worker."""
from __future__ import annotations


def match_property(criteria: dict, listing: dict) -> dict:
    checks = []
    budget = criteria.get("max_price")
    price = listing.get("price")
    checks.append({"criterion": "budget", "matched": budget is not None and price is not None and price <= budget, "evidence": {"max_price": budget, "price": price}})
    min_bedrooms = criteria.get("min_bedrooms")
    bedrooms = listing.get("bedrooms")
    checks.append({"criterion": "bedrooms", "matched": min_bedrooms is not None and bedrooms is not None and bedrooms >= min_bedrooms, "evidence": {"minimum": min_bedrooms, "listing": bedrooms}})
    preferred = {str(x).lower() for x in criteria.get("preferred_locations", [])}
    location = str(listing.get("location", "")).lower()
    checks.append({"criterion": "location", "matched": bool(preferred and location in preferred), "evidence": {"preferred": sorted(preferred), "listing": location or None}})
    required = {str(x).lower() for x in criteria.get("must_haves", [])}
    features = {str(x).lower() for x in listing.get("features", [])}
    checks.append({"criterion": "must_haves", "matched": required.issubset(features), "evidence": {"required": sorted(required), "missing": sorted(required - features)}})
    known = [check for check in checks if all(value is not None for value in check["evidence"].values())]
    score = round(100 * sum(check["matched"] for check in checks) / len(checks))
    return {"listing_id": listing.get("id"), "match_score": score, "checks": checks, "trade_offs": [c["criterion"] for c in checks if not c["matched"]], "evidence_coverage": round(len(known) / len(checks), 2), "human_review_required": True}
