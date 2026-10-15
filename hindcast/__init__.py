"""Point-in-time hindcast of the live decision engine.

fetch.py downloads prices once (network); everything else runs offline from
the committed cache in data/prices/. Tax and transaction costs are excluded
by design, so every return reported here is an upper bound.
"""
