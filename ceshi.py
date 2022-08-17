from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver  # 从selenium库中调用webdriver模块
import time  # 调用time模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()


driver.get('https://www.shanghairanking.cn/rankings/bcmr/2022/030101K')  # 访问页面

driver.maximize_window()
time.sleep(2)  # 暂停两秒，等待浏览器缓冲



def enter():
    # 点击登录按钮
    demo = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[3]/button')
    time.sleep(3)
    ActionChains(driver).move_to_element(demo).perform()
    demo.click()
    # 登录账号密码
    username = driver.find_element(By.ID, 'phoneInput')
    username.send_keys('17843091491')
    # 获取短信验证码
    driver.find_element(By.XPATH, '//*[@id="smsCodeBtn"]').click()
    key_dx = str(input('请输入验证码：'))
    code = driver.find_element(By.XPATH, '//*[@id="smsCodeInput"]')
    code.send_keys(key_dx)
    # 点击登录
    driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()

enter()

# 点击下一页
# 取该专业有多少页
time.sleep(5)
school_name_end = []
school_rank_end = []
school_code_end = []
major_name_end = []
lis = driver.find_elements(By.XPATH, '//*[@id="content-box"]/ul/li[*]')
lis_text = lis[-3].text
num = len(lis)
major_name = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[1]/div[1]/div[2]').text
# 本页有多少个学校需要循环
school_name_num = len(driver.find_elements(By.XPATH,'//*[@id="content-box"]/div[2]/div/div[2]/div[*]/div[*]/div[3]/div[2]/div/div/div/a'))
# 循环该页的所有学校，存储学校名称、排名、总分
for k in range(school_name_num):
    # 学校名称
    school_name = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
        k + 1) + ']/div[*]/div[3]/div[2]/div/div/div/a').text
    # 学校排名
    school_rank = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
        k + 1) + ']/div[*]/div[2]/div').text
    # 学校总分
    school_code = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
        k + 1) + ']/div[*]/div[5]').text
    # 添加到列表中
    school_name_end.append(school_name)
    school_rank_end.append(school_rank)
    school_code_end.append(school_code)
    major_name_end.append(major_name)

for next in range(int(lis_text)):
    # 如果有好几页，则点击下一页，如果没有则返回上一页
    if driver.find_element(By.XPATH, '//*[@id="content-box"]/ul/li[*]/a'):
        # 倒数第三个“li”标签的文本是数量
        driver.find_element(By.XPATH, '//*[@id="content-box"]/ul/li[{}]'.format(num - 1)).click()
        lis = driver.find_elements(By.XPATH, '//*[@id="content-box"]/ul/li[*]')
        num = len(lis)
        time.sleep(4)
        school_name_num = len(driver.find_elements(By.XPATH,
                                                   '//*[@id="content-box"]/div[2]/div/div[2]/div[*]/div[*]/div[3]/div[2]/div/div/div/a'))
        # 循环该页的所有学校，存储学校名称、排名、总分
        for k in range(school_name_num):
            # 学校名称
            school_name = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                k + 1) + ']/div[*]/div[3]/div[2]/div/div/div/a').text
            # 学校排名
            school_rank = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                k + 1) + ']/div[*]/div[2]/div').text
            # 学校总分
            school_code = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                k + 1) + ']/div[*]/div[5]').text
            # 添加到列表中
            school_name_end.append(school_name)
            school_rank_end.append(school_rank)
            school_code_end.append(school_code)
            major_name_end.append(major_name)

    else:
        driver.back()
print(school_name_end)
print(school_rank_end)
print(school_code_end)
print(major_name_end)
# 单击下一页按钮


# # 定义存储列表
# school_name_end = []
# school_rank_end = []
# school_code_end = []
# major_name_end = []
# # 专业名称
# major_name = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[1]/div[1]/div[2]').text
# # 本页有多少个学校需要循环
# school_name_num = len(driver.find_elements(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[*]/div[*]/div[3]/div[2]/div/div/div/a'))
# # 循环该页的所有学校，存储学校名称、排名、总分
# for k in range(school_name_num):
#     # 学校名称
#     school_name = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
#         k + 1) + ']/div[*]/div[3]/div[2]/div/div/div/a').text
#     # 学校排名
#     school_rank = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
#         k + 1) + ']/div[*]/div[2]/div').text
#     # 学校总分
#     school_code = driver.find_element(By.XPATH, '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
#         k + 1) + ']/div[*]/div[5]').text
#     # 添加到列表中
#     school_name_end.append(school_name)
#     school_rank_end.append(school_rank)
#     school_code_end.append(school_code)
#     major_name_end.append(major_name)
# print(school_name_end)
# print(school_rank_end)
# print(school_code_end)
# print(major_name_end)