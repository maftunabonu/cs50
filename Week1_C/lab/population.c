#include <cs50.h>
#include <stdio.h>

int calculate_years_llamas(int current_number, int number_wanted);

int main(void)
{
    int llamas_now;
    int llamas_wanted;
    // promt the user how many llamas are present
    do
    {
        llamas_now = get_int("Start size: ");
    }
    while (llamas_now < 9);

    // promt how many llamas are needed
    do
    {
        llamas_wanted = get_int("End size: ");
    }
    while (llamas_wanted < llamas_now);

    // calculation started
    int years_needed = calculate_years_llamas(llamas_now, llamas_wanted);
    printf("Years: %i year(s)\n", years_needed);
}

// calculate how many year it will take to get to a certain number of llamas, n/3 are born every year and n/4 die
int calculate_years_llamas(int current_number, int number_wanted)
{
    int count_years = 0;
    while (current_number < number_wanted)
    {
        current_number += current_number / 3 - current_number / 4;
        count_years++;
    }
    return count_years;
}