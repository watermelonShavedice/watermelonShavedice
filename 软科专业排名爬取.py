import pandas as pd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver  # 从selenium库中调用webdriver模块
import time  # 调用time模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
import pymssql


#
driver.get('https://www.shanghairanking.cn/rankings/bcmr/2022')  # 访问页面
# 窗口最大化
driver.maximize_window()
time.sleep(2)  # 暂停两秒，等待浏览器缓冲
#登录功能（接收验证码）
def enter():
    # 点击登录按钮
    demo = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/div/span')
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


# driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[1]").click()
titles = len(driver.find_elements(By.CLASS_NAME, "catogry"))

#打印门类所在长度
# print(titles)
school_name_end = []
school_rank_end = []
school_code_end = []
major_name_end = []
# 循环
for i in range(titles):
    time.sleep(2)
    # 每次循环，都重新获取元素，防止元素失效或者页面刷新后元素改变了
    num = "//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(i+1) + "]"

    item = driver.find_element(By.XPATH, num)

    # 循环点击获取的元素
    item.click()
    # 依次点击右侧的专业
    major_item = driver.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[*]/div[2]/div/div[*]/div[1]')
    # print(len(major_item))
    # 存储学校名称、排名、总分
    # 循环后侧的专业数量
    for j in major_item:
        j.click()
        time.sleep(3)
        # 点击下一页
        # 取该专业有多少页

        # 专业名称
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
         # 如果有好几页，则点击下一页，如果没有则返回上一页
        try:
            # driver.find_element(By.XPATH, '//*[@id="content-box"]/ul/li*')
            # 获取所有的“li”标签
            lis = driver.find_elements(By.XPATH, '//*[@id="content-box"]/ul/li[*]')
            # 倒数第三个“li”标签的文本是数量
            lis_text = lis[-3].text
            # “li”标签的数量
            num = len(lis)
            for next in range(int(lis_text)):
                # 单击下一页按钮
                driver.find_element(By.XPATH, '//*[@id="content-box"]/ul/li[{}]'.format(num - 1)).click()
                # 没刷新一页，重新获取所有的“li”标签
                time.sleep(1)
                lis = driver.find_elements(By.XPATH, '//*[@id="content-box"]/ul/li[*]')
                # “li”标签的数量
                num = len(lis)
                # 本页有多少个学校需要循环
                school_name_num = len(driver.find_elements(By.XPATH,
                                                           '//*[@id="content-box"]/div[2]/div/div[2]/div[*]/div[*]/div[3]/div[2]/div/div/div/a'))
                # 循环该页的所有学校，存储学校名称、排名、总分
                for k in range(school_name_num):
                    # 学校名称
                    school_name = driver.find_element(By.XPATH,
                                                      '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                                                          k + 1) + ']/div[*]/div[3]/div[2]/div/div/div/a').text
                    # 学校排名
                    school_rank = driver.find_element(By.XPATH,
                                                      '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                                                          k + 1) + ']/div[*]/div[2]/div').text
                    # 学校总分
                    school_code = driver.find_element(By.XPATH,
                                                      '//*[@id="content-box"]/div[2]/div/div[2]/div[' + str(
                                                          k + 1) + ']/div[*]/div[5]').text
                    # 添加到列表中
                    school_name_end.append(school_name)
                    school_rank_end.append(school_rank)
                    school_code_end.append(school_code)
                    major_name_end.append(major_name)
            driver.back()
            time.sleep(2)
        except:
            driver.back()
            time.sleep(2)
    df = pd.DataFrame(
        {
            '专业名称': major_name_end, '学校名称': school_name_end, '学校排名': school_rank_end, '学校总分': school_code_end
        }
    )
    df.to_excel(r"D:\数据部\常用通用数据\软科专业排名.xlsx", index=False)
    time.sleep(2)

driver.quit()






