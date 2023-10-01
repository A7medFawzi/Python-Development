print('''
████████╗██╗██████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██║██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ██║██████╔╝    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
   ██║   ██║██╔═══╝     ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
   ██║   ██║██║         ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
   ╚═╝   ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                        '''
)

print("Welcome to the tip calculator")

total_bill=float(input("What was the total bill ? $"))

percentage_tip=float(input("what percentage tip would you like to give? 10, 12, or 15? %"))

calculation= total_bill * (percentage_tip)/100

calculation2=calculation+total_bill


split_bill=float(input("how many people to split the bill? "))

calculation3=calculation2/split_bill

round_float=round(calculation3,2)
format_calculation3="{:.2f}".format(round_float)

print(f"Each person should pay: {format_calculation3}$")




