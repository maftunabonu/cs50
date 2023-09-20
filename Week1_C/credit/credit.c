#include <cs50.h>
#include <stdio.h>

bool is_valid(long number);
int find_length(long number);
string card_type(long number);

int main(void)
{
    // promting the user to enter their card's number
    long card_number;
    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number < 1);
    if (is_valid(card_number))
    {
        printf("%s", card_type(card_number));
    }
    else
    {
        printf("INVALID\n");
    }
}

bool is_valid(long number)
{
    int number_length = find_length(number);
    int digits[number_length];
    int digits_sum = 0;
    int multiplied_digit;
    if (number < 1000000000000)
    {
        return false;
    }
    for (int j = 0; j < number_length; j++)
    {
        digits[j] = number % 10;
        number /= 10;
    }
    for (int j = 0; j < number_length; j++)
    {
        if (digits[j] != 0)
        {
            if (j % 2 == 0)
            {
                digits_sum += digits[j];
            }
            else
            {
                multiplied_digit = digits[j] * 2;
                if (multiplied_digit < 10)
                {
                    digits_sum += multiplied_digit;
                }
                else
                {
                    digits_sum += multiplied_digit / 10 + multiplied_digit % 10;
                }
            }
        }
    }
    // check if it is valid
    if (digits_sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int find_length(long number)
{
    int count = 1;
    for (long i = 10; i < number; i *= 10)
    {
        count++;
    }
    return count;
}

// identifies what card it is

string card_type(long number)
{
    if (number / 10000000000000 == 34 || number / 10000000000000 == 37)
    {
        return "AMEX\n";
    }
    else if (number / 100000000000000 == 51 || number / 100000000000000 == 52 || number / 100000000000000 == 53 ||
             number / 100000000000000 == 54 || number / 100000000000000 == 55)
    {
        return "MASTERCARD\n";
    }
    else if (number / 1000000000000 == 4 || number / 1000000000000000 == 4)
    {
        return "VISA\n";
    }
    else
    {
        return "INVALID\n";
    }
}