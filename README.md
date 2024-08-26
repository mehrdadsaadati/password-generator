# password-generator

Password generator CLI app. Generates secure random passwords based on the user input.

## What does it do?

Generates a secure random password based on user request in specified length and format

## How to use?

```bash
password_generator g len format exclude
```

- g: The generate command
- len: Integer. Length of the generated password
- format: String (optional, default to 'Aa0@'). Format of the password. Can be one of these options or a mix of them:
  - 'a': lower case characters
  - 'A': lower case characters
  - '0': numbers from 0 to 9
  - '@': symbols
- exclude: String (optional, default to ''). A string of characters (letters, numbers and symbols) to exclude from the generated password

### Examples

```bash
password_generator g 16

```

## Installation

```bash
poetry install
poetry run password_generator
```
