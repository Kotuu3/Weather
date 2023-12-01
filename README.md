# Weather
Customizable weather terminal python script 

### OpenWeatherMap api is needed 
To obtain it you need to make account on https://openweathermap.org/
Then you need to head to https://home.openweathermap.org/api_keys
And generate API key


### Installation
Clone git repo
```bash
git clone https://github.com/Kotuu3/Weather.gits
cd Weather
```
IMPORTANT - Edit python file and change variables

```py
api_key = "Your api key"

#for example: city = "Warsaw,PL"
city = "City,COUNTRY"

lang = "en"

```
Also you can change displayed text on the bottom 

```py
#Custom messages showed under forecast
messages = [
    "Stay Hydrated!",
    "Hey! What's up? :3",
    "Have a good day!"
]
```


Then 
```bash
sudo chmod +x weather.py
sudo cp weather.py /usr/local/bin/weather
```
### Usage
Simply type ```weather``` in terminal for this to work!

### Screenshot
![alt text](https://github.com/Kotuu3/Weather/blob/main/image.png?raw=true)

