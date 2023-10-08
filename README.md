# retable.io-api
https://app.retable.io

https://docs.retable.io/retable-user-guide/retable-api/api
```
import RetableAPI
api_key = "RTBLv1-EqujAOSANmjCGzPCkIFPEnRFU"
retable_id="Y7ICPfEwYkx4pyRM"
retable = RetableAPI.RetableAPI(api_key)

title_to_search = "hh"
#column_id = retable.get_column_id_by_title(retable_id, title_to_search)
if column_id:
    print(column_id)



rows_to_insert = [
        {
            "columns": [
                {
                    "column_id": retable.get_column_id_by_title(retable_id, "Email"),
                    "cell_value": "one@gmail.com"
                },
                
                {
                    "column_id": retable.get_column_id_by_title(retable_id, "pass"),
                    "cell_value": "one178882"
                },
                
            ]
        }
    ]
#inserted_rows = retable.insert_rows_to_retable(retable_id, rows_to_insert)
#print("Inserted Rows:", inserted_rows)

search_term="hh"
#search_result = retable.search_retable(retable_id, column_id, search_term)
#print("Search Result:", search_result)

#deleted_rows = retable.delete_rows_from_retable(retable_id, [  search_result["data"]["rows"][0]["row_id"]  ])
#print("Deleted Rows:", deleted_rows)


#updated_row = retable.update_row_in_retable(retable_id, [  search_result["data"]["rows"][0]["row_id"]  ], column_id, "new_value")
print("Updated Row:", updated_row)


#retable_info = retable.get_retable_info(retable_id)
print("Retable Info:", retable_info)


#retable_data = retable.get_retable_data(retable_id)
print("Retable Data:", retable_data)
```

