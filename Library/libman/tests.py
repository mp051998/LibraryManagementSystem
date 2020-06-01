from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.auth.models import User


##### Monish Prakasan ----- mp051998@gmail.com ----- PES University

class RunThrough(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('libman/chromedriver.exe')
        self.browser.implicitly_wait(3)
        time.sleep(5)
        try:
            user = User.objects.create_superuser(
                username='test',
                email='test@test.com',
                password='test',
            )
            self.client.force_login(user)
        except:
            pass

    def tearDown(self):
        self.browser.close()

    def test_all(self):
        #####-----TEST1:Login-----#####
        print("TEST1 : Login")
        self.browser.get(self.live_server_url)
        time.sleep(1)
        username='test'
        password='test'
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys(username)
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("    TEST1 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST2:Checking if all Pages are accessible-----#####
        print("TEST2 : Checking if all Pages are accessible")
        books_link = self.browser.find_element_by_name("Books")
        books_link.click()
        time.sleep(3)

        student_link = self.browser.find_element_by_name("Student")
        student_link.click()
        time.sleep(3)

        employer_link = self.browser.find_element_by_name("Employer")
        employer_link.click()
        time.sleep(3)

        issue_link = self.browser.find_element_by_name("Issue")
        issue_link.click()
        time.sleep(3)

        return_link = self.browser.find_element_by_name("Return")
        return_link.click()
        time.sleep(3)

        dashboard_link = self.browser.find_element_by_name("Dashboard")
        dashboard_link.click()
        print("    TEST2 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST3:Adding a new book-----#####
        print("TEST3 : Adding a Book")
        books_link = self.browser.find_element_by_name("Books")
        books_link.click()
        time.sleep(3)

        addBook_link = self.browser.find_element_by_name("addBook")
        addBook_link.click()
        time.sleep(3)

        self.browser.find_element_by_name('isbn_no').send_keys("123123321")
        time.sleep(2)
        self.browser.find_element_by_name('barcode').send_keys("916916916")
        time.sleep(2)
        self.browser.find_element_by_name('book_name').send_keys("Linear Algebra")
        time.sleep(2)
        self.browser.find_element_by_name('author_name').send_keys("Gilbert Strang")
        time.sleep(2)
        self.browser.find_element_by_name('no_of_books').send_keys(10)
        time.sleep(2)

        #Clear the textbox to ensure no other text is added unnecessarily.
        self.browser.find_element_by_name('book_detail').clear()
        self.browser.find_element_by_name('book_detail').send_keys(
            "This book helps strengthen matrix concepts and related calculation methods. The book also has numerous problems which makes good practice material."
        )
        time.sleep(2)
        
        Select(self.browser.find_element_by_name('department')).select_by_value('COM')
        time.sleep(2)

        self.browser.find_element_by_name('publisher').send_keys("Goyal Brothers")
        time.sleep(2)
        self.browser.find_element_by_name('rack_no').send_keys("919")
        time.sleep(2)

        self.browser.find_element_by_name("Submit").click()

        books_link = self.browser.find_element_by_name("Books")
        books_link.click()
        print("    TEST3 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST4:Adding a Student-----#####
        print("TEST4 : Adding a Student")
        student_link = self.browser.find_element_by_name("Student")
        student_link.click()
        time.sleep(3)

        addStudent_link = self.browser.find_element_by_name("addStudent")
        addStudent_link.click()
        time.sleep(3)

        self.browser.find_element_by_name('Fname').send_keys("Monish")
        time.sleep(2)
        self.browser.find_element_by_name('Lname').send_keys("Prakasan")
        time.sleep(2)
        self.browser.find_element_by_name('Address').send_keys("Rockbottom, Bengalore")
        time.sleep(2)
        self.browser.find_element_by_name('phone').send_keys(7054236958)
        time.sleep(2)
        self.browser.find_element_by_name('Email').send_keys("mp051998@gmail.com")
        time.sleep(2)
        self.browser.find_element_by_name('student_id').send_keys("PES1201700232")
        time.sleep(2)
        Select(self.browser.find_element_by_name('batch')).select_by_value('2017')
        time.sleep(2)
        Select(self.browser.find_element_by_name('depart')).select_by_value('BEC')
        time.sleep(2)
        self.browser.find_element_by_name('semester').send_keys('6')
        time.sleep(2)

        self.browser.find_element_by_name("Submit").click()

        student_link = self.browser.find_element_by_name("Student")
        student_link.click()
        print("    TEST4 passed successfully")
        time.sleep(3)
        #####-----      -----#####




        #####-----TEST5:Adding an Employer-----#####
        print("TEST5 : Adding an Employer")
        employer_link = self.browser.find_element_by_name("Employer")
        employer_link.click()
        time.sleep(3)

        addEmployer_link = self.browser.find_element_by_name("addEmployer")
        addEmployer_link.click()
        time.sleep(3)

        self.browser.find_element_by_name('Fname').send_keys("Rahul")
        time.sleep(2)
        self.browser.find_element_by_name('Lname').send_keys("Sharma")
        time.sleep(2)
        self.browser.find_element_by_name('Address').send_keys("Capitol City, World's End")
        time.sleep(2)
        self.browser.find_element_by_name('phone').send_keys(9981214652)
        time.sleep(2)
        self.browser.find_element_by_name('Email').send_keys("rahul@yahoo.com")
        time.sleep(2)
        self.browser.find_element_by_name('emp_id').send_keys("EMP123")
        time.sleep(2)
        Select(self.browser.find_element_by_name('timer')).select_by_value('FT')
        time.sleep(2)

        self.browser.find_element_by_name("Submit").click()

        employer_link = self.browser.find_element_by_name("Employer")
        employer_link.click()
        print("    TEST5 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST6:Issue a Book-----#####
        print("TEST6 : Issue a book")
        issue_link = self.browser.find_element_by_name("Issue")
        issue_link.click()
        time.sleep(3)

        newIssue_link = self.browser.find_element_by_name("newIssue")
        newIssue_link.click()
        time.sleep(3)

        self.browser.find_element_by_name('borrower_id').send_keys("PES1201700232")
        time.sleep(2)
        self.browser.find_element_by_name('borrower_name').send_keys("Monish Prakasan")
        time.sleep(2)
        self.browser.find_element_by_name('book_name').send_keys("Linear Algebra")
        time.sleep(2)
        self.browser.find_element_by_name('isbn').send_keys("123123321")
        time.sleep(2)

        self.browser.find_element_by_name("Submit").click()

        issue_link = self.browser.find_element_by_name("Issue")
        issue_link.click()
        print("    TEST6 passed successfully")
        time.sleep(3)
        #####-----      -----#####     





        #####-----TEST7:Accept return-----#####
        print("TEST7 : Accept return")
        return_link = self.browser.find_element_by_name("Return")
        return_link.click()
        time.sleep(3)

        self.browser.find_element_by_name('borrower_id').send_keys("PES1201700232")
        time.sleep(2)
        self.browser.find_element_by_name('isbn_no').send_keys("123123321")
        time.sleep(2)

        self.browser.find_element_by_name("Submit").click()
        print("    TEST7 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST8:Admin Portal Visit-----#####
        print("TEST8 : Admin Portal Check")
        admin_link = self.browser.find_element_by_name("admin")
        admin_link.click()
        time.sleep(3)

        self.browser.find_element_by_link_text('Bookss').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Employers').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Issues').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Returns').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Students').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Groups').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        self.browser.find_element_by_link_text('Users').click()
        time.sleep(6)
        self.browser.execute_script("window.history.go(-1)")
        time.sleep(3)

        #self.browser.find_element_by_link_text('View site').click()
        self.browser.get(self.live_server_url)
        print("    TEST8 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST9:Sign Up-----#####
        print("TEST9 : Sign Up and checking if the new credentials work.")
        signup_link = self.browser.find_element_by_name("signup")
        signup_link.click()
        time.sleep(3)

        username='test1'
        password='password123321'

        self.browser.find_element_by_name('username').send_keys(username)
        time.sleep(1)
        self.browser.find_element_by_name('password1').send_keys(password)
        time.sleep(1)
        self.browser.find_element_by_name('password2').send_keys(password)
        time.sleep(1)

        self.browser.find_element_by_name("Submit").click()
        time.sleep(3)

        
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys(username)
        time.sleep(2)
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys(password)
        time.sleep(2)
        password_field.send_keys(Keys.RETURN)
        print("    TEST9 passed successfully")
        time.sleep(3)
        #####-----      -----#####





        #####-----TEST10:Logout-----#####
        print("TEST10 : Logout")
        logout_link = self.browser.find_element_by_name('logout')
        logout_link.click()
        print("    TEST10 passed successfully")
        time.sleep(3)
        #####-----      -----#####