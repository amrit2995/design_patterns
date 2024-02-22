import time
STEP_DELAY = 1

class Pizza:    
    def __init__(self, name):        
        self.name = name        
        self.dough = None        
        self.sauce = None        
        self.topping = []    
    def __str__(self):        
        return self.name    
    def prepare_dough(self, dough):        
        self.dough = dough        
        print(f'preparing the {self.dough.name} dough of your {self}...')        
        time.sleep(STEP_DELAY)        
        print(f'done with the {self.dough.name} dough')

class Pizza:     
    def __init__(self, builder):         
        self.garlic = builder.garlic         
        self.extra_cheese  = builder.extra_cheese      
    def __str__(self):         
        garlic = 'yes' if self.garlic else 'no'         
        cheese = 'yes' if self.extra_cheese else 'no'         
        info = (f'Garlic: {garlic}', f'Extra cheese: {cheese}')         
        return '\n'.join(info)      
    # class PizzaBuilder:         
    #     def __init__(self):             
    #         self.extra_cheese = False             
    #         self.garlic = False

class MargaritaBuilder:    
    def __init__(self):        
        self.pizza = Pizza('margarita')        
        self.progress = PizzaProgress.queued        
        self.baking_time = 5 # in seconds for the sake of         the example    
        def prepare_dough(self):        
            self.progress = PizzaProgress.preparation        
            self.pizza.prepare_dough(PizzaDough.thin)    
            def add_sauce(self):        print('adding the tomato sauce to your margarita...')        
            self.pizza.sauce = PizzaSauce.tomato        
            time.sleep(STEP_DELAY)        
            print('done with the tomato sauce')
            
    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'        
        topping_items = (
            PizzaTopping.double_mozzarella,        
            PizzaTopping.oregano
            )        
        print(f'adding the topping ({topping_desc}) to your        margarita')        
        self.pizza.topping.append([t for t in topping_items])        
        time.sleep(STEP_DELAY)        
        print(f'done with the topping ({topping_desc})') 
           
    def bake(self):        
        self.progress = PizzaProgress.baking        
        print(f'baking your margarita for {self.baking_time}        seconds')        
        time.sleep(self.baking_time)        
        self.progress = PizzaProgress.ready        
        print('your margarita is ready')
        
        
class CreamyBaconBuilder:    
    def __init__(self):        
        self.pizza = Pizza('creamy bacon')        
        self.progress = PizzaProgress.queued        
        self.baking_time = 7 # in seconds for the sake of         the example    
    def prepare_dough(self):        
        self.progress = PizzaProgress.preparation        
        self.pizza.prepare_dough(PizzaDough.thick)    
    def add_sauce(self):        
        print('adding the crème fraîche sauce to your creamy        bacon')        
        self.pizza.sauce = PizzaSauce.creme_fraiche        
        time.sleep(STEP_DELAY)        
        print('done with the crème fraîche sauce')    
    def add_topping(self):        
        topping_desc = 'mozzarella, bacon, ham, mushrooms,        red onion, oregano'        
        topping_items =  (
            PizzaTopping.mozzarella,                          
            PizzaTopping.bacon,                          
            PizzaTopping.ham,                          
            PizzaTopping.mushrooms,                          
            PizzaTopping.red_onion,                           
            PizzaTopping.oregano)        
        print(f'adding the topping ({topping_desc}) to your         creamy bacon')        
        self.pizza.topping.append([t for t in topping_items])        
        time.sleep(STEP_DELAY)        
        print(f'done with the topping ({topping_desc})')
           
    def bake(self):        
        self.progress = PizzaProgress.baking        
        print(f'baking your creamy bacon for {self.baking_time}        seconds')        
        time.sleep(self.baking_time)

        print(f'baking your creamy bacon for {self.baking_time}        
               seconds')        
        time.sleep(self.baking_time) 
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')
        
class Waiter:    
    def __init__(self):        
        self.builder = None    
    def construct_pizza(self, builder):        
        self.builder = builder        
        steps = (builder.prepare_dough,                  
                 builder.add_sauce,                  
                 builder.add_topping,                  
                 builder.bake
                 )        
        [step() for step in steps]

    @property   
    def pizza(self):        
        return self.builder.pizza
    
    
def validate_style(builders):    
    try:        
        input_msg = 'What pizza would you like, [m]argarita or        [c]reamy bacon? '        
        pizza_style = input(input_msg)        
        builder = builders[pizza_style]()        
        valid_input = True    
    except KeyError:        
        error_msg = 'Sorry, only margarita (key m) and creamy        bacon (key c) are available'        
        print(error_msg)
        
        
def main():    
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)    
    valid_input = False    
    while not valid_input:        
        valid_input, builder = validate_style(builders)    
        print()    
        waiter = Waiter()    
        waiter.construct_pizza(builder)    
        pizza = waiter.pizza    
        print()    
        print(f'Enjoy your {pizza}!')


# if __name__ == '__main__':    
#     pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()     
#     print(pizza)