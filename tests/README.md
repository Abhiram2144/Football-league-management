# Football League Management System - Test Suite

## Overview
Simplified test suite with 3-4 focused test cases per testing technique for each member.

## Test Structure

```
tests/
├── member_a_neel/          # Member A (Neel) - League Manager Tests
│   ├── test/blackbox/
│   │   ├── boundary_values/test_league_manager_boundary.py (4 tests)
│   │   ├── category_partition/test_league_manager_category.py (4 tests)
│   │   └── random_testing/test_league_manager_random.py (3 tests)
│   ├── test/whitebox/
│   │   ├── basis_path/test_league_manager_basis.py (4 tests)
│   │   └── branch_coverage/test_league_manager_branch.py (3 tests)
│   └── test/symbolic/
│       ├── symbolic_execution/test_league_manager_symbolic.py (4 tests)
│       └── concolic_testing/test_league_manager_concolic.py (3 tests)
│
├── member_b_mahir/         # Member B (Mahir) - Fixture Scheduler Tests
│   ├── test/blackbox/boundary_values/test_fixture_scheduler_boundary.py (4 tests)
│   ├── test/whitebox/basis_path/test_fixture_scheduler_basis.py (3 tests)
│   └── test/symbolic/symbolic_execution/test_fixture_scheduler_symbolic.py (3 tests)
│
├── member_c_abhishek/      # Member C (Abhishek) - Results Manager Tests
│   ├── test/blackbox/boundary_values/test_results_manager_boundary.py (4 tests)
│   ├── test/whitebox/basis_path/test_results_manager_basis.py (3 tests)
│   └── test/symbolic/symbolic_execution/test_results_manager_symbolic.py (3 tests)
│
└── member_d_dhawal/        # Member D (Dhawal) - Diagnostics Engine Tests
    ├── test/blackbox/boundary_values/test_diagnostics_engine_boundary.py (4 tests)
    ├── test/whitebox/basis_path/test_diagnostics_engine_basis.py (3 tests)
    └── test/symbolic/symbolic_execution/test_diagnostics_engine_symbolic.py (3 tests)
```

## Running Tests

### Install Dependencies
```bash
pip install pytest pytest-cov
```

### Run All Tests
```bash
python run_tests.py all
```

### Run Tests for Specific Member
```bash
python run_tests.py a_neel
python run_tests.py b_mahir
python run_tests.py c_abhishek
python run_tests.py d_dhawal
```

### Run with Coverage
```bash
python run_tests.py coverage
python run_tests.py coverage a_neel
```

### Run Using pytest Directly
```bash
# All tests
pytest tests/ -v

# Specific member
pytest tests/member_a_neel/ -v

# Specific technique
pytest tests/member_a_neel/test/blackbox/ -v
pytest tests/member_a_neel/test/whitebox/ -v
pytest tests/member_a_neel/test/symbolic/ -v

# With coverage
pytest tests/ -v --cov --cov-report=html
```

## Test Statistics

- **Total Test Files**: 16
- **Member A (Neel)**: 7 test files (25 test cases)
- **Member B (Mahir)**: 3 test files (10 test cases)
- **Member C (Abhishek)**: 3 test files (10 test cases)
- **Member D (Dhawal)**: 3 test files (10 test cases)
- **Total Test Cases**: ~55

## Testing Techniques Covered

### Black-Box Testing
- **Boundary Value Analysis**: Tests edge cases and boundaries
- **Category Partition**: Tests different input categories
- **Random Testing**: Tests with random inputs

### White-Box Testing
- **Basis Path Testing**: Tests independent execution paths
- **Branch Coverage**: Tests all TRUE/FALSE branches

### Symbolic Testing
- **Symbolic Execution**: Path conditions and execution trees
- **Concolic Testing**: Concrete + symbolic exploration

## Quick Examples

### Run and see results
```bash
# Quick test run
python run_tests.py all

# Detailed output
pytest tests/ -v -s

# Stop on first failure
pytest tests/ -x

# Run specific test
pytest tests/member_a_neel/test/blackbox/boundary_values/test_league_manager_boundary.py::TestLeagueManagerBoundary::test_create_league_minimum_boundary -v
```

## Notes

- Each test file contains 3-4 focused test cases
- Tests include symbolic execution trees and path conditions as documentation
- All tests follow the naming convention: `student_id.test.technique_category.technique_name.py`
- Tests are designed to be quick and maintainable
