# User Analyzer

This is a small Python script that fetches user data from an example API and analyzes it.

## What it does

- Fetches a list of users from `https://jsonplaceholder.typicode.com/users`
- Prints each user's name, username, email, and city
- Counts how many users live in a specific city

## Requirements

- Python 3
- `requests` library (`pip install requests`)

## How to run

```bash
python user_analyzer.py
````

Then enter the name of a city when prompted.

## Example

```
Enter city to count how many live in: South Christy
Request successful
Name: Clementina DuBuque | Username: Moriah.Stanton | Email: Rey.Padberg@karina.biz | City: South Christy
--------------------------------------------------------------------------------
1 lives in South Christy
```

## Notes

This script uses dummy data from the [JSONPlaceholder](https://jsonplaceholder.typicode.com) API.

```

