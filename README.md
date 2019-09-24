# Baseball_Injury
## Final Project for Harvey Mudd CS35: Computer Science for Insight


Over the course of my own personal baseball research experience, I've found a significant dearth of injury information. Any information out there also isn't particularly easy to work with. This repository hopes to serve as a brief synthesization of biographical, website ID, and injury information from 2015 onwards. The injuries included on this list are ones suffered by players on the big-league roster; there is no information (at least on Spotrac) on injuries suffered by players in amateur/minor league baseball. 

An example final dataset that you can create using the script is included in the repo with the file name `injury_df`. The script is automatically formatted to scrape from 2015-2019, but this can easily be changed (line 144). The dataset is formatted such that each row is an injury occurence, and includes information ranging from type of injury, how long they spent on the IL, and Spotrac's estimation of how much money they accumulated while injured. 

## Issues / Other Info
As of now, though, there are several aspects to keep in mind. For starters, players may show up multiple times (multiple injuries over the course of one season). Additionnally, there currently is an error where injuries will be double counted if a player was traded midseason.

Also included at the end of the script is the code necessary to synthesize and combine your dataframes, as well as export your dataframes to CSV files. These sections are commented out, and are included with the intention of a user changing them. On my machine, I tend to run the script in an IPython shell in Visual Studio code.

Data necessary to run script:
- `People`, `people1` from the Lahman dataset (`people1` is `People` with some columns removed... both are included)
  + Biographical information 
- `master` from Crunchtime Baseball
  + Player ID information
- `teams`
  + Reference dataframe for full team names and their abbreviations
  
## Downstream Goals
  - Latent updating of `master`, `People`
  - Fixing double-counting error
  - Repeated updating of scraping Spotrac
  - Use of Fangraphs and Baseball Reference IDs to scrape statistics / combine with injury data
 
## Possible Uses
Not sure where to begin? Possibly analyses could include:

- Creating a time-to-event variable and performing Survival Analysis/Cox PH
- Running a Logistic Regression to predict injury
- Visualize differences in injury prevalance / type across positions

## Resources

All of the websites and resources I am accessing are tremendous resources and are worth exploring on their own. The individual datasets from both the Lahman set and Crunchtime Baseball as well as the Spotrac individual team injury information can be found at the links below.


#### Lahman website: http://www.seanlahman.com/baseball-archive/statistics/
  - You can find the `People` dataset here within the Lahman database downloads
  - Lahman Creative License: https://creativecommons.org/licenses/by-sa/3.0/

#### Crunchtime Baseball: http://crunchtimebaseball.com/baseball_map.html
  - `master` dataset for player IDs and criterion for inclusion can be found at this site

#### Spotrac: https://www.spotrac.com/mlb/disabled-list/2019/cumulative-team/
  - Injury information can been found here.
  
 ## Contact
 
 If you have any questions or concerns, feel free to contact my at jackthhanley@gmail.com
