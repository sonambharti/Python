x=int(input("Enter the no: "))
def numbers_to_months(x):
    switcher ={
        1: ("January"),
        2: "Feburary",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    result=switcher.get(x, lambda:"Invalid")
    print(result)

