
# InSis: Remove Notifications  

**InSis Remove Notifications** is a Python script designed to simplify the process of clearing notifications on the **inSIS student platform** for **VŠE University**. The script automates the task of closing all notifications, which would otherwise need to be done manually one by one.  

## Features  
- Uses **Selenium** to simulate user interactions on the inSIS platform.  
- Automatically logs in and clears all notifications.  
- Saves time and effort for students overwhelmed by multiple notifications.  

## Requirements  

Before running the script, make sure you have the following installed:  
- Python 3.8 or newer  
- The following Python packages:  
  ```plaintext
  time  
  selenium  
  webdriver_manager  
  pwinput  
  ```
- You can install packages via pip:
  ```bash
   pip install selenium webdriver-manager pwinput
   ```  


## Usage  

1. Run the script using Python:  
   ```bash
   python InSis.py
   ```  

2. You will be prompted to enter your inSIS credentials securely including 2FA code.  

3. The script will log into your account, locate all notifications, and close them.  

## Security  

- The script uses the **pwinput** package to securely hide your password during input.
- The script does not store the credentials in any way.
- The script is open-source so you can make sure that there is no malicious intent.

## Disclaimer  

This script is intended for educational purposes and personal use only. Use it responsibly and at your own risk. The author is not responsible for any misuse or potential breaches of the inSIS platform's terms of service.  

## Contributing  

Contributions are welcome! Feel free to open issues or submit pull requests.  
