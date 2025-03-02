import os
import re
import csv
import argparse

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

# Extract Python code from a message (if needed).
def get_python(message):
    start_code_block = message.find("```Python")
    if start_code_block == -1:
        start_code_block = message.find("```python")
    if start_code_block == -1:
        start_code_block = message.find("```")
        cut_string = message[start_code_block + 3:]
    else:
        cut_string = message[start_code_block + 10:]
    end_code_block = cut_string.find("```")
    return cut_string[:end_code_block].strip()

# Process a single problem folder for a given model.
def process_problem_folder(folder_path, model, attempts=3):
    submissions_folder = os.path.join(folder_path, f"submissions_{model}")
    results_folder = os.path.join(folder_path, f"results_{model}")
    
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
            # Both status and error message are the same; we keep one column.
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
    model = "qwen2.5-coder:7b"
    base_dir = "./auto_miningTesting"

    attempts = 3
    
    # Create the summaries directory relative to this script's location.
   
    
    # Define the output CSV path in the summaries directory.
    output_csv = os.path.join('./summaries', f"{model} results_data.csv")
    
    # Define CSV columns.
    header = ["problem", "difficulty"]
    for attempt in range(1, attempts + 1):
        header += [
            f"attempt {attempt} status",
            f"attempt {attempt} passed",
            f"attempt {attempt} total"
        ]
    header += ["passed w prompting", "best attempt"]
    
    csv_rows = []
    
    # Iterate over each problem folder in the base directory.
    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue
    
        print(f"Processing problem folder: {folder_name}")
    
        # Read the difficulty from metadata.
        difficulty = ""
        metadata_file = os.path.join(folder_path, "metadata")
        if os.path.exists(metadata_file):
            with open(metadata_file, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                if len(lines) >= 2:
                    difficulty = lines[-2].strip()  # Second-to-last line
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
    
    # Write rows to the CSV file.
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in csv_rows:
            writer.writerow(row)
    
    print(f"\nCSV summary written to {output_csv}")


if __name__ == "__main__":
    main()
