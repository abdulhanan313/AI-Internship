global_var = "I'm global"

def demo_local_global():
    global global_var   # needed to modify global
    local_var = "I'm local"
    print("Inside function:", global_var, local_var)
    global_var = "Changed global"
    
demo_local_global()
print("Outside function:", global_var)