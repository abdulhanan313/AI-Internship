str_num = "42"
int_from_str = int(str_num)
float_from_str = float(str_num)
str_from_int = str(123)
print(f"Explicit: {int_from_str} ({type(int_from_str)}), "
          f"{float_from_str} ({type(float_from_str)}), "
          f"{str_from_int} ({type(str_from_int)})")