# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:09:01 2021

@author: engin
"""
import unittest
from selenium import webdriver
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
class TestFunctional(StaticLiveServerTestCase):
    def setUp(self):
        ##Chrome Session
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        ##link to website that we are going to test


    """def test_forNavItems(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        ImgClick = server + reverse('index')
        self.imgClick = self.driver.find_element_by_tag_name("img").click()
        self.assertEqual(
        self.driver.current_url,
        ImgClick
        )

        homeClick = server + reverse('index')
        self.HomeClick = self.driver.find_element_by_link_text('Home').click()
        self.assertEqual(
        self.driver.current_url,
        homeClick
        )


        shopClick = server + str(reverse("shop"))
        self.ShopClick = self.driver.find_element_by_link_text('Shop').click()
        self.assertEqual(
        self.driver.current_url,
        shopClick
        )

        cartClick = server  + str(reverse("cart"))
        self.CartClick = self.driver.find_element_by_link_text('Cart').click()
        self.assertEqual(
        self.driver.current_url,
        cartClick
        )

        checkoutClick = server  + str(reverse("checkout"))
        self.CheckoutClick = self.driver.find_element_by_link_text('Checkout').click()
        self.assertNotEqual(
        self.driver.current_url,
        checkoutClick
        )

        contactClick = server + str(reverse("contact"))
        self.ContactClick = self.driver.find_element_by_link_text('Contact').click()
        self.assertEqual(
        self.driver.current_url,
        contactClick
        )
    def test_forSearchBox(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        self.search_field = self.driver.find_element_by_name("keyword")
        self.search_field.send_keys("Mouse")
        self.search_field.submit()
        lists = self.driver.find_elements_by_class_name("Product")
        no=len(lists)
        self.assertEqual(4, len(lists))
    def test_ProductClick(self):
         server = "https://computerbyte.pythonanywhere.com"
         self.driver.get(server)

         productClick = server +  reverse('productdetail',args=["mouse", "dell-wired-mouse"])
         self.ProductClick = self.driver.find_element_by_link_text('Dell Wired Mouse').click()
         self.assertEqual(
            self.driver.current_url,
            productClick
            )
    def test_CatClick(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)

        catClick = server +  reverse('shop',args=["mouse"])
        self.CatTagClick = self.driver.find_element_by_link_text('Categories').click()
        self.CatClick = self.driver.find_element_by_link_text('Mouse').click()
        self.assertEqual(
           self.driver.current_url,
           catClick
           )

    def test_AddToCARTClick(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        productClick = server +  reverse('productdetail',args=["mouse", "dell-wired-mouse"])
        self.ProductClick = self.driver.find_element_by_link_text('Dell Wired Mouse').click()
        self.assertEqual(
            self.driver.current_url,
            productClick
            )
        addToCartClick = server +  reverse('add_cart',args=[2])
        self.AddToCartClick = self.driver.find_element_by_link_text('Add To Cart').click()

        self.assertEqual(
            self.driver.current_url + "add_cart/2/",
            addToCartClick
          )
        lists = self.driver.find_elements_by_tag_name("tr")
        no=len(lists)
        self.assertEqual(2, len(lists))"""


    def test_CHECKOUTClick(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        self.ProductClick = self.driver.find_element_by_link_text('Dell Wired Mouse').click()
        self.AddToCartClick = self.driver.find_element_by_link_text('Add To Cart').click()
        self.checkoutClick = self.driver.find_element_by_link_text('Checkout').click()

        self.username_field = self.driver.find_element_by_name("username")
        self.password_field = self.driver.find_element_by_name("password")
        self.username_field.send_keys("computerbyte")
        self.password_field.send_keys("WebCEP9999")
        self.username_field.submit()

        self.checkoutClick = self.driver.find_element_by_link_text('Checkout').click()
        self.Email_field = self.driver.find_element_by_name("Email")
        self.PhoneNo_field = self.driver.find_element_by_name("PhoneNo")
        self.DeliverAddress_field = self.driver.find_element_by_name("DeliverAddress")
        self.Email_field.send_keys("computerbyte@gmail.com")
        self.PhoneNo_field.send_keys("+9200000000")
        self.DeliverAddress_field.send_keys("Mardan, KPK, Pakistan")
        self.Email_field.submit()

        CheckoutClick = server +  reverse('index')
        self.assertEqual(
         self.driver.current_url,
         CheckoutClick
         )
    def test_CheckouCheck_EmptyCart(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        self.checkoutClick = self.driver.find_element_by_link_text('Checkout').click()
        self.username_field = self.driver.find_element_by_name("username")
        self.password_field = self.driver.find_element_by_name("password")
        self.username_field.send_keys("computerbyte")
        self.password_field.send_keys("WebCEP9999")
        self.username_field.submit()

        self.checkoutClick = self.driver.find_element_by_link_text('Checkout').click()
        self.Email_field = self.driver.find_element_by_name("Email")
        self.PhoneNo_field = self.driver.find_element_by_name("PhoneNo")
        self.DeliverAddress_field = self.driver.find_element_by_name("DeliverAddress")
        self.Email_field.send_keys("computerbyte@gmail.com")
        self.PhoneNo_field.send_keys("+9200000000")
        self.DeliverAddress_field.send_keys("Mardan, KPK, Pakistan")
        self.Email_field.submit()

        CheckoutClick = server +  reverse('shop')
        self.assertEqual(
         self.driver.current_url,
         CheckoutClick
         )
    def test_Contact(self):
        server = "https://computerbyte.pythonanywhere.com"
        self.driver.get(server)
        self.contactClick = self.driver.find_element_by_link_text('Contact').click()
        self.Email_field = self.driver.find_element_by_name("email")
        self.subject_field = self.driver.find_element_by_name("subject")
        self.message_field = self.driver.find_element_by_name("message")
        self.Email_field.send_keys("computerbyte@gmail.com")
        self.subject_field.send_keys("Need Some Replacements")
        self.message_field.send_keys("I had buy this while now want this thanks.")
        self.Email_field.submit()
        ContactClick = server +"/"
        self.assertEqual(
            self.driver.current_url,
            ContactClick
        )
    def tearDown(self):
        # close the browser window
        self.driver.quit()
if __name__ == "__AutomatedTestingUsingSelenium__":
    unittest.AutomatedTestingUsingSelenium()
