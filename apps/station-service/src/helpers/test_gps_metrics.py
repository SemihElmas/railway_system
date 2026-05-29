# Import the tools you made in previous steps
from gps_validator import validate_polish_coordinates
from precision_formatter import format_coordinate_precision

def run_gps_system_tests():
    print(" Starting Automated QA Tests for GPS Metrics...")
    
    # Test 1: Valid Polish Coordinate Case (Gdansk)
    is_valid, msg = validate_polish_coordinates(54.3551, 18.6441)
    assert is_valid == True, f"Failed valid coordinate check: {msg}"
    
    # Test 2: Invalid Out-of-Bounds Case (New York)
    is_valid, msg = validate_polish_coordinates(40.7128, -74.0060)
    assert is_valid == False, "Failed boundary check! New York allowed inside Poland."
    
    # Test 3: Precision Truncation Verification
    rounded_val = format_coordinate_precision(18.64412345, 4)
    assert rounded_val == 18.6441, f"Expected 18.6441, got {rounded_val}"
    
    print(" All System GPS Utility Tests Passed Successfully!")

if __name__ == "__main__":
    run_gps_system_tests()