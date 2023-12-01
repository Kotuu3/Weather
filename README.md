# Weather
Customizable weather terminal python script 
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
Then 
```bash
sudo chmod +x weather.py
sudo cp weather.py /usr/local/bin/weather
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


### Screenshot
![alt text](https://github.com/Kotuu3/Weather/blob/main/image.png?raw=true)
