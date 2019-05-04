import request

def main():
    # print the hearder
    print_the_header()
    # get zip code from user
    city_name=get_city_name_from_user()

    html_text=get_html_from_web(city_name)
    #

def print_the_header():
    print('-----------------------------------')
    print('       WEATHER CLIENT     ')
    print('-----------------------------------')
    print()

def get_city_name_from_user():
    city = input("Please enter the zip code of the City:")
    return city

def get_html_from_web(city_name):
    url = "https://www.wunderground.com/weather/in/{}".format(city_name)
    response = request.GET(url)
    return response.text

if __name__ =='__main__':
    main()