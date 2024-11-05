from selenium.webdriver.common.by import By

class TestLocators:
    REGISTRATION_URL                = By.XPATH, ".//a[text() = 'Зарегистрироваться']"
    REGISTRATION_TITLE              = By.XPATH, ".//h2[text() ='Регистрация']"
    REGISTRATION_NAME               = By.XPATH, ".//label[text() = 'Имя']/parent::*/input"
    REGISTRATION_EMAIL              = By.XPATH, ".//label[text() = 'Email']/parent::*/input"
    REGISTRATION_PASSWORD           = By.XPATH, ".//input[@type = 'password']"
    REGISTRATION_BUTTON             = By.XPATH, ".//button[text() = 'Зарегистрироваться']"

    ENTRANCE_TITLE                  = By.XPATH, ".//h2[text() ='Вход']"
    ENTRANCE_EMAIL                  = By.XPATH, ".//input[@type = 'text']"
    ENTRANCE_PASSWORD               = By.XPATH, ".//input[@type = 'password']"
    ENTRANCE_BUTTON                 = By.XPATH, ".//button[text() = 'Войти']"
    ENTRANCE_FORGOT_PASSWORD_URL    = By.XPATH, ".//a[@href = '/forgot-password']"

    MAIN_TITLE_CONSTRUCTOR          = By.XPATH, ".//p[text() ='Конструктор']"
    MAIN_ACCOUNT_URL                = By.XPATH, ".//a[@href = '/account']"
    MAIN_LOGON_ACCOUNT_BUTTON       = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    MAIN_PLACE_ORDER_BUTTON         = By.XPATH, ".//button[text() = 'Оформить заказ']"

    MAIN_SAUCES_TAB                 = By.XPATH, ".//span[text() = 'Соусы']"
    MAIN_CURR_STATUS_SAUCES_TAB     = By.XPATH, ".//span[text() = 'Соусы']/parent::div[contains(@class, 'current')]"
    MAIN_FILLINGS_TAB               = By.XPATH, ".//span[text() = 'Начинки']"
    MAIN_CURR_STATUS_FILLINGS_TAB   = By.XPATH, ".//span[text() = 'Начинки']/parent::div[contains(@class, 'current')]"
    MAIN_BUNS_TAB                   = By.XPATH, ".//span[text() = 'Булки']"
    MAIN_CURR_STATUS_BUNS_TAB       = By.XPATH, ".//span[text() = 'Булки']/parent::div[contains(@class, 'current')]"

    PASSWORD_RECOVERY_TITLE         = By.XPATH, ".//h2[text() ='Восстановление пароля']"
    PASSWORD_RECOVERY_REMEMBER_URL  = By.XPATH, ".//a[@href = '/login']"

    PERS_ACC_PROFILE_BUTTON         = By.XPATH, ".//button[text() = 'Выход']"   #кнопка выход
    PERS_ACC_TITLE_CONSTRUCTOR      = MAIN_TITLE_CONSTRUCTOR
    PERS_ACC_LOGOTYPE_URL           = By.XPATH, ".//a[@href = '/']"
    PERS_ACC_CONSTRUCTOR_URL        = MAIN_TITLE_CONSTRUCTOR