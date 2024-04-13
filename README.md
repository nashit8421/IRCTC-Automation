

# IRCTC Ticket Booking Automation

This Python project automates the process of booking train tickets on India's IRCTC website. The script uses Selenium and undetected Chromedriver to simulate a user interacting with the website. It includes features such as logging in, searching for trains, entering passenger details, and completing the booking process.

## Features

- **Automated Login**: Logs into the IRCTC portal automatically.
- **Train Search**: Searches for available trains between specified stations.
- **Passenger Input**: Automatically inputs passenger and infant details.
- **Booking Finalization**: Handles seat selection, payment options, and final confirmation steps.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- pip (Python package installer)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/irctc-automation.git
   cd irctc-automation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This command installs the following necessary Python packages:
   - `selenium`
   - `undetected_chromedriver`

## Configuration

Before running the script, update the following details in the script:
- `USERNAME`: Your IRCTC username.
- `PASSWORD`: Your IRCTC password.
- `JOURNEY_DATE`: The date of your journey in DD/MM/YYYY format.
- `source_station`: The code or name of the source station.
- `destination_station`: The code or name of the destination station.

## Usage

To use the script, follow these instructions:

1. **Open the script**:
   Open `booking_script.py` in a text editor and fill in your details for `USERNAME`, `PASSWORD`, and `JOURNEY_DATE`.

2. **Run the script**:
   ```bash
   python booking_script.py
   ```

   Ensure you are ready to manually solve the captcha that appears during login.

3. **Follow on-screen instructions**:
   The script will instruct you to solve the captcha manually and press enter in the console to continue.

## Known Issues

- **Captcha Requirement**: The script cannot bypass the captcha during login, requiring manual intervention.

## Contributing

Contributions to enhance the functionality, improve efficiency, or fix issues in the script are welcome. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. Please ensure that you are not violating IRCTC's terms of service or any laws regarding automation and data privacy. Automated interactions with IRCTC can lead to account suspension. Use this script responsibly and at your own risk.
