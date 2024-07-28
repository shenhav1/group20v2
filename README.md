# group20v2
##  323108621, 209307115
### Part C
#### A brief explanation of our website Happy Soul:
Our website allows the user to schedule mental and physical treatments according to his needs and desires, and to be monitored after the treatments he performed. The site allows the user to rate the treatments that have taken place in the past and search for additional treatments that are relevant to him.

#### Actions:
After the user registers and connects to the site, he can perform several different actions:
- The user can make an appointment with a therapist, the sequence is:
1. The user fills in his preferences for handling the search page.
2. The site filters the results for the user, and displays the relevant therapists.
3. The user chooses a therapist and treatment and submits a request for an appointment at the desired time.
- The user can view his personal profile - can view received messages, a list of future treatments and access his treatment history page.
- The user can rate treatments that took place according to several categories.
- The user can send a request to the site team.
The project is organized in a structured folder hierarchy. The structure includes separate folders for java, html, css and python files for each page.

The site connects to a MONGO database (has functions in the MONGODB.PY file). The functions perform all the validations in the DB according to the user input.

Customer routing requests:
The application includes functions to handle requests coming from the client. When a user registers on the site, if he does not yet exist in the system, his personal information is saved in the site's database. Every prescribed treatment, request sent, details of therapists and messages received are also saved in the database and the user can view these details at any given moment. 

The HTML pages of the application were converted to templates as learned in class by blocks. In addition, on the relevant pages (for example userProfile.html), functions were written in blocks that are relevant for displaying output on the HTML page (functions that use the DB).

#### ScreenShots:
![img_7.png](img_7.png)