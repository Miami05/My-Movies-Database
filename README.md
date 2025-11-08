# My Movies Database

A feature-rich command-line application for managing your personal movie collection. Add ratings, search, get statistics, and visualize your movie data with an intuitive menu-driven interface featuring colored terminal output.

## 🎯 About This Project

This project demonstrates practical software engineering skills:
- **Data structure management** - Dictionary-based database for persistence
- **User interface design** - Interactive menu system with input validation
- **Data analysis** - Statistical calculations (mean, median, min, max)
- **Search algorithms** - Fuzzy matching with similarity suggestions
- **Data visualization** - Histogram generation with matplotlib
- **Error handling** - Robust exception handling throughout
- **Terminal UI** - Professional colored output with colorama

The application provides a complete CRUD (Create, Read, Update, Delete) interface for managing movie ratings and metadata.

## ✨ Features

### Core Functionality
- ✅ **List all movies** - Display entire collection with ratings
- ✅ **Add movies** - Insert new films with ratings (0-10 validation)
- ✅ **Delete movies** - Remove films from collection
- ✅ **Update ratings** - Modify existing movie ratings
- ✅ **Search movies** - Find films by partial name match

### Analytics & Insights
- ✅ **Statistics** - Average, median, best, and worst rated movies
- ✅ **Sorted view** - Movies ordered by rating (highest first)
- ✅ **Random picker** - Get a random movie recommendation
- ✅ **Histogram** - Visual rating distribution chart (saved as PNG)

### User Experience
- ✅ **Colored output** - Green for success, red for errors, cyan for menus
- ✅ **Input validation** - Validates ratings and user choices
- ✅ **Fuzzy search** - Suggests similar titles when movie not found
- ✅ **Error messages** - Clear feedback for all operations
- ✅ **Duplicate prevention** - Prevents adding same movie twice

## 📋 Requirements

Python 3.6+  
matplotlib>=3.0.0  
colorama>=0.4.3


### Installation

```bash
pip install matplotlib colorama
```

## 🚀 Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/Miami05/My-Movies-Database.git
```

```bash
cd My-Movies-Database
```


### Run the Application
```bash
python3 main.py
```


## 📖 User Guide

### Main Menu
** My Movies Database **

Menu

1.  List movies
    
2.  Add movie
    
3.  Delete movie
    
4.  Update movie
    
5.  Stats
    
6.  Random movie
    
7.  Search movie
    
8.  Movies sorted by rating
    
9.  Create Rating Histogram

### Feature Walkthroughs

#### 1. List Movies
Displays all movies in your database with their ratings.
The Shawshank Redemption, 9.5  
Pulp Fiction, 8.8  
The Room, 3.6


#### 2. Add Movie
Add a new movie with validation for ratings (0-10).
Enter a new movie name: Inception  
Enter new movie rating (0-10): 8.7  
Movie Inception successfully added


**Error handling:**
- Prevents duplicate movies
- Rejects ratings outside 0-10 range
- Handles non-numeric input gracefully

#### 3. Delete Movie
Remove a movie from your collection.
Enter movie name to delete: The Room  
Movie The Room successfully delete


#### 4. Update Movie
Modify the rating of an existing movie.
Enter movie name: Pulp Fiction  
Enter new movie rating (0-10): 9.0  
Movie Pulp Fiction successfully updated


#### 5. Statistics
Displays comprehensive analytics about your collection:
Average rating: 8.74  
Median rating: 8.85  
Best movie: The Shawshank Redemption, 9.5  
Worst movie: The Room, 3.6


Calculated metrics:
- **Average** - Mean rating across all movies
- **Median** - Middle value when ratings sorted
- **Best** - Highest rated film(s)
- **Worst** - Lowest rated film(s)

#### 6. Random Movie
Get a surprise movie recommendation.
Your movie for tonight: Forrest Gump, it's rated 8.8


#### 7. Search Movie
Find movies by partial name with fuzzy matching.

**Example 1: Exact match**
Enter part of movie name: Dark Knight  
The Dark Knight, 9.0


**Example 2: Partial match**
Enter part of movie name: godfather  
The Godfather, 9.2  
The Godfather: Part II, 9.0


**Example 3: No match with suggestions**
Enter part of movie name: Inception  
The movie "Inception" does not exist.  
Did you mean:  
Everything Everywhere All At Once


#### 8. Movies Sorted by Rating
Displays all movies ordered from highest to lowest rating.
The Shawshank Redemption, 9.5  
The Godfather, 9.2  
The Godfather: Part II, 9.0


#### 9. Create Rating Histogram
Generates a visual chart of rating distribution.
Enter output filename (e.g., ratings.png): my_ratings.png  
Histogram saved to my_ratings.png


Creates a PNG file showing:
- X-axis: Rating values (0-10)
- Y-axis: Number of movies in each rating bracket
- Title: "Movie Rating Histogram"

## 📝 Code Architecture

### Main Components

**`print_menu()`**
- Displays the main menu with all available options
- Uses colorama for formatted, colored output

**`list_movies(movies)`**
- Iterates through movie dictionary
- Displays title and rating for each movie

**`add_movie(movies)`**
- Prompts for movie name and rating
- Validates rating is between 0-10
- Checks for duplicates
- Handles non-numeric input

**`delete_movies(movies)`**
- Prompts for movie name
- Removes from dictionary
- Provides error if movie not found

**`update_movies(movies)`**
- Finds existing movie
- Updates rating with validation
- Provides feedback

**`stats(movies)`**
- Calculates average: `sum(ratings) / count`
- Calculates median: Middle value when sorted
- Finds min/max ratings
- Lists all movies with min/max ratings

**`search_movies(movies)`**
- Case-insensitive partial string matching
- Uses `difflib.get_close_matches()` for fuzzy matching
- Suggests similar titles if exact match not found

**`movies_sorted_by_rating(movies)`**
- Sorts dictionary items by rating (descending)
- Uses lambda: `key=lambda item: item[1]`

**`create_rating_histogram(movies)`**
- Creates histogram using matplotlib
- 11 bins for 0-10 range
- Saves as PNG file
- Error handling for file I/O

**`display_menu(movies)`**
- Main loop handling user input
- Routes to appropriate function based on choice
- Validates menu selections
- Continues until user exits

**`main()`**
- Initializes movie database with sample data
- Calls main menu loop

## 🔍 How It Works

### Data Structure
movies = {  
"The Shawshank Redemption": 9.5,  
"Pulp Fiction": 8.8,  
"The Room": 3.6,  
...  
}


Dictionary format allows:
- O(1) lookup by movie name
- Easy addition/deletion
- Quick value (rating) access

### Fuzzy Search Algorithm

Uses Python's `difflib.get_close_matches()`:
suggestions = difflib.get_close_matches(  
movie, # User input  
titles, # List to search  
n=5, # Max 5 suggestions  
cutoff=0.4 # 40% similarity threshold  
)


**Example:**
- User enters: "Shawshank"
- Finds: "The Shawshank Redemption" (90% similar)

### Statistics Calculation

**Median calculation:**
rating = sorted(movies.values()) # Sort ratings  
n = len(rating)  
median = rating[n // 2] if n % 2 == 1  
else (rating[n // 2 - 1] + rating[n // 2]) / 2


- Odd count: middle value
- Even count: average of two middle values

### Histogram Generation

plt.hist(ratings, bins=11, range=(0, 10))


- **bins=11**: Creates buckets [0-1), [1-2), ..., [9-10]
- **range=(0, 10)**: Covers full rating scale
- **edgecolor="black"**: Clear separation between bars

## 💡 What I Learned

Building this project reinforced:
- **Data structure selection** - Dictionaries for key-value storage
- **User interface design** - Creating intuitive menu systems
- **Input validation** - Ensuring data integrity
- **Error handling** - Graceful failures with helpful messages
- **Algorithms** - Sorting, searching, statistical calculations
- **Data visualization** - Using matplotlib for charts
- **Terminal styling** - Using colorama for professional output
- **CRUD operations** - Complete database management
- **Code organization** - Modular function design


## 📖 Code Quality

**Strengths:**
- ✅ Clean, readable code with clear function names
- ✅ Comprehensive input validation
- ✅ Colorized output for better UX
- ✅ Error handling throughout
- ✅ Modular design with single-responsibility functions
- ✅ Good use of built-in Python features
- ✅ Proper use of data structures

**Potential Improvements:**
- Could add docstrings to functions
- Could implement file persistence
- Could add more detailed error messages
- Could add configuration options
- Could optimize search for large datasets

## 🧪 Testing Scenarios

**Test 1: Add and search**
1.  Add "Dune" with rating 8.0
    
2.  Search "dune" (lowercase)
    
3.  Verify case-insensitive search works
    


 `**Test 2: Invalid input**` 

4.  Try to add movie with rating 15
    
5.  Verify rejection with error message
    

 `**Test 3: Fuzzy matching**` 

6.  Search "Shawshank"
    
7.  Verify suggestion for "The Shawshank Redemption"
    

 `**Test 4: Histogram generation**` 

8.  Create histogram
    
9.  Verify PNG file created
    
10.  Check file contains chart


## 🎬 Sample Database

The application comes pre-loaded with 10 classic films:
- The Shawshank Redemption (9.5)
- Pulp Fiction (8.8)
- The Room (3.6)
- The Godfather (9.2)
- The Godfather: Part II (9.0)
- The Dark Knight (9.0)
- 12 Angry Men (8.9)
- Everything Everywhere All At Once (8.9)
- Forrest Gump (8.8)
- Star Wars: Episode V (8.7)

## 🤝 Contributing

Contributions welcome! Ideas:
- Add more features to feature list
- Implement persistence
- Create GUI version
- Add more analysis options
- Performance optimizations

## 📄 License

This project is open source under the MIT License.

## 👤 Author

**Ledio Durmishaj**
- GitHub: [@Miami05](https://github.com/Miami05)
- Email: lediodurmishaj16@gmail.com

---
 
