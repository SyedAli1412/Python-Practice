from collections import defaultdict
from functools import reduce


class GroupBy:

    def __init__(self, records, number_data):
        self.records = records
        self.number_data = number_data

    # Function to Group By Records with respective of crime
    def normal_convention_loop(self):
        crimes_records = {}
        for record in self.records:
            crime = record['crime']
            if crime in crimes_records:
                crimes_records[crime].append(record)
            else:
                crimes_records[crime] = [record]
        return crimes_records

    # Function to Group By Records using Higher-order function (map)
    # Map returns object so explicit casting to list is necessary else we get memory location of object being created
    def map_records(self):
        crimes_records = {}
        _ = list(map(lambda record: crimes_records[record['crime']].append(record) if record[
                                                                                          'crime'] in crimes_records else crimes_records.update(
            {record['crime']: [record]}), self.records))
        return crimes_records

    # Function to Group By Records using Higher-order function (reduce)
    #  Use reduce with a default-dict to group records by crime
    def reduce_records(self):
        crimes_records = reduce(
            lambda acc, record: acc[record['crime']].append(record) or acc if record['crime'] in acc else acc.update(
                {record['crime']: [record]}) or acc, self.records, defaultdict(list))
        # Convert the default-dict to a regular dictionary
        crimes_records = dict(crimes_records)
        return crimes_records

    #  Function to Group By Records using Higher-order functions (reduce and then filtering)
    #  Use reduce with a default-dict to group records by crime
    #  Use filter to filter the records returned from reduce
    def filter_reduce_records(self):
        crimes_records = reduce(
            lambda acc, record: acc[record['crime']].append(record) or acc if record['crime'] in acc else acc.update(
                {record['crime']: [record]}) or acc, self.records, defaultdict(list))
        # Convert the default-dict to a regular dictionary
        crimes_records = dict(crimes_records)
        crimes_records = list(filter(lambda record: record['crime'] == 'Drinking', crimes_records['Drinking']))
        return crimes_records

    def double_value(self):
        doubled_value_list = list(map(lambda number: number * 2, self.number_data))
        return doubled_value_list

    def max_value(self):
        numbers = [4, 2, 8]
        max1 = None
        max2 = None
        for number in numbers:
            if max1 is None or number > max1:
                max2 = max1
                max1 = number
            else:
                max2 = number
        return max1, max2
