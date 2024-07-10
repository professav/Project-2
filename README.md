# TEAM APOLLO
![GameMatch](https://github.com/professav/Project-2/assets/162828309/63e89a09-c66d-4b93-8704-de9a4aa2243c)

# Project 2 Overview
Team Apollo is currently conducting data model implementation, optimization, and GitHub documentation. We have considered a videogame recommendation system via the Gamespot and Steam platforms.


## Roster List
Team Apollo includes:
- Timothy Heidcamp
- Duane Anglin 
- Aniel Rios 
- Vanessa Wright 
- Daniyar Temirkhanov 
- Riley (Josephine) Robideau


## Purpose
The primary purpose of this project is to provide the next generation of gamers with the optimal online experience, we are introducing a cutting-edge personalized recommendation system that tailors game suggestions based on users' individual preferences and comprehensive game reviews. By implementing a sophisticated system utilizing the K-Nearest Neighbor (KNN) algorithm, we ensure that gamers receive highly relevant and accurate recommendations, streamlining their game discovery process. This advanced algorithm analyzes various data points to identify patterns and similarities among users, delivering personalized game suggestions that match their unique tastes and interests. By minimizing the trial-and-error, gamers can now lead their new online adventure with less time, energy, and money wasted on games they may not like.


## Goals & Problems Solved

- To provide the next generation of gamers with the ultimate online experience, we are committed to minimizing wasted time, energy, and money. 
- To design a **FREE** recommendation system that optimizes the search for game options from a vast library of games.
- Our platform features intuitive interfaces that simplify searching gaming options based on classification and affordability. 
- Our system is designed to be quick, easy, and effective.


## Process
### Data Collection and Cleanup
- In our first attempt to collect data, we used Steam. Some of us were not able to download a set of games. Also, all of our team members have varying operating systems (PC/Mac), which affected data collection for our project.
- For our next attempt, we gathered a dataset from Kaggle, but unfortunately, the dataset was not large enough for data manipulation, with only 14 entries.

### Cleanup
- We reviewed value counts, displayed recommended value counts, and weighed value counts to verify whether the data was sufficient.
- To clean up the initial data, we;
    - Merged all data on review ID
    - Filtered the main data frame on ID, app name, and recommendation (True/False)
    - Converted DataFrame to CSV
    - Dropped duplicates
    - Grouped rating count by app name and whether or not it was recommended as a good game
    - Displayed rating count
    - Filtered rating count for all ratings that were greater than 2
    - Made game_pivot, used pivot function for game data : index = app name, columns = Author ID, made values = recommendation
    - Filled the NA values for the game_pivot table with 0

### Exploration Process
 After exploring several datasets regarding reviews from varied and distinct gaming websites, the final decision was...
- Ask
- Tim
- for
- his
- summary
- on
- this.

### Recreate System
To achieve your objective, implement the following strategy with the tools provided:

	1. Clean and organize your data
 	2. Apply a pivot table using the pandas package
	2. Apply a sparse matrix to the data using spicy.sparse
	3. Fit your data into a KNN model
	4. Vectorize your inputs and determine likely matches using NumPy

*You are now ready to suggest with confidence the likely matches for a user given a set of games they like.*

From the app folder, run:

	fastapi dev .\main.py

![FastAPI](https://github.com/professav/Project-2/assets/163040617/4eeda4ee-fdde-479d-99b8-2463f8820ab9)

### Tools Used
- Final Cut Pro (Movie and film editing software)
- Adobe Photoshop (Image editing)
- Runway (AI editor and generator)
- Fotor (AI photo generator)
- Narakeet (AI Voiceovers)
- Pandas (Used for manipulation of all arrays and matrices)
- SciPy (Used for scientific and technical computing, as well as optimization, statistics, linear algebra, etc.)
- SciPy Sparse (A submodule of SciPy, used for sparse matrices *(a matrix in which most elements are zeros)*)
- SciPy Sparse (CSR matrix: A class within SciPy Sparse, used for CSR *(Compressed Sparse Row)*, which is a common format for sparse matrices and allows for various methods of efficiency within this format)
- NumPy (Used for scientific computing and provides support for arrays, mathematics, etc.)
- Sklearn (Used for Machine Learning)
- Sklearn.neighbors (A submodule of scikit-learn *(sklearn)* used for identifying nearest neighbors and includes methods for classification, regression, and clustering)
- Sklearn.neighbors (NearestNeighbor: A class within Sklearn.neighbors used to find K nearest neighbor)

### Visuals/Fast API

![image](https://github.com/professav/Project-2/assets/163040617/ecd9b408-aadb-4912-9f84-1072754b7437)


<hr>
	
## Summary
Team Apollo's project aimed to create a robust recommendation system for video games, leveraging data from various sources and employing advanced data processing techniques. Despite facing various challenges, we successfully implemented a system that can provide personalized game recommendations. By utilizing tools and resources, we ensured that our methodology was both efficient and effective.
We believe that this recommendation system can be a valuable tool for gamers looking to discover new games based on their preferences and past reviews. We look forward to further refining and expanding the system in future iterations.
<br>

## Problems Encountered
> - One significant challenge was the limited access to Steam's API keys due to the team's small Steam libraries. This limitation hindered our ability to download games and fully utilize Steam's API for data collection.
> - Hesitancy to use game spot
> - There was some hesitation within the team regarding the use of Game Spot due to its relatively small number of reviewers. This concern was based on the potential lack of diversity in the reviews, which could impact the accuracy of our recommendation system.
> - Finding new data, after concluding ours needed a larger scale
<br>

## Future Considerations
> - Explore different data options, and assess possible challenges before committing to a resource.
> - Troubleshoot every issue for every team member before continuing the project, to ensure there are no serious roadblocks for anyone that could lead to needing a new source.
> - Look at the extend of the data we have, and think ahead to possible challenges rated to data availability that could potentially be avoided with further exploration early on.
> - Research similar objectives done by other people or companies (if possible) to think about the challenges they faced along the way, if they were easily avoidable, and if we can do anything to better avoid challenges by strategic planning.
> - Think more about how to best distribute work to team members, and how we can all best contribute during team meetings without being disruptive to any individual, or smaller group within the team. 
> - Two breakout rooms for our team (including moments of coming back together in one breakout room to get all updates) seemed to work best, since the whole team did not need to contribute to the syntax, and a smaller group within our team could be in another breakout room working on another task or troubleshooting an issue, helping the team stay as efficient as possible.
<br>

<hr>


## Resources
- [Game Reviews Dataset by Shashank Kalanithi](https://www.kaggle.com/datasets/sridharstreaks/game-reviews-dataset/data)
- [Jared's Recommedation System Data Analysis](https://github.com/Jmp13033/reccomendation_system/tree/master/app/helpers)
- [Runway](https://app.runwayml.com)
- [Fotor](https://www.fotor.com)
- [Narakeet](https://www.narakeet.com)
- [Final Cut Pro](https://www.apple.com/final-cut-pro/) 
- [Adobe Photoshop](https://www.adobe.com/products/photoshop/landpa.html?gclid=CjwKCAjwnK60BhA9EiwAmpHZw6BSusCcXE6LUb_ohdht07UVhbxYpBynGabLDEu4H94mWq3J0_93LRoCbv8QAvD_BwE&sdid=NC5FRF5H&mv=search&mv2=paidsearch&ef_id=CjwKCAjwnK60BhA9EiwAmpHZw6BSusCcXE6LUb_ohdht07UVhbxYpBynGabLDEu4H94mWq3J0_93LRoCbv8QAvD_BwE:G:s&s_kwcid=AL!3085!3!697384330723!e!!g!!adobe%20photoshop!1712238394!67643541820&mv=search&gad_source=1)
