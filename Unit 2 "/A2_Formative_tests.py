#!/usr/bin/env python3
"""
A2_Formative_tests.py

"""

# ====== TEST CONFIGURATION ======

MODULE = "P4DS_Formative_A2"

SHOW_TEST_CALL = True
SHOW_TEST_RESULT = True
SHOW_TEST_ANSWER = True

# Test data for holiday recommendation functions
HOLIDAYS_TEST = [
    ["Brighton", 150, ["beach", "culture"]],
    ["Whitby", 100, ["beach", "culture"]],
    ["Barcelona", 320, ["beach", "culture", "hot"]],
    ["Doncaster", 40, []],
    ["Crete", 300, ["beach", "hot"]],
    ["London", 250, ["culture"]],
    ["Sicily", 300, ["culture", "hot", "beach"]],
    ["Barbados", 1250, ["hot", "beach"]],
    ["Tanzania", 2500, ["hot", "beach", "wildlife"]],
    ["Galapagos Islands", 4500, ["beach", "wildlife"]],
]

# Test specifications for each function
TESTS = {
    "anagrams": [
        ('__M__.anagrams("listen","silent")', "eq_bool", True, 1),
        ('__M__.anagrams("Listen","Silent")', "eq_bool", True, 1),
        ('__M__.anagrams("this","that")', "eq_bool", False, 1),
        ('__M__.anagrams("this","This")', "eq_bool", False, 1),
    ],
    "is_palindrome": [
        ('__M__.is_palindrome("Abba")', "eq_bool", True, 1),
        ('__M__.is_palindrome("Python")', "eq_bool", False, 1),
        ('__M__.is_palindrome("Rotator")', "eq_bool", True, 1),
        ('__M__.is_palindrome("Was it a cat I saw?")', "eq_bool", True, 1),
    ],
    "is_english_word": [
        ('__M__.is_english_word("this")', "eq_bool", True, 1),
        ('__M__.is_english_word("Python")', "eq_bool", True, 1),
        ('__M__.is_english_word("HelP")', "eq_bool", False, 1),
        ('__M__.is_english_word("Flibbertigibbet")', "eq_bool", True, 1),
        ('__M__.is_english_word("Brexit")', "eq_bool", False, 1),
    ],
    "find_all_anagrams": [
        ('__M__.find_all_anagrams("cheese")', "eq_list", [], 1),
        ('__M__.find_all_anagrams("Python")', "eq_list", ['phyton', 'typhon'], 1),
        ('__M__.find_all_anagrams("Listen!")', "eq_list", [], 1),
        ('__M__.find_all_anagrams("SeaBird")', "eq_list", ['abiders', 'braised', 'darbies', 'sidebar'], 1),
    ],
    "find_palindromes_of_length": [
        ('__M__.find_palindromes_of_length(7)', "eq_list",
         ['deified', 'halalah', 'reifier', 'repaper', 'reviver', 'rotator', 'sememes'], 1),
        ('__M__.find_palindromes_of_length(10)', "eq_list", [], 1),
    ],
    "password_strength": [
        ('__M__.password_strength("boa constrictor")', "eq_str", "ILLEGAL", 1),
        ('__M__.password_strength("Secret")', "eq_str", "ILLEGAL", 1),
        ('__M__.password_strength("secret99")', "eq_str", "WEAK", 1),
        ('__M__.password_strength("Secret999!")', "eq_str", "MEDIUM", 1),
        ('__M__.password_strength("7Kings8all9Pies!")', "eq_str", "STRONG", 1),
    ],
    "available_features": [
        ("__M__.available_features(100, HOLIDAYS_TEST)", "eq_list", ["beach", "culture"], 1),
        ("__M__.available_features(5000, HOLIDAYS_TEST)", "eq_list",
         ["beach", "culture", "hot", "wildlife"], 1),
    ],
    "recommend_holidays": [
        ('__M__.recommend_holidays(200, ["beach"], HOLIDAYS_TEST)', "eq_list",
         ["Brighton", "Whitby"], 1),
        ('__M__.recommend_holidays(500, ["beach"], HOLIDAYS_TEST)', "eq_list",
         ['Barcelona', 'Brighton', 'Crete', 'Sicily', 'Whitby'], 1),
        ('__M__.recommend_holidays(300, ["culture"], HOLIDAYS_TEST)', "eq_list",
         ["Brighton", "London", "Sicily", "Whitby"], 1),
        ('__M__.recommend_holidays(5000, ["beach", "wildlife"], HOLIDAYS_TEST)', "eq_list",
         ["Galapagos Islands", "Tanzania"], 1),
    ],
}

# Comparison functions for checking test results
CHECK_TYPES = {
    "equal": lambda x, y: (type(x) == type(y) and x == y),
    "eq_bool": lambda x, y: (type(x) == bool and type(y) == bool and x == y),
    "eq_int": lambda x, y: (type(x) == int and type(y) == int and x == y),
    "eq_str": lambda x, y: (type(x) == str and type(y) == str and x == y),
    "eq_list": lambda x, y: (type(x) == list and type(y) == list and x == y),
}


# ====== TESTING FUNCTIONS ======


def run_single_test(func, func_name, test_call, check_type, expected, marks):
    """
    Run a single test case for a function
    
    Args:
        func: The function to test
        func_name: Name of the function
        test_call: String representation of the test call
        check_type: Type of comparison to perform
        expected: Expected result
        marks: Marks available for this test
        
    Returns:
        tuple: (marks_earned, feedback_string)
    """
    # Extract the function call part after __M__.function_name
    # e.g., '__M__.anagrams("listen","silent")' -> 'anagrams("listen","silent")'
    # Then replace function_name with func to get 'func("listen","silent")'
    
    # Replace __M__.function_name with just the function reference
    import re
    pattern = r'__M__\.' + re.escape(func_name)
    test_call_actual = re.sub(pattern, func_name, test_call)
    
    # Make function and test data available in eval context
    eval_context = {func_name: func, 'HOLIDAYS_TEST': HOLIDAYS_TEST}
    
    try:
        if SHOW_TEST_CALL:
            print(f"\nTest: {test_call}")
        
        # Execute the function call
        result = eval(test_call_actual, eval_context)
        
        if SHOW_TEST_RESULT:
            print(f"  Result: {result}")
        if SHOW_TEST_ANSWER:
            print(f"  Expected: {expected}")
        
        # Check if result matches expected
        check_function = CHECK_TYPES.get(check_type, CHECK_TYPES["equal"])
        passed = check_function(result, expected)
        
        if passed:
            print(f"  ✓ PASSED ({marks} mark{'s' if marks != 1 else ''})")
            return (marks, "PASSED")
        else:
            print(f"  ✗ FAILED (0 marks)")
            return (0, f"Failed: got {result}, expected {expected}")
            
    except Exception as e:
        print(f"  ✗ ERROR: {str(e)}")
        return (0, f"Error: {str(e)}")


def do_tests(func):
    """
    Run all tests for a given function
    
    Args:
        func: The function object or function name (string) to test
    """
    # Get function name
    if callable(func):
        func_name = func.__name__
    else:
        func_name = func
        print(f"Error: {func_name} is not a callable function")
        return
    
    # Check if tests exist for this function
    if func_name not in TESTS:
        print(f"No tests defined for function: {func_name}")
        return
    
    print(f"\n{'='*60}")
    print(f"Testing function: {func_name}")
    print(f"{'='*60}")
    
    tests = TESTS[func_name]
    total_marks = 0
    earned_marks = 0
    
    for test_spec in tests:
        test_call, check_type, expected, marks = test_spec
        total_marks += marks
        
        marks_earned, feedback = run_single_test(
            func, func_name, test_call, check_type, expected, marks
        )
        earned_marks += marks_earned
    
    print(f"\n{'-'*60}")
    print(f"Score for {func_name}: {earned_marks}/{total_marks}")
    print(f"{'='*60}\n")
    
    return earned_marks


def do_all_tests():
    """
    Run all tests for all functions defined in TESTS
    Returns the total mark earned
    """
    import sys
    
    # Try to get the module that called this function
    frame = sys._getframe(1)
    caller_globals = frame.f_globals
    
    print(f"\n{'#'*60}")
    print(f"# RUNNING ALL TESTS FOR {MODULE}")
    print(f"{'#'*60}\n")
    
    total_earned = 0
    total_possible = 0
    results = []
    
    for func_name in TESTS.keys():
        # Get the function from caller's globals
        if func_name in caller_globals:
            func = caller_globals[func_name]
            
            # Count total possible marks for this function
            func_total = sum(test[3] for test in TESTS[func_name])
            total_possible += func_total
            
            # Run tests
            earned = do_tests(func)
            total_earned += earned
            results.append((func_name, earned, func_total))
        else:
            print(f"\n⚠ Function '{func_name}' not found in notebook")
            func_total = sum(test[3] for test in TESTS[func_name])
            total_possible += func_total
            results.append((func_name, 0, func_total))
    
    # Print summary
    print(f"\n{'#'*60}")
    print(f"# SUMMARY OF RESULTS")
    print(f"{'#'*60}\n")
    
    for func_name, earned, possible in results:
        percentage = (earned / possible * 100) if possible > 0 else 0
        print(f"{func_name:30s}: {earned:2d}/{possible:2d} ({percentage:5.1f}%)")
    
    print(f"\n{'-'*60}")
    percentage = (total_earned / total_possible * 100) if total_possible > 0 else 0
    print(f"{'TOTAL SCORE':30s}: {total_earned:2d}/{total_possible:2d} ({percentage:5.1f}%)")
    print(f"{'-'*60}\n")
    
    # Final comment
    comment = get_final_comment(total_earned, total_possible)
    print(comment)
    print(f"\n{'#'*60}\n")
    
    return total_earned


def get_final_comment(marks, total):
    """Return a comment based on the percentage score"""
    if total == 0:
        return ""
    
    percent = (marks / total) * 100
    
    if percent == 100:
        return "**** PERFECT SCORE ****"
    elif percent >= 90:
        return "*** SPECTACULAR ***"
    elif percent >= 70:
        return "*** EXCELLENT ***"
    elif percent >= 60:
        return "** VERY GOOD **"
    elif percent >= 50:
        return "* GOOD *"
    elif percent >= 40:
        return "A reasonable attempt but more study is advised."
    else:
        return ("You are advised to revisit this exercise and ask\n"
                "for help regarding any difficulties you are having.")


# Make sure the module doesn't run tests when imported
if __name__ == "__main__":
    print("This is a testing module. Import it from your notebook to use it.")
    print("Example usage:")
    print("  do_tests(your_function)")
    print("  do_all_tests()")
