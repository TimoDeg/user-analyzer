import requests

class UserAnalyzer:
    def __init__(self, url):
        self.url = url

    def get_users(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            print("Request successful")
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return [] 
        
    def print_users_data(self, users):
        for user in users:
            print(f"Name: {user['name']}", end=" | ")
            print(f"Username: {user['username']}", end=" | ")
            print(f"Email: {user['email']}", end=" | ")
            print(f"City: {user['address']['city']}")
            print("-" * 120)

    def count_city(self, users, city):
        city_count = 0
        for user in users:
            if user["address"]["city"] == city:
                city_count += 1
        if city_count == 1:
            return f"{city_count} lives in {city}"
        elif city_count > 1:
            return f"{city_count} live in {city}"
        else:
            return f"No one live in {city}"

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    city_to_count = input("Enter city to count how many live in: ")
    analyzer = UserAnalyzer(url)

    users = analyzer.get_users()
    analyzer.print_users_data(users)
    print(analyzer.count_city(users, city_to_count))