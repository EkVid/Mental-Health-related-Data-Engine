import matplotlib.pyplot as plt
import sql_tools
import sqlite3 as sql


def add_data(file_name, empty_list):
    '''
    INPUT:
      A file and an empty list
    OUTPUT:
      A list with all the data from the file inputted
    '''

    my_file = open(file_name, "r")
    with open(file_name, "r") as f:
        for line in f:
            x = line[:-1]
            empty_list.append(x)
    my_file.close()

    return empty_list


def plot_comparison(title_name, x_name, y_name, arg_1, arg_2, arg_3, label_1, label_2):
    '''
    INPUT:
      Desired title name, x-axis name, y-axis,name, four arguments that want to
      be plotted, and the desired label (first arg will be plotted on x-axis,
      second arg will be plotted on y-axis). The legend will be on top right corner
    OUTPUT:
      A plotted graph compares two components with labels based on all the components entered
    '''
    plt.plot(arg_1, arg_2, label=label_1)
    plt.plot(arg_1, arg_3, label=label_2)
    plt.title(title_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    plt.show()


def plot_data_linear(title_name, x_name, y_name, arg_1, arg_2, colors):
    '''
    INPUT:
      Desired title name, x-axis name, y-axis,name, two arguments that want to
      be plotted, and the desired color (first arg will be plotted on x-axis,
      second arg will be plotted on y-axis)
    OUTPUT:
      A graph plotted based on all the components entered
    '''
    plt.plot(arg_1, arg_2, color=colors)
    plt.title(title_name)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


# add data into a list
all_data = []
bipolar_data = []
add_data("data.csv", all_data)           # Anxiety Data
add_data("bipolar.csv", bipolar_data)    # Bipolar Data

# Get 2019's data for all countries
year_2019_data = []
bi_2019_data = []
for i in all_data:
    if '2019' in i:
        year_2019_data.append(i)         # Anxiety Data

for i in bipolar_data:
    if '2019' in i:
        bi_2019_data.append(i)           # Bipolar Data

# Get countries, acronmies, and percentage
country = []
acronmy = []
percent = []
percent_bi = []

for x in year_2019_data:
    country.append(x.split(",")[0])
    acronmy.append(x.split(',')[1])
    percent.append(float(x.split(',')[-1]))    # anxiety data for 2019

for i in bi_2019_data:
    percent_bi.append(float(i.split(',')[-1]))  # bipolar data for 2019

# Get all the years with the last two numbers
all_years = []

for y in all_data:
    all_years.append(y.split(',')[-2])
all_years.pop(0)
all_years_2 = list(set(all_years))
all_years_2.sort()

all_years_final = []
for i in all_years_2:
    all_years_final.append(i[2:4])

while 1:

    option = ('''
    B = Learn more about Bipolar Disorder Prevalence in each country
    M = Learn more about Anxiety prevalence in each country
    P = Print out all data used for your reference
    E = End the program
    Choose an option: ''')

    menu_option = input(option)

    if menu_option == 'B':
        checkpoint = True
        print(
            "The problem of increasing bipolar disorder has troubled the researchers for decades")
        while checkpoint:
            data_bi = []
            question = input(
                "You can type in the Country Name to check that country's Bipolar Disorder Prevalence from 1990 - 2019 or 'Next' to proceed: ")
            if question in country:
                for i in bipolar_data:
                    if question in i:
                        data_bi.append(float(i.split(',')[-1]))
                plot_data_linear(question + " 's Bipolar Disorder Prevalence from 1990 - 2019",
                                 "Years", "Percent", all_years_final, data_bi, 'green')

            elif question == 'Next':
                print("\n\n\n\n\n\n\n\n\n\nNow let's compare different countries' Bipolar Disorder Prevalence Percantage, type in two countries "
                      + "or 'No' to end this section")
                while 1:
                    data_bi_2 = []
                    question_2 = input("Country Name 1 or 'No': ")
                    if question_2 in country:
                        for i in bipolar_data:
                            if question_2 in i:
                                data_bi_2.append(float(i.split(',')[-1]))
                        question_3 = input("Country Name 2 or 'No': ")
                        data_bi_3 = []
                        if question_3 in country:
                            for i in bipolar_data:
                                if question_3 in i:
                                    data_bi_3.append(
                                        float(i.split(',')[-1]))
                            print("A graph has been plotted")

                            plot_comparison("Comparison between two countries' Bipolar Disorder Prevalence",
                                            "Years", "Bipolar Disorder Prevalence Percentage", all_years_final, data_bi_2, data_bi_3, question_2, question_3)
                        elif question_3 == 'No':
                            print("Program Ended")
                            checkpoint = False
                            break

                        else:
                            print(
                                "Probably the country doesn't exist or there is a typo, please try again!")

                    elif question_2 == 'No':
                        print("Program Ended")
                        checkpoint = False
                        break

                    else:
                        print(
                            "Probably the country doesn't exist or there is a typo, please try again!")
            else:
                print(
                    "Probably the country doesn't exist or there is a typo, please try again!")

    elif menu_option == 'M':
        turning_point = True
        print(
            "Nowadays, the eleviation of anxiety level is also becoming a big issue in the society.")
        while turning_point:
            data = []
            ask = input(
                "You can type in the Country Name to check that country's Anxiety Prevalence from 1990 - 2019 or 'Next' to proceed: ")
            if ask in country:
                for i in all_data:
                    if ask in i:
                        data.append(float(i.split(',')[-1]))
                plot_data_linear(ask + "'s Anxiety Prevalance from 1990 - 2019",
                                 "Years", "Percent", all_years_final, data, 'red')

            elif ask == 'Next':
                print("\n\n\n\n\n\n\n\n\n\nNow let's compare different countries' Anxiety Prevalence Percantage, type in two countries "
                      + "or 'No' to end this section")
                while 1:
                    data_1 = []
                    ask_2 = input("Country Name 1 or 'No': ")
                    if ask_2 in country:
                        for i in all_data:
                            if ask_2 in i:
                                data_1.append(float(i.split(',')[-1]))
                        ask_3 = input("Country Name 2 or 'No': ")
                        data_2 = []
                        if ask_3 in country:
                            for i in all_data:
                                if ask_3 in i:
                                    data_2.append(float(i.split(',')[-1]))
                            print("A graph has been plotted")

                            plot_comparison("Comparison between two countries' Anxiety Prevalence",
                                            "Years", "Anxiety Prevalence Percentage", all_years_final, data_1, data_2, ask_2, ask_3)
                        elif ask_3 == 'No':
                            print("Program Ended")
                            turning_point = False
                            break

                        else:
                            print(
                                "Probably the country doesn't exist or there is a typo, please try again!")

                    elif ask_2 == 'No':
                        print("Program Ended")
                        turning_point = False
                        break

                    else:
                        print(
                            "Probably the country doesn't exist or there is a typo, please try again!")
            else:
                print(
                    "Probably the country doesn't exist or there is a typo, please try again!")

    elif menu_option == 'P':
        print("Here are all the data used in the program merged into a single table with the first row of percent representing Bipolar Disorder"
              + " and second row representing Anxiety Prevalence")
        db_handle = sql.connect("test.db")

        in_file = open("bipolar.csv", "r")
        sql_tools.csv_to_table(db_handle, in_file, "Bipolar_Disorder", [
                               'TEXT', 'TEXT', 'INTEGER', 'REAL'])
        in_file.close()

        in_file = open("data.csv", "r")
        sql_tools.csv_to_table(db_handle, in_file, "Anxiety", [
                               'TEXT', 'TEXT', 'INTEGER', 'REAL'])
        in_file.close()

        my_list = """
        SELECT Bipolar_Disorder.Entity, Bipolar_Disorder.Code, Bipolar_Disorder.Year, Bipolar_Disorder.Percent, Anxiety.Percent
        FROM Bipolar_Disorder, Anxiety
        WHERE Bipolar_Disorder.Entity = Anxiety.Entity
        AND Bipolar_Disorder.Code = Anxiety.Code
        AND Bipolar_Disorder.Year = Anxiety.Year
        """

        sql_tools.print_select(db_handle, my_list)

        db_handle.close()

    elif menu_option == 'E':
        print("Program Ended.")
        break

    else:
        print("Invalid input, please try again!")
