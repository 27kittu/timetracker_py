from module1 import *
def main():
    trades = int(input('Please enter the number of trades: '))
    mastr_lst = []
    i = 1
    while i < trades + 1:
        print('Please enter the trade details as buy rate, sell rate, lot size respectively')
        b_rate = float(input("buy rate: "))
        s_rate = float(input("sell rate: "))
        lots = int(input("lot size: "))
        lst_inputs = "lst_input" + str(i)
        lst_inputs = [[b_rate, lots], [s_rate, lots]]
        mastr_lst.append(lst_inputs)
        i += 1
    return mastr_lst


if __name__ == '__main__':
    response = main()
    bro_billing_print(response)
