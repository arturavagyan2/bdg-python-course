# F · Build a postcard receipt · 18 minutes
#
# Plan and build independently after A–E. A small shop sells one kind of postcard per purchase. Ask the customer for the number of postcards (positive integer), price per postcard (positive decimal number) and amount paid. A single packaging charge of 0.50 applies to the entire purchase. Assume the amount paid covers the purchase. All amounts use the same currency.
#
# Display a readable receipt with item subtotal, packaging charge, total charge and change. Choose meaningful names and decide which inputs need int or float. Calculate results from the entered values; ordinary print calls with labels and values are sufficient. Plan the calculation on paper/in your notes before coding.
#
# **Sample input:** count 3, unit price 1.50, paid 10. **Expected amounts:** item subtotal 4.5, packaging 0.5, total 5.0, change 5.0. Another check: count 4, price 2.25, paid 20 → subtotal 9.0, total 9.5, change 10.5. Predict the second result before running it. Equivalent labels and ordinary float output are accepted.
#
# Use this empty area or receipt.py, save/run as a script and compare both cases. Notebook users also save their own code into receipt.py. A partner should understand the receipt without reading your source. No conditions, loops, imports, functions, f-strings, round() or error handling are needed.
#
# **Optional extension:** a customer asks for gift wrapping costing another 0.75 per purchase. Update the total using += and calculate the change from the updated total. Keep the item subtotal unchanged.
