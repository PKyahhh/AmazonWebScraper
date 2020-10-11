#pip install selenium
from selenium import webdriver

#Takes input of the chromedriver path, The name of the item you are searching for, and wether you want to print all of the products found
def input(path, searchval, printv):
    get(path, searchval, printv) #Piping data into other function

#Uses the path to create the driver in order for web manipulation and then pipes data
def get(path, searchval, printv):
    driver = webdriver.Chrome(path)
    driver.get('https://amazon.com')
    searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    searchbox.send_keys(searchval)
    searchbutton = driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input')
    searchbutton.click()
    products(driver, printv)   

#Actually scrapes the site for the product's name, price, and link
def products(driver, printv):
    counter = 0
    global productname #Allows for later use between different functions
    global prices
    global links
    productname = []
    prices = []
    links = []
    #We actually begin to scrape each of the products here
    for element in driver.find_elements_by_xpath('//div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a'):
        name = driver.find_elements_by_tag_name('h2')[counter].text
        price = driver.find_elements_by_class_name('a-price')[counter].text
        link = driver.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
        counter += 1
        productname.append(name)
        prices.append(price)
        links.append(link)
        if (printv != False): #In case you don't want it to print all of the products
            print("\nName: " + name + "\n" + "Price: " + str(price) + "\n" + "Link: " + link)

#This allows user to access list with all of the product names
def productnames():
    return productname

#This allows the user to access the list with all of the prices
def productprices():
    return prices

#This allows the user to access the list with all of the links
def productlinks():
    return links
