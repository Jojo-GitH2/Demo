import sys
from typing import List, Tuple


def sum_of_negative_powers(numbers: List[int]) -> int:
    """Return the sum of the 4th powers of all negative numbers in the list."""

    if not numbers:
        return 0
    first_number, *remaining_numbers = numbers
    if first_number < 0:
        return first_number ** 4 + sum_of_negative_powers(remaining_numbers)
    return sum_of_negative_powers(remaining_numbers)

def process_single_case(tokens: List[str], current_index: int) -> Tuple[int, int]:
    """
    Process a single test case from tokens starting at current_index.
    Returns a tuple of (new_index, result).
    """
    if current_index >= len(tokens):
        return current_index, - 1
    
    expected_count = int(tokens[current_index])
    current_index += 1

    if current_index + expected_count > len(tokens):
        return current_index + expected_count, - 1
    
    case_numbers = list(map(int, tokens[current_index: current_index + expected_count]))
    current_index += expected_count

    if len(case_numbers) != expected_count:
        return current_index, -1

    result = sum_of_negative_powers(case_numbers)
    return current_index, result

def process_all_cases(tokens: List[str], case_number: int, current_index: int, total_cases: int, results: List[int]) -> List[int]:
    """
    Recursively process all test cases. Returns a list of results.
    """
    if case_number == total_cases:
        return results
    current_index, result = process_single_case(tokens, current_index)
    results.append(result)
    return  process_all_cases(tokens, case_number + 1, current_index, total_cases, results)





def main():
    input_tokens = sys.stdin.read().strip().split()
    if not input_tokens:
        return
    
    total_cases = int(input_tokens[0])
    results = process_all_cases(input_tokens, 0, 1, total_cases, [])
    sys.stdout.write("\n".join(map(str, results)))

 

if __name__ == "__main__":
    main()