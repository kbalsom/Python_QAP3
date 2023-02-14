# A program written for Honest Harry Car Sales
# to keep track of sales by generating sales receipts.

# Written by Kara Balsom
# Date written: February 22, 2022

# Import libraries:

import datetime

# Define Constants:

HST_RATE = .15
MAX_SELL_PRICE = 50000.00
LICENSE_FEE_LIMIT = 5000.00
LICENSE_FEE_5000_UNDER = 75.00
LICENSE_FEE_OVER_5000 = 165.00
TRANSFER_FEE_LIMIT = 20000.00
TRANSFER_FEE = 0.01
LUX_TAX_RATE = 0.016
FINANCE_FEE = 39.99

# Inputs and validations:

while True:
# Starts Loop for whole program.

    while True:
        try:
            InvDate = input("Enter the Invoice Date (YYYY-MM-DD): ")
            InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
        except:
            print("Invoice Date is not a valid format (YYYY-MM-DD) - Please re-enter.")
        else:
            break

    while True:
        CustFirstName = input("Enter the Customer's First Name: ").title()

        if CustFirstName == "":
            print("Customer's First Name cannot be blank - Please re-enter.")
        else:
            break

    while True:
        CustLastName = input("Enter the Customer's Last Name: ").title()

        if CustLastName == "":
            print("Customer's Last Name cannot be blank - Please re-enter.")
        else:
            break

    while True:
        PhoneNum = input("Please enter the Customer's Phone Number (0000000000): ")

        if PhoneNum == "":
            print("Customer's Phone Number cannot be blank - Please re-enter.")
        elif PhoneNum.isdigit() == False:
            print("Customer's Phone Number can only contain numbers (0000000000) - Please re-enter.")
        elif len(PhoneNum) != 10:
            print("Customer's Phone Number must be 10 digits long (0000000000) - Please re-enter.")
        else:
            break

    while True:
        StreetAdd = input("Enter the Customer's Street Address: ").title()

        if StreetAdd == "":
            print("Customer's Street Address cannot be blank - Please re-enter.")
        else:
            break

    while True:
        City = input("Enter City: ").title()

        if City == "":
            print("City cannot be blank - Please re-enter.")
        else:
            break

    while True:
        Province = input("Enter Province / Territory (XX): ").upper()

        if Province == "":
            print("Province / Territory cannot be blank (XX) - Please re-enter.")
        elif Province.isalpha() == False:
            print("Province / Territory cannot include numbers - Please re-enter.")
        elif len(Province) != 2:
            print("Province / Territory must be 2 letters (XX) - Please re-enter.")

        else:
            break

    while True:
        Postal = input("Enter Postal Code (A1A1A1): ").upper()

        if Postal == "":
            print("Postal Code cannot be blank (A1A1A1) - Please re-enter.")
        elif len(Postal) != 6:
            print("Postal Code must be 6 characters - Please re-enter.")
        else:
            break

    while True:
        PlateNum = input("Enter the Licence Plate Number (XXX999): ").upper()

        if PlateNum == "":
            print("License Plate Number cannot be blank - Please re-enter.")
        elif len(PlateNum) != 6:
            print("License Plate Number must be 6 characters (XXX999) - Please re-enter.")
        elif PlateNum[0:3].isalpha() == False:
            print("License Plate Number must start with 3 letters (XXX999) - Please re-enter.")
        elif PlateNum[3:6].isdigit() == False:
            print("License Plate Number must end with 3 numbers (XXX999) - Please re-enter.")
        else:
            break

    while True:
        CarMake = input("Enter the Car Make (ex. Toyota): ").title()

        if CarMake == "":
            print("Car Make cannot be blank - Please re-enter.")
        else:
            break

    while True:
        CarMod = input("Enter the Car Model (ex. Corolla): ").title()

        if CarMod == "":
            print("Car Model cannot be blank - Please re-enter.")
        else:
            break

    while True:
        CarYear = input("Enter the Car Year (0000): ")

        if CarYear == "":
            print("Car Year cannot be blank (0000) - Please re-enter.")
        elif len(CarYear) != 4:
            print("Car Year must be 4 digits (0000) - Please re-enter.")
        elif CarYear.isdigit() == False:
            print("Car Year must only contain numbers (0000) - Please re-enter.")
        else:
            break

    while True:
        try:
            SellPrice = float(input("Enter the Selling Price (Cannot exceed $50,000.00): "))
        except:
            print("Selling Price is not a valid number - Please re-enter.")
        else:
            if SellPrice > MAX_SELL_PRICE:
                print("Selling Price cannot exceed $50,000.00 - Please re-enter.")
            else:
                break


    while True:
        try:
            TradeAmnt = float(input("Enter the Trade In Amount (Cannot exceed Selling Price): "))
        except:
            print("Trade In Amount is not a valid number - Please re-enter.")
        else:
            if TradeAmnt > SellPrice:
                print("Trade In Amount cannot exceed Selling Price - Please re-enter.")
            else:
                break

    while True:
        SalesName = input("Enter Salesperson's Name: ")

        if SalesName == "":
            print("Salesperson's Name cannot be blank - Please re-enter.")
        else:
            break

    while True:
        CredCardNum = input("Enter Credit Card Number: ")

        if CredCardNum == "":
            print("Credit Card Number cannot be blank - Please re-enter.")
        elif CredCardNum.isdigit() == False:
            print("Credit Card Number can only contain numbers - Please re-enter.")
        else:
            break

    while True:
        try:
            CardExpDate = input("Enter the Credit Card Expiry Date (YYYY-MM-DD): ")
            CardExpDate = datetime.datetime.strptime(CardExpDate, "%Y-%m-%d")
        except:
            print("Credit Card Expiry Date is not a valid format (YYYY-MM-DD) - Please re-enter.")
        else:
            break

# Perform required calculations:

    PriceAftTrade = SellPrice - TradeAmnt
    Tax = SellPrice * HST_RATE

    if SellPrice <= LICENSE_FEE_LIMIT:
        LicenseFee = LICENSE_FEE_5000_UNDER
    else:
        LicenseFee = LICENSE_FEE_OVER_5000

    if SellPrice <= TRANSFER_FEE_LIMIT:
        TransFee = SellPrice * TRANSFER_FEE
    else:
        TransFee = (SellPrice * TRANSFER_FEE) + (SellPrice * LUX_TAX_RATE)

    TotSalePrice = PriceAftTrade + Tax + LicenseFee + TransFee

    ReceiptNo = CustFirstName[0] + CustLastName[0] + "-" + PlateNum[3: 6] + "-" + PhoneNum[6: 11]


# Display Payment Schedule Loop:

    print()
    print("# Years    # Payments    Financing Fee    Total Price  Monthly Payment")
    print("----------------------------------------------------------------------")

    for Years in range(1, 5):
        PaymentNum = Years * 12
        FinanceFee = FINANCE_FEE * Years
        TotPrice = TotSalePrice + FinanceFee
        MonPayment = TotPrice / PaymentNum

        FinanceFeeDsp = "${:,.2f}".format(FinanceFee)
        TotPriceDsp = "${:,.2f}".format(TotPrice)
        MonPaymentDsp = "${:,.2f}".format(MonPayment)

        print("    {:>1d}           {:>2d}          {:>10s}     {:>10s}       {:>10s}".format(Years, PaymentNum, FinanceFeeDsp, TotPriceDsp, MonPaymentDsp))
        print()

# Customer input for payment schedule:

    while True:
        try:
            PaymentYears = int(input("Please choose a Payment Schedule (1 - 4): "))
        except:
            print("Payment Schedule is not a valid number - Please re-enter.")
        else:
            if PaymentYears < 1 or PaymentYears > 4:
                print("Payment Schedule must be between 1 and 4 - Please re-enter.")
            else:
                break


# Calculations for the payment terms:

    TotPayments = PaymentYears * 12
    FirstPayDate = InvDate + datetime.timedelta(days=30)

# Print and format outputs:

    print()
    print("        Honest Harry Car Sales")
    print("       Used Car Sale and Receipt")
    print()
    InvDateDsp = InvDate.strftime("%B %d, %Y")
    print("Invoice Date: {:>18s}".format(InvDateDsp))
    print("Receipt No: {:>11s}".format(ReceiptNo))
    print()

    print("Sold to:")
    print("     {:<1s}. {:<26s}".format(CustFirstName[0], CustLastName))
    print("     {:<29s}".format(StreetAdd))
    CityDsp = City + ","
    print("     {:<14} {:<2s}, {:<6s}".format(CityDsp, Province, Postal))
    print()
    print("Car details:")
    print("     {:<4s} {:<13s} {:<10s}".format(CarYear, CarMake, CarMod))
    print("------------------------------------")

    SellPriceDsp = "${:,.2f}".format(SellPrice)
    print("Sale Price:               {:>10s}".format(SellPriceDsp))
    TradeAmntDsp = "${:,.2f}".format(TradeAmnt)
    print("Trade Allowance:          {:>10s}".format(TradeAmntDsp))
    PriceAftTradeDsp = "${:,.2f}".format(PriceAftTrade)
    print("Price after Trade:        {:>9s}".format(PriceAftTradeDsp))
    print("                          ----------")

    TaxDsp = "${:,.2f}".format(Tax)
    print("HST:                       {:>9s}".format(TaxDsp))
    LicenseFeeDsp = "${:,.2f}".format(LicenseFee)
    print("License Fee:              {:>10s}".format(LicenseFeeDsp))
    TransFeeDsp = "${:,.2f}".format(TransFee)
    print("Transfer Fee:             {:>10s}".format(TransFeeDsp))
    print()

    TotSalePriceDsp = "${:,.2f}".format(TotSalePrice)
    print("Total Sales Cost:         {:>10s}".format(TotSalePriceDsp))
    print("------------------------------------")

    print("Terms: {:<1d}          Total Payments: {:>2d}".format(PaymentYears, TotPayments))
    MonPaymentDsp = "${:,.2f}".format(MonPayment)
    print("Monthly payment:           {:>9s}".format(MonPaymentDsp))
    FirstPayDateDsp = FirstPayDate.strftime("%d-%b-%y").upper()
    print("First payment date:        {:>9s}".format(FirstPayDateDsp))
    print()

    print("        Honest Harry Car Sales")
    print("  Best used cars at the best price!")
    print()

# End loop:

    while True:
        Continue = input("Do you want to Process Another Sale (Y / N)?: ").upper()
        if Continue != "Y" and Continue != "N":
            print("Enter Y to Process Another Sale, or N to exit - Please re-enter.")
        elif Continue == "N":
            exit()
        else:
            break









































































