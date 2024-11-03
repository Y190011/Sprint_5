from selenium.webdriver.common.by import By

class TestLocators:
    SEARCH_REGISTRATION_URL                = By.XPATH, ".//a[text() = 'Зарегистрироваться']"
    SEARCH_REGISTRATION_TITLE              = By.XPATH, ".//h2[text() ='Регистрация']"
    SEARCH_REGISTRATION_NAME               = By.XPATH, ".//label[text() = 'Имя']/parent::*/input"
    SEARCH_REGISTRATION_EMAIL              = By.XPATH, ".//label[text() = 'Email']/parent::*/input"
    SEARCH_REGISTRATION_PASSWORD           = By.XPATH, ".//input[@type = 'password']"
    SEARCH_REGISTRATION_BUTTON             = By.XPATH, ".//button[text() = 'Зарегистрироваться']"

    SEARCH_ENTRANCE_TITLE                  = By.XPATH, ".//h2[text() ='Вход']"
    SEARCH_ENTRANCE_EMAIL                  = By.XPATH, ".//input[@type = 'text']"
    SEARCH_ENTRANCE_PASSWORD               = By.XPATH, ".//input[@type = 'password']"
    SEARCH_ENTRANCE_BUTTON                 = By.XPATH, ".//button[text() = 'Войти']"
    SEARCH_ENTRANCE_FORGOT_PASSWORD_URL    = By.XPATH, ".//a[@href = '/forgot-password']"

    SEARCH_MAIN_TITLE_CONSTRUCTOR          = By.XPATH, ".//p[text() ='Конструктор']"
    SEARCH_MAIN_ACCOUNT_URL                = By.XPATH, ".//a[@href = '/account']"
    SEARCH_MAIN_LOGON_ACCOUNT_BUTTON       = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    SEARCH_MAIN_PLACE_ORDER_BUTTON         = By.XPATH, ".//button[text() = 'Оформить заказ']"

    SEARCH_MAIN_SAUCES_TAB                 = By.XPATH, ".//span[text() = 'Соусы']"
    SEARCH_MAIN_CURR_STATUS_SAUCES_TAB     = By.XPATH, ".//span[text() = 'Соусы']/parent::div[contains(@class, 'current')]"
    SEARCH_MAIN_FILLINGS_TAB               = By.XPATH, ".//span[text() = 'Начинки']"
    SEARCH_MAIN_CURR_STATUS_FILLINGS_TAB   = By.XPATH, ".//span[text() = 'Начинки']/parent::div[contains(@class, 'current')]"
    SEARCH_MAIN_BUNS_TAB                   = By.XPATH, ".//span[text() = 'Булки']"
    SEARCH_MAIN_CURR_STATUS_BUNS_TAB       = By.XPATH, ".//span[text() = 'Булки']/parent::div[contains(@class, 'current')]"

    SEARCH_PASSWORD_RECOVERY_TITLE         = By.XPATH, ".//h2[text() ='Восстановление пароля']"
    SEARCH_PASSWORD_RECOVERY_REMEMBER_URL  = By.XPATH, ".//a[@href = '/login']"

    SEARCH_PERS_ACC_PROFILE_BUTTON         = By.XPATH, ".//button[text() = 'Выход']"   #кнопка выход
    SEARCH_PERS_ACC_TITLE_CONSTRUCTOR      = SEARCH_MAIN_TITLE_CONSTRUCTOR
    SEARCH_PERS_ACC_LOGOTYPE_URL           = By.XPATH, ".//a[@href = '/']"
    SEARCH_PERS_ACC_CONSTRUCTOR_URL        = SEARCH_MAIN_TITLE_CONSTRUCTOR