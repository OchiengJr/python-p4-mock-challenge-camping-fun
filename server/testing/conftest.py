#!/usr/bin/env python3

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par and par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node and node.__doc__ else node.__name__

    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

    # Add logging or debugging statements if needed
    # print(f"Collected item: {item._nodeid}")

    # Consider adding error handling for unexpected cases

    # Optionally, return a value indicating success/failure or None
    return True  # or None or any relevant status

# Add any additional functionality or handling as per your requirements
