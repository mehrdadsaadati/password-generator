# password-generator

Password generator CLI app. Generates secure random passwords based on the user input.

## What does it do?

Generates a secure random password based on user request in specified length and format

## How to use?

```bash
password_generator len -f (--format) -e (--exclude) -c (--custom)
```

- len: Integer (positional argument, required). Length of the generated password
- f, format: String (optional, default to 'Aa0@'). Format of the password. Can be one of these options or a mix of them:
  - 'a': lower case characters
  - 'A': lower case characters
  - '0': numbers from 0 to 9
  - '@': symbols
  - 'h': lower case hex number (other formats and `exclude` will be ignored)
  - 'H': upper case hex number (other formats and `exclude` will be ignored)
- e, exclude: String (optional, default to ''). A string of characters (letters, numbers and symbols) to exclude from the generated password
- c, custom: String (optional, default to ''). A string of letters, numbers and symbols to pick characters from. If this parameter is passed, `format` and `exclude` is ignored

### Examples

```bash
# 16 chars length
password_generator 16
> 0N3l<l*9HmV7gn£?

# 16 chars length, only lower and upper case letters
password_generator 16 -f aA
> KOpNxKrnuSXUNuFs

# 32 chars length, only lower case letters and numbers
password_generator 32 -f a0
> 2xyf75zh026zp02d5zl12kgj2ogimoch

# 16 chars length, only numbers and symbols
password_generator 16 -f 0@
> 3?!555?&%<+7+*$£

# 16 chars length, everything excluding symbols, 0,8,o and O
password_generator 16 -f aA0 -e 08oO
> s4dUG2R66rv1BkxY

# 8 chars length, from custom list (format will be ignored)
password_generator 8 -c abcdefgXYZ01234
> ecX2a34X

# 16 chars length, lower case hex number
password_generator 16 -f h
> a02349f3e0b12c39

# 16 chars length, upper case hex number
password_generator 16 -f H
> 90C932340FE0B23A

```

## Installation

```bash
poetry install
poetry run password_generator
```
