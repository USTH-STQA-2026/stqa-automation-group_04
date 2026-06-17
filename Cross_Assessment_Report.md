# Cross-Assessment Report - Group 10 - Automation Testing

## File Assessment

| File                   | Maximum Score | Awarded Score | Brief Comments                                                                                                                                                              |
| ---------------------- | ------------: | ------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| test_login.py          |           2.0 |           1.8 | Good coverage of successful login, incorrect password, blank fields, email format validation, and password masking. Appropriate use of parameterization and xfail.          |
| test_view_book.py      |           2.0 |           1.7 | Covers book listing, book status display, and status updates after borrowing and returning. Some assertions are relatively broad and could be more precise.                 |
| test_search.py         |           2.0 |          1.85 | Covers a wide range of search and filtering scenarios. Includes case-insensitive validation and effectively uses xfail to document a filtering bug.                         |
| test_borrow_return.py  |           2.0 |           1.9 | Comprehensive coverage of borrowing and returning workflows, borrowing limits, suspended/expired members, overdue cases, and permission checks. Strong negative testing.    |
| test_admin_features.py |           2.0 |           1.8 | Covers administrative functions, member creation, overdue checking, member management, and role-based access control. Several test cases successfully identify defects.     |
| test_borrow_receipt.py |           2.0 |           1.5 | Includes validation of borrowing records for both librarians and members. However, assertions are relatively weak and mainly verify data existence rather than correctness. |
| test_general.py        |           2.0 |           1.7 | Covers logout and language-switching functionality. Test scenarios are reasonable, but the testing scope remains somewhat limited.                                          |

---

## Overall Assessment

| Criteria                 | Maximum Score | Awarded Score | Brief Comments                                                                                               |
| ------------------------ | ------------: | ------------: | ------------------------------------------------------------------------------------------------------------ |
| Requirements Coverage    |           2.0 |           1.9 | Covers almost all requirements from REQ-01 to REQ-08.                                                        |
| Test Design              |           2.0 |           1.8 | Includes a good balance of happy-path, negative, and permission-based test scenarios.                        |
| Bug Detection Capability |           2.0 |           1.9 | Effective use of xfail to document, track, and validate known defects.                                       |
| Assertion Quality        |           2.0 |           1.6 | Some test cases rely on weak test oracles or use overly broad pass conditions.                               |
| Consistency              |           2.0 |           1.7 | Well-structured overall, but there are duplicate test case identifiers and dependencies on seeded test data. |
| **Total Score**          |      **10.0** |       **8.9** | Strong coverage with extensive edge cases and permission-based testing.                                      |
