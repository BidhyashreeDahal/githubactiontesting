"""
Module: conftest.py
This module contains custom hooks for pytest to handle traceability matrix.
"""

def pytest_configure(config):
    '''Initialize traceability matrix at the start of the test session.'''
    config.traceability_matrix = {}

def pytest_runtest_protocol(item, nextitem):
    '''Custom implementation of pytest_runtest_protocol hook to print test requirements.'''
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")
    # continue with the default test protocol
    return None

def pytest_runtest_makereport(item, call):
    '''Custom implementation of pytest_runtest_makereport hook to update traceability matrix.'''
    if call.when == 'call':
        result = 'NOT RUN'
        if call.excinfo is not None:
            if call.excinfo.typename == 'Skipped':
                result = 'SKIP'
            elif call.excinfo.typename == 'XFailed':
                result = 'XFAIL'
            else:
                result = 'FAIL'
        else:
            result = 'PASS'
        if not hasattr(item.config, 'traceability_matrix'):
            item.config.traceability_matrix = {}
        item.config.traceability_matrix[item.nodeid] = (getattr(item.function, 'requirement', None), result)

def pytest_sessionfinish(session, exitstatus):
    '''Custom implementation of pytest_sessionfinish hook to print traceability matrix.'''
    print("Traceability Matrix:")
    if hasattr(session.config, 'traceability_matrix'):
        for test, (requirement, result) in session.config.traceability_matrix.items():
            print(f"{test}: {requirement}, {result}")