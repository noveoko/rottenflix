# RottenFlix
See the top movies on Netflix by Rottentomato.com score

## How it works
This is an in-progress script so it requires quite a few manual steps (these will be automated soon!)

1. Log in to Netflix.com
2. Click on `movies`
3. Press and hold the `pg dn` button on your keyboard until no more movie are loaded  
4. Press `CTRL+SHIFT+i` on your keyboard to launch the Chrome toolbar
5. In the Chrome toolbar under the `Elements` tab right-click on `<html lang="en-PL">`
6. Select `copy` then `copy-element`
7. Open the file `netflix.html` and paste data from step 6
8. save the file
9. Visit `https://www.rottentomatoes.com/browse/cf-dvd-streaming-all?services=netflix_iw&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release`
10. Click the button `Show More` until no more data is loaded
11. Repeat steps 4-6
12. Open the file `rotten.html` and paste the data collected in the previous step
13. Save the file
14. Open a terminal window
15. In the terminal window type `python netrot.py`
16. View your top movies by opening the file `top_movies_today.txt`
