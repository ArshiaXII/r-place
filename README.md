# r-place

# Reddit r/place Pixel Placer

This script is a simple bot that uses the Reddit API to place pixels on r/place.

## Requirements

* Python 3.x
* `requests` library

## Usage

1. Clone this repository.
2. Install the required Python libraries with `pip install requests`.
3. Replace the `username`, `password`, `app_id`, and `app_secret` placeholders in the `place_bot.py` script with your own Reddit API credentials.
4. Modify the `pixels` list in the `place_bot.py` script to include the coordinates and colors of the pixels that you want to place. The color should be an integer from 0-15, corresponding to the color palette of r/place.
5. Run the script with `python place_bot.py`.

## Notes

Please respect the API usage limitations and rules imposed by Reddit. Improper use may result in your Reddit account being suspended or banned. This script is intended for educational purposes, and I am not responsible for any misuse.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
