select count(*) from actors

It throws an error...
ERROR:  syntax error at or near ","
LINE 1: ..., last_name, age, number_oscars) VALUES ('Jessica','Alba',,)
                                                                     ^
SQL state: 42601
Character: 88