# Cyber Gladiators
## API endpoints

---------


### /announcements

------------------

/announcements/add (POST) Data('title', 'body')


/announcements/delete/$id (DELETE) (Pass in announcement id into the url)


/announcements/view/$id


/announcements/edit/$id (POST) Data("title","body")



--------------------


### /auth

/auth/register (POST) Data("first-name", "last-name", "email","password")


/auth/register/activate (PATCH) Data("secondary-email", "id"


/auth/login (POST) Data("email","password")


/auth/logout (GET) 

---------------------


### /events


/events/add(POST) Data("event-title","date-start","date-end","time-start","time-end","location")


/events/all (GET)


/events/view/$id (GET) Data("event id in url") 


/events/delete/$id (DELETE) 


