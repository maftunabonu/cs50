// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, float tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, float tip)
{
    tax = bill * tax / 100; // calculates how much is the tax
    tip = (bill + tax) * tip / 100; // calculates how much is the tip
    float final_bill = bill + tax + tip; // addes athe bill, tax, and tip
    return final_bill / 2; // sevides by 2 and, then, returns the final value in float
}
