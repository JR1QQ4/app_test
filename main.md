# Appium 自动化测试(Python 版)

## 一、前言

### 目前手机自动化的方案

#### iOS

- calabash-ios
- Frank
- UIAutimation
- ios-driver
- KeepltFunctional

#### Android

- calabash-android
- Monkey Talk
- Robotium
- UiAutomator
- selendroid

### 自动化工具选择

- MonkeyRunner: Android、功能测试、Python、不跨应用
- Instrumentation: Android(<4.1)、功能测试、Java
- Uiautomator2: Android(>=4.1) 、功能测试、Java
- Adb-For-Test: Android(>=4.1)、功能测试、Java/Python
- Monkey: Android、稳定测试、Java、不支持H5、不跨应用
- CTS: Android、兼容性测试、Java
- Uiautomation: iOS、功能测试、JS
- Calabash: Android/iOS、功能测试、Ruby
- Appium: Android/iOS、功能测试、Java/Python/JS/C/C#/Perl

### Appium

Android/iOS/Windows/Mac、Java/Python/JS等

#### 引擎列表

- iOS: The XCUITest Driver
- Android:
    - The UiAutomator2 Driver
    - The Espresso Driver

#### 设计理念

WebDriver script(Client) <-> Appium Modules(Server) <-> apk

#### 生态工具

- adb
    - 获取当前界面元素: adb shell dumpsys activity top (推荐) (重点)
    - 获取任务列表: adb shell dumpsys activity activities
    - 获取 app 入口
        - adb logcat | grep -i displayed (推荐) (重点)
        - aapt dump badging mobike.apk | grep launchable-activity
        - apkanalyzer (最新版本的 sdk 才有)
    - 启动应用: adb shell am start -W -n appPackage/appActivity -S (重点)
        - S 会重启
    - 获取所有 webview 的进程: adb shell cat /proc/net/unix | grep webview
    - 查看进程所对应的应用: adb shell ps | grep 1136
- android的控制工具
- Appium Desktop
    - 内嵌了 appium server 和 inspector 
- Appium server
    - appium 的核心工具，命令行工具
- Appium Client
    - 各种语言的客户端封装库
- AppCrawler
    - 自动遍历工具

## 二、环境安装

- Java 1.8 + Android SDK + Node js(>10, npm) + python3 + appium-desktop + Appium python client
- 如果不需要 appium inspector，可以通过 npm 直接安装
    - npm install -g cnpm --registry=https://registry.npm.taobao.org
    - cnpm install -g appium
    - 运行: appium -g appium.log

### appium client

pip install appium-python-client

### 使用 appium-doctor 检测 appium 的安装环境

- cnpm install appium-doctor
- 运行
    - 运行之前需要配置环境变量
    - C:/Users/username/node_modules/.bin
    - 运行: appium-doctor

## 三、基本应用

### 导入

from appium import webdriver

### Capability 设置

- 文档地址: `https://appium.io/docs/en/writing-running-appium/caps/`
- appPackage 包名
- appActivity Activity名字
- automationName 安卓默认uiautomator2/iOS默认XCUITest
- noRest<->fullReset 是否在测试前后重置相关环境
- unicodeKeyBoard resetKeyBoard 是否需要输入非英文之外的语言并在测试完成后重置输入法
- dontStopAppOnRest 首次启动的时候不停止app(可以提升运行速度)
- skipDeviceInitialization 跳过安装/权限设置等操作(可以提升运行速度)
- newCommandTimeOut 命令发送的间隔时间
- uuid 模拟器id: 如 emulator-5554
- autoGrantPermissions 权限授予
- waitForIdleTimeout 为了防止客户端程序响应超时，表示等待空闲
- skipUnlock 
- skipLogcatCapture 跳过日志的获取
- skipLogCapture
- systemPort
- ignoreUnimportantViews  #跳过不知

### 日志

appium -g appium.log

## 四、核心技术

### 定位工具

- uiautomatorviewer 安卓 sdk 工具
- Appium-Desktop inspecter 工具

### 扩展定位

- id定位
    - driver.find_element_by_id(resource-id)
    - driver.find_element(MobileBy.ID, "resource-id")
- accessibility_id定位
    - driver.find_element_by_accessibility_id(content-desc)
    - driver.find_element(MobileBy.ACCESSIBILITY_ID, conten-desc)
- xpath 定位
    - driver.find_element_by_xpath(xpath属性值)
- classname定位（不推荐）
- uiautomator Android定位
    - driver.find_element_by_android_uiautomator('new UiSelector().resourceId("id")')
    - new UiSelector().className("className")
    - new UiSelector().description("content-desc")
    - new UiSelector().text("文本")
    - new UiSelector().textContains("文本")
    - new UiSelector().testStartsWith("开始文本")
    - new UiSelector().textMatches("正则")
    - 父子关系定位 new UiSelector().resourceId("id").childSelector(text("文本"))
    - 兄弟定位 new UiSelector().resourceId("id").fromParent(text("文本"))
    - 实现滚动查找元素 new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("文本").instance(0)) 

### 三种等待

- sleep()
- 服务端全局隐式等待 driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS)
- 客户端显式等待 WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MobileBy.ID, "com.android.settings:id/title")))

### 元素的常用方法

- 点击 ele.click()
- 输入 ele.send_keys()
- 设置元素的值 ele.set_value()
- 清除 ele.clear()
- 是否可见 ele.is_displayed()
- 是否可用 ele.is_enabled
- 是否被选中 ele.is_selected
- 获取属性值 ele.get_attribute(name)

### 元素常用的属性

- 获取文本 ele.text
- 获取坐标 ele.location
- 获取尺寸(高和宽) ele.size

### TouchAction

- action=TouchAction(driver)
- `w, h = driver.get_window_rect()["width"], driver.get_window_rect()["height"]`
- action.press(x=int(w/2),y=int(h*4/5)).wait(200).move_to(x=int(w/2), y=int(h/5)).release().perform()

### Toast 控件识别

- 步骤一: automationName: uiautomator2
- 步骤二: 必须使用xpath查找元素，找到后driver.page_source可以查看结构
    - `//*[@class='android.widget.Toast']`
    - `//*[contains(@Text, "xxxxx")]`
- `driver.find_element(MobileBy.XPATH, '//*contains[@text, "xxx"]')`

### 获取属性 get_attribute

- ele.get_attribute("content-desc")
- ele.get_attribute("resource-id")
- ele.get_attribute("enabled")
- ele.get_attribute("clickable")
- ele.get_attribute("bounds")

### 参数化

@pytest.mark.parametrize

### 设备交互 API(部分不支持)

电话: `driver.make_gsm_call("138xxxxxxxx", GsmCallActions.CALL)`
短信: `driver.send_sms("135xxxxxxxx","msg")`
网络: `driver.network_connection(1)`
截图: `driver.get_screenshot_as_file(',./img.png')`
录屏:
    - `driver.start_recording_screen()`
    - `driver.stop_recording_screen()`

### 启动应用

- driver.launch_app()
- driver.start_activity(app_package="", app_activity="")

## 五、Android/iOS

### Android

- 七大布局方式:
    - LinearLayout 线性布局
    - RelativeLayout 相对布局
    - FrameLayout 帧布局
    - AbsoluteLayout 绝对布局
    - TableLayout 表格布局
    - GridLayout 网格布局
    - ConstraintLayout 约束布局
- 四大组件:
    - activity 与用户交互的可视化界面
    - service 实现程序后台运行的解决方案
    - content provider 内容提供者，提供程序所需要的数据
    - broadcast receiver 广播接收器，监听外部事件的到来(比如来电)
- 常用的控件:
    - TextView 文本控件、EditText 可编辑文本控件
    - Button 按钮、ImageButton 图片按钮、ToggleButton 开关按钮
    - ImageView 图片控件
    - CheckBox 复选框控件、RadioButton 单选框控件

### iOS

- MacOS X 系统、Xcode 开发工具、ObjectC 开发语言
    - `.ipa` 文件 / `.app` 文件 为安装文件

### iOS与Android的区别

- dom属性和节点结构类似
- 名字和属性的命名不同:
    - android resource-id <-> ios name
    - android content-desc <-> ios accessibility-id

## 六、第三方扩展

- 自带断言 assert
- hamcrest 断言: `pip install PyHamcrest`

## 七、Android Webview 和 纯 web 页面测试

### 纯 web 页面

- 手机端:
    - 被测浏览器(不可以是第三方浏览器): Safari for iOS and Chrome/Chromium/Browser for Android
- PC 端：
    - 安装Chrome/Chromium浏览器，并能登录谷歌
        - chrome://inspect/#devices 用于定位手机页面元素
    - 下载对应手机浏览器对应的driver版本(向上兼容)
        - `https://npm.taobao.org/mirrors/chromedriver`
    - 客户端代码(desirecapability)
        - `"browser"="Browser"或者"browser"="Chrome"`
        - `"chromedriverExecutable"="指定下载的driver的路径"`

```python
# 1.The desired should not include both of an 'appPackage' and a 'browserName' 两个不能一起使用，在这里使用 browserName

# 2.browserName 指定浏览器

# 3.如果没有指定 chromedriverExecutable 和 chromedriverExecutableDir，会出现 WebDriverException
# Original error: No Chromedriver found that can automate Chrome '52.0.2743'. You could also try to enable automated 
# chromedrivers download server feature. 
# See https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md for more detail
# 原因: appium 会从 ..\npm\node_modules\appium\node_modules\_appium-chromedriver.. 下查找 chromedriver

# 4.指定目录，chromedriverExecutable 与 chromedriverExecutableDir 等价，前者指明具体文件，后者只需指明目录
# 在把 chromedriver 添加刀环境变量的情况下，还是不能运行，所以还是指定了查找目录

# 5.chrome://inspect/#devices，在使用 mumu 模拟器自带浏览器的情况下能进行查看
caps = {
    "deviceName": "127.0.0.1:7555", # mumu 模拟器连接时需要指定 adb connect 127.0.0.1:7555
    "platformName": "Android",
    "platformVersion": "6.0.1",
    "browserName": "Browser",
    "automationName": "UiAutomator2",
    "chromedriverExecutable": "C:\\webdriver\\chromedriver.exe",
    # "chromedriverExecutableDir": "C:\\webdriver",
    # "appPackage": "com.android.browser",  # 查看手机自带浏览器的包名 adb shell pm list packages -s | findstr browser
    # "appActivity": "com.android.browser.BrowserActivity", # 打开引用查看当前应用 adb shell dumpsys window | findstr mCurrent
    "noRest": True
}
```

### 混合页面测试

- WebView - Android 系统提供能显示网页的系统控件（特殊的 View）
- PC
    - 浏览器能访问谷歌，并下载 chromedriver 对应的版本
- 手机端
    - 应用代码需要打开 webview 开关
    - (ps: 如果知道生成的 webview 的网址(抓包)，那么可以复制网址到浏览器查看页面元素的结构) 
- 代码
    - appPackage, appActivity
    - `"chromedriverExecutableDir": "C:\\webdriver"`，使用 chrome inspect 查看元素定位，必须使用此参数
- 上下文切换
    - `driver.switch_to.context(driver.contexts[-1])`
    - `driver.switch_to.default_content()`
    - `driver.switch_to.windows(driver.window_handles[-1])`
- adb
    - 查看 webview 包名: adb shell pm list package | findstr webview
    - 查看 webview 版本: adb shell pm dump com.android.webview | findstr version，用于选择合适的 chromedriver
    - 查看命令使用: adb | grep froward
    - 把本地的8888端口映射到手机的9999端口: adb forward tcp:8888 tcp:9999
    - 查看所有的映射: adb forward --list
    - 删除映射，手动释放: adb forward --remove tcp:8888

### 遇到的坑

- Android 模拟器 6.0 默认支持 webview 操作(mumu模拟器不可以，genimotion和sdk自带的emulator可以)
- 其他模拟器和物理机需要打开app内开关(webview体调试开关)
- chrome浏览器-Chrome62才可以更好的看见webview的内部
- 换成chromium浏览器可以避免很多坑，展示效果比chrome快

## 八、ADB

- 获取所有 webview 的进程
    - adb shell cat /proc/net/unix | grep webview
    - adb shell ps | grep 1136 查看进程的应用 
- 查看本机和远程手机端的映射
    - adb forward --list
    - adb forward --remove name:port
- 查看模拟器列表
    - `emulator.exe -list-avds`，或者 `android.bat list avd`
- 启动模拟器
    - `emulator.exe -netdelay none -netspeed full -avd 虚拟机名称`

## 九、Appium 原理

### JsonWap(先打开模拟器)

- 建立在 WebDirver 之上
- /session  表示自动化测试开始
- /status  获取当前 session 的状态
- session_id 创建
    - `curl -l -H "Content-type:application/json" -X POST -d '{"desiredCapabilities":{...}}' 'http://127.0.0.1:4723/wd/hub/session'`
- session_id 获取
    - `session_id = $(curl 'http://127.0.0.1:4723/wd/hub/sessions' \ | awk -F \" '{print $6}')`
- 获取 sessions 状态信息
    - `curl 'http://127.0.0.1:4723/wd/hub/sessions'`

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("invoke " + func.__name__ + "\n args \n" + repr(args[1:]) + repr(kwargs))
```