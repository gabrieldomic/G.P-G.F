import sqlite3

def listar_vendas():
    print("\n" + "="*45)
    print("      RELATÓRIO DE VENDAS CADASTRADAS")
    print("="*45)
    print(f"{'ID':<4} | {'PRODUTO':<15} | {'QTD':<6} | {'VALOR':<10}")
    print("-" * 45)

    try:
        # Conecta ao banco (mesmo caminho usado pelo Renan)
        conexao = sqlite3.connect('data/sistema.db')
        cursor = conexao.cursor()

        # Comando SQL para ler tudo
        cursor.execute("SELECT id, produto, quantidade, valor FROM vendas")
        vendas = cursor.fetchall()

        if not vendas:
            print("Poxa, nenhuma venda cadastrada ainda! 😅")
        else:
            for v in vendas:
                # v[0]=ID, v[1]=Produto, v[2]=Qtd, v[3]=Valor
                print(f"{v[0]:<4} | {v[1]:<15} | {v[2]:<6} | R$ {v[3]:<8.2f}")
        
        print("="*45)

    except Exception as e:
        print(f"\n❌ Erro ao ler o banco de dados: {e}")
    
    finally:
        conexao.close()

# Teste para ver se está funcionando
if __name__ == "__main__":
    listar_vendas()