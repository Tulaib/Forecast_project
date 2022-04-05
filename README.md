# Forecast_project
the basic things you need to work on this project is to download the requirements first by running the following command 

pip install -r requirements.txt

then simply run the server by following command

python manage.py runserver

by hiting :
http://127.0.0.1:8000/index/register/
and passing the json as"
 {
    "username":"sample json",
    "email":"a@gmail.com",
    "first_name":"mas",
    "last_name":"asdasd",
    "password":"anypass",
    "password2":"anypass",
 }


by hitting:
http://127.0.0.1:8000/index/login/
and passing the json as:
{
    "email":"a@gmail.com",
    "password":"pass123"
 }
description:
it will generate you the token which will be used to autheticate which user is logged in 

by hitting :
http://127.0.0.1:8000/index/logout/ 
description:
you will be logged out

by hitting :
http://127.0.0.1:8000/index/reset_pass/
and passing the json as:
{
    "email":"a@gmail.com",
    "new_pass":"password",
    "confirm_pass":"password"
 }
description:
it will change your password
 
by hitting :
http://127.0.0.1:8000/weather_forecasts/fetch_my_location/
description:
it will tell you your exact location ,longitude , latitude , ip and city and will update your search in your table along with the time you logged in 

by hitting :
http://127.0.0.1:8000/weather_forecasts/weather_forecast_for_me/
description:
it will give you the complete weather forcast for your current location 
