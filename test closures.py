def main():
    string: str = "Asumakina"
    
    def print_en():
        string_en: str = "Papu!"
        print(string, " " , string_en)
        
    return print_en    
       

init_func = main()
del(main) 

init_func()