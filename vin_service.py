global_vin_counter = 1

def get_next_vin():
    global global_vin_counter
    vin = f"{global_vin_counter:07d}"
    global_vin_counter += 1
    return vin
