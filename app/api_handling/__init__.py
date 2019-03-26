class api_handling:

    def __init__(self, csv_url):
        self.path = {}

        import csv
        import json

        csv.register_dialect('myDialect',
        delimiter = ',',
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True)

        try:
            with open(csv_url, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data = dict(row)
                    current_path = data.get('path','/')
                    if current_path not in self.path:
                        self.path[current_path] = {}
                    
                    self.path[current_path][data.get('method','GET')] = {
                        'response': json.loads(data.get('response','').replace('\n','')),
                        'wait':data.get('wait',0)
                        }
                csvfile.close()

        except Exception as error:
            print('Error on reading csv: ', error)