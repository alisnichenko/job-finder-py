from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from utilities.output import info

def selenium_script(url: str) -> str:
    """
    A very specific method to press buttons and get the source code of the page.
    I couldn't use requests or urllib, because some of the website have
    strong security against spiders/bots and I couldn't bypass it.
    
    Args:
        url: the url of the specific website to be used.
    Returns:
        the source code as a string of the page with some modifications.
    """
    info("i", "Started specific_selenium_script()...")
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()

    wait = WebDriverWait(driver, 100000)
    temp = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "raised")))
    sort_by_money_btn = driver.find_elements_by_class_name('raised')[0]

    actions = ActionChains(driver)
    actions.move_to_element(sort_by_money_btn)
    actions.click().perform()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    temp = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "more")))

    try:
        for i in range(20):
            actions = ActionChains(driver)
            actions.move_to_element(temp)
            actions.click().perform()
            info("i", "Showing more. Clicked " +  str(i) + " times...")
            driver.execute_script("arguments[0].scrollIntoView();", temp)
            temp = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "more")))
    except:
        src = driver.page_source
    
    driver.close()
    return src
