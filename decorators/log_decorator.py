def log_operacao(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] Finalizado: {func.__name__}")
        return resultado
    return wrapper