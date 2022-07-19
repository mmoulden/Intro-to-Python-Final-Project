import xlrd

location = (r"BLS_Gender_Wage_Data.xls")
wagedata = xlrd.open_workbook(location)
wagesheet = wagedata.sheet_by_index(0)

maleeddata1 = wagesheet.cell_value(38, 2)
maleeddata2 = wagesheet.cell_value(39, 2)
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

fwage = input("weekly wage of female worker: ")
mwage = input("weekly wage of male worker: ")
fhours = input("hours of female worker: ")
mhours = input("hours of male worker: ")
print("For education level, please input a number of 0 through 3, they are as follows:")
print("0: less than a high school diploma")
print("1: Highschool Diploma or GED")
print("2: Some college or Associates Degree")
print("3: Bachelor's Degree or higher")
melevel = input("Education level of male: ")
felevel = input("Education level of female: ")
print("Now please input the years of relevant experience")
print("please input the ages of the workers: ")
mage = input("Age of male worker: ")
fage = input("Age of female worker: ")
mexp = input("Years of experience for male worker: ")
fexp = input("Years of experience for female worker: ")

ederrmess = "Error: edecation level input was not 0 through 3."
agerrmess = "Ages under 16 not accounted for."


class main(): 

    def main():
        
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
        hourwagem = calculator.mhourwage(mahours)
        hourwagef = calculator.fhourwage(fehours)
        calculator.wagediff(malechar, femalechar, hourwagef, hourwagem)
        
        return

class calculator(object):

    def wagediff(malechar ,femalechar, hourwagef, hourwagem):
        

        discdiff = malechar * (hourwagem - hourwagef)
        nondiscdiff = hourwagef * (malechar - femalechar)
        totaldiff = discdiff + nondiscdiff

        print("Total salary differential:", totaldiff)
        print("Salary differences due to discrimination:", discdiff)
        print("Salary differences due to non-discriminatatory factors:", nondiscdiff)

        return


    def maleelevel():


        elevelm = int(melevel)
        
        if elevelm == 0:
            
            return 1
        
        if elevelm == 1:
            
            return maleeddata2/maleeddata1

        if elevelm == 2:
            
            return maleeddata3/maleeddata1

        if elevelm == 3:
            
            return maleeddata4/maleeddata1

        else:
            print(ederrmess)
            return

    def femaleelevel():
        
        elevelf = int(felevel)
        
        if elevelf == 0:
            
            return 1
        
        if elevelf == 1:
            
            return femaleeddata2/femaleeddata1

        if elevelf == 2:
            
            return femaleeddata3/femaleeddata1

        if elevelf == 3:
            
            return femaleeddata4/femaleeddata1

        else:
            print(ederrmess)

    def maleage():
        
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
            print(agerrmess)
            return

    def femaleage():

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
            print(agerrmess)
            return

    def mhourwage(mahours):
        mawage = float(mwage)
        hourwagem = mawage/mahours
        return hourwagem

    def fhourwage(fehours):
        fawage = float(fwage)
        hourwagef = fawage/fehours 
        return hourwagef

    def malehours():
        mahours = float(mhours)
        return mahours


    def maleexperience():
        maleexp = int(mexp)
        mexpadjust = maleexp * 1.03
        return mexpadjust

    def femaleexperience():
        femaleexp = int(fexp)
        fexpadjust = femaleexp * 1.03
        return fexpadjust

    def femalehours():
        fehours = float(fhours)
        return fehours

    def mchar(medmult, mahours, mexpadjust, maleageadjust):
        malechar = mahours/(medmult * mexpadjust * maleageadjust)
        return malechar
        
    def fchar(fedmult, fehours, fexpadjust, femageadjust):
        femalechar = fehours/(fedmult * fexpadjust * femageadjust)
        return femalechar

main.main()

