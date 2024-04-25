# alVatross

alVatross is a Vlnerabirity Web Application.

alVatross mean the "albatross".
This change b to v, Because V meaning Vulnerability.
And, This is a mistake like a Vulnerability.


## Default User

Admin/ adminadmin

## UP Server
```
python alVatross/manage.py runserver [port number]
```


## Unit Test
Command

### Run Unit Test
```
coverage run --source '.' manage.py test 
```

### Output Converage Report
```
$ coverage report
Name                                      Stmts   Miss  Cover
-------------------------------------------------------------
alVatross/__init__.py                         0      0   100%
alVatross/apps.py                             3      3     0%
alVatross/form/__init__.py                    0      0   100%
alVatross/form/post.py                       10      0   100%
alVatross/form/user.py                        6      0   100%
alVatross/migrations/0001_initial.py          7      0   100%
alVatross/migrations/__init__.py              0      0   100%
alVatross/models/__init__.py                  1      0   100%
alVatross/models/post.py                     28      0   100%
alVatross/settings.py                        20      0   100%
alVatross/tests/__init__.py                   0      0   100%
alVatross/tests/models/__init__.py            0      0   100%
alVatross/tests/models/test_post.py          63      0   100%
alVatross/tests/views/__init__.py             0      0   100%
alVatross/tests/views/test_index.py          19      0   100%
alVatross/tests/views/test_login.py          53      0   100%
alVatross/tests/views/test_myprofile.py      19      0   100%
alVatross/tests/views/test_post.py          159      0   100%
alVatross/tests/views/test_user.py           83      0   100%
alVatross/urls.py                             9      0   100%
alVatross/views/__init__.py                   0      0   100%
alVatross/views/index.py                      5      0   100%
alVatross/views/login.py                     52      0   100%
alVatross/views/myprofile.py                  6      0   100%
alVatross/views/post.py                      44      1    98%
alVatross/views/users.py                     68      8    88%
alVatross/wsgi.py                             4      4     0%
manage.py                                     9      2    78%
-------------------------------------------------------------
TOTAL                                       668     18    97%
```

### Output Coverage Repoert as html
```
$ coverage html
Wrote HTML report to htmlcov/index.html
```

