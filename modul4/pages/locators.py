from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REDISTR_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-title.hidden-xs")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")

