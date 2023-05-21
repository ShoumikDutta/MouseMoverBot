# Mouse Mover

The Mouse Mover is a Python script that moves the mouse cursor randomly on the screen at regular intervals. It can be used to prevent the computer from going into sleep mode or to simulate user activity.

## Prerequisites

- Python 3.x
- `pyautogui` library

## Installation

1. Make sure you have Python 3.x installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install the `pyautogui` library by running the following command in your terminal or command prompt:

   ```
   pip install pyautogui
   ```

## Usage

1. Open a text editor and create a new Python file.

2. Copy and paste the provided code into the file.

3. Save the file with a `.py` extension, for example, `mouse_mover.py`.

4. Run the script by executing the following command in your terminal or command prompt:

   ```
   python mouse_mover.py
   ```

5. The mouse cursor will start moving randomly on the screen at regular intervals. To stop the script, press `Ctrl+C` in the terminal or command prompt.

## Customization

You can customize the behavior of the Mouse Mover script by modifying certain parameters in the code:

- **Interval:** By default, the mouse cursor moves every 1 second. You can adjust the interval by changing the `sleep` function argument in the `main` function. For example, `sleep(0.5)` will move the mouse every 0.5 seconds.

- **Random Range:** The mouse cursor moves to a random position on the screen within a range defined by `x` and `y` coordinates. By default, the range is set from 1 to 1000 for both `x` and `y` coordinates. You can modify these ranges by changing the arguments in the `randint` function. For example, `x = randint(500, 1000)` and `y = randint(500, 1000)` will limit the cursor movement to the top-right quadrant of the screen.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it according to the terms of the license.

## Disclaimer

The Mouse Mover script is intended for educational or personal use only. Use it responsibly and in compliance with the laws and regulations of your jurisdiction. The script should not be used for any malicious or unauthorized activities.

## Support

If you have any questions, issues, or suggestions regarding the Mouse Mover script, please feel free to [open an issue](https://github.com/yourusername/mouse-mover/issues) in the GitHub repository.

## Acknowledgments

The Mouse Mover script utilizes the `pyautogui` library to control the mouse cursor. Special thanks to the developers of `pyautogui` for providing such a useful tool.

## Contributing

Contributions are welcome! If you find any bugs or have ideas for enhancements, please submit a pull request or open an issue in the GitHub repository.

## Author

The Mouse Mover script was created by [Shoumik Dutta](https://github.com/ShoumikDutta).

