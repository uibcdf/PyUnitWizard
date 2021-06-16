def initialize():
    global form
    global parser
    global fundamental_units
    global combination_units
    form = None
    parser = None
    standards = {}
    dimensional_fundamental_standards = {}
    dimensional_combinations_standards = {}
    adimensional_standards = {}
    tentative_base_standards = {}

order_fundamental_units = ['[L]', '[M]', '[T]', '[K]', '[mol]', '[A]', '[Cd]']

