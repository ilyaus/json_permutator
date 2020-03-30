import json
import logging
import argparse
import csv


logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)-8s:%(message)s')
perm_logger = logging.getLogger('permutator')
perm_logger.setLevel(logging.WARN)


def command_line_args():
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--input-file', type=str, required=True)

    return parser.parse_args()


def data_file_to_json(file_name):
    """
    Reads text file in JSON format and returns it as dict
    """
    perm_logger.debug('Reading file: {}'.format(file_name))

    ret_data = None

    try:
        with open(file_name, 'r') as fp:
            ret_data = json.load(fp)
    except Exception as ex:
        perm_logger.error("Error: {}".format(ex))

    return ret_data


def perm_data_to_dict_list(perm_data):
    """
    Converts list of permutated data into list of dictionaries.
    List of dictionaries is needed to use CSV writer.
    """
    dict_list = list()    

    for row in perm_data:
        dict_row = dict()
        for item in row:
            dict_row[list(item.keys())[0]] = item[list(item.keys())[0]]

        dict_list.append(dict_row)

    perm_logger.debug("Permutated data dictionary: {}".format(dict_list))

    return dict_list


def heap_permutate(data, size, n):
    """
    This function is not used.
    # -- 
    If size is odd  -> swap first and last
    If size is even -> swapfd ith and last
    If size is 1 -> done
    """
    if size == 1:
        perm_logger.debug(data)

    for i in range(0, size - 1):
        if size & 1:
            # odd: swap first and last
            data[0], data[size - 1] = data[size - 1], data[0]
            heap_permutate(data, size - 1, n)
        else:
            # even: swap ith and last
            data[i], data[size - 1] = data[size - 1], data[i]
            heap_permutate(data, size - 1, n)


def add_data_to_perm_table(base_key, values, perm_table):
    """
    Adds list of new items into already permutated list.
 
    """
    ret_perm_table = list()
    
    if len(perm_table) == 0:
        for item in values:
            row = list()
            row.append(dict({base_key: item}))            
            ret_perm_table.append(row)

    else:
        for existing_items in perm_table:
            for new_item in values:
                row = list(existing_items)
                row.append(dict({base_key: new_item}))
                ret_perm_table.append(row)

    return ret_perm_table


def permutate(data):
    """
    Creates permutations of JSON lists.
    """
    
    ret_value = list()

    for key in data.keys():
        perm_logger.debug("Perm table before: {} -> {}".format(data[key], ret_value))
        ret_value = add_data_to_perm_table(key, data[key], ret_value)
        perm_logger.debug("Perm table after: {}".format(ret_value))

    return ret_value


def make_csv_file(file_name, data, fieldnames):
    """
    Create CSV file from permutated data.
    """

    if len(data) == 0:
        perm_logger.info("There no permutations.  Output file is not created.")
        return

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(perm_data_to_dict_list(data))


def main():
    args = command_line_args()

    data = data_file_to_json(args.input_file)
    perm = permutate(data)
    make_csv_file('{}.{}'.format(args.input_file, 'csv'), perm, fieldnames=list(data.keys()))


if __name__ == '__main__': 
    main()
