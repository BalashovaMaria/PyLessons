rain = input('идет дождь?')
rain = str.lower(rain)
if rain == 'yes':
    wind = input('сейчас ветрено?')
    wind = str.lower(wind)
    if wind == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
