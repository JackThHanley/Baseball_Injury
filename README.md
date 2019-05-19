# Baseball_Injury
## Final Project for Harvey Mudd CS35: Computer Science for Insight

### Incomplete

Over the course of my own personal baseball research experience, I've found a significant dearth of injury information. Any information out there also isn't particularly easy to work with. This repository hopes to serve as a brief synthesization of biographical, website ID, and injury information from 2015 onwards. The injuries included on this list are ones suffered by players on the big-league roster; there is information on injuries suffered by players in amateur/minor league baseball. I intend to update this information every few months or so. 

The final dataset `injury` is formatted such that each row is an injury occurence. Players may show up multiple times (multiple injuries over).

The data used to create the final dataset: `People` (removed certain columns, eventualy used edited `people1`), `master` from Crunchtime Baseball, and `sp_injury` (created from scraped Spotrac.com using the functions in the script provided).

Not sure where to begin? Possibly analyses could include:

- Creating a time-to-event variable and performing Survival Analysis/Cox PH
- Running a Logistic Regression to predict injury
- Visualize differences in injury prevalance / type across positions

This data combines information from the Lahman dataset, IDs from Crunchtime Baseball, and injury information from Spotrac.com.
The individual datasets from both the Lahman set and Crunchtime Baseballas well as the Spotrac individual team injury information can be found at the links below.


#### Lahman website: http://www.seanlahman.com/baseball-archive/statistics/
  - You can find the `People` dataset here within the Lahman database downloads
  - Lahman Creative License: https://creativecommons.org/licenses/by-sa/3.0/

#### Crunchtime Baseball: http://crunchtimebaseball.com/baseball_map.html
  - `master` dataset for player IDs and criterion for inclusion can be found at this site

#### Spotrac: https://www.spotrac.com/mlb/disabled-list/2018/cumulative-team/
  - Injury information can been found here.
