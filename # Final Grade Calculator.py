# Final Grade Calculator

def calculate_required_final(current_grade, final_weight, target_grade):
    final_weight /= 100 
    required_final = (target_grade - (1 - final_weight) * current_grade) / final_weight
    return min(max(required_final, 0), 100) 
def main():
    grade_cutoffs = {
        "A": 92.5,
        "A-": 89.5,
        "B+": 86.5,
        "B": 82.5,
        "B-": 79.5,
        "C+": 76.5,
        "C": 72.5,
        "C-": 69.5,
        "D+": 66.5,
        "D": 62.5,
        "D-": 59.5,
        "F": 0
    }

    current_grade = float(input("Enter your current grade (as a percentage): "))
    final_weight = float(input("Enter the weight of the final exam (as a percentage of the final grade): "))

    print("\nGrades needed on the final exam to achieve:")
    print("(Note: Anything over 100% is not possible without extra credit. 100% likely means impossible.)")
    print("--------------------------------------------------------")

    for grade, cutoff in grade_cutoffs.items():
        required_score = calculate_required_final(current_grade, final_weight, cutoff)
        print(f"{grade}: {required_score:.2f}% on final exam")

if __name__ == "__main__":
    main()
