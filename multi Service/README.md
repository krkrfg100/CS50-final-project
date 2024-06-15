# multi Service
#### Video Demo:  <[URL https://youtu.be/u_UD06ccJRc](https://youtu.be/Zi8GbgAwYw8?si=s78GK61T7n_sWbXA) >
#### Description:
The project is multiple services that you may need in your day in one place.
The project also contains 4 services and a log page.
Services all come 
1. to do list
2. A calculator with the ability to calculate measurements
3. Adjust sleep based on Multi-cycle sleep system or internal clock system
4. Know the weather for any region in the world
5. A page of records of the operations I performed on the site. 
Not all operations are certain. For example, the calculator does not use logs in it.



First, the basic pages
All came
1. layout.html
2. index.html
3. errors.html
4. login.html
5. register.html

layout.html 
    This is the main structure of the project that contains the Navbar before logging in 
    There is also a floating button after login that allows you to move between pages
    The floating button is taken from here https://codepen.io/RaduBratan/pen/eYJZLpN
    I modified it to suit the size of my pages and my website based on my design

index.html
    The home page in Project A is technically responsible for directing the user to the site based on the data in the session
    After logging in, it contains a service, which is the to do list

errors.html
    It is a page that displays errors instead of the flash function, because I designed this page because I cannot use the 'return'  with the flash function effectively.
    The file contains the basic structure based on the session data and a red box in which the error number or pixel font found in static is displayed.
    The error is in normal font

login.html
    A normal login page. If you enter something wrong, you will be directed to the errors page and the error will be displayed

register.html
    The registration page is normal, and if you enter something wrong, it directs you to the errors page and the error is displayed

Secondly, the services pages
All came
1. calculator.html
2. weather-news.html
3. sleep.html
4. log.html

calculator.html
    Calculator page with a simple design. I borrowed the calculator buttons from this link: https://codepen.io/ahart814/pen/yLNMZGa
    also at the bottom of the page you can calculate the conversion of measurement units
    From different units to different units

weather-news.html
    The weather page is a page to know the weather through the name of the city.
    Weather information is fetched 
    The name of the city, the name of the country, the temperature and the weather condition from the API from https://openweathermap.org/
    The picture above shows the weather condition

sleep.html
    Sleep Page is a page to determine which sleep cycle is right for you
    It consists of a title at the top and a bar that gives you the benefit of determining sleep cycles
    At the bottom is a box with a simple design that helps you determine your sleep time based on when you want to wake up and how many hours you will sleep

log.html
    The log page is a page with a simple design. There are 3 buttons. Each button directs you to the records. The service written in the button. The background design is taken from a website from the 1990s. Website link https://www.spacejam.com/1996/.

    The log page is divided into 3 pages, each of which is as follows

    1. to_do_list_log.html
    2. weather log.html
    3. sleep_log.html

    to_do_list.html
        It is a page for the to do list service records. It consists of the same style as the to do list recipe.
        The table design is taken from a YouTube video. Link to the video https://youtu.be/biI9OFH6Nmg?si=rxd_E2aTGfkaKD_x  
        I changed the time to suit the design of the to do list service

    weather_log.html
        It is a page for the weather service records. It consists of the same style as the wether recipe.
        The table design is taken from a YouTube video. Link to the video https://youtu.be/biI9OFH6Nmg?si=rxd_E2aTGfkaKD_x  
        I changed the time to suit the design of the weather service

    sleep_log.html
        It is a page for the sleep cycle service records. It consists of the same style as the sleep cycle recipe.
        The table design is taken from a YouTube video. Link to the video https://youtu.be/biI9OFH6Nmg?si=rxd_E2aTGfkaKD_x  
        I changed the time to suit the design of the sleep cycle service


There is also a helpers file
    It has an errors function
    and Dictionary contains as a value the names of the countries and the abbreviation key for the countries
    Here I used artificial intelligence chat-gbt To generate this Dictionary for use on the weather page


The last thing is database design

    The database contains 4 tables, as follows:

    1. users
    2. todos
    3. weather
    4. Sleep_cycles

    .schema

         TABLE `users` (
        `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        `username` TEXT NOT NULL,
        `password` TEXT NOT NULL
        )

        TABLE "todos" (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         user_id INTEGER NOT NULL,
          Content TEXT,
           "done" BOOLEAN,
            deleted BOOLEAN,
            Date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )


        TABLE "weather" (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        city_name TEXT,
        weather_condition TEXT,
        temperature TEXT,
        country_name TEXT,
        image TEXT,
        Query_history TIMESTAMP DEFAULT CURRENT_TIMESTAMP)

        TABLE "Sleep_cycles" (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
         Desired_wake_up_time TEXT,
        system_12_hour TEXT,
        system_24_hour TEXT,
        Query_history TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )


