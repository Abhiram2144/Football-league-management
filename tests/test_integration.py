"""
Sample integration test demonstrating all member modules working together.

This test creates a complete workflow:
1. Member A creates league and adds teams
2. Member B generates fixtures
3. Member C records results and displays table
4. Member D calculates metrics
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from member_a_mahir.league_manager import LeagueManager
from member_b_abhishek.fixture_scheduler import FixtureScheduler
from member_c_neel.results_manager import ResultsManager
from member_d_dhawal.diagnostics_engine import DiagnosticsEngine


def test_complete_league_workflow():
    """Integration test for complete league workflow."""
    
    # Member A: Create league and add teams
    print("\n=== Member A: League Management ===")
    league_mgr = LeagueManager()
    
    success, msg, league = league_mgr.create_league("Test League", "2024-2025")
    assert success, f"Failed to create league: {msg}"
    print(f"✓ {msg}")
    
    teams = [
        ("Team A", "Stadium A"),
        ("Team B", "Stadium B"),
        ("Team C", "Stadium C"),
        ("Team D", "Stadium D")
    ]
    
    for name, stadium in teams:
        success, msg = league_mgr.add_team(name, stadium)
        assert success, f"Failed to add team: {msg}"
        print(f"✓ {msg}")
    
    # Validate league
    success, msg = league_mgr.validate_for_scheduling()
    assert success, f"League validation failed: {msg}"
    print(f"✓ League validated for scheduling")
    
    # Member B: Generate fixtures
    print("\n=== Member B: Scheduling ===")
    scheduler = FixtureScheduler(league)
    
    success, msg = scheduler.generate_fixtures("2024-12-01")
    assert success, f"Failed to generate fixtures: {msg}"
    print(f"✓ {msg}")
    
    # Validate fixtures
    is_valid, errors = scheduler.validate_fixtures()
    assert is_valid, f"Fixture validation failed: {errors}"
    print(f"✓ Fixtures validated successfully")
    
    fixtures = scheduler.get_all_fixtures()
    print(f"✓ Generated {len(fixtures)} fixtures")
    
    # Member C: Record some results and view table
    print("\n=== Member C: Results & Rankings ===")
    results_mgr = ResultsManager(league)
    
    # Record results for first few matches
    sample_results = [
        (fixtures[0]['match_id'], 2, 1),
        (fixtures[1]['match_id'], 0, 0),
        (fixtures[2]['match_id'], 3, 2),
    ]
    
    for match_id, home_score, away_score in sample_results:
        success, msg = results_mgr.record_result(match_id, home_score, away_score)
        assert success, f"Failed to record result: {msg}"
        print(f"✓ {msg}")
    
    # Display table
    table = results_mgr.get_league_table()
    assert len(table) == 4, "Table should have 4 teams"
    print(f"✓ League table generated with {len(table)} teams")
    
    # Test head-to-head
    h2h = results_mgr.get_head_to_head("Team A", "Team B")
    if h2h:
        print(f"✓ Head-to-head stats calculated")
    
    # Member D: Diagnostics & Analytics
    print("\n=== Member D: Diagnostics & Analytics ===")
    diagnostics = DiagnosticsEngine()
    
    # D1: Detect anomalies
    anomalies = diagnostics.detect_scheduling_anomalies(league, save_results=False)
    print(f"✓ Anomaly detection: {len(anomalies)} anomalies found")
    
    # D2: Workload analysis
    workload = diagnostics.analyse_team_workload(league, save_results=False)
    assert len(workload) == 4, "Should have workload for 4 teams"
    print(f"✓ Workload analysis: {len(workload)} teams analyzed")
    
    # D3: Congestion identification
    congestion = diagnostics.identify_fixture_congestion(league, save_results=False)
    print(f"✓ Congestion detection: {len(congestion)} zones identified")
    
    # D4: Rule compliance
    violations = diagnostics.check_rule_compliance(league, save_results=False)
    print(f"✓ Rule compliance: {len(violations)} violations found")
    
    # D5: Trend predictions
    trends = diagnostics.predict_outcome_trends(league, save_results=False)
    assert len(trends) == 4, "Should have trends for 4 teams"
    print(f"✓ Trend predictions: {len(trends)} teams analyzed")
    
    # D6: Season summary
    summary = diagnostics.generate_season_summary(league, save_results=False)
    assert 'statistics' in summary
    print(f"✓ Season summary: {summary['matches_played']} matches played")
    
    # D7: Test data generation
    test_data = diagnostics.generate_test_data("validate_team", {"name": "string", "stadium": "string"}, save_to_file=False)
    assert test_data['total_generated'] > 0
    print(f"✓ Test generation: {test_data['total_generated']} test cases created")
    
    # D9: Symbolic paths (D8 test harness is simulation only)
    sample_code = "def f(x):\n    if x > 0:\n        return True\n    return False"
    paths = diagnostics.extract_symbolic_paths(sample_code, "f", save_results=False)
    assert 'cyclomatic_complexity' in paths
    print(f"✓ Symbolic paths: CC={paths['cyclomatic_complexity']}, {paths['total_branches']} branches")
    
    print("\n" + "=" * 70)
    print("✅ INTEGRATION TEST PASSED - All member modules work together!")
    print("=" * 70)


if __name__ == "__main__":
    test_complete_league_workflow()
