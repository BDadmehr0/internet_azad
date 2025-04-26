# Internet Azad - اینترنت آزاد

## Table of Contents
- [How to Install](#how-to-install)
- [Requirements](#requirements)
- [About the Code & Functions](#about-the-code--functions)
  - [Main Features](#main-features)
  - [Key Functions](#key-functions)
  - [Execution Flow](#execution-flow)
  - [Output Files](#output-files)
- [Usage](#usage)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## How to Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/BDadmehr0/internet_azad
   ```

2. **Install Python**: Ensure Python 3.x is installed on your system.

3. **Install Dependencies**: Run the following command to install the required Python packages:
   ```bash
   pip install -r requrments.txt
   ```

## Requirements

The `requrments.txt` file should contain the following dependencies:
- `requests`
- `tqdm`
- `rich`

Ensure these libraries are installed for the script to function correctly.

## About the Code & Functions

### Main Features
The script fetches and processes encoded and plain-text URLs to extract various protocols such as `vmess://`, `vless://`, `ss://`, and `trojan://`. It provides options to save these protocols into separate files.

### Key Functions

1. **`fetch_encoded_content(url_list, all_protocols)`**:
   - Fetches content from a list of encoded URLs.
   - Decodes the content using Base64 and extracts supported protocols.

2. **`save_protocols(protocol_type, all_protocols)`**:
   - Saves protocols of a specific type (e.g., `ss`, `vless`) to a file named `<protocol_type>_protocols_<date>.txt`.

3. **`save_all_protocols(all_protocols)`**:
   - Saves all collected protocols to a file named `all_protocols_<date>.txt`.

4. **`display_menu()`**:
   - Displays a menu for the user to choose which protocols to save.
   - Calls the appropriate save function based on user input.

### Execution Flow
1. Collects protocols from a list of encoded and plain-text URLs.
2. Displays a summary table of protocol counts using the `rich` library.
3. Provides an interactive menu for saving protocols.

### Output Files
- `all_protocols_<date>.txt`: Contains all collected protocols.
- `<protocol_type>_protocols_<date>.txt`: Contains protocols of a specific type (e.g., `ss`, `vless`).

## Usage

Run the script using the following command:
```bash
python main.py
```

Follow the on-screen menu to save the desired protocols.

## Contribution Guidelines

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
