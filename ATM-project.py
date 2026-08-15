details = {"name":"Lohitha",
           "balance":90000,
           "ATM_PIN":"9966"}

remaining_atp = 3
print("-----Welcome To ATM-----")
Transaction = []
while remaining_atp > 0:
    user_pin = input("Enter your ATM pin: ")
    if len(user_pin) == 4:
        if user_pin in details["ATM_PIN"]:
            func_=int(input("Enter your choice :\n1.withdraw \n2.deposit \n3.change pin \n4.check balance \n5.Transaction history \n6.Exit: "))

            if func_ == 1:
                withdraw_m = int(input("Enter the amount you want to withdraw: "))
                if withdraw_m <= details["balance"] and withdraw_m % 100 == 0:
                    details["balance"] -= withdraw_m
                    Transaction.append(f"withdraw:{withdraw_m}")
                    print(f"you have withdraw {withdraw_m} and total balance is {details["balance"]}")
                else:
                    print("Insufficient funds")

            if func_ == 2:
                deposit_m = int(input("Enter the amount you want to deposit: "))
                if deposit_m % 100 == 0:
                    details["balance"] += deposit_m
                    Transaction.append(f"deposit:{deposit_m}")
                    print(f"you have deposit {deposit_m}")
                else:
                    print("Change can not be deposited in ATM")
                    
            if func_ == 3:

                correct_pin = details["ATM_PIN"]
                attempts = 0

                while attempts < 3:
                    entered_pin = input("Enter your current pin: ")
                    if entered_pin == correct_pin:
                        new_pin = input("Enter your New pin: ")
                        confirm_pin = input("Confirm pin: ")
                        if new_pin == confirm_pin:
                            correct_pin = new_pin
                            print("PIN is changed Successfully...")
                            break
                        else:
                            print("New pin is not matches confirm pin.Try again..")
                                  
                    else:
                        attempts += 1
                        print("Incorrect pin")
                        if attempts == 3:
                            print("your card is Blocked...")
                            remaining_atp = 0
                            break
             
            if func_ == 4:
                print(f"your balance is {details["balance"]}")
                break

            if func_ == 5:
                if Transaction == []:
                    print("No Transaction found")
                else:
                    print("Transaction History:")
                    print(Transaction)

            if func_ == 6:
                print("Thank for using our ATM")
                print("Visit Again...")
                break
                            
        else:
            remaining_atp -= 1
            if remaining_atp > 0:
                print(f"you have entered incorrect pin and you left {remaining_atp} attempts")
            else:
                print(f"your card is temperorly Blocked")
            
    else:
        print("pls enter only 4 digit pin")

    
