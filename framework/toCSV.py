import os
import re
import csv


# Remove ANSI escape codes and get the last non-empty line.
def get_last_non_empty_line(text):
    clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    lines = clean_text.splitlines()
    for line in reversed(lines):
        if line.strip():
            return line.strip()
    return ""

# Extract passed and total test cases from feedback.
def get_test_cases_info(feedback):
    matches = re.findall(r"Test cases:\s*\[.*?\]\s*(\d+)\s*/\s*(\d+)", feedback)
    if matches:
        last_match = matches[-1]
        passed = int(last_match[0])
        total = int(last_match[1])
        if passed == total:
            return passed, total
        return passed - 1, total  # Adjust passed count if needed.
    return 0, 0

# Process a single problem folder for a given model.
def process_problem_folder(folder_path, model, attempts=3):
    submissions_folder = os.path.join(folder_path, "submissions", model)
    results_folder = os.path.join(folder_path, "results", model)
    
    attempt_data = {}
    for attempt in range(1, attempts + 1):
        result_file = os.path.join(results_folder, f"attempt_{attempt}_result.txt")
        submission_file = os.path.join(submissions_folder, f"attempt_{attempt}.py")
        
        # If neither result nor submission file exists, assume no further attempts exist.
        if not os.path.exists(result_file) and not os.path.exists(submission_file):
            break
        
        data = {"status": None, "passed": 0, "total": 0, "code": ""}
        
        if os.path.exists(result_file):
            with open(result_file, "r", encoding="utf-8") as f:
                result_content = f.read()
            data["status"] = get_last_non_empty_line(result_content)
            passed, total = get_test_cases_info(result_content)
            data["passed"] = passed
            data["total"] = total
        else:
            print(f"Result file for attempt {attempt} in {folder_path} does not exist.")
        
        if os.path.exists(submission_file):
            with open(submission_file, "r", encoding="utf-8") as f:
                data["code"] = f.read()
        else:
            print(f"Submission file for attempt {attempt} in {folder_path} does not exist.")
        
        attempt_data[attempt] = data
        
        # If the solution is accepted, skip checking further attempts.
        if data["status"] == "Accepted":
            break
    
    # Determine if the problem "passed with prompting":
    passed_with_prompting = (
        attempt_data.get(1, {}).get("status") != "Accepted" and
        (attempt_data.get(2, {}).get("status") == "Accepted" or 
         attempt_data.get(3, {}).get("status") == "Accepted")
    )
    
    # Choose best attempt: earliest accepted if available; otherwise, the one with the most passed tests.
    accepted_attempts = {a: d for a, d in attempt_data.items() if d["status"] == "Accepted"}
    if accepted_attempts:
        best_attempt = min(accepted_attempts.keys())
    else:
        if attempt_data:
            best_attempt = max(attempt_data.items(), key=lambda item: item[1]["passed"])[0]
        else:
            best_attempt = None
    
    return attempt_data, passed_with_prompting, best_attempt

def main():
    model = "codeqwen:7b"
    base_dir = "./auto_miningTesting"
    attempts = 3
    
    output_csv = os.path.join('./summaries', f"{model} results_data.csv")
    
    header = ["problem", "difficulty"]
    for attempt in range(1, attempts + 1):
        header += [
            f"attempt {attempt} status",
            f"attempt {attempt} passed",
            f"attempt {attempt} total"
        ]
    header += ["passed w prompting", "best attempt"]
    
    csv_rows = []
    
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue
    
        print(f"Processing problem folder: {folder_name}")
    
        difficulty = ""
        metadata_file = os.path.join(folder_path, "metadata")
        if os.path.exists(metadata_file):
            with open(metadata_file, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                if len(lines) >= 2:
                    difficulty = lines[-2].strip()
                else:
                    print(f"Metadata file in {folder_path} does not have enough lines for difficulty.")
        else:
            print(f"Metadata file in {folder_path} does not exist.")
    
        attempt_data, passed_with_prompting, best_attempt = process_problem_folder(folder_path, model, attempts)
    
        row = {"problem": folder_name, "difficulty": difficulty}
        for attempt in range(1, attempts + 1):
            data = attempt_data.get(attempt, {})
            row[f"attempt {attempt} status"] = data.get("status") if data.get("status") is not None else ""
            row[f"attempt {attempt} passed"] = data.get("passed")
            row[f"attempt {attempt} total"] = data.get("total")
        row["passed w prompting"] = passed_with_prompting
        row["best attempt"] = best_attempt if best_attempt is not None else ""
    
        csv_rows.append(row)
    
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)
    
    print(f"\nCSV summary written to {output_csv}")

if __name__ == "__main__":
    main()
