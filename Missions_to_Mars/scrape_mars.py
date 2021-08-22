
# [<title>News - Mars Exploration Program</title>]
import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = "https://redplanetscience.com/"
    browser.visit(url)



    mars_pg = browser.html
    soup = BeautifulSoup(mars_pg, 'html.parser')


    soup



    road_trip=soup.find_all("div",class_  = "content_title")[0].text
    road_trip



    road_trip_log=soup.find_all("div",class_  = "article_teaser_body")[0].text
    road_trip_log


# JPL MARS SPACE IMAGES
    url = "https://spaceimages-mars.com/"
    browser.visit(url)



    selfie=browser.links.find_by_partial_text("FULL IMAGE")
    selfie.click()



    images=browser.html
    soup_pic = BeautifulSoup(images, 'html.parser')



#get image source
    image_url=soup_pic.find("img", class_="headerimage fade-in")["src"]
    image_url



#get image url
    featured_image_url=f"https://spaceimages-mars.com/{image_url}"
    print(featured_image_url)


# Mars facts
    mars_facts=pd.read_html("https://galaxyfacts-mars.com/")[0]
    print(mars_facts)



    mars_facts.columns=["Info","Mars","Earth"]
    mars_facts.set_index("Info",inplace=True)
    mars_facts=mars_facts.iloc[1:7]
    mars_facts


# Mars Hemispheres
    url = "https://marshemispheres.com/"
    browser.visit(url)



    hemispheres = []
    items = browser.find_by_tag('h3')
#for the length of all items in loop
    items_length = len(items)
    items[0].click()
    for item in range(items_length): 
        diff_hemispheres = {}
        browser.find_by_tag("h3")[item].click()
        images=browser.html
        hemisphere_pic = BeautifulSoup(images, 'html.parser')
        title=hemisphere_pic.find("h2", class_="title").text
        diff_hemispheres["title"]=title
        figure=hemisphere_pic.find("img", class_="thumb")["src"]
        diff_hemispheres["image_url"]=url + figure 
        hemispheres.append(diff_hemispheres)
        browser.back()




    hemispheres




    browser.quit()







