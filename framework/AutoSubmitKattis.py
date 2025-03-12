import os
import ollama
import subprocess

############# Automate getting the generated solutions from Ollama and Submitting to Kattis ################ 
## Each problem folder must have a 'problem_text' of the problem's description ##
## Must have a .kattisrc configuration file in root directory ##

model = "qwen2.5-coder:7b"  # Example model name; can also be codellama:7b, codegemma:7b, etc.

# Helper function to format the model name for file naming
def format_model_name(model_name):
    if ":" in model_name:
        parts = model_name.split(":", 1)
        return f"{parts[0]}-{parts[1]}"
    else:
        return model_name

# Use the formatted model name for file names
formatted_model = format_model_name(model)

# Prompting Ollama model
def api_call(input_text):
    question = (
        "Write a Python program for this problem and make sure that the variables' names "
        "and functions' names are different, and also only using internal Python libraries, "
        "not using external Python libraries: \n\n" + input_text
    )
    response = ollama.chat(
        model=model,  # using original model string for the API call
        messages=[{"role": "user", "content": question}]
    )
    return response["message"]["content"]

# Convert Ollama output to just Python code
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

# Directories and files
dir_path = "./auto_miningTesting2"  # Root directory containing problem folders
file_name = "problem_text"           # File containing the problem description
test_cases = "sample_input_and_ouput" # File in problem folder with test cases
text_output_file = formatted_model + ".txt"  # File name for the full Ollama response

for folder_name in os.listdir(dir_path):

    # Get the folder path
    folder_path = os.path.join(dir_path, folder_name)
    if not os.path.isdir(folder_path):
        continue  # Only work on directories

    # Uncomment to process a specific problem folder
    # if not folder_name == "abc": continue 

    problem_id = folder_name
    output_file = formatted_model + ".py"
    
    # Create a 'submissions' folder for generated solutions
    submissions_folder = os.path.join(folder_path, "submissions")
    os.makedirs(submissions_folder, exist_ok=True)

    # Create a 'results' folder for Kattis submission results
    results_folder = os.path.join(folder_path, "result")
    os.makedirs(results_folder, exist_ok=True)

    # Get the file path for the problem description
    file_path = os.path.join(folder_path, file_name)

    # Read the problem description
    with open(file_path, "r", encoding="utf-8") as file:
        problem_description = file.read()
    
    # Read test cases if the file exists
    test_cases_path = os.path.join(folder_path, test_cases)
    test_cases_content = ""
    if os.path.exists(test_cases_path):
        with open(test_cases_path, "r", encoding="utf-8") as test_file:
            test_cases_content = "\n\nTest Cases:\n" + test_file.read()

    # Combine problem description and test cases
    full_input_text = problem_description + test_cases_content

    # Make API call to generate Python solution
    api_answer = api_call(full_input_text)
    
    # Get the Python code from Ollama output
    api_python = get_python(api_answer)

    # Save the generated Python code to 'submissions/[formatted_model].py'
    output_path = os.path.join(submissions_folder, output_file)
    with open(output_path, "w") as file:
        file.write(api_python)

    # Save the full API response to 'submissions/[formatted_model].txt'
    text_output_path = os.path.join(submissions_folder, text_output_file)
    with open(text_output_path, "w") as file:
        file.write(api_answer)
    
    # Get generated solution file path and the submit.py filepath
    file_path = os.path.join(folder_path, "submissions", output_file)
    submit_script_path = os.path.join(os.getcwd(), "framework", "submit.py")

    # Use Kattis configuration file to submit with submit.py
    result = subprocess.run(
        ["python3", submit_script_path, "-p", problem_id, file_path, "-f"],
        capture_output=True,  # Capture stdout and stderr
        text=True,            # Return stdout and stderr as strings 
    )
    
    # Print result from Kattis submission
    print(result.stdout)
    print(result.stderr)  

    # Write results to results folder with formatted model name
    result_path = os.path.join(results_folder, formatted_model + "_result.txt")
    with open(result_path, 'w') as stdout_file:
        stdout_file.write(result.stdout)  # Write stdout to a file
    
    # break  # Only iterate once
