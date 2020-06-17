# RinnBlackJackPro

RinnBlackJackPro is a console game where the user can make bets and play BlackJack. It uses a single standard deck of 52 cards, which all start off in a card shoe. Cards move from the card shoe to a recycle before they get reshuffled in. I made UTC-8 graphics for the cards and the logic to display single cards or multiple cards side-by-side. All cards begin as a template and depending on the suit and value, will pull from a lookup table with the coded information to feed into the template.

## Usage

```python
python run.py
```

## Unittest

```python
python -m unittest discover
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://github.com/Hey-Its-Rinn/RinnBlackJackPro/blob/master/LICENSE)
