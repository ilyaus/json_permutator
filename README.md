# json permutator
Python script that makes permutations from JSON lists.

Input json file (resources/data.json):

    {
        "list-1": [
            "red",
            "blue",
            "orange"
        ],
        "list-2": [
            "tomato",
            "potato",
            "carrots",
            "apples"
        ],
        "list-3": [
            "left",
            "right",
            "down",
            "up"
        ]
    }

Run json permutator:

    python permutator.py --input-file resources/data.json

The script will produce CVS file: resources/data.json.csv

    list-1,list-2,list-3
    red,tomato,left
    red,tomato,right
    red,tomato,down
    red,tomato,up
    red,potato,left
    red,potato,right
    red,potato,down
    red,potato,up
    red,carrots,left
    red,carrots,right
    red,carrots,down
    red,carrots,up
    red,apples,left
    ...