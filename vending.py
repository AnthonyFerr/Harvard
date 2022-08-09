import machine

drinks = {"Coke": 1.99, "Arizona Tea": 0.99, "Dasani": 1.50}

vm = machine.Vending_Machine(drinks)

vm.getDrink("Arizona Tea")
vm.getPrice("Coke")
vm.listDrinks()
