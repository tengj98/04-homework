#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[1]:


import requests


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[12]:


laurl = "http://api.weatherapi.com/v1/current.json?key=29872720da6d4e50b6d231629221406&q=91754"
laresp = requests.get(laurl)
ladata = laresp.json()


# In[13]:


print(ladata)


# In[ ]:





# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[24]:


windspeed = ladata['current']['wind_kph']
currenttemp = ladata['current']['temp_c']
feelslike = ladata['current']['feelslike_c']


# In[77]:


print(f"The current windspeed is {windspeed} kph.")


# In[26]:


if currenttemp > feelslike:
    print(f"It feels {tempdiff:.1f} degrees cooler.")
elif currenttemp == feelslike:
    print(f"It feels like the same temperature.")
else:
    print(f"It feels {tempdiff:.1f} degrees warmer.")


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[89]:


forecasturl = "http://api.weatherapi.com/v1/forecast.json?key=29872720da6d4e50b6d231629221406&q=91754&days=7"
forecastresp = requests.get(forecasturl)
forecastdata = forecastresp.json()


# In[90]:


print(forecastdata)


# In[91]:


moonillu = forecastdata['forecast']['forecastday'][1]['astro']['moon_illumination']
print(f"{moonillu}% of the moon will be visible tomorrow.")


# 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[92]:


todayshigh = forecastdata['forecast']['forecastday'][0]['day']['maxtemp_c']
todayslow = forecastdata['forecast']['forecastday'][0]['day']['mintemp_c']
todaysdiff = todayshigh - todayslow
print(f"The difference between the high and low temperatures for today is {todaysdiff} degrees Celsius.")


# In[ ]:





# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# In[ ]:


# I renamed them as [city]data and forecastdata


# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[94]:


forecastdays = forecastdata['forecast']['forecastday']

for days in forecastdays:
    todayshigh = days['day']['maxtemp_c']
    if todayshigh > 27:
        print("It's hot.")
    elif todayshigh > 19:
        print("It's warm.")
    else:
        print("It's cold.")


# In[ ]:





# In[ ]:





# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[ ]:


# I'm on the free plan. 
# "Depending upon your subscription plan we provide current and 3 day air quality data for the given location in json and xml."


# In[ ]:





# In[ ]:





# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[106]:


high = 0 
for days in forecastdays:
    todayshigh = days['day']['maxtemp_c']
    if todayshigh > high:
        high = todayshigh

hottestday = ""
for hotday in forecastdays: 
    if hotday['day']['maxtemp_c'] == todayshigh:
        hottestday = days['date']

print(f"The hottest day is {hottestday} and the high will be {high} degrees Celsius.")


# In[ ]:





# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[ ]:





# In[ ]:





# In[ ]:





# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[108]:


miami = "http://api.weatherapi.com/v1/forecast.json?key=29872720da6d4e50b6d231629221406&q=Miami&days=1"
miamiresp = requests.get(miami)
miamidata = miamiresp.json()

print(miamidata['forecast']['forecastday'][0]['hour'][0]['temp_f'])


# In[145]:


miamiday = miamidata['forecast']['forecastday']
count = 0
hourcount = 0

for time in miamiday: 
    for temperature in time['hour']: 
        if temperature['temp_f'] > 85: 
            count = count + 1

percent = count/24*100            
print(f"It is above 85 degrees {percent:.0f}% of the time.")


# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# In[ ]:


# $4/month
# https://www.weatherapi.com/pricing.aspx


# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# In[ ]:


# Make a second account / use a different API key

