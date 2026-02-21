# tests/test_week1.py
#
# PERSON C — WEEK 1 DELIVERABLE
# ==============================
# These are the two dummy tests that prove the CI pipeline is working.
#
# "Dummy" means they don't test real science yet — they just check that:
#   1. The package can be imported at all (basic sanity check)
#   2. pytest itself is installed and running correctly
#
# When you run `pytest tests/test_week1.py -v` locally, both should show PASSED.
# When you push to GitHub, the Actions tab should also show them as green.
#
# You do NOT need to change anything in this file for Week 1.
# In Week 2 we'll start replacing these with tests for real functions.

import pytest


def test_package_is_importable():
    """
    Check that the metrec package can be imported without crashing.

    This will fail if:
    - The package wasn't installed (did you run `pip install -e ".[dev]"`?)
    - There's a syntax error somewhere in the package
    - A required dependency is missing

    If this fails on GitHub Actions but passes locally, check that
    requirements.txt includes everything needed.
    """
    # If this line doesn't raise an exception, the test passes.
    # It's the most basic possible check — "does the package exist?"
    import metrec

    # Also check the version string is there (defined in src/metrec/__init__.py)
    assert hasattr(metrec, "__version__"), (
        "metrec.__version__ is missing — check src/metrec/__init__.py"
    )


def test_placeholder_always_passes():
    """
    A trivially true test that exists purely to show pytest is working.

    Once real functions are implemented (Week 2+), this file will grow
    with meaningful tests. For now, this is our "hello world" for pytest.

    Think of it like a smoke detector test — we're just confirming the
    alarm system is installed and switched on.
    """
    # 1 + 1 == 2 will always be True.
    # If pytest is installed and running, this will always pass.
    assert 1 + 1 == 2, "Mathematics has broken down. Panic."
