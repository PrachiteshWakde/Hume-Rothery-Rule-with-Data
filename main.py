from Data import elements


def check_atomic_size_factor(element_1, element_2):
    atomic_difference = abs(element_1 - element_2) / element_1 * 100
    atomic_difference = round(atomic_difference, 2)
    # print(f"Atomic Size difference is {atomic_difference}")
    if atomic_difference < 15:
        print(
            f"Atomic Size difference is {atomic_difference} which is favaorable for Substitunal Alloy Formation with Atomic Difference of {atomic_difference} which is less than 15%")
    else:
        print(
            f"Atomic Size difference is {atomic_difference} which is not favaorable for Substitunal Alloy Formation with Atomic Difference of {atomic_difference}which is greater than 15%")


def check_electronegtivity(element_1, element_2):
    element_1_en = element_1
    # print(element_1_en)
    element_2_en = element_2
    # print(element_2_en)
    en_diff = round(abs(element_1_en - element_2_en), 2)
    # print(en_diff)
    if en_diff < 0.4:
        print(
            f"Electronegativity is Favorable for Substitutional Alloy Formation with {en_diff} which is Less than 0.4")
    else:
        print(
            f"Electronegativity is not Favorable for Substitutional Alloy Formation with {en_diff} which is Greater than 0.4")

def check_valency(element_1, element_2):
    status = True
    element_1_oxidation = element_1
    # print(element_1_oxidation)
    element_2_oxidation = element_2
    # print(element_2_oxidation)
    for oxi in element_1_oxidation:
        for oxidize in element_2_oxidation:
            if oxi == oxidize:
                print(f"Valancy {oxi} matches substitiutional Alloy Formation is Favorable")
                status = False
    if status:
        print(
            f"No Valancy matches in {element_1_name} and {element_2_name}, So substitiutional Alloy Formation is NOT Favorable")

def check_lattice_structure(element_1, element_2):
    element_1_cs = element_1
    # print(element_1_cs)
    element_2_cs = element_2
    # print(element_2_cs)
    if element_1_cs == element_2_cs:
        print(f"Substitutional Alloy Formation is Favorable with same crystal structure of {element_1_cs}")
    else:
        print(f"Substitutional Alloy Formation is not Favorable with different crystal structure of {element_1_name} {element_1_cs} and {element_2_name} {element_2_cs}")


print("Welcome to Hume Rothery Rule Program")
print("This Program will help you to Figure Out whether Substitution Solid Solutions will form or not")
element_1 = int(input("Please enter atomic number of element 1: \n"))
element_2 = int(input("Please enter atomic number element 2: \n"))

element_1_name = elements[element_1]["name"]
element_1_symbol = elements[element_1]["symbol"]
element_1_lattice_structure = elements[element_1]["lattice_structure"]
element_1_en_pauling = elements[element_1]["en_pauling"]
element_1_metallic_radius_c12 = elements[element_1]["metallic_radius_c12"]
element_1_oxistates = elements[element_1]["oxistates"]

element_2_name = elements[element_2]["name"]
element_2_symbol = elements[element_2]["symbol"]
element_2_lattice_structure = elements[element_2]["lattice_structure"]
element_2_en_pauling = elements[element_2]["en_pauling"]
element_2_metallic_radius_c12 = elements[element_2]["metallic_radius_c12"]
element_2_oxistates = elements[element_2]["oxistates"]


print(f"You have selected {element_1_name}({element_1_symbol}) and {element_2_name}({element_2_symbol})")
check_atomic_size_factor(element_1_metallic_radius_c12, element_2_metallic_radius_c12)
check_electronegtivity(element_1_en_pauling, element_2_en_pauling)
check_valency(element_1_oxistates, element_2_oxistates)
check_lattice_structure(element_1_lattice_structure, element_2_lattice_structure)
