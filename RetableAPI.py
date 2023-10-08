import requests
import json
class RetableAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.retable.io/v1/public"
        self.column_mapping = self.load_column_mapping()

    def _send_request(self, method, endpoint, data=None):
        headers = {'ApiKey': self.api_key}
        response = None

        if method == 'GET':
            response = requests.get(f'{self.base_url}/{endpoint}', headers=headers)
        elif method == 'POST':
            response = requests.post(f'{self.base_url}/{endpoint}', headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(f'{self.base_url}/{endpoint}', headers=headers, json=data)
        elif method == 'DELETE':
            response = requests.delete(f'{self.base_url}/{endpoint}', headers=headers, json=data)

        if response:
            return response.json()
        else:
            return None
    
    def load_column_mapping(self):
        try:
            with open('column_mapping.json', 'r') as file:
                return json.load(file)
        except :
            return {}

    def save_column_mapping(self):
        with open('column_mapping.json', 'w') as file:
            json.dump(self.column_mapping, file)

    def get_column_id_by_title(self, retable_id, title):
        if retable_id in self.column_mapping and title in self.column_mapping[retable_id]:
            return self.column_mapping[retable_id][title]

        retable_info = self.get_retable_info(retable_id)
        if retable_info:
            columns = retable_info['data']['columns']
            for column in columns:
                if column['title'] == title:
                    if retable_id not in self.column_mapping:
                        self.column_mapping[retable_id] = {}
                    self.column_mapping[retable_id][title] = column['column_id']
                    self.save_column_mapping()
                    return column['column_id']
        return None
    
    def get_retable_data(self, retable_id):
        return self._send_request('GET', f'retable/{retable_id}/data')

    
    def insert_rows_to_retable(self, retable_id, rows):
        data = {
            "data": rows
        }
        return self._send_request('POST', f'retable/{retable_id}/data', data)

    
    def update_row_in_retable(self, retable_id, row_id, column_id, update_cell_value):
        data = {
            "rows": [
                {
                    "row_id": row_id,
                    "columns": [
                        {
                            "column_id": column_id,
                            "update_cell_value": update_cell_value
                        }
                    ]
                }
            ]
        }
        return self._send_request('PUT', f'retable/{retable_id}/data', data)

    
    def delete_rows_from_retable(self, retable_id, row_ids):
        data = {"row_ids": row_ids}
        return self._send_request('DELETE', f'retable/{retable_id}/data', data)

    
    def search_retable(self, retable_id, column_id, term):
        return self._send_request('GET', f'retable/{retable_id}/search?columnID={column_id}&term={term}')

   
    def get_retable_info(self, retable_id):
        return self._send_request('GET', f'retable/{retable_id}')

