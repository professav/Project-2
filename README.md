# TEAM APOLLO
![GameMatch](https://github.com/professav/Project-2/assets/162828309/63e89a09-c66d-4b93-8704-de9a4aa2243c)

# Project 2 Overview
Team Apollo is currently conducting data model implementation, optimization and GitHub documentation. We have considered a videogame recommendation system via the Gamespot and Steam platforms.

## Roster List
Team Apollo includes..
- Timothy Heidcamp
- Duane Anglin 
- Aniel Rios 
- Vanessa Wright 
- Daniyar Temirkhanov 
- Riley (Josephine) Robideau

## Purpose
The purpose of our project purpose is to…
- Provide users with a stress-free approach to finding their next best game.
- Provide users with a game recommendations system using the K-Nearest Neighbor algorithm.
- Give the next generation of gamers the optimal online experience.
- Provide users and developers with a recommendation system based on game reviews and the users' input, consisting of their top favorite games.
- Give the next generation of gamers the optimal online experience, by providing a personalized recommendation system that is based on the users' preferences and game reviews. With this, gamers can now lead their new online adventure with less time, energy, and money wasted on games the user may not like.



## Goals; Problem Solved 
Our goals and the problem that could be solved would be....
- To provide the next generation of gamers with the ultimate online experience, we are committed to minimizing wasted time, energy, and money. 
- To design a **FREE** recommendation system that optimizes the search for game options from a vast library of games.
- Our platform features intuitive interfaces that simplify searching gaming options based on classification and affordability. 
- Our system is designed to be quick, easy, and effective.

## Data Collection; Cleanup; Exploration Process
- In our first attempt to collect data, we used Steam, some of us were not able to download a set of games. Also, all of our team members have varying operating systems (PC/Mac) which affected data collection from Steam.
- For our next attempt, we gathered a dataset from Kaggle, but unfortunately, the dataset was not large enough for data manipulation, with only 14 entries.
  - We reviewed value counts, displayed recommended value counts, and weighed value counts to verify whether data was sufficient.
  - To clean up the initial data, we ...
    - Merged all data on review ID
    - Filtered the main data frame on ID, app name, and recommendation (True/False)
    - Converted DataFrame to CSV
    - Dropped duplicates
    - Grouped rating count by app name and whether or not it was recommended as a good game
    - Displayed rating count
    - Filtered rating count for all ratings that were greater than 2
    -  Made game_pivot, used pivot function for game data : index = app name, columns = Author ID, made values = recommendation
    -  Filled the NA values for the game_pivot table with 0

## DATA C, C, & E SUMMARY :
First, we explored Kaggle for our ideal dataset, and found what we were looking for from a steam video game review DF. From there, we imported our data and took necessary steps to confirm our data had everything we needed to be an optimal recommendation system. Initially, our data was downloaded as 4 different DataFrames, so we merged all on the review ID column to get our main DF. Next, we filtered our data based our 3 most important columns (ID, app name, and recommendation), and converted our main filtered DF to a CSV. We then grouped by rating count, and whether or not it was deemed as a good game. For simplicity, we also used the pivot function to make our index = app name, columns = ID, and values = recommendation. Lastly, to make our data complete, we filled all NA values with 0, so there is zero interruption to the recommendation system, without losing valuable data.
! QUESTION :  Why did we drop duplicates after converting main DataFrame to CSV?

APPROACH TAKEN TO ACHIEVE GOALS & TOOLS USED TO DO SO
	IV.A. Pandas - Used for manipulation of all arrays and matrices
	IV.B. SciPy - Used for scientific and technical computing, as well as optimization, statistics, linear algebra, etc.
	IV.B.1. SciPy Sparce - A submodule of SciPy, used for sparce matrices (a matrix in which most elements are zeros)
	IV.B.1.a) SciPy Sparce - CSR matrix - A class within SciPy Sparce, used for CSR (Compressed Sparce Row), which is a common format for sparce matrices, and allows for various methods of efficiency within this format
	IV.C. NumPy - Used for scientific computing, and provides support for arrays, mathematics, and more
	IV.D. Sklearn - Used for Machine Learning
	IV.D.1. Sklearn.neighbors - A submodule of scikit-learn (sklearn) used for identifying nearest neighbors, and includes methods for classification, regression, and clustering
	IV.D.1.a) Sklearn.neighbors - NearestNeighbor - A class within Sklearn.neighbors used to find K nearest neighbor
5-7 : SUMMARY OF RESULTS WITH VISUAL : WAITING FOR OUR METRICS SINCE WE HAVE NO VISUALS
	OVERALL SUMMARY & OVERVIEW : 
Team Apollo's project aimed to create a robust recommendation system for video games, leveraging data from various sources and employing advanced data processing techniques. Despite facing various challenges, we successfully implemented a system that can provide personalized game recommendations. By utilizing tools and resources, we ensured that our methodology was both efficient and effective.
We believe that this recommendation system can be a valuable tool for gamers looking to discover new games based on their preferences and past reviews. We look forward to further refining and expanding the system in future iterations.
PROBLEMS ENCOUNTERED
	VI.A. Limited steam access
	VI.A.1. One significant challenge was the limited access to Steam's API keys due to the team's small Steam libraries. This limitation hindered our ability to download games and fully utilize Steam's API for data collection.
	VI.B. Hesitancy to use game spot
	VI.B.1. There was some hesitation within the team regarding the use of Game Spot due to its relatively small number of reviewers. This concern was based on the potential lack of diversity in the reviews, which could impact the accuracy of our recommendation system.
	VI.C. Finding new data, after concluding ours needed a larger scale 
	VI.C.1. Ask Tim for his summary on this.
FUTURE CONSIDERATIONS
	VII.A. Explore different data options, and assess possible challenges before committing to a resource.
	VII.B. Troubleshoot every issue for every team member before continuing the project, to ensure there are no serious roadblocks for anyone that could lead to needing a new source.
	VII.C. Look at the extend of the data we have, and think ahead to possible challenges rated to data availability that could potentially be avoided with further exploration early on.
	VII.D. Research similar objectives done by other people or companies (if possible) to think about the challenges they faced along the way, if they were easily avoidable, and if we can do anything to better avoid challenges by strategic planning.
	VII.E. Think more about how to best distribute work to team members, and how we can all best contribute during team meetings without being disruptive to any individual, or smaller group within the team. 
	VII.E.1. Two breakout rooms for our team (including moments of coming back together in one breakout room to get all updates) seemed to work best, since the whole team did not need to contribute to the syntax, and a smaller group within our team could be in another breakout room working on another task or troubleshooting an issue, helping the team stay as efficient as possible.
TEAM QUESTIONS (YET TO BE ANSWERED):
Is there anything that needs to be added (besides things already noted in red)
Were there any challenges we faced that we did not yet recognize on this log? …Vanessa?
Does anyone have anything to add for future considerations?
Can everyone download and edit this doc without any issues? - If not message me
Does everyone agree with my highlighted suggestions for the first two sections of this doc? (Project purpose & Goals / Problem to be solved)
Are we able to combine the answer for those two (Project purpose & Goals / Problem to be solved), or does it need to be a separate answer for both? Would we be docked points for using one answer for both questions, even though it would answer both questions?
What are our metrics, and how do we incorporate them? …Revati?
Do we need a further explanation on how the recommendation system actually works? (Syntactically) ….Tim? ….Jared?
Should we have converted the CSV after we dropped the duplicates? Can we still do that? Does it make a big enough difference to take the time to do so?
Tim : Can you give us a summary for the challenge encountered relating to starting over with fresh data?
Aniel : Any suggestions for the doc? Is there anything that needs to be clarified, or is confusing when reading through? - Also, can we get a separate doc strictly for the readme?
Does the Data c, c, & e summary need to be better/more in depth?
Any suggestions or thoughts?


Video made by Duane included high-quality graphics, reducing the frustration of lag and glitches 

[**Click this link to Summmary Doc** (Will delete this from our repo before project submission)**](https://docs.google.com/document/d/1_uuymdDroABmK8becVYevVApo8j1_2vc_oRuBR6Cp7w/edit)

# References
- [Game Reviews Dataset by Shashank Kalanithi](https://www.kaggle.com/datasets/sridharstreaks/game-reviews-dataset/data)
- [Jared's Recommedation System Data Analysis](https://github.com/Jmp13033/reccomendation_system/tree/master/app/helpers)
