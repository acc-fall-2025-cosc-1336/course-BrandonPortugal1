from value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax

def display_payroll_check(hours, rate):
    """
    Displays a formatted payroll check including gross pay, FICA tax, federal tax, and net pay.

    Parameters:
        hours (float): Number of hours worked.
        rate (float): Hourly pay rate.

    Returns:
        None
    """
    gross = get_gross_pay(hours, rate)
    fica = get_fica_tax(gross)
    federal = get_federal_tax(gross)
    net = gross - fica - federal

    print("Payroll Check")
    print(f"Gross Pay:      {gross:.2f}")
    print(f"FICA:           {fica:.2f}")
    print(f"Federal Tax:    {federal:.2f}")
    print(f"Net Pay:        {net:.2f}")

