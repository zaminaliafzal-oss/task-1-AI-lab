class MovieBudget:
    def __init__(self):
        self.movies = [
            ("Eternal Sunshine of the Spotless Mind", 20000000),
            ("Memento", 9000000),
            ("Requiem for a Dream", 4500000),
            ("Pirates of the Caribbean: On Stranger Tides", 379000000),
            ("Avengers: Age of Ultron", 365000000),
            ("Avengers: Endgame", 356000000),
            ("Incredibles 2", 200000000)
        ]
    def calculate_average(self):
        total = 0
        for movie in self.movies:
            total += movie[1]
        return total / len(self.movies)
    def high_budget_movies(self):
        average = self.calculate_average()
        count = 0
        print(f"Average Budget: {average}\n")
        print("Movies with budget higher than average:\n")
        for title, budget in self.movies:
            if budget > average:
                print(f"{title} - {budget}")
                count += 1
        print(f"\nNumber of movies above average: {count}")
    def add_movies(self):
        n = int(input("How many movies do you want to add? "))
        for _ in range(n):
            title = input("Enter movie title: ")
            budget = float(input("Enter movie budget: "))
            self.movies.append((title, budget))
movie_system = MovieBudget()
movie_system.add_movies()
movie_system.high_budget_movies()