# import time
# from playwright.sync_api import sync_playwright


# orders = '''303731072
# 304235511
# 304232801
# 304239131
# 304227502
# 303961430
# 303547725
# 301740558
# 305042629
# 303666931
# 303964679
# 304214557
# 304847784
# 301437926
# 305041858
# 304231621
# 305033873
# 304234377
# 304227018
# 304054434
# 304216519
# 304811961
# 304406842
# 304597545
# 303324594
# 304660005
# 304225680
# 304231957
# 303732678
# 303963343
# 304413194
# 305036894
# 303955327
# 304414331
# 304229542
# 304175787
# 303956978
# 303952962
# 302790342
# 302206762
# 304224159
# 304546603
# 305009033
# 303532848
# 303716965
# 303962306
# 305041949
# 304231755
# 303963322
# 304235844
# 304219867
# 304234479
# 304218358
# 302966897
# 303942112
# 304220929'''

# order_list = orders.splitlines()


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://backoffice.azki.com/financial/overdue-installments-by-order')

#     def generate_orders(order_list):
#         for order in order_list:
#             yield order

#     order_gen = generate_orders(order_list)

#     while True:
#         nextt = input('\'n\' = next | \'e\' = exit : ')

#         if nextt == 'n':
#             try:

#                 next_order = next(order_gen)

#                 input_field = page.query_selector('xpath=//input[@id=":r4:"]')

#                 input_field.fill(next_order)

#                 input_field.press('Enter')

#                 while True:
#                     press_field = page.query_selector(
#                         '//tr[@name="highlighted-row"]')

#                     if press_field:
#                         press_field.click()
#                         break

#                     else:
#                         input_field.fill(next_order)

#             except StopIteration:
#                 print("orders are done")
#                 break

#         elif nextt == 'e':
#             print("exiting")
#             browser.close()
#             break
#         else:
#             print("options are n and e")



import time
from playwright.sync_api import sync_playwright


orders = '''303731072
304235511
304232801
304239131
304227502
303961430
303547725
301740558
305042629
303666931
303964679
304214557
304847784
301437926
305041858
304231621
305033873
304234377
304227018
304054434
304216519
304811961
304406842
304597545
303324594
304660005
304225680
304231957
303732678
303963343
304413194
305036894
303955327
304414331
304229542
304175787
303956978
303952962
302790342
302206762
304224159
304546603
305009033
303532848
303716965
303962306
305041949
304231755
303963322
304235844
304219867
304234479
304218358
302966897
303942112
304220929'''

order_list = orders.splitlines()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://backoffice.azki.com/financial/overdue-installments-by-order')

    def generate_orders(order_list):
        for order in order_list:
            yield order

    order_gen = generate_orders(order_list)

    while True:
        nextt = input('\'n\' = next | \'e\' = exit : ')

        if nextt == 'n':
            try:
                while True:

                    next_order = next(order_gen)

                    input_field = page.query_selector(
                        'xpath=//input[@id=":r4:"]')

                    input_field.fill(next_order)

                    input_field.press('Enter')

                    press_field = page.wait_for_selector(
                        '[name="highlighted-row"]', timeout=3000)

                    if press_field:
                        press_field.click()
                        break

                    else:
                        continue

            except StopIteration:
                print("orders are done")
                break

        elif nextt == 'e':
            print("exiting")
            browser.close()
            break
        else:
            print("options are n and e")
