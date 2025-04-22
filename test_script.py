import os
import pickle

def load_data():
    file = open("data.pkl", "rb")
    data = pickle.load(file)  # risky
    return data

def dynamic_exec(code_str):
    exec(code_str)  # risky

def insecure_input():
    user_input = input("Enter command to run: ")  # low risk
    os.system(user_input)  # should flag this if extended

def vulnerable_eval():
    command = input("Enter Python code to run: ")
    eval(command)  # high risk

def safe_function():
    print("This function is completely safe!")

if __name__ == "__main__":
    load_data()
    dynamic_exec("print('executed')")
    insecure_input()
    vulnerable_eval()
    safe_function()
