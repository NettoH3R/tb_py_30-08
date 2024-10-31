def substituir_string(input_file, output_file, old_string, new_string):
    with open(input_file, "r") as file:
        content = file.read()
    
    new_content = content.replace(old_string, new_string)
    
    with open(output_file, "w") as file:
        file.write(new_content)
    print("Substituição concluída com sucesso!")


substituir_string("financeiro.log", "novo_financeiro.log", "venda", "comercialização")