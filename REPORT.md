
### TC-01: Login success with valid credentials
**Description**:
Enter valid email and password, then verify user is logged in successfully and redirected to the main page.

### TC-02: Login fail with incorrect password
**Description**:
Enter a valid email and an invalid password,then verify the login is rejected and an error message is displayed.

### TC-03: Login fail with empty credentials
**Description**:
Leave both email and password fields empty,click Login, and verify the validation message is displayed.

### TC-04: Search book by name
**Description**:
Search for the keyword "Flutter" and verify that matching books are displayed.

### TC-05: Search book with no matching result
**Description**:
Search for a non-existent keyword and verify that no books are returned

### TC-06: Filter books by category
**Description**:
Filter books by the "Công nghệ" category and verify all displayed books belong to that category.

### TC-07: Search book by author
**Description**:
Search for books written by "Nguyễn Minh Đức" and verify matching results are displayed.

### TC-08: Borrow an available book
**Description**:
Borrow an available book and verify the borrowing operation completes successfully.

### TC-09: View borrowed books
**Description**:
Open the Borrow/Return tab and verify borrowed books are displayed.

### TC-10: Return a borrowed book
**Description**:
Return a borrowed book and verify the return operation completes successfully.

### TC-11: Logout success
**Description**:
 Verify successful logout redirects the user back to the login page.

### TC-12: Switch language to English
**Description**:
Verify the application language can be switched from Vietnamese to English.

### AI Usage Declaration
"The group used ChatGPT to assist with suggesting structure and reviewing for missing test cases; the final content was cross-referenced against the SRS and confirmed by the group."