import difflib
import random

import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)


def list_movies(movies):
    for title, rating in movies.items():
        print(Fore.GREEN + f"{title}, {rating}")
    print()


def print_menu():
    print(Fore.MAGENTA + "********** My Movies Database **********\n")
    print(Fore.CYAN + "Menu")
    print(Fore.CYAN + "1. List movies")
    print(Fore.CYAN + "2. Add movie")
    print(Fore.CYAN + "3. Delete movie")
    print(Fore.CYAN + "4. Update movie")
    print(Fore.CYAN + "5. Stats")
    print(Fore.CYAN + "6. Random movie")
    print(Fore.CYAN + "7. Search movie")
    print(Fore.CYAN + "8. Movies sorted by rating")
    print(Fore.CYAN + "9. Create Rating Histogram\n")


def add_movie(movies):
    movie = input(Fore.CYAN + "Enter a new movie name: ")
    if movie in movies:
        print(Fore.YELLOW + f"Movie {movie} already exists!")
        return
    try:
        rating = float(input(Fore.CYAN + "Enter new movie rating (0-10): "))
    except ValueError:
        rating = -1
    if 0 <= rating <= 10:
        movies[movie] = rating
        print(Fore.GREEN + f"Movie {movie} successfully added")
    else:
        print(Fore.RED + f"Rating {rating} is invalid")


def delete_movies(movies):
    movie = input(Fore.CYAN + "Enter movie name to delete: ")
    if movie not in movies:
        print(Fore.RED + f"Movie {movie} doesn't exist\n")
    else:
        del movies[movie]
        print(Fore.GREEN + f"Movie {movie} successfully deleted\n")


def update_movies(movies):
    movie = input(Fore.CYAN + "Enter movie name: ")
    if movie in movies:
        try:
            rating = float(input(Fore.CYAN + "Enter new movie rating (0-10): "))
        except ValueError:
            rating = -1
        if 0 <= rating <= 10:
            movies[movie] = rating
            print(Fore.GREEN + f"Movie {movie} successfully updated\n")
        else:
            print(Fore.RED + f"Rating {rating} is invalid\n")
    else:
        print(Fore.RED + f"Movie {movie} doesn't exist")


def stats(movies):
    total = sum(movies.values())
    avg = total / len(movies)
    rating = sorted(movies.values())
    n = len(rating)
    median = rating[n // 2] if n % 2 == 1 else (rating[n // 2 - 1] + rating[n // 2]) / 2
    min_rating = min(movies.values())
    max_rating = max(movies.values())
    lowest_movies = [title for title, r in movies.items() if r == min_rating]
    highest_movies = [title for title, r in movies.items() if r == max_rating]
    print(Fore.GREEN + f"Average rating: {avg}")
    print(Fore.GREEN + f"Median rating: {median}")
    print(Fore.GREEN + f"Best movie: {', '.join(highest_movies)}, {max_rating}")
    print(Fore.GREEN + f"Worst movie: {', '.join(lowest_movies)}, {min_rating}\n")


def random_movie(movies):
    movie, rating = random.choice(list(movies.items()))
    print(Fore.GREEN + f"Your movie for tonight: {movie}, it's rated {rating}\n")


def search_movies(movies):
    movie = input(Fore.CYAN + "Enter part of movie name: ")
    print()
    found_any = False
    q = movie.lower()
    for title, rating in movies.items():
        if q in title.lower():
            print(Fore.GREEN + f"{title}, {rating}")
            found_any = True
    if not found_any:
        titles = list(movies.keys())
        suggestions = difflib.get_close_matches(movie, titles, n=5, cutoff=0.4)
        print(Fore.RED + f'The movie "{movie}" does not exist.')
        if suggestions:
            print(Fore.YELLOW + "Did you mean:")
            for s in suggestions:
                print(Fore.GREEN + f"{s}")
        else:
            print(Fore.RED + "No similar movies were found.")
    print()


def movies_sorted_by_rating(movies):
    for title, rating in sorted(movies.items(), key=lambda item: item[1], reverse=True):
        print(Fore.GREEN + f"{title}, {rating}")
    print()


def create_rating_histogram(movies):
    ratings = list(movies.values())
    if not ratings:
        print(Fore.RED + "No ratings to plot\n")
        return
    filename = input(Fore.CYAN + "Enter output filename (e.g., ratings.png): ")
    if not filename:
        print(Fore.RED + "Invalid filename\n")
        return
    plt.figure()
    plt.hist(ratings, bins=11, range=(0, 10), edgecolor="black")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.title("Movie Rating Histogram")
    try:
        plt.savefig(filename, bbox_inches="tight")
        print(Fore.GREEN + f"Histogram saved to {filename}")
    except Exception as e:
        print(Fore.RED + f"Failed to save the file: {e}\n")
    finally:
        plt.close()


def display_menu(movies):
    while True:
        print_menu()
        try:
            choice = int(input(Fore.CYAN + "Enter choice (1-9): "))
            print()
        except ValueError:
            choice = -1
        if 1 <= choice <= 9:
            if choice == 1:
                list_movies(movies)
            elif choice == 2:
                add_movie(movies)
            elif choice == 3:
                delete_movies(movies)
            elif choice == 4:
                update_movies(movies)
            elif choice == 5:
                stats(movies)
            elif choice == 6:
                random_movie(movies)
            elif choice == 7:
                search_movies(movies)
            elif choice == 8:
                movies_sorted_by_rating(movies)
            elif choice == 9:
                create_rating_histogram(movies)
            input(Fore.CYAN + "Press Enter to continue")
        else:
            print(Fore.RED + "Invalid choice\n")


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7,
    }
    display_menu(movies)


if __name__ == "__main__":
    main()
