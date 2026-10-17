#!/usr/bin/env python3
import sys

def bmi(weight_kg, height_m):
    val = weight_kg / (height_m ** 2)
    if val < 18.5: cat = "Underweight"
    elif val < 25: cat = "Normal"
    elif val < 30: cat = "Overweight"
    else: cat = "Obese"
    return val, cat

if __name__ == "__main__":
    w, h = float(sys.argv[1]), float(sys.argv[2]) / 100
    val, cat = bmi(w, h)
    print(f"BMI: {val:.1f} ({cat})")
