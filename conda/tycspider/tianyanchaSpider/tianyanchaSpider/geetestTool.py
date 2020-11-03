import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
EMAIL = '13580380595'
PASSWORD = 'liu75040333'
BORDER_1 = 8
BORDER_2 = 15
import random
BORDER_3 = 28
INIT_LEFT = 60

class CrackGeetest():
    def __init__(self):
        self.url = 'https://www.tianyancha.com/company/33657264'
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    # def __del__(self):
    #     self.browser.close()

    def check_login(self):
        try:
            self.browser.find_element_by_xpath("//a[contains(text(),'登录/注册')]")
            return True
        except Exception as e:
            return False

    def get_geetest_button(browser):
        """
               获取初始验证按钮
               :return:
               """
        button = browser.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_box')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.browser.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")  # 'gt_slider_knob gt_show')))
        return slider

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        # print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        # self.browser.get(self.url)
        # email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        # password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        # email.send_keys(self.email)
        # password.send_keys(self.password)
        self.browser.implicitly_wait(4)
        self.browser.get(self.url)
        try:
            # self.browser.find_element_by_xpath("//div[6]/a").click()
            # self.browser.implicitly_wait(2)
            wait = WebDriverWait(self.browser, 20)
            wait.until(lambda driver: self.browser.find_element_by_xpath("//div[text()='密码登录']"))
            self.browser.find_element_by_xpath("//div[text()='密码登录']").click()
            self.browser.find_element_by_xpath("//div[text()='密码登录']").click()
            phone = wait.until(EC.presence_of_element_located((By.ID, 'mobile')))
            password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
            phone.send_keys('135803805951')
            self.browser.implicitly_wait(2)
            password.send_keys('liu75040333')
            one_button = self.browser.find_element_by_xpath("//div[@class='btn -xl btn-primary -block' and text()='登录']")
            self.browser.find_element_by_xpath("//div[@class='btn -xl btn-primary -block' and text()='登录']").click()
            time.sleep(1)
            ActionChains(self.browser).double_click(one_button).perform()
            time.sleep(1)
        except Exception as e:
            print(e)

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1: 不带缺口图片
        :param image2: 带缺口图片
        :return:
        """
        left = 62
        print(image1.size[0])
        has_find = False
        for i in range(62, image1.size[0]):
            if has_find:
                break
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    has_find = True
                    break
        left -= 16
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 103
        # print(x,'---',y,'image1:-',pixel1[0],'-----',pixel2[0])
        # print('image1:-',pixel1[1],'-----',pixel2[1])
        # print('image1:-',pixel1[2],'-----',pixel2[2])
        # print('========')

        if abs(pixel1[0] - pixel2[0]) > threshold and abs(pixel1[1] - pixel2[1]) > threshold and abs(
                pixel1[2] - pixel2[2]) > threshold:
            # print('--False-', abs(pixel1[0] - pixel2[0]), '：', abs(pixel1[1] - pixel2[1]), '：', abs(
            #     pixel1[2] - pixel2[2]))
            return False
        else:
            # print('--True-',abs(pixel1[0] - pixel2[0]) ,':',abs(pixel1[1] - pixel2[1]),':',abs(
            #     pixel1[2] - pixel2[2]))
            return True

    def get_track(self, left):
        """
            根据偏移量获取移动轨迹
            :param distance: 偏移量
            :return: 移动轨迹
            """
        # 移动轨迹
        track = []
        # 当前位移
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = left * 3 / 4
        # 间隔时间
        t = 1
        v = 0
        while current < left:
            if current < mid:
                a = random.randint(2, 3)
            else:
                a = - random.randint(6, 7)
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            track.append(round(move))

        slider = self.get_slider()
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        ActionChains(self.browser).release().perform()

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')
    def close_browse(self):
        self.browser.close()

    def crack(self):
        # 输入用户名密码


        self.open()
        # 点击验证按钮
        # button = self.get_geetest_button()
        # button.click()
        # 获取验证码图片
        first = 0

        # while self.check_login:
            # captchaTest = self.browser.find_element_by_xpath(".//div[@class='content']/div[@class='captcha-title']").extract_first()
            # print('captchaTest---', captchaTest)
            # print('')
        #     self.browser.close()
            # refresh_button = self.browser.find_element_by_xpath("//a[@class='gt_refresh_button']")
            # if first > 0:
            #     time.sleep(5)
            #     ActionChains(self.browser).click(refresh_button).perform()
            # first += 1
            # image1 = self.get_geetest_image('captcha1.png')
            # # 点按呼出缺口
            # slider = self.get_slider()
            # slider.click()
            # # 获取带缺口的验证码图片
            # image2 = self.get_geetest_image('captcha2.png')
            # # 获取缺口位置
            #
            # gap = self.get_gap(image1, image2)
            # print('缺口位置', gap)
            # # 减去缺口位移
            # # gap -= 6
            # # 获取移动轨迹
            # self.get_track(gap)
        time.sleep(7)
        Cookies = self.browser.get_cookies()
        # print(Cookies)
        cookie_dict = {}
        cookie_str = []
        for cookie in Cookies:
            # cookie_dict[cookie['name']] = cookie['value']
            resutl = cookie['name']+"="+cookie['value']+";"
            cookie_str.append(resutl)
        return "".join(cookie_str)



if __name__ == '__main__':
    crack = CrackGeetest()
    cookie_dict = crack.crack()
    print('cookie:--',cookie_dict)