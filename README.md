# SQL Parser

SQLite dialect SQL parser written in Python. Based on the ANTLR4 grammar by Bart Kiers.

## Input

```
cat input.txt

SELECT log AS x FROM t1
GROUP BY x
HAVING count(*) >= 4
ORDER BY max(n) + 0
```

## Output

```
./Test.py input.txt

(parse (sql_stmt_list (sql_stmt (factored_select_stmt 
(select_core SELECT (result_column (expr (column_name (any_name log))) AS (column_alias x)) 
FROM (table_or_subquery (table_name (any_name t1))) 
GROUP BY (expr (column_name (any_name x))) 
HAVING (expr (expr (function_name (any_name count)) ( * )) >= (expr (literal_value 4)))) 
ORDER BY (ordering_term (expr (expr (function_name (any_name max)) ( (expr (column_name (any_name n))) )) + (expr (literal_value 0))))))) <EOF>)
```
