"""
Module: conftest.py
This module contains test cases for testing the JsonHandler class methods.
"""
def pytest_runtest_protocol(item):
    '''Custom implementation of pytest_runtest_protocol hook to print test requirements.'''
    if hasattr(item, 'function') and hasattr(item.function, 'requirement'):
        print(f"Running test {item.nodeid} with requirement {item.function.requirement}")
     # continue with the default test protocol

def pytest_runtest_makereport(item, call):
    ''' Custom implementation of pytest_runtest_makereport hook to update traceability matrix.'''
    if call.when == 'call':
        result = 'NOT RUN'
        if call.excinfo is not None:
            if call.excinfo.typename == 'pytest.skip':
                result = 'SKIP'
            elif call.excinfo.typename == 'pytest.xfail':
                result = 'XFAIL'
            else:
                result = 'FAIL'
        else:
            result = 'PASS'
        item.config.traceability_matrix[item.nodeid] = (item.function.requirement, result)

def pytest_sessionstart(session):
    '''Custom implementation of pytest_sessionstart hook to initialize traceability matrix.'''
    session.config.traceability_matrix = {}

def pytest_sessionfinish(session):
    '''Custom implementation of pytest_sessionfinish hook to print traceability matrix.'''
    print("Traceability Matrix:")
    for test, (requirement, result) in session.config.traceability_matrix.items():
        print(f"{test}: {requirement}, {result}")
