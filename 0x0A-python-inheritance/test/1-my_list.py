#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Represents MyList."""

    def print_sorted(self):
        """  Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
