# Greek Alphabet
A Python module for working with the Greek alphabet.

## Usage
### Importing the module
```python
from greek_alphabet import Alphabet
```

### Getting a list of all Greek alphabet characters
```python 
alphabet_list = Alphabet.get_list()
```

### Getting a dictionary of all Greek alphabet characters
```python
alphabet_dict = greek_alphabet.Alphabet.get_dict()
```

The `get_dict()` method takes two optional parameters:

- `key`: a function that takes an `AlphabetChar` object and returns a string to use as the dictionary key. By default, the Greek name of the character is used.
- `value`: a function that takes an `AlphabetChar` object and returns the value to use in the dictionary. By default, the `AlphabetChar` object is used.

### Converting between upper and lower case
```python 
# Convert a lower case letter to upper case
upper_case_char = greek_alphabet.Alphabet.upper('a')

# Convert an upper case letter to lower case
lower_case_char = greek_alphabet.Alphabet.lower('Γ')
```


## AlphabetChar class
The `AlphabetChar` class represents a single character of the Greek alphabet. It has the following attributes:

- `char`: the character itself
- `capitalized`: the capitalized version of the character
- `name`: the name of the character in Greek
- `lower`: the lower case equivalent of the character

# License
This module is released under the MIT License. See LICENSE for more information.