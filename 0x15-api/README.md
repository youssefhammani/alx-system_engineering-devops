# API Project

## Overview
This project involves working with a REST API to retrieve information about employee tasks, organize them, and export them into different data structures such as CSV and JSON. The tasks are implemented using Python scripts adhering to industry-standard practices and guidelines.

## Installation
1. Clone this repository to your local machine.
2. Ensure you have Python 3.8.5 installed.
3. Install the required dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Navigate to the project directory.
2. Execute the Python scripts with the appropriate command-line arguments.

### Task 0: Gather data from an API
```bash
python3 0-gather_data_from_an_API.py <employee_id>
```

### Task 1: Export to CSV
```bash
python3 1-export_to_CSV.py <employee_id>
```

### Task 2: Export to JSON
```bash
python3 2-export_to_JSON.py <employee_id>
```

## Project Structure
- `0-gather_data_from_an_API.py`: Python script for Task 0.
- `1-export_to_CSV.py`: Python script for Task 1.
- `2-export_to_JSON.py`: Python script for Task 2.
- `requirements.txt`: Contains the required Python libraries.
- `README.md`: Project documentation.

## Development Environment
- **Editor**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: 3.8.5

## Coding Standards
- All files use the `#!/usr/bin/python3` shebang.
- Libraries are imported in alphabetical order.
- Code follows PEP8 Python style guidelines.
- Documentation is provided for all modules.
- Code is not executed when imported.

## Author
[Your Name]

## Acknowledgments
- This project is part of [Holberton School](https://www.holbertonschool.com/)'s curriculum.
- Special thanks to Sylvain Kalache, co-founder at Holberton School, for the guidance.
