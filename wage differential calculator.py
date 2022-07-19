import xlrd                                                                                                             ## import xlrd library

## The wage differential calculator is designed to take a weekly wage input from one male and one female worker, along with characteristics of each that
## are limited to the number of hours worked per week, education level, age, and years of relevant experience. This is meant to use the concept of wage
## differentials for a class project and not meant to be used for professional measures of wage discrimination. Primarily because more factors can be added,
## and because the amount different characteristics effect wages can change depending upon the specific industry. This uses public aggregate data from the
## Bureu of Labor Statistics but is in no way associated with the Bureu of Labor Statistics. This is my submissionfor my Intro to Python class final project.

initfilepath = input(r"Please enter the filepath for BLS_Gender_Wage_Data.xls here: ")                                  ## input filepath for BLS_Gender_Wage_Data.xls note: files must be saved as .xls for xlrd
   
if initfilepath[0] and initfilepath[-1] == '"':                                                                         ## strip quotation marks if present
    filepath = initfilepath[1:-1]                                                                                       
if initfilepath[0] and initfilepath[-1] != '"':
    filepath = initfilepath

location = filepath
wagedata = xlrd.open_workbook(location)                                                                                 ## read data from the Bureu of Labor Statistics
wagesheet = wagedata.sheet_by_index(0)                                                                                  ## create variale to index sheet 1

maleeddata1 = wagesheet.cell_value(38, 2)                                                                               ## pull data from BLS_Gender_Wage_Data.xls based on cell location on excell sheet
maleeddata2 = wagesheet.cell_value(39, 2)                                                                               ## all stored as global variables
maleeddata3 = wagesheet.cell_value(40, 2)
maleeddata4 = wagesheet.cell_value(41, 2)

femaleeddata1 = wagesheet.cell_value(38, 5)
femaleeddata2 = wagesheet.cell_value(39, 5)
femaleeddata3 = wagesheet.cell_value(40, 5)
femaleeddata4 = wagesheet.cell_value(41, 5)

maleagedata1 = wagesheet.cell_value(7, 2)
maleagedata2 = wagesheet.cell_value(8, 2)
maleagedata3 = wagesheet.cell_value(9, 2)
maleagedata4 = wagesheet.cell_value(10, 2)
maleagedata5 = wagesheet.cell_value(11, 2)
maleagedata6 = wagesheet.cell_value(12, 2)
maleagedata7 = wagesheet.cell_value(13, 2)

femaleagedata1 = wagesheet.cell_value(7, 5)
femaleagedata2 = wagesheet.cell_value(8, 5)
femaleagedata3 = wagesheet.cell_value(9, 5)
femaleagedata4 = wagesheet.cell_value(10, 5)
femaleagedata5 = wagesheet.cell_value(11, 5)
femaleagedata6 = wagesheet.cell_value(12, 5)
femaleagedata7 = wagesheet.cell_value(13, 5)

print("Please input the weekly wages of the workers.")
fwage = input("weekly wage of female worker: ")                                                 ## take user input for data related to specific situation, all stored as global variables
mwage = input("weekly wage of male worker: ")
print("Please input the weekly hours of the workers.")
fhours = input("hours worked per week by female worker: ")
mhours = input("hours worked per week male worker: ")
print("For education level for the workers, please input a number of 0 through 3, they are as follows:")
print("0: less than a high school diploma")
print("1: Highschool Diploma or GED")
print("2: Some college or Associates Degree")
print("3: Bachelor's Degree or higher")
melevel = input("Education level of male worker: ")
felevel = input("Education level of female worker: ")
print("Please input the ages of the workers.")
mage = input("Age of male worker: ")
fage = input("Age of female worker: ")
print("Please input the years of relevant experience for the workers.")
mexp = input("Years of experience for male worker: ")
fexp = input("Years of experience for female worker: ")

ederrmess = "Error: edecation level input was not 0 through 3."
agerrmess = "Ages under 16 not accounted for."

class main():                                                       ## main class containing main method                                                   

    def main():                                                     ## main method to call the methods in class calculator
        
        medmult = calculator.maleelevel()
        fedmult = calculator.femaleelevel()
        mahours = calculator.malehours()
        fehours = calculator.femalehours()
        mexpadjust = calculator.maleexperience()
        fexpadjust = calculator.femaleexperience()
        femageadjust = calculator.femaleage()
        malageadjust = calculator.maleage()
        malechar = calculator.mchar(medmult, mahours, mexpadjust, malageadjust)
        femalechar = calculator.fchar(fedmult, fehours, fexpadjust, femageadjust)
        hourwagem = calculator.mhourwage(malechar)
        hourwagef = calculator.fhourwage(femalechar)
        calculator.wagediff(malechar, femalechar, hourwagef, hourwagem)
        
        return

class calculator(object):                                                               ##calculator class containing all methods used in main class

    def wagediff(malechar ,femalechar, hourwagef, hourwagem):                           ##the wage difference calculator, where the final calculation is completed
        

        wagediscdiff = round(malechar * (hourwagem - hourwagef), 2)
        chardiscdiff = round(hourwagef * (malechar - femalechar), 2)
        totaldiff = wagediscdiff + chardiscdiff

        print("Total weekly wage differential:", totaldiff)                             
        print("Salary differences due to wage discrimination:", wagediscdiff)
        print("Salary differences due to a combination of non-discrimination and characteristic discrimination factors:", chardiscdiff)

        return


    def maleelevel():                           ## takes the user input male education level and returns the appropriate multipier for that level (calculated based upon data from BLS_Gender_Wage_Data.xls)


        elevelm = int(melevel)
        
        if elevelm == 0:
            return 1
        
        if elevelm == 1:
            return maleeddata2/maleeddata1

        if elevelm == 2:
            return maleeddata3/maleeddata1

        if elevelm == 3:
            return maleeddata4/maleeddata1

        else:                                   ##error message for inproper inputs
            print(ederrmess)
            return

    def femaleelevel():                         ## takes the user input female education level and returns the appropriate multiplier (calculated based upon data from BLS_Gender_Wage_Data.xls)
        
        elevelf = int(felevel)
        
        if elevelf == 0:
            return 1
        if elevelf == 1:
            return femaleeddata2/femaleeddata1

        if elevelf == 2:
            return femaleeddata3/femaleeddata1

        if elevelf == 3:
            return femaleeddata4/femaleeddata1

        else:                                    ##error message for inproper inputs
            print(ederrmess)

    def maleage():                               ## takes user input male age and returns the approprate multiplier (calculated based upon data from BLS_Gender_Wage_Data.xls)
        
        malage = int(mage)

        if 16 <= malage <= 19:
            return 1

        if 19 < malage <= 24:
            return maleagedata2/maleagedata1

        if 24 < malage <=34:
            return maleagedata3/maleagedata1
        
        if 34 < malage <= 44:
            return maleagedata4/maleagedata1

        if 44 < malage <= 54:
            return  maleagedata5/maleagedata1

        if 54 < malage <= 64:
            return  maleagedata6/maleagedata1

        if 64 < malage:
            return maleagedata7/maleagedata1

        else:
            print(agerrmess)                        ## error message for inproper inputs
            return

    def femaleage():                                ## takes user input female age and returns the appropriate multiplier (calculated based upon data from BLS_Gender_Wage_Data.xls)

        femage = int(fage)

        if 16 <= femage <= 19:
            return 1
        
        if 19 < femage <= 24:
            return femaleagedata2/femaleagedata1

        if 24 < femage <= 34:
            return femaleagedata3/femaleagedata1

        if 34 < femage <= 44:
            return femaleagedata4/femaleagedata1

        if 44 < femage <= 54:
            return femaleagedata5/femaleagedata1

        if 54 < femage <= 64:
            return femaleagedata6/femaleagedata1

        if 64 < femage:
            return femaleagedata7/femaleagedata1

        else:
            print(agerrmess)                        ## error message for improper inputs
            return

    def mhourwage(malechar):                        ## calculates male hourly wage based upon weekly wage and male characteristics
        mawage = float(mwage)
        hourwagem = mawage/malechar
        return hourwagem

    def fhourwage(femalechar):                      ## calculates female hourly wage based upon weekly wage and female characterstics
        fewage = float(fwage)
        hourwagef = fewage/femalechar
        return hourwagef

    def malehours():                                ## creates float out of mhours
        mahours = float(mhours)
        return mahours

    def femalehours():                              ## creates float out of fhours
        fehours = float(fhours)
        return fehours

    def maleexperience():                           ## creates an experience multiplier for the male worker (uses average 3% yearly raise assumption as income increase to experience)
        maleexp = int(mexp)
        mexpadjust = maleexp * 1.03
        return mexpadjust

    def femaleexperience():                         ## creates an experence multiplier for the female worker (uses average 3% yearly raise assumption as income increase to experience)
        femaleexp = int(fexp)
        fexpadjust = femaleexp * 1.03
        return fexpadjust

    def mchar(medmult, mahours, mexpadjust, maleageadjust):         ## takes the education multiplier, hours, experience mulitplier, and age multiplier for the male worker and returns a male characteristics variable
        malechar = mahours * medmult * mexpadjust * maleageadjust
        return malechar
        
    def fchar(fedmult, fehours, fexpadjust, femageadjust):          ## takes the education multiplier, hours, experience mulitplier, and age multiplier for the female worker and returns a female characteristics variable
        femalechar = fehours * fedmult * fexpadjust * femageadjust
        return femalechar

main.main()                                                         ## call the main class and the main function