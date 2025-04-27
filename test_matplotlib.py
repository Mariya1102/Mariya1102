import matplotlib
print(f"Matplotlib version: {matplotlib.__version__}")
print(f"Matplotlib backend: {matplotlib.get_backend()}")
try:
    import matplotlib.pyplot as plt
    print("Successfully imported matplotlib.pyplot")
except Exception as e:
    print(f"Error importing matplotlib.pyplot: {str(e)}") 