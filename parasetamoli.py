"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
Author: Ifeoma Nwankwo
"""

MAX_DAILY_DOSE = 4000  #mg
SINGLE_DOSE_PER_KG = 15  #mg / kg
MIN_INTERVAL_HOURS = 6  #h

def calculate_dose(weight, hours_since_prev, total_24h):
    """
    Returns the paracetamol dose (mg) that can be safely given now

    :param weight:            Patient's weight in kg (int)
    :param hours_since_prev:  Full hours since the previous dose (int)
    :param total_24h:         Total paracetamol taken in the last 24 h (mg) (int)
    :return:                  Dose to give now in milligrams (int)
    """

    #Rule 1: must wait at least 6h between doses
    if hours_since_prev < MIN_INTERVAL_HOURS:
        return 0

    #Rule 3: if the daily maximum is already reached, give nothing
    if total_24h >= MAX_DAILY_DOSE:
        return 0

    #Normal single dose by weight
    normal_dose = weight * SINGLE_DOSE_PER_KG

    #Rule 3 continued: Cap so we never exceed the daily maximum
    max_allowed_now = MAX_DAILY_DOSE - total_24h
    return min(normal_dose, max_allowed_now)

def main():
    weight = int(input("Patient's weight (kg): "))
    hours = int(input("How much time has passed from the previous dose (full hours): "))
    total = int(input("The total dose for the last 24 hours (mg): "))

    dose = calculate_dose(weight, hours, total)
    print(f"The amount of Parasetamol to give to the patient: {dose}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

if __name__ == "__main__":
  main()
