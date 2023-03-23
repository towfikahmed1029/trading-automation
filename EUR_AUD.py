gmail = 'sorifultowfik404@gmail.com'
passwd = 'gmail.com'
#signal_length = 5 , 6, 10+   { line number 90 } 
save_file = "EUR_AUD.text"
print("EUR_AUD >> 5, 6, 10+")


from datetime import datetime
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
driver = uc.Chrome(
    driver_executable_path='chromedriver.exe', use_subprocess=True)
time.sleep(2)
login_url = 'https://www.olymptrade.com/login'
driver.get(login_url)
input("Press Enter to continue After Loading Complete...")
login = driver.find_element(By.XPATH, '//span[text()="Login"]//parent::span//parent::span//parent::div//parent::button').click()
time.sleep(2)
driver.find_element(By.XPATH, ' //input[@name = "email"]').send_keys(gmail)
driver.find_element(By.XPATH, ' //input[@name = "password"]').send_keys(passwd)
input("Press Enter to continue After Login Complete...")
driver.find_element(By.XPATH, '//button[@data-test="signals-menu"]').click()
input("Press Enter to continue After Login SuccessFull...")
print("Success Fully Running")
def add_count(count_len,up_down):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open(save_file, "a") as f:
        f.write(f"{count_len} time>> {current_time} trade>> {up_down}\n")

def trade_click(trade_up_down):
    print("trade_click")
    if 'down' in trade_up_down:
        driver.find_element(By.XPATH,('//button[@data-test="deal-button-down"]')).click()
    elif 'up' in trade_up_down:
        driver.find_element(By.XPATH,('//button[@data-test="deal-button-up"]')).click()
    print(trade_up_down)

def time_select(trade_time,trade_up_down):
    input_tag = driver.find_element(By.XPATH,('//input[@data-test="deal-duration-input"]'))
    value = input_tag.get_attribute("value").split(' ')[0]
    value =int(value)
    if value == trade_time :
        trade_click(trade_up_down)
    elif value < trade_time:
        trade_time = trade_time - value
        for x in range(0, trade_time):
            driver.find_element(By.XPATH,('(//button[@data-test="deal-form-input-controls-plus"])[2]')).click()
        trade_click(trade_up_down)
    elif value > trade_time:
        trade_time = value - trade_time
        for x in range(0, trade_time):
            driver.find_element(By.XPATH,('(//button[@data-test="deal-form-input-controls-minus"])[2]')).click()
        trade_click(trade_up_down) 

while True:
    try:
        soup = BeautifulSoup(driver.page_source,'html.parser')
        find_1 = soup.find(class_ = 'nQfrSgmi').parent
        find_2 = find_1.findAll(class_="KXZ_4YGY")
    except Exception as e:
        continue
    signal_list_1_min = []
    signal_list_3_min = []
    signal_list_5_min = []

    if len(find_2) == 2:
        signal = find_2[0].findAll(attrs={"data-trans" : "trading_signals_advice"})
        for x in signal:
            signal_txt = x.text
            if "1" in signal_txt:
                signal_list_1_min.append(signal_txt)
            elif "3" in signal_txt:
                signal_list_3_min.append(signal_txt)
            else:
                signal_list_5_min.append(signal_txt)
    else:
        continue

    signal_check = []
    all_signal_list = [signal_list_1_min,signal_list_3_min,signal_list_5_min]
    for x in all_signal_list:
        if len(x) == 5 or len(x) == 6 or len(x) >= 10:
            signal_check.append(x[0])
            count_len = len(x)
            up_down = x[0]
            add_count(count_len,up_down)
            
    click_count = 0
    for x in signal_check:
        print("\nSignal Found")
        
        trade_time = x.split(" ")[0]
        trade_time = int(trade_time)
        trade_up_down = x.split(" ")[2]
        time_select(trade_time,trade_up_down)
        click_count +=1
        if click_count >= 1:
            time.sleep(35)
            break
    continue
        
    
