**Leame do Script: Gerador de Senhas Seguras**

Este script Python oferece uma solução interativa para gerar senhas seguras com base nas preferências do usuário. Ele incorpora uma apresentação gráfica inicial, fornecendo opções para incluir letras, números e símbolos, garantindo assim senhas robustas.

### Apresentação Visual:
```
 ____ _            
/ ___| ___ _ __ __ _ __| | ___ _ __
| | _ / _ \ '__/ _` |/ _`| / _ \| '__|
| |_| | __/ | | (_| | (_||  (_) | |  
 \____|\___|_| \__,_|\__,_| \___/|_|  
```

### Padrões Estilizados:
```plaintext
..%%%%...%%%%%%..%%..%%..%%..%%...%%%%....%%%%..
.%%......%%......%%%.%%..%%..%%..%%..%%..%%.....
..%%%%...%%%%....%%.%%%..%%%%%%..%%%%%%...%%%%..
.....%%..%%......%%..%%..%%..%%..%%..%%......%%.
..%%%%...%%%%%%..%%..%%..%%..%%..%%..%%...%%%%..
.................................................
```

### Funcionalidades Principais:

1. **Geração de Senhas:**
   - A função `gerar_senha` gera senhas aleatórias com base nas preferências do usuário, incluindo letras, números e símbolos.
   - As senhas geradas são validadas para atender a critérios mínimos de força, como comprimento mínimo, presença de letras maiúsculas, números e caracteres especiais.

2. **Hashing de Senhas:**
   - A função `hash_senha` utiliza o algoritmo de hash SHA-256 para criar hashes seguros das senhas geradas, adicionando uma camada extra de proteção.

3. **Armazenamento em Arquivo:**
   - As senhas geradas, juntamente com seus hashes, são salvas no arquivo 'senha.txt'.
   - Informa ao usuário quantas senhas foram salvas no final do processo.

### Utilização:
- Execute o script em um ambiente Python compatível.
- Siga as instruções interativas para definir as preferências de senha.
- As senhas geradas e seus hashes serão salvas no arquivo 'senhas.txt'.

### Pré-requisitos:
Certifique-se de ter as bibliotecas necessárias instaladas:
```bash
pip install termcolor pyfiglet
```

Esperamos que este script torne o processo de geração de senhas mais fácil e seguro. Sinta-se à vontade para personalizar conforme necessário e contribuir com melhorias.
