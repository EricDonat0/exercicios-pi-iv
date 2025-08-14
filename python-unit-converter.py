print('Conversor de Unidades: Pés, Metros, Jardas\n')

#Conversion constants
meters_to_feet = 3.281
meters_to_yards = 1.094
yards_to_feet = 3
yards_to_meters = 0.9144
feet_to_meters = 0.3048
feet_to_yards = 0.3333

#variable result
result = None

#function
def unit_converter():
    #User input
    measurement_unit = input("Digite a unidade de medida que deseja converter (pé, metro, jarda): ")
    value = float(input("Digite o valor: "))
    target_unit = input("Digite a unidade de medida destino (pé, metro, jarda): ")
    
    valid_units = ["pé", "metro", "jarda"]
    if measurement_unit not in valid_units or target_unit not in valid_units:
        print("Erro: unidade inválida! Escolha entre pé, metro ou jarda.\n")
        return unit_converter()
    
    # Conversion
    if measurement_unit == "metro" and target_unit == "pé":
        result = value * meters_to_feet

    elif measurement_unit == "metro" and target_unit == "jarda":
        result = value * meters_to_yards

    elif measurement_unit == "jarda" and target_unit == "pé":
        result = value * yards_to_feet

    elif measurement_unit == "jarda" and target_unit == "metro":
        result = value * yards_to_meters

    elif measurement_unit == "pé" and target_unit == "metro":
        result = value * feet_to_meters

    elif measurement_unit == "pé" and target_unit == "jarda":
        result = value * feet_to_yards

    elif measurement_unit == target_unit:
        result = value

    print(f"Resultado: {result}\n")

unit_converter()