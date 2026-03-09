"""
Tests for the Project Starter Template.
"""

import sys
import os

# Add src to path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

def test_imports() -> None:
    """
    Test that the main module can be imported.
    """
    from aigravscode import main
    assert main.main is not None

def test_main_function() -> None:
    """
    Smoke test for the main function.
    """
    from aigravscode import main
    # Just ensure it's callable
    assert callable(main.main)
